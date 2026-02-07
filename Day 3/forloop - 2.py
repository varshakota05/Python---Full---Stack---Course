'''
for var in seq:
#stmts

seq : list, tuple, set, dict, str, range


products = ['bread', 'butter', 'milk', 'sugar', 'salt']

for product in products:
    print(f'{product} - Add to fav | Buy now | Add to cart')
'''

sizes = ('xs', 's', 'm', 'l', 'xl', 'xxl', 'xxxl')

for s in sizes:
     print(f'... |{s}| ...')

followers = {'saaketh', 'swapnil', 'dileep', 'varsha', 'sathvik'}

for i in followers:
    print(f'{i} - |follow back|remove|message|')

'''
data = {
    'Varsha': ['C', 'Python', 'Java'],
    'Saaketh': ['ML', 'AI', 'Python'],
    'Meghana': ['java', 'linux', 'Python'],
    'Sirisha':['Figma', 'UI/UX', 'Python']
}

for i in data:
    print(f"{i}: {data[i]}")
    
'''

s = 'Python Programming'

for i in s:
    print(i)


#range(start, stop+1, step) = range(0,n,1)
for i in range(1,11):
    print(i)

#range(start, stop+1, step) = range(0, n, 1)
for i in range(1, 100, 2):
        print(i)

n = int(input("Enter the number:"))

print(f"{n}-Table")
for i in range(1, 11):
    print(f'{n}*{i}={n*i}')
'''
for i in range(1,10):
    if i==7:
        continue
    print(i)

for i in range(1,10):
    if i==7:
        break
    print(i)

'''

i = 1
while i<=10:
    print(i)
    i=i+1

''

moves = 15
winning_point = int(input("Tell me how many moves are required"))

while moves >= 1:
  if 15 -  winning_point == moves:
    print("You won the game")
    break
  print(f"{moves} are left")
  moves-=1

else:
  print("Game Over")

''

bullets = 10

while bullets > 0:
  print(f"You have {bullets} bullets, shoot them!")
  bullets -= 1

else:
  print("Game Over")
