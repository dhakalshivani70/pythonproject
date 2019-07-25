def add(*args):
    num = 0
    for number in args:
         num += number

    return num



print(add(1,2,3))
print(add(1,2,3,4,5))