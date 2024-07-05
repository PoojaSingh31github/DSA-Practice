height = int(input("Enter the size of pine tree pattern's height: "))
for i in range(height):
        spaces = ' ' * (height - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)

trunk = ' ' * (height - 1) + '|'
print(trunk)

 