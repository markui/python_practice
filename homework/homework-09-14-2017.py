#1.
def which_fruit(fruit_color):
    if fruit_color == 'red':
        return 'apple'
    elif fruit_color == 'yellow':
        return 'banana'
    elif fruit_color == 'green':
        return 'melon'
    else:
        return 'I don\'t know'

result = which_fruit('yellow')
print(result)

#2.
def which_fruit(fruit_color):
    '''a function that receives fruit color
    and returns the matching fruit
    '''
    if fruit_color == 'red':
        return 'apple'
    elif fruit_color == 'yellow':
        return 'banana'
    elif fruit_color == 'green':
        return 'melon'
    else:
        return 'I don\'t know'

result = which_fruit('yellow')
print(result)

#3.
def func_3(*args):
    if len(args) == 1:
        return args[0] ** 2
    elif len(args) == 2:
        return args[0] * args[1]
    else:
        return "Too many numbers!"
    
func_3(4, 2)

#4.
func_sum_sub = lambda x, y: (x+y, abs(x-y))
func_sum_sub(4, 50)

#5.
def num_pos_argument(*args):
    print(len(args))
    return len(args)

num_pos_argument(1, 'hello', 3)

#6.
[
 (lambda x, y: x * y)(x, y)
 for x in range(2, 10)
 for y in range(1, 10)
]