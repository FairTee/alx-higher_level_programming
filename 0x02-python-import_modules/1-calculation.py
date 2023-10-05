#!//usr/bin/python3
a = 10
b = 5

from calculator_1 import add, sub, mul, div

add_result = add(a, b)
print("{} + {} = {}".format(a, b, add_result))

sub_result = sub(a, b)
print("{} - {} = {}".format(a, b, sub_result))

mul_result = mul(a, b)
print("{} * {} = {}".format(a, b, mul_result))

div_result = div(a, b)
print("{} / {} = {}".format(a, b, div_result))
