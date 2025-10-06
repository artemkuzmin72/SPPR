import numpy as np

matrix  = np.array([[7, 3, 6, 10, 1],
                    [0, 6, 8, 6, 11],
                    [9, 4, 6, 10, 5],
                    [3, 3, 9, 8, 3],
                    [6, 5, 11, 4, 4]])
q=[0.15, 0.79, 0.0, 0.06, 0.0]
p=[0.0, 0.21, 0.11, 0.0, 0.68]
answer = {}
# Находим нижнюю и верхнюю цены
lower_price = max([min(x) for x in matrix])
upper_price = min([max(x) for x in matrix.T])  # ТУТ я иправил np.rot90(matrix) на matrix.T, выдает разные результаты, хотя
# хотя по идее должно одно и тоже выводить, код без изменений выложен
print(lower_price, upper_price)# выводит 6 и 9 соответственно
if lower_price==upper_price:print("седловая точка есть", f"ответ v={lower_price}") # Ищем седловую точку
  # едловой точки нет- значит  первый игрок может гарантировать себе выигрыш не менее 6 единиц (нижняя цена)
  # и может надеяться на выигрыш не более 9 единиц (верхняя цена)
# Игра решается в смешанных стратегиях.

# Определить выигрыши игрока А в ситуации (P; Q), (P; B1), (P; B2), (P; B3):
else:
  buff=0
  for i,pin in zip(matrix,p):
    buff+=pin*sum([x*y for x,y in zip(i,q)])
  answer["H(P,Q)"]=buff
  for k in range(len(q)): 
    answer["H(P,B{})".format(k+1)]=sum([p[i]*matrix[i][k] for i in range(len(p))])
for i in [(x,y) for x,y in answer.items()]:
  print("Ответ выйгрыш игрока А в ситуации {0[0]} = {0[1]}".format(i))
