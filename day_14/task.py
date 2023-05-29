student = [{"name": "Jon", "age": 19},
            {"name": "Jane", "age": 45},
            {"name": "Harry", "age": 15},
            {"name": "Arya", "age": 34}
            ]
#
# def get_even_nums(data):
#     return data % 2 == 0
# #or
#
# result = filter(lambda data: data % 2 == 0, a)
# print(list(result))

def less_than_twe(age):
    return age < 20

result = filter(lambda data: data['age'] < 20, student)
print(list(result))


a = [1, 2, 3, 4]
result =  map(lambda x: x ** 2, a)
print(list(result))


a = [1, 5, 3, 15, 9, 10]
result = filter(lambda x : x % 5 == 0, a)
print(list(result))