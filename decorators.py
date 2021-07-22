
def check_decorator(func):
    def decorated(**kwargs):
        if kwargs['x'] >= 0 and kwargs['y']>= 0:
            return func(**kwargs)
        else:
            print('error')

    return decorated

def login_decorator(func):
    def decorated(**kwargs):
        if kwargs['user'].is_authenticated:
            return func(**kwargs)
        else:
            print('error')

    return decorated

@check_decorator
@login_decorator
def triangle(x,y):
    print((x*y)/2)

@check_decorator
@login_decorator
def Quad(x,y):
    print(x*y)

x = int(input())
y= int(input())


class User:
    def __init__(self, auth):
        self.is_authenticated = auth


user = User(auth= False)

triangle(user, x,y)

Quad(user, x,y)

