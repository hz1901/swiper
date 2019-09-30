def deco1(func):
    print('func 1 in')
    def wrapper1():
        print('wrap1 in')
        func()
        print('wrap1 out')
    print('func 1 out')
    return wrapper1

def deco2(func):
    print('func 2 in')
    def wrapper2():
        print('wrap2 in')
        func()
        print('wrap2 out')
    print('func 2 out')
    return wrapper2

@deco1
@deco2
def foo():
    print('foo')


if __name__ == '__main__':
    foo()
