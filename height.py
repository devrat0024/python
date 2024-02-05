#write a program for calculating average height from the given list of height
height_input = input("Enter the list of heights separated by commas: ")
height_list = height_input.split(",")
count = 0

for i in height_list:
    height_list[count] = int(i)
    count += 1

total = sum(height_list)
average = total / count
print("Total number of heights:", count)
print("Average height:", round(average))
