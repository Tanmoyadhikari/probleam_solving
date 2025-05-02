from palindrom import IsPalindrom
from twonumsum import Twonum

#Testing Instance ...
obj1 = IsPalindrom(121)
obj3 = IsPalindrom(175)

print(obj1.checknum())
print(obj3.checknum())

test1 = Twonum(6)
test2 = Twonum(21)
test3 = Twonum(22)
test4 = Twonum(23)
test5 = Twonum(24)
test6 = Twonum(101)
print(test1.test())
print(test2.test())
print(test3.test())
print(test4.test())
print(test5.test())
print(test6.test())
