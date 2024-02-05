import random
text="Welcome to my coding world !!"
text_splitted =text.split ("e")
print(text_splitted)# see if we put print("text_splitted") then it will generate only text_splitted to the output #
distance = len (text_splitted)
random_point = random.randint(0,distance-1)
print(f"{text_splitted[random_point]}")
