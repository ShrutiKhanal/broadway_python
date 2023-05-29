# class Department:
#     def __init__(self, name, number_of_students):
#         self.name = name
#         self.number_of_student = number_of_students
#
#     def total_students(self, obj1, obj2):
#         return self.number_of_student + obj1.number_of_student + obj2.number_of_student
#
#
# d1 = Department("CS", 20)
# print(d1.number_of_student)
# d2 = Department("Math", 10)
# d3 = Department("Civil", 30)
#
# print(d1.total_students(d2, d3))

class Department:
    def __init__(self, name, number_of_students):
        self.name = name
        self.number_of_student = number_of_students

    def total_students(self, *args):
      students_list = []
      for obj in args:
            students_list.append(obj.number_of_student)
      students = sum(students_list)
      return self.number_of_student + students


d1 = Department("CS", 20)
print(d1.number_of_student)
d2 = Department("Math", 10)
d3 = Department("Civil", 30)
d4 = Department("Civil", 5)

print(d1.total_students(d2, d3, d4))