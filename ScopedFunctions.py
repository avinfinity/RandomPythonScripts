import time
def min(a,b):
        if a<b:
                return("a in Global")
        return("b in Global")

def   FunA():
        ctr=1;
        while ctr<100000: ctr+=1
        def min(a,b):
                if a<b:
                        return("a in FunA")
                return("b in FunA")
        def   FunB():
                ctr=1;
                while ctr<1000000: ctr+=1
                def min(a,b):
                        if a<b:
                                return("a in FunB")
                        return("b in FunB")
                def   FunC():
                        ctr=1;
                        while ctr<10000000: ctr+=1
                        def min(a,b):
                                ctr=1;
                                while ctr<100000000: ctr+=1
                                if a<b:
                                        return("a in FunC")
                                return("b in FunC")
                        print(min(10,20))
                FunC()
        FunB()

FunA()