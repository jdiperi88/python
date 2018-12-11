x = 50


def func():
    global x
    x = 1000


print(x)
func()
print(x)
