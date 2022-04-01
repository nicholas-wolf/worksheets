# Problems to solve

# 1. Reverse a string
# a. Write code that takes a string as input and returns the string reversed
# b. i.e. “Hello” will be returned as “olleH”

# def reverse_word(word):
    
#     new_list = list(reversed(word))
#     new_word = ""
#     for letter in new_list:
#         new_word = new_word + letter
#     return new_word


# print(reverse_word("hello"))

# 2. Capitalize letter
# a. Write code that takes a string as input and capitalize the first letter of each word.
#    Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World”

def capitalize_word(word):
   new_word = ""
   for place_in_string in range(0, len(word)):
       if place_in_string == 0:
        new_word += word[place_in_string].upper()
       elif word[place_in_string - 1] == " ":
            new_word += word[place_in_string].upper()
       else:
           new_word += word[place_in_string]
   
   
   return new_word



print(capitalize_word("hello world"))

# 3. Palindrome
# a. A word, phrase, or sequence that reads the same backward as forward i.e. madam
# b. Write code that takes a user input and checks to see if it is a Palindrome and reports the result

# def palindrome(word):
#     x = word
#     letter = ""
#     for letters in word:
#         letter = letters + letter
 
#     if (x == letter):
#         print("Yes")
#     else:
#         print("No")

# palindrome("madam")



# 4. BONUS CHALLENGE: Compress a string of characters
# a. For example, an input of "aaabbbbbccccaacccbbbaaabbbaaa" would compress to "3a5b4c2a3c3b3a3b3a"




# def string_compression(string):
#    new_string = ""
#    count = 1
#    for place_in_string in range(1, len(string)):
#       if string[place_in_string - 1] == string[place_in_string]:
#          count += 1
#       else:
#          new_string = new_string + string[place_in_string - 1]
#          if count > 1:
#             new_string += str(count)
#          count = 1
#    new_string = new_string + string[-1]
#    if count > 1:
#       new_string += str(count)
#    return new_string


# print(string_compression("aaabbb"))
