# write a python program to calculate student grades 

# I will give input as student score 88. If score > 90 he is A. > 80 < 90 grade is  B. > 70 <80 C.
#  D anf F below 40 he is F.

# psuedo Code / Algorithm
'''
1. Read the input and store in a variable score
2. If score is greater than 90 then print student grade is A
3. If score is greater than 80 and less than 90 then print grade is B
4.
5.
6. If score is less than 40 then grade is F
'''

# python program
score = int(input("please enter student score: "))

if score > 0:
    if score > 90:
        print("student grade is A")
    elif score >=70 and score <80:
        print("student grade is C")
    elif score >=40 and score <70:
        print("students grade is D")
    elif score>=80 and score <=90:
        print("student grade is B")
    else: 
        print("student grade is F")
else:
    print("Hey user! give me number greater than zero")



