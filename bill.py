import random 
names=input ("enter everbody's names separated by comma :")
names_list =names.split(",")
length = len (names_list)
random_choice = random.randint(0,length-1)
print(f"{names_list[random_choice]}will pay the whole bill ") 