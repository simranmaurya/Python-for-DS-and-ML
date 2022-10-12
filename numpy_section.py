def somefunc(*args):
    for arg in args:
        return sum(args)

res = somefunc(1,2,3,4,5)

def kfunc(**kwargs):
    for k,v in kwargs.items():
        print(k, "is {}".format(v))

dic = { 'name' : 'Simran' , 'age' : 29}
kfunc(**dic)