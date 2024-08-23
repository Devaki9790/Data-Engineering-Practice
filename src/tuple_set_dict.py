x=(1,2,3,4,50)
#print(type(x))
y=[1,2,3,4,5]
#print(x[2])
y[2]=33
#print(y)
#x[2]=33
#print(x)
z=("string","character","python")
result=x+z
#result1=join(x,z)
print(result)
#print(result1)
#print(result.count(2))

#sets
x={"sai","apple","ball","apple",2,4,6,2,4}
#print(x)
x.add(3)
x.update(["g","t",1])
x.remove("apple")
#for element in x : 
#     print(element)

#dictionaries
z={"class":"python","year":2024,"time":7.44}
y={"class":"python","phone":"Iphone"}
print(y)
print(z)
print(z["time"])
print("-------------------")
v=z.get("time")
print(v)
print(z.keys())
print(z.values())
z["time"]=8.55
print(z)
z["month"]="August"
print(z)
z.update(y)
print(z)