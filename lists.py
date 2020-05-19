demoList = [1, 'Hello', 3.4, True, [1, 2, 3]]
colors = ['red', 'green', 'black']

numbers = list((1, 2, 3, 4))
print(numbers)

r = list(range(1, 101))
# print(r)

print(type(colors))

print(len(colors))
print(colors[-1])
print('red' in colors)
colors[1] = 'yellow'
print(colors)
colors.append('orange')
print(colors)
colors.extend(['brown', 'blue', 'violet'])
print(colors)
colors.insert(1, 'white')
print(colors)
# colors.pop()
# colors.pop(1)
print(colors)
colors.remove('orange')
print(colors)
# colors.clear()
colors.sort()
colors.sort(inverse=True)
colors.index('blue')
colors.count('red')
