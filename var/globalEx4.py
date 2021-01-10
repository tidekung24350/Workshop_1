x = "1"


def myFunc4():
    global x
    print(x)
    x = "2"


myFunc4()
print(x)