def tmp(*args,**kwargs):
    print(args)
    print(kwargs)
    

c = {
    "d": 0,
    "b": 11,
    "b": 22,
}

tmp(1,2,c, b=5)