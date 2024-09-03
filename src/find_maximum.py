# Write a program to determine the maximum value in the list
# user input 2,55,7,23,89,68 . Hey 89 is the maximum value

# pseudo/ algorithm
'''
1. read input from user 
2. compare each element with other and find the highest value
3. we create a max_value and after each comparison we will store the maximum value into thos var
4. after all comp print max_value
''' 

# python Program
lista = list(map(int,input("Please Enter the values: ").split(",")))

#print(max(lista))
max_value = 0
for i in lista:
    if max_value < i:
        max_value = i
        
print(max_value)





