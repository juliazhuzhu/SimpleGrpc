import collections
from collections import namedtuple

EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')
ll = []
c1 = EmployeeRecord('xiaoye', 43, 'engineer', 'r&d', 9)
c2 = EmployeeRecord('zhangsan', 45, 'engineer', 'r&d', 8)
c3 = EmployeeRecord('laoyao', 56, 'engineer', 'r&d', 11)

ll.append(c1)
ll.append(c2)
ll.append(c3)

print(c1.name)

data = [1,3,5,2,9]

data.sort()

print(data)

ll.sort(key=lambda x:x.paygrade)

for item in ll:
    print(item)


