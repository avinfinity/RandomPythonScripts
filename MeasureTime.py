import time
a,b=10,20
start=time.time()
t=a
a=b
b=t
print(a,b)
end=time.time()
print("Time Taken to swap with temp variable", end-start)

start=time.time()
a,b=b,a
print(a,b)
end=time.time()
print("Time Taken to swap without temp variable", end-start)