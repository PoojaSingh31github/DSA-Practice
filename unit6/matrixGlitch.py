def print_hollow_rectangle(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            # Print the top and bottom borders
            print('*' * n)
        else:
            # Print the hollow part with spaces in between
            print('*' + ' ' * (n - 1) + '*')


# Input handling
t = int(input("Enter the number of test cases: "))  # Number of test cases
for _ in range(t):
    n = int(input())  # Size of the rectangle
    print_hollow_rectangle(n)
    print()  # Add a blank line between test cases
