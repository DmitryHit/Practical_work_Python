def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg2 >= arg1 and arg3 >= arg1:
        return arg2 + arg3
    else:
        return arg1 + arg3


print(my_func(int(input("enter first argument ")), int(input("enter second argument ")),
              int(input("enter third argument "))))
