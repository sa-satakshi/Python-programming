a=input("data1:")
b=input("data2:")
a=a.split(",")
b=b.split(",")
d=dict(zip(a,b))
c=input("key:")
print("value:",d.get(c))