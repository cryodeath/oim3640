num = 100 
try:
    a = float(input('Enter a number to divide by:'))
    print(num/a)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("That's not a valid number!")
finally:
    print("we still want to print this!")

print("Let;s move on to the next part of the code...")

names = ['Alice', 'Bob', 123, 'Charlie']
uppercase_names = []

for name in names:
    try:
        print(name.upper())
        uppercase_names.append(name.upper())
    except AttributeError:
        print(f"Error: '{name}' is not a string and cannot be converted to uppercase.")

        print("Ippercase names:", uppercase_names)

print("Let's move on to the next part of the code...")
print[num/10]
