def decorate_me(func): #func = tala ko message
    def inner_func():
        print("I'm a decorated function")
        func() ##function le tala ko message call garya cha
    return inner_func

###decorate_me le inner_fun return garcha
def message():
    print("Hello World")

nested_function_of_decorator = decorate_me(message)
nested_function_of_decorator()


def to_upper(func):
    def inner_func():
        value = func()
        return value.upper()
    return inner_func

def login_required():
    def inner_function():
        pw = input("Enter the passwprd:")
        if pw == "123":
            return func()
        else:
            return "Invalid password"
        return inner_function