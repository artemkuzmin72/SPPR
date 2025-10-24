import numpy as np

matrix  = np.array([[7, 3, 6, 10, 1],
                    [0, 6, 8, 6, 11],
                    [9, 4, 6, 10, 5],
                    [3, 3, 9, 8, 3],
                    [6, 5, 11, 4, 4]])
q=[0.15, 0.79, 0.0, 0.06, 0.0]
p=[0.0, 0.21, 0.11, 0.0, 0.68]
answer = {}
lower_price = max([min(x) for x in matrix])
upper_price = min([max(x) for x in matrix.T])
print(lower_price, upper_price)
if lower_price==upper_price:print("седловая точка есть", f"ответ v={lower_price}") 

else:
  buff=0
  for i,pin in zip(matrix,p):
    buff+=pin*sum([x*y for x,y in zip(i,q)])
  answer["H(P,Q)"]=buff
  for k in range(len(q)): 
    answer["H(P,B{})".format(k+1)]=sum([p[i]*matrix[i][k] for i in range(len(p))])
for i in [(x,y) for x,y in answer.items()]:
  print("Ответ выйгрыш игрока А в ситуации {0[0]} = {0[1]}".format(i))
