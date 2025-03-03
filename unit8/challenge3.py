'''
Micah Kennedy
3/3/2025
Pd 1-2
'''


#Original function
def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')

do_twice(print_spam)
print("In the original version, spam is printed twice.\n")

#Modified do_twice
def do_twice(f, v):
    f(v)
    f(v)

#More general version
def print_twice(s):
    print(s)
    print(s)

#Modified do_twice + print_twice testing
do_twice(print_twice, "spam")
print("With modified do_twice + print_twice, spam is printed four times.\n")

#New do_four
def do_four(f, v):
    do_twice(f, v)
    do_twice(f, v)

#New do_four testing
do_four(print_twice, 'spam')
print("With do_four, print_twice is called four times making a total of 8 times that spam is printed.")
