try:
    x="a"
    y=0
    print(x/y)

except ZeroDivisionError:
    print("divided by zero")
   
except TypeError:
    print("types are not the same")
except NameError:
    print("name error")
except ArithmeticError:
    print("a error")



