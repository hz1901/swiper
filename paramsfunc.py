def deco(params):     # params 为需要传入的参数
    print('floor1')
    def inner(func):
        print('floor2')
        def warp(*args, **kwargs):
            print('floor3')
            print('装饰开始')
            for i in range(params):
                func(*args, **kwargs)
            print('装饰结束')
            print('out3')
        print('out2')
        return warp
    print('out1')
    return inner


@deco(5)        #这个就是生成一个函数warp指向demo

def demo():
    print('ok')

if __name__ == '__main__':
    demo()
