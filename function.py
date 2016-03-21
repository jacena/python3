def my_test(x):
    if x>=5:
        print(3)
        return x
    else:
        print(4)
        return -x

num = input('type a num:')
num = int(num)

my_test(num)
