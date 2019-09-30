def warp(func):
    print('我是装饰器，碰到需要装饰的函数，一开始执行这里')
    def inner(*args, **kwargs):
        print('这里才是真正的装饰开始！')
        res = func(*args, **kwargs)
        print('装饰结束')
        return res
    print('我这里是外围，先出去了，里面的等需要的时候执行')
    return inner

@warp   # 装饰器符号


def demo(x, y):
    return x + y

if __name__ == '__main__':
    demo(1, 2)