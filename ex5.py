name = "Jorge Vergara"
age = 35 # not a lie
height = 188 # cm
height_in_inches = height / 2.84
weight = 130 #kgs
weight_in_pounds = weight * 2.20
eyes = "Brown"
teeth = "White"
hair = "Black"

print(f"Let's talk about {name}")
print(f"He is {height} cm tall.")
print(f"He is {weight} kgs heavy.")
print("It is too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee")

# This line is tricy, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}")
print(f"If I change my weight to pounds it'll be {round(weight_in_pounds)}, and my height in inches would be {round(height_in_inches)}")

