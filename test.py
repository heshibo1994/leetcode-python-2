x = 3
def f():
    global x
    if x<10:
        x= x+2
        print(x)
    else:
        return
    f()
f()