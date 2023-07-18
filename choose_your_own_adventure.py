name = input("Type your name: ")
print("Welcome", name, "to this adventure! Good luck!")

small_bag = "25 gold pieces, a pocketwatch, a photo of your family, and an elaborately crafted pen."
medium_bag = "3 pieces of burnt toast, a lockpick, half a bottle of water, and a blueprint for a trebuchet."
large_bag = "50 gold pieces, a lockpick, a small dagger, a small length of rope, mirrored sunglasses, and a small bottle of rum."

user_bag = []
answer = input("Before you embark you grab a pre-made satchel to assist in your adventure. There is a small, ornate one made of dark leather. A medium-sized one made of coarse burlap with the words JERRYS DO NOT TOUCH! written on it. The last satchel is a large plain bag with nothing descriptive on it. Which do you choose (small/medium/large) " ).lower()

def bag_check():
    if small_bag in user_bag:
        print("You look into your bag and find:", str(user_bag) + ".")
    if medium_bag in user_bag:
        print("You look into your bag and find:", str(user_bag) + ".")
    if large_bag in user_bag:
        print("You look into your bag and find:", str(user_bag) + ".")

if answer == "small":
    print("You grab the small bag and head for the door. Checking to make sure you outfit is complete.")
    user_bag.append(small_bag)
elif answer == "medium":
    print("You've never heard of this Jerry fellow before, why should you care if this bag supposedly belongs to him?! You walk smugly out the door.")
    user_bag.append(medium_bag)
elif answer == "large":
    print("You pick up the large bag, happily attach it to your person and set off for adventure! The stories are more important to you than some silly earthly possessions anyway.")
    user_bag.append(large_bag)
else:
    print("You are spoiled for choice and cannot choose. Instead you grab nothing and rush out the door.")

answer = input("You are on a dirt road that forks to the left and right. Which way would you like to go? (left/right)? ").lower()

if answer == "left":
    answer = input("You walk to the left and see that everything looks charred and burnt. After walking for quite some time, you approach the remnants of a large chest with a shiny padlock. What do you do? (ignore/smash/use item)? ").lower()

    if answer == "ignore":
        print("You are too busy looking at the treetops to notice the chest and continue walking. You walk so far that you find yourself back at home. Goodbye traveler.")
    elif answer == "smash":
        answer = input("You attempt to smash through the burnt chest to open it. The chest crumbles easily under your weight and inside you see a small, silver box. Do you take it? (yes/no)? ").lower()
        if answer == "yes":
            print("As you begin pulling the silver box from the chest, you hear a whistle sounding. Faintly at first but soon growing to an ear piercing volume. You soon lose consciousness. The last thing you see are the words,'Protected by Falcons' engraved on the box.")
        if answer == "no":
            print("You know better than to pick up a duck in a dungeon and leave the box alone. ")
    # TODO: Finish fleshing out new options
    elif answer == "use item":
        bag_check()
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back)? ").lower()

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? (yes/no)? ").lower()

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print("Not a valid option. You lose.")

    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")

print("Thank you for trying", name + "!")