#Local Scope
#Enclosed Scope
#Global Scope
#Built-in Scope

y = 10
def outer():
    z = 4
    global y
    y = y+1
    print("inside the outer function y:", y)
    def inner():
        x=4
        nonlocal z
        print("inside the inner func z", z)
        z = z+1
        print("inside the inner func z", z)
        print("x:", x)

        global y
        y = y+1
        print("inside the function y:", y)
    inner()
    print("z:", z)
outer()