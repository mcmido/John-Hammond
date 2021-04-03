class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay,):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return ' {} {} '.format(self.first, self.last,)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('cory', 'schafer', 50000)
emp_2 = Employee('test', 'User', 60000)


print(Employee.__dict__)
# print(emp_1)
# print(emp_2)
# print(emp_2.last, emp_1.email)

# emp_1.first = 'Corey'
# emp_1.last = 'Ahmed'
# emp_1.email = 'Corey.Ahmed@gmail.com'
# emp_1.pay = 50000
#
# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.test@gmail.com'
# emp_2.pay = 60000

# print(emp_1.email)
# print(emp_2.email)

# print(' {} {} {} {} '.format(emp_1.first,emp_1.last, emp_2.pay,emp_2.email))

# print(emp_2.fullname())
# emp_1.fullname()
# print(Employee.fullname(emp_1))
#
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)


# class HQ:
#     def __init__(self, name, last):
#         self.fname = name
#         self.last = last
#
#     def fullname(self):
#         print(self.fname, self.last)
#         return "COOOL"
#
# hq = HQ('mohamed', 'Ahmed')
# HQ.fullname(hq)
# print(hq.fullname())