def print_twice(functionInput):
    def do_twice(*args, **kwargs):
        functionInput(*args, **kwargs)
        functionInput(*args, **kwargs)
    return do_twice

@print_twice
def doWork(data):
    print(data)

doWork("Work done")