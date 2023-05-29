from day_15.decorators import decorate_me, to_upper

@to_upper
def next_message():
    return "hello world"

print(next_message)

@to_upper
def next_message():
    return "python is awesome"

print(next_message)