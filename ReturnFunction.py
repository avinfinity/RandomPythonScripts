def returnFuncToExecute():
    def returnFunc(data):
        print(data)
    return returnFunc


returnFunc = returnFuncToExecute()

print(returnFunc)

returnFunc("Print this")
