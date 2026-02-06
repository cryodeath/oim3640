# for i in range (4, 1, -1): 

#     print("Iteration", i)
#     # print("Square:", i * i)

# name = 'Alejandro'
# type(Alejandro)

def double(number):
    '''Return double the input number'''
    return number * 2

print(double(4))
print(double(10))   

a = 5 # assign 5 to variable a
b = a
a = 10
print(b)
print(a)
# always works this way for immutable types

a = [1, 2, 3] # list is mutable
b = a
a.append(4)
print(b)
print(a)
# list changes because both a and b point to the same list object in memory

x = 10 

def f():
    message = 'Hello'
    x = 5 
    return message + str(x)
print(f())
print(x)
# print(message)  # This will raise an error because message is not defined globally  
# x defined inside f() is local to that function, and there is an x defined globally

y=f()
print(y)
print(x)

# Draw a square
'''
🧱🧱🧱🧱
🧱🧱🧱🧱
🧱🧱🧱🧱
🧱🧱🧱🧱
'''
def draw_square(size):
    for i in range(size):
        print('🧱' * size)
        for j in range(size):
            print('🧱', end='')
            print()  # Move to the next line after inner loop

def draw_square(size):
    for i in range(size):
        print('🧱' * size)

draw_square(4)

# draw a triangle

'''create a function that draws a triangle
🧱             1 = 0 + 1
🧱🧱           2 = 1 + 1
🧱🧱🧱         3 = 2 + 1
🧱🧱🧱🧱        4 = 3 + 1

In row i, how many bricks are there?  i = i + 1 
# rows start from 0
def draw_triangle(rows):
    for i in range(rows):
        print('🧱' * (i + 1))
# If i want rows to start from 1 to rows
def draw_triangle(rows):
    for i in range(1, rows + 1):
        print('🧱' * i)
'''
'''
Draw a triangle like this (size=5)

    #        4 spaces + 1 # = 5 5 - 0 -1 = 4
   ##        3 spaces + 2 # = 5 5 -1 -1 =3
  ###        2 spaces + 3 # = 5 5 -2 -1 =2
 ####        1 space +  4 # = 5 5 -3 -1 =1
#####  

for i in range (size):
In row i, how many spaces are there? size -i -1
 how many #s are there? i + 1
'''

# a comment

def draw_triangle(size):
    """Draw a triangle"""
    for i in range(size):
        print(' ' * (size - i - 1) + '#' * (i + 1))

draw_triangle(5)

# create a function to draw a pyramid
'''
   #  
  ###
 #####
####### 

'''