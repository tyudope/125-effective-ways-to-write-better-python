'''

a poorly constructed  if statement will raise a SyntaxError exception indicating what's wrong with the code
if True # -> BAD SYNTAX
    print("hello world")

1.3j5 # -> Bad Number


Unfortunately, that's about all the protection you can expect from Python before execution.
Anything beyond basic tokenization errors and parse errors will not be flagged as a problem.
'''

def bad_reference():
    print(my_var)
    my_var = 123

# bad_reference() -> raise an error.


def sometime_ok(x):
    if x:
        my_var = 123
    print(my_var)


sometime_ok(True) # won't raise an error because we'll define my_var


sometime_ok(False) # will raise and error because we wont't define my_var.


# Python also won't catch math error upfront. It would seem that this is cleary and error before the program executes.
def bad_math():
    return 16 / 0

# bad_math() will raise an Error. -> ZeroDivisionError: division by zero

