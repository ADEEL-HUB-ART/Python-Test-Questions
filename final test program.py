# QUESTION NO 01

# Write a function which will take an integer as input and print each digit in a separate line. You are not
#  allowed to use str or any other method  will convert the integer into string.  Done

def print_digits(n):
    while n != 0:
        digit = n % 10
        print(digit)
        n = n // 10

nums = int(input("Enter the numbers:"))
print_digits(nums)


# QUESTION NO 02
# You are given words. Some words may repeat. For each word, output its number of occurrences.
# The output order should correspond with the input order of appearance of the word.  Done

from collections import Counter

def count_word_occurrences(words):
    word_count = Counter(words)
    print(len(word_count))  
    print(' '.join(map(str, word_count.values())))  
    return word_count

words = ["apple", "banana", "apple", "apple", "banana", "orange"]
word_count = count_word_occurrences(words)
     

# QUESTION NO 03 
#You are given a positive integer. You can only use one for loop and one print statement.
#  Print a numerical triangle of height like the one below:     



for i in range(1,5):
    print(str(i)*i)



# QUESTION NO 04
# You are given a string. Suppose a character ‘c’ occurs 4 times in the string.
# Replace these consecutive occurrences of the character 'c' with (4, c) in the string.              ***

from itertools import groupby

def replace_consecutive_occurances(input_string):
    result  = []

    for char, group in groupby(input_string):
        count = len(list(group))
        result.append(f"({count},{char})")

    return "".join(result)

input_str = "1222311"
output_str = replace_consecutive_occurances(input_str)
print(output_str)  

# QUESTION NO 05
# Remove symbols from the string                       ***

def remove_symbols(input_string):
    symbols = "!@#$%^&*()_-+=<>?,.;:{}[]"
    
    for symbol in symbols:
        input_string = input_string.replace(symbol, "")
    
    return input_string

input_string = "Hello! How are you? This is an example string with symbols: !@#$%^&*()_-+=<>?,.;:{}[]"
result = remove_symbols(input_string)
print("Original string:", input_string)
print("String with symbols removed:", result) 


# QUESTION NO 06
# 
# You get an array of numbers, and return the sum of all of the positive ones.
# Example [1, -4, 7, 12] => 1+7+12 = 20.# If there is nothing to sum return 0. You can not use the if statement.\

def sum_positive_numbers(arr):
    return sum([num for num in arr if num > 0])

nums = [1,-4,7,12]
result = sum_positive_numbers(nums)
print(result)



# QUESTION NO 07 
# Sum all the numbers of a given array ( cq. list ), except # the highest and the lowest element 
#  ( by value, not by index! ). You can not use the if statement.

def sum_except_high_low(arr):
    
    arr_sorted = sorted(arr)
    arr_filtered = arr_sorted[1:-1]

    return sum(arr_filtered)

arr =  [ 1 , 5 , 2 , 9 , 3]   
result = sum_except_high_low(arr)
print(result)

# QUESTION NO 08
# Calculate total score                                 ***

def calculate_points(match_results):                   

    total_points = 0

    for result in match_results:
        x,y = map(int,result.split(':'))

        if x > y:
            total_points += 3
        if x < y:
            total_points += 1

    return total_points        
matches = ["3:1","0:0","2:4","1:1","4:0"]
total_points = calculate_points(matches)
print(f"total_points:{total_points}")

# QUESTION NO 09
# Complete the function that accepts a string parameter, and reverses each word in the string. 
# All spaces in the string should be retained.

def reverse_words(sentence):
    words = sentence.split(' ')  
    reversed_words = [word[::-1] for word in words]  
    reversed_sentence = ' '.join(reversed_words)  
    return reversed_sentence

input_string = "Hello world! how are you."
reversed_string = reverse_words(input_string)
print("Original string:", input_string)
print("Reversed string:", reversed_string)


# QUESTION NO 10
# You are going to be given a word. Your job is to return the middle character of the word.
#  If the word's length is odd, return the middle character. 
# If the word's length is even, return the middle 2 characters.

def get_middle_char(word):
    length = len(word)
    middle_index = length // 2

    if length % 2 == 1:
        return word[middle_index]
    else:
        return word[middle_index -1 : middle_index +1]

word1 = "ADEEL UR REHMAN"
word2 = "ABDULREHMAN"

print(f"get middle char of '{word1}'is '{get_middle_char(word1)}'")
print(f"get middle char of '{word2}'is '{get_middle_char(word2)}'")


# QUESTION NO 11
# You are given an array(list) strarr of strings and an integer k. 
# Your task is to return the first longest string consisting of k consecutive strings taken in the array.  ***

def longest_consecutive_strings(strarr,k):
    if k > len(strarr):
        return ""

    longest_str = ""
    temp_str = ""
    for i in range(len(strarr) - k +1) :
        temp_str = ''.join(strarr[i:i+k])
        if len (temp_str) > len(longest_str):
            longest_str = temp_str
    return longest_str

result =longest_consecutive_strings(["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2)
print(result)


# QUESTION NO 12

def order_words(s):
    words = s.split()
    result = [''] * len(words)
    for word in words:
        for char in word:
            if char.isdigit():
                result[int(char) - 1] = word
    return ' '.join(result)

print(order_words("is2 Thi1s T4est 3a"))


# QUESTION NO 13
# Your task is to create a program which will play Rock Paper Scissors with the user.Take input from the user
# for his/her selection like scissors/rock/paper. Program should select randomly rock/paper/scissors.
# Output should be indicating who won the user or computer. 

import random
choices = ["rock","paper","scissors"]
computer = random.choice(choices)
user = input("Enter your Choice:").lower()
if user not in choices:
    print("invalid input")
else:
    print(f"computer chose:{computer}")
    if user == computer:
        print("it is draw")
    elif(user == "rock" and computer == "scissors") or(user == "scissors" and computer == "paper") or(user == 
     "scissors" and computer == "paper") or(user == "paper" and computer == "rock"):     
         print("hurraw you win")
    else:
        print("ooh you lose")         

# QUESTION NO 14
# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without
# any elements with the same value next to each other and preserving the original order of elements.
def unique_in_order(sequence):
    if not sequence:
        return []
    
    result = [sequence[0]]
    for item in sequence [1:]:
        if item.lower() != result[-1].lower():
             result.append(item)

    return result 
print(unique_in_order('AAAABBBCCDAABBB'))  


# QUESTION NO 15
# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or 
#  or exactly 6 digits.If the function is passed a valid PIN string, return true, else return false.

def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        if pin.isdigit():
            return True
    return False

print(validate_pin("1234"))  
print(validate_pin("12345"))  
print(validate_pin("123456"))  
print(validate_pin("123abc")) 

# QUESTION NO 16
# Complete the solution so that the function will break up camel casing, using a space between words.

def break_camel_case(text):
    result = ""
    for char in text:
        if char.isupper():
            result += "" + char.lower()
        else:
            result += char
    return result


print(break_camel_case("identifier"))            


# QUESTION NO 18
# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.
# The function should return true if the string is valid, and false if it's invalid.

def valid_parantheses(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

print(valid_parantheses("()"))            
print(valid_parantheses("((()))"))            
print(valid_parantheses("(())"))            
print(valid_parantheses(")(())("))            
print(valid_parantheses("(()()"))            
































