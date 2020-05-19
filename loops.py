foods = ['apples', 'bread', 'cheese', 'milk', 'grapes', 'apples']

for food in foods:
    print(food)
    if food == 'cheese':
        print('Gotta buy some cheese')


for food in foods:
    print(food)  # Breaking the loop
    if food == 'cheese':
        break
    print('Gotta buy some cheese')

for food in foods:
    print(food)
    if food == 'cheese':
        continue  # Skips the code
    print('Gotta buy some cheese')

for number in range(1, 20):
    print(number)


count = 4

while count <= 10:
    print(count)
    count = count + 1
