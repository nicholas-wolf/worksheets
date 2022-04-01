# 1. Write a function that takes in a string of “Packers” and takes the first and last character of the string, concatenates them together to form a new string variable, then print that string to the console
# a. Expected outcome: “Ps”


def first_and_last(word):
    first_and_last_letter = word[0] + word[-1]
    print(first_and_last_letter)

first_and_last("Packers")    


# 2. Peanut Butter Jelly
# a. Write a function that prints every number from 0 to 100 to the console
# b. If a number is divisible by 3, print 'peanut butter’ instead of the number
# c. If a number is divisible by 5, print ‘jelly’ instead of the number
# d. If a number is divisible by 3 and 5, print ‘peanut butter jelly’ instead of the number


def pbj():
    for pbj in range(101):
        if pbj % 3 == 0 and pbj % 5 == 0:
            print("peanut butter jelly")   
        elif pbj % 3 == 0:
            print("peanut butter")
        elif pbj % 5 == 0:
            print("jelly")
        
           
    print(pbj)

pbj()



# 3. Write a function that takes in a single parameter called “word”. This parameter will be a string.
# a. Inside the function, create a variable called “final_result” and set it equal to an empty string.
# b. Loop over the letters in the word and append the letter and its index to the final_result variable.
# c. Print to the terminal the final_result variable.
# d. Example Input: “World Peace”
# e. Example Output: “W0o1r2l3d4 5P6e7a8c9e10”


def crazy_text(word):
    final_result = ""
    num = 0
    for letter in word:
            combined = letter + str(num)
            final_result = final_result + combined
            num = num + 1

    return final_result   


print(crazy_text("World Peace"))



   


# 4. Write a function that takes in a single parameter called “ingredients”. This parameter will be a List.
# a. Inside of the function, take user input that asks if the user knows what ingredient they want to search for
# b. Check the List parameter and see if the user’s input is an element in the List.
# i. If the ingredient is present, return the string ingredient from the function
# ii. If the ingredient is not there, ask the user if they want to search again and restart the operation

ingredients = ["salt", "pepper", "milk", "water"]

def check_ingredients(ingredients):
    user_ingredients = input("What ingredient do you want to search for?")
    for ingredient in ingredients:
        if user_ingredients == ingredient:
            return ingredient
    
    re_do = input("Do you want to search again?")
    if re_do == "y":
        check_ingredients(ingredients)


food = check_ingredients(ingredients)
print(food)


# 5. Write a function that takes in a list of strings, the logic of the function should reverse the order of the 
# values inside the list then return it back as a new list
# a. Note: Cannot use list.reverse() for this problem
# i. Input: [“Yellow”, “Purple”, “Orange”]
# ii. Output: [“Orange”, “Purple”, “Yellow”]

list = ["yellow", "purple", "orange"]

def reverse_list(list):
    new_list = list[::-1]
    return new_list
    
print(reverse_list(list))    



# 6. Write a function that takes in a single parameter called ‘names’.
# a. When you call the function, pass in a list containing 6 different names.
# b. The function should create and return a new list filled with any name from the ‘names’ parameter that 
# contains more than 4 characters.
# c. Ex Input: [‘Rebecca’, ‘Sam’, ‘Bob’, ‘Dante’, ‘Monica’, ‘Brad’]
# d. Ex Output: [‘Rebecca’, ‘Dante’, ‘Monica’]

names = ["Rebecca", "Sam", "Bob", "Dante", "Monica", "Brad"]

def my_func(names):
    new_list = []
    for name in names:
        name_list = len(name) 
        if name_list > 4:
            new_list.append(name)

    return new_list

print(my_func(names))    


