# import time

# def timer(func):
#     start_time = time.time()
#     func()
#     end_time = time.time()
#     execution_time = end_time - start_time
#     print(execution_time)
#     return end_time
# @timer
# def test_fxn():
#     for i in range(100000000):
#         pass
#     return "Done!!"
#
# print(test_fxn)

import time
def exec_time(func):
    def inner_func():
        start = time.time()
        a = func()
        end = time.time()
        print(f"Execution time is {end-start}")
        return a
    return inner_func
@exec_time
def test_fxn():
   for i in range(100000000):
    pass
    return "Done!!"

print(test_fxn())