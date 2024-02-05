numbers  = (12,34,2,1,452,45)
for i in numbers:
    print(i)
    if i==2: # in this actually it will stop the for loop till the i value is put and if we put all the value of i it would be print the else statement in the output 
        break # in this we use break so that it cannot moves to the next line  
else:
    print(" loop successfully completed and we are in if else ")