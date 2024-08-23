#looping statements while and for
i = 6

while i<14:
    print(i)
    if i==10:
      break
    i+=1 # i = i+1

print("===============================")
i=6
while i<14:
   i+=1
   if i==10:
      continue
   print(i)

print("-----------------------------")
i=6
while i<14:
   i+=1
   if i<10:
      continue
   print(i)
else:
   b=9
   print("value of i is greater or equla to 14 now")

# for statement examples

colors = ["green", "blue", "red", "white", "yellow"]
fruits = ["apple", "banana", "cherry", "fig", "mango"]

name = " veera venkata satya narayana swami "
#  0123456789
for i in name:
   if i== 'a':
      continue
   print(i)

# range(5) - 0,1,2,3,4, range(0,5,1)= start-0, end -5, increm =1
# for(i=0; i<10; i+=3)

# for i in range(len(colors)):
   # print(colors[i])

# for i in colors:
   # print(i)

#for i in range(2,6):
#  print(i)

#for i in range(2,16,3):
#   print(i)

#for i in range(2,17,3):
#   print(i)

colors = ["green", "blue", "red", "white", "yellow"]
fruits = ["apple", "banana", "cherry", "fig", "mango"]

for i in colors:
   for j in fruits:
      print(i,j)