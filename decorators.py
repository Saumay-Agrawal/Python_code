"""This python file is meant to deal with the menace creating but very useful decorators.
Take 'em all down."""

"""1. An ordinary decorator."""

def decorate(func):

    def confirm():
        print('The function is decorated successfully.')
        func()
    
    return confirm

@decorate
def to_be_decorated():
    print('I am going to be decorated. yeeeeeei!')

to_be_decorated()

