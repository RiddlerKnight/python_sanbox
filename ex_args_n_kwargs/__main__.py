def f(*args, **kwargs):
    print("Positional Args:", args)
    print("Positional kwargs:", kwargs)

f(100, 75, 50, 25, 0)

f(gold=10, sliver=20, platinum=30)
