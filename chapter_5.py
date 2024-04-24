# r w >
"""
***9 Operator in python
1.Arithmetic Operator
2.Assignment Operator
3.Unary Minus Operator
4.Relational Operator
5.Logical Operator
6.Boolean Operator
7.Bitwise Operator
 ---Bitwise Complement Operator   [~]
 ---Bitwise AND Operator          [&]
 ---Bitwise OR Operator           [||] 
 ---Bitwise XOR Operator          [^]
 ---Bitwise Left Shift Operator   [<<]
 ---Bitwise  right Operator       [>>]
8.Membership Operator
--in Membership Operator
--not in Membership Operator
9.Identity Operators
-- is Identity Operators
-- is not Identity Operators
"""
#  ---Bitwise Complement Operator   [~]
x = 10
y = 11
print(~x)
print(x & y)
print(x | y)
print(x ^ y)
print(x << y)
print(x >> y)

names = ["Rani", "Yamini", "Susmita", "Veena"]
# --in Membership Operator
print("Rani" in names)
# --not in Membership Operator
print("Rani" not in names)

postal_code = {"Delhi": 11001, "Chenni": 60001, "Kolkata": 700001, "Bangalore": 560001}

for city in postal_code:
    print(city, postal_code[city])


a = 25
b = 25
print(id(a))
print(id(b))


# -- is Identity Operators
if a is b:
    print("a and b have same value")
else:
    print("a and b have not same value")
# -- is not Identity Operators
one = [1, 2, 3, 4]
two = [1, 2, 3, 4]
if one is two:
    print("one and two are same")
else:
    print("one and two are not  same")
print("The id of one", id(one))
print("The id of two", id(two))

if id(one) is id(two):
    print("They same ")
else:
    print("The not same")

if one == two:
    print("value same")
else:
    print("value not same")
##precendence
print(3 / 2 * 4 + 3 + (10 / 4) ** 3 - 2)

##Mathematics Function
import math as m
from math import sqrt, factorial, ceil
from math import floor
from math import degrees
from math import radians
from math import sin, cos, tan

x = m.sqrt(16)
print(x)
x = m.factorial(15)
print(x)
x = m.ceil(4.5)
print("ceil", x)
x = m.floor(4.5)
print("floor", x)
x = m.degrees(3.14159)
print("degrees", x)
x = m.radians(180)
print("radians", x)
x = m.sin(0.5)
print("sin", x)
x = m.cos(0.5)
print("cos", x)
x = m.tan(0.5)
print("tan", x)
x = m.exp(0.5)
print("exponential", x)
x = m.fabs(-4.56)
print("fabs", x)
x = m.fmod(3.5, 2)
print("f-mod", x)
x = m.fsum([3.3, 3.0, 2.4])
print("fsum", x)
x = m.modf(2.56)
print("modf", x)
x = m.log10(5.2345)
print("log", x)
x = m.log(5.5, 2)
print("log10", x)
x = m.pow(2, 3)
print("pow", x)
x = m.gcd(25, 30)
print("gcd", x)
x = m.trunc(15.5676)
print("trunc", x)
num = float("inf")
x = m.isinf(num)
print("isinf", x)
num = float("NaN")
x = m.isnan(num)
print("isnan", x)

"""
pi-3.141692
e-2.718281
inf-a floting-point posotive infinitive
nan- a flotinf point not a number
"""
