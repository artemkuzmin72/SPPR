from pulp import *
import time

print("ТРАНСПОРТНАЯ ЗАДАЧА - ВАРИАНТ 16")


supply = [200, 300, 200, 200, 100]  
demand = [200, 200, 400, 200, 100]  

cost_matrix = [
    [5, 2, 1, 6, 4],
    [6, 2, 4, 4, 6],
    [9, 2, 3, 7, 5],
    [7, 3, 5, 8, 7],  
    [3, 2, 4, 2, 3]
]

print("Дано:")
print(f"Запасы поставщиков: {supply} (сумма = {sum(supply)})")
print(f"Потребности потребителей: {demand} (сумма = {sum(demand)})")

total_supply = sum(supply)
total_demand = sum(demand)

if total_supply != total_demand:
    print(f"\n Задача несбалансированная! Разница: {abs(total_supply - total_demand)}")
    if total_supply < total_demand: 
        supply.append(total_demand - total_supply)
        cost_matrix.append([0, 0, 0, 0, 0])
        print("Добавлен фиктивный поставщик")
    else:
        demand.append(total_supply - total_demand)
        for row in cost_matrix:
            row.append(0)
        print("Добавлен фиктивный потребитель")

m = len(supply)
n = len(demand)

print(f"\nРазмерность задачи: {m} поставщиков × {n} потребителей")

print("Решение методом PULP")

start_time = time.time()

variables = []
for i in range(m):
    for j in range(n):
        variables.append(LpVariable(f"x_{i+1}_{j+1}", lowBound=0)) 

problem = LpProblem("Transport_Problem", LpMinimize)

cost_coeffs = []
for i in range(m):
    for j in range(n):
        cost_coeffs.append(cost_matrix[i][j])

problem += lpDot(cost_coeffs, variables), "Total_Cost" 

for i in range(m):
    constraint_vars = variables[i*n : (i+1)*n] 
    problem += lpSum(constraint_vars) == supply[i], f"Supply_{i+1}" 

for j in range(n):
    constraint_vars = [variables[i*n + j] for i in range(m)]
    problem += lpSum(constraint_vars) == demand[j], f"Demand_{j+1}"

problem.solve(PULP_CBC_CMD(msg=0))
pulp_time = time.time() - start_time

print("оптимальный план перевозок:")

total_cost = 0
for variable in problem.variables():
    if variable.varValue > 0.001: 
        parts = variable.name.split('_')
        supplier = int(parts[1])  
        consumer = int(parts[2])  
        amount = variable.varValue
        cost = amount * cost_matrix[supplier-1][consumer-1] 
        total_cost += cost
        print(f"поставщик{supplier} → потребитель{consumer}: {amount:.1f} ед. × {cost_matrix[supplier-1][consumer-1]} = {cost:.1f}")

print(f"минимальная стоимость: {total_cost:.1f}")
print(f"время выполнения: {pulp_time:.4f} сек")
