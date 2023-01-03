# Write an expression that calculates the average of 23, 32 and 64
# Place the expression in this print statement
import random
from ast import Num
from cgitb import html
from email.policy import default
from importlib.util import module_for_loader
from operator import length_hint
from py_compile import PycInvalidationMode
from tkinter import N

print("\nPRIMER EJERCICIO")


print((23 + 32 + 64) / 3)

# ------------------------------------------------------
print("\nSEGUNDO EJERCICIO")
# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall *= .9

# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall

# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume *= 1.05

# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume *= 0.95

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5

# print the new value of the reservoir_volume variable
print(reservoir_volume)

# -------------------------------------------------------
print("\nTERCER EJERCICIO")


age = 14

is_teen = age > 12 and age < 20
print(is_teen)
# -------------------------------------------------------

print("\nCUARTO EJERCICIO")

sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise
if (rio_de_janeiro_pop_density > san_francisco_pop_density):
    print(True)
else:
    print(False)
# -----------------------------------------------------------
print("\nQUINTO EJERCICIO")


coconut_count = "34"  # Dato curioso.
mango_count = "15"
tropical_fruit_count = coconut_count + mango_count
print(tropical_fruit_count)  # esto es una cadena y se imprime como 3415
# --------------------------------------------------------------

print("\nSEXTO EJERCICIO")


given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length = length_hint(
    given_name) + length_hint(middle_names) + length_hint(family_name) + 2

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)
# ---------------------------------------------------------------------------------------------------------------------------------------

print("\nSEPTIMO EJERCICIO")


mon_sales = 121
tues_sales = 105
wed_sales = 110
thurs_sales = 98
fri_sales = 95

# TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.

total_sales = 0

total_sales += mon_sales + tues_sales + wed_sales + thurs_sales + fri_sales
total_sales = str(total_sales)

print("This week's total sales: " + total_sales)
# ----------------------------------------------------------------------------------------------------------------------------------------

print("\nOCTAVO EJERCICIO")

verse = "If you can keep your head when all about you\n  Are losing \
theirs and blaming it on you,\nIf you can trust yourself when all men \
doubt you,\n  But make allowance for their doubting too;\nIf you can\
wait and not be tired by waiting,\n  Or being lied about, don’t \
deal in lies,\nOr being hated, don’t give way to hating,\n  And\
yet don’t look too good, nor talk too wise:"


# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!

print("The lenght of the string variable verse is {}".format(len(verse)))
print("The index of the first occurrence of the word and in 'verse' is {}".format(
    verse.find('and')))
print("The index of the last occurrence of the word 'you' in the verse is {}".format(
    verse.rfind('you')))
print("The count of occurences of the word 'you' in ther verse is {}".format(
    verse.count('you')))
# -------------------------------------------------------------------------------------------------------------------------------------------

print("\nNOVENO EJERCICIO")

month = 8
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# use list indexing to determine the number of days in month

num_days = days_in_month[0]

print(num_days)
# -------------------------------------------------------------------------------------------------
print("\nDECIMO EJERCICIO")

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']

# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3:])
# ------------------------------------------------------------------

print("\nONCEAVO EJERCICIO")

# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {'Shangai': 17.8,
              'Istanbul': 13.3,
              'Karachi': 13.0,
              'Mumbai': 12.5}

print(population)
# ---------------------------------------------------------------------------------------------------

print("\nDOCEAVO EJERCICIO")

# Test the code here if you'd like
a = [1, 2, 3]
b = a  # a and b are the same object, that's why it returns true
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)
# ---------------------------------------------------------------------------------------------------------------------------------------------

print("\nTRECEAVO EJERCICIO")  # Data structure: 'dictionary'

animals = {'dogs': [20, 10, 15, 8, 32, 15],
           'cats': [3, 4, 2, 8, 2, 4],
           'rabbits': [2, 3, 3],
           'fish': [0.3, 0.5, 0.8, 0.3, 1]}

print(animals['dogs'][3])

# This is known as a 'set' of elements
set_example = {'element1', 'element2', 'element3'}


elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},    # Compound dictionarys
            "helium": {"number": 2,
                       "weight": 4.002602,
                       "symbol": "He"}}
# ----------------------------------------------------------------------------------------------

print("\nCATORCEAVO EJERCICIO")

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True

print(elements['hydrogen']['is_noble_gas'])
print(elements['helium']['is_noble_gas'])
# -------------------------------------------------------------------------------------------------
print("\nQUINCEAVO EJERCICIO")

verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, '\n')

# split verse into list of words
verse_list = verse.split()
print(verse_list, '\n')

# convert list to a data structure that stores unique elements
verse_set = set(verse_list)
print(verse_set, '\n')

# print the number of unique words
num_unique = len(verse_set)
print(num_unique, '\n')

# -------------------------------------------------------------------------------------------
print("\nDIECISEIAVO")

verse_dict = {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1,
              'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

# find number of unique keys in the dictionary
num_keys = len(verse_dict)
print(num_keys)

# find whether 'breathe' is a key in the dictionary
contains_breathe = "whether" in verse_dict
print(contains_breathe)

# create and sort a list of the dictionary's keys
sorted_keys = sorted(verse_dict.keys())

# get the first element in the sorted list of keys
print(sorted_keys[0])

# find the element with the highest value in the list of keys
print(sorted_keys[-1])
# --------------------------------------------------------------------------------
print("\nDIECISIETEAVO EJERCICIO")

# First Example - try changing the value of phone_balance
phone_balance = 8
bank_balance = 50

if phone_balance < 10:
    phone_balance += 10
    bank_balance -= 10

print(phone_balance)
print(bank_balance)

# Second Example - try changing the value of number

number = 145
if number % 2 == 0:
    print("Number " + str(number) + " is even.")
else:
    print("Number " + str(number) + " is odd.")

# Third Example - try to change the value of age
age = 35

# Here are the age limits for bus fares
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

# These lines determine the bus fare prices
concession_ticket = 1.25
adult_ticket = 2.50

# Here is the logic for bus fare prices
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket

message = "Somebody who is {} years old will pay ${} to ride the bus.".format(
    age, ticket_price)
print(message)
# -----------------------------------------------------------------------------------------------------------
print("\nDIECIOCHOAVO EJERCICIO")

points = 123  # use this input to make your submission


# write your if statement here

if points <= 50:
    result = 'Congratulations! You won a wooden rabbit'
elif points <= 150:
    result = 'Oh dear, no prize this time'
elif points <= 180:
    result = 'Congratulations! You won a wafer-thin mind'
else:
    result = 'Congratulations! You won a penguin'

print(result)


# ------------------------------------------------------------------------------------------

print("\nDIECINUEVEAVO EJERCICIO")

# You decide you want to play a game where you are hiding
# a number from someone.  Store this number in a variable
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''
answer = 49
guess = 101

if guess < answer:
    result = "Oops!  Your guess was too low."
elif guess > answer:
    result = "Oops!  Your guess was too high."
elif guess == answer:
    result = "Nice!  Your guess matched the answer!"

print(result)
# ----------------------------------------------------------------------------------------

print("\nEJERCICIO 20")

# Depending on where an individual is from we need to tax them
# appropriately.  The states of CA, MN, and
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and
# the corresponding state to assure that they are taxed by the right
# amount.
# '''
state = "NY"
purchase_amount = 20

if state == 'CA':
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(
        state, total_cost)

elif state == "MN":
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(
        state, total_cost)

elif state == "NY":
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(
        state, total_cost)

print(result)
# --------------------------------------------------------------------------------------------------------------------------------------------
print("\nEJERCICIO 21")

points = 174
# establish the default prize value to None
prize = None
# use the points value to assign prizes to the correct prize names

if points <= 50:
    prize = 'wooden rabbit'
elif 151 <= points <= 180:
    prize = 'wafer-thin mint'
elif points >= 181:
    prize = 'penguin'


# use the truth value of prize to assign result to the correct prize
if prize:
    result = 'Congratulations! You won a penguin'
else:
    result = 'Oh dear, no prize this time'

print(result)
# ------------------------------------------------------------------------------------------

print("\nEJERCICIO 22")

sentence = ["the", "quick", "brown", "fox",
            "jumped", "over", "the", "lazy", "dog"]

# Write a for loop to print out each word in the sentence list, one word per

for i in sentence:
    print(i)
# ------------------------------------------------------------------------------------------------

print("\nEJERCICIO 23")

# Write a for loop using range() to print out multiples of 5 up to 30 inclusive

for i in range(5, 35, 5):
    print(i)
# ---------------------------------------------------------------------------------------------------------

print("\nEJERCICIO 24")

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here

for i in names:
    usernames.append(i.lower().replace(" ", "_"))

print(usernames)
# ----------------------------------------------------------------------------------------------------------

print("\nEJERCICIO 25")

usernames = ["Joey Tribbiani", "Monica Geller",
             "Chandler Bing", "Phoebe Buffay"]

# write your for loop here

for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(" ", "_")

print(usernames)
# -----------------------------------------------------------------------------------------------------------

print("\nEJERCICIO 26")

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1

print(count)
# ---------------------------------------------------------------------------------------------

print("\nEJERCICIO 27")

items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
# the characters that are after it in html_str are on the next line

# write your code here
for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)
# ----------------------------------------------------------

print("AREA DE PRÁCTICA\n")

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(range(4)))

print(list(range(4, 8)))

print(list(range(4, 10, 2)))

print(list(range(0, -5)))


colors = ['Red', 'Blue', 'Green', 'Purple']
lower_colors = []

for color in colors:
    lower_colors.append(color.lower())

print(lower_colors)

book_title = ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes',
              'the', 'great', 'gasby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin']

word_counter = {}

for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1

        # --------------------#
for word in book_title:
    word_counter[word] = word_counter.get(word, 0)+1

    # --------------------#
cast = {
    "Jerry Seinfeld": "Jerry Seinfeld",
    "Julia Louis-Dreyfus": "Elaine Benes",
    "Jason Alexander": "George Costanza",
    "Michael Richards": "Cosmo Kramer"
}

print("Iterating through keys:")
for key in cast:
    print(key)

print("\nIterating through keys and values:")
for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))

# -----------------------------------------------------------------------------------

print("\nEJERCICIO 28")

# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of 34
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Iterate through the dictionary
for object, count in basket_items.items():
    if object in fruits:
        result += count
print('There are {} fruits in the basket'.format(result))
# if the key is in the list of fruits, add the value (number of fruits) to result

# ------------------------#

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Iterate through the dictionary
for object, count in basket_items.items():
    if object in fruits:
        fruit_count += count
    elif object not in fruits:
        not_fruit_count += count

print('There are {} fruits in the basket. There are {} objects that are not fruits'.format(
    fruit_count, not_fruit_count))
# if the key is in the list of fruits, add to fruit_count.

# if the key is not in the list, then add to the not_fruit_count
# -----------------------------------------------------------------------------------------------------------------------------------------------------

print("\n EJERCICIO 29")
# number to find the factorial of
number = 6

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while current <= 6:
    # multiply the product so far by the current number
    product *= current
    # increment current with each iteration until it reaches number
    current += 1
# print the factorial of number
print(product)

# --------------------#

# number to find the factorial of
number = 6

# start with our product equal to one
product = 1

# write your for loop here
for num in range(2, number + 1):
    product *= num
# print the factorial of number
print(product)

# ----------------------#

start_num = 5
end_num = 30
count_by = 2

# write a while loop that uses break_num as the ongoing number to
#   check against end_num
break_num = start_num
while break_num <= 30:
    break_num += 2

print(break_num)
# -----------------------#

start_num = 1
end_num = 20
count_by = 2

# write a condition to check that end_num is larger than start_num before looping
if start_num > end_num:
    result = 'Oops! Looks like your start value is greater than the end value. Please try again.'
# write a while loop that uses break_num as the ongoing number to
break_num = start_num

while break_num < end_num:
    break_num += count_by
#   check against end_num
result = break_num

print(result)

# -------------------------#

limit = 40

# write your while loop here
num = 0

while (num+1)**2 < limit:
    num += 1
nearest_square = num**2

print(nearest_square)

# -------------------------#

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542,
            87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

count_odd = 0
list_sum = 0
i = 0
len_num_list = len(num_list)

while (count_odd < 5) and (i < len(num_list)):
    if num_list[i] % 2 != 0:
        list_sum += num_list[i]
        count_odd += 1
    i += 1

print("The numbers of odd numbers added are {}".format(count_odd))
print("the sum of the odd number added are {}".format(list_sum))
# ---------------------------------------------------------------------------------------------------

print("\nEJERCICIO NUMERO 30")

# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break


print(news_ticker)
# ----------------------------------------------------------------------------------

print("\nEJERCICIO 31")

# Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

# write your code here
# HINT: You can use the modulo operator to find a factor

for num in check_prime:
    for i in range(2, num):
        if (num % i) == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(
                num, i, num))
            break
        if i == num - 1:
            print("{} IS a prime number".format(num))
 # -----------------------------------------------------------------------------------------------------------

print("\nEjercicio 32")

names = ["Rick Sanchez", "Morty Smith",
         "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = ['rick', 'morty', 'summer', 'jerry', 'beth']
print(first_names)

# ----------------------#

multiples_3 = [3, 6, 9, 12, 15, 18, 21, 24, 27,
               30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]
print(multiples_3)

# ----------------------#

scores = {
    "Rick Sanchez": 70,
    "Morty Smith": 35,
    "Summer Smith": 82,
    "Jerry Smith": 23,
    "Beth Smith": 98
}

passed = ["Rick Sanchez", "Summer Smith", "Beth Smith"]
print(passed)
# --------------------------------------------------------------------------------------------------------------------

print("\nEJERCICIO 33")

nominated = {1931: ['Norman Taurog', 'Wesley Ruggles', 'Clarence Brown', 'Lewis Milestone', 'Josef Von Sternberg'], 1932: ['Frank Borzage', 'King Vidor', 'Josef Von Sternberg'], 1933: ['Frank Lloyd', 'Frank Capra', 'George Cukor'], 1934: ['Frank Capra', 'Victor Schertzinger', 'W. S. Van Dyke'], 1935: ['John Ford', 'Michael Curtiz', 'Henry Hathaway', 'Frank Lloyd'], 1936: ['Frank Capra', 'William Wyler', 'Robert Z. Leonard', 'Gregory La Cava', 'W. S. Van Dyke'], 1937: ['Leo McCarey', 'Sidney Franklin', 'William Dieterle', 'Gregory La Cava', 'William Wellman'], 1938: ['Frank Capra', 'Michael Curtiz', 'Norman Taurog', 'King Vidor', 'Michael Curtiz'], 1939: ['Sam Wood', 'Frank Capra', 'John Ford', 'William Wyler', 'Victor Fleming'], 1940: ['John Ford', 'Sam Wood', 'William Wyler', 'George Cukor', 'Alfred Hitchcock'], 1941: ['John Ford', 'Orson Welles', 'Alexander Hall', 'William Wyler', 'Howard Hawks'], 1942: ['Sam Wood', 'Mervyn LeRoy', 'John Farrow', 'Michael Curtiz', 'William Wyler'], 1943: ['Michael Curtiz', 'Ernst Lubitsch', 'Clarence Brown', 'George Stevens', 'Henry King'], 1944: ['Leo McCarey', 'Billy Wilder', 'Otto Preminger', 'Alfred Hitchcock', 'Henry King'], 1945: ['Billy Wilder', 'Leo McCarey', 'Clarence Brown', 'Jean Renoir', 'Alfred Hitchcock'], 1946: ['David Lean', 'Frank Capra', 'Robert Siodmak', 'Clarence Brown', 'William Wyler'], 1947: ['Elia Kazan', 'Henry Koster', 'Edward Dmytryk', 'George Cukor', 'David Lean'], 1948: ['John Huston', 'Laurence Olivier', 'Jean Negulesco', 'Fred Zinnemann', 'Anatole Litvak'], 1949: ['Joseph L. Mankiewicz', 'Robert Rossen', 'William A. Wellman', 'Carol Reed', 'William Wyler'], 1950: ['Joseph L. Mankiewicz', 'John Huston', 'George Cukor', 'Billy Wilder', 'Carol Reed'], 1951: ['George Stevens', 'John Huston', 'Vincente Minnelli', 'William Wyler', 'Elia Kazan'], 1952: ['John Ford', 'Joseph L. Mankiewicz', 'Cecil B. DeMille', 'Fred Zinnemann', 'John Huston'], 1953: ['Fred Zinnemann', 'Charles Walters', 'William Wyler', 'George Stevens', 'Billy Wilder'], 1954: ['Elia Kazan', 'George Seaton', 'William Wellman', 'Alfred Hitchcock', 'Billy Wilder'], 1955: ['Delbert Mann', 'John Sturges', 'Elia Kazan', 'Joshua Logan', 'David Lean'], 1956: ['George Stevens', 'Michael Anderson', 'William Wyler', 'Walter Lang', 'King Vidor'], 1957: ['David Lean', 'Mark Robson', 'Joshua Logan', 'Sidney Lumet', 'Billy Wilder'], 1958: ['Richard Brooks', 'Stanley Kramer', 'Robert Wise', 'Mark Robson', 'Vincente Minnelli'], 1959: ['George Stevens', 'Fred Zinnemann', 'Jack Clayton', 'Billy Wilder', 'William Wyler'], 1960: ['Billy Wilder', 'Jules Dassin', 'Alfred Hitchcock', 'Jack Cardiff', 'Fred Zinnemann'], 1961: ['J. Lee Thompson', 'Robert Rossen', 'Stanley Kramer', 'Federico Fellini', 'Robert Wise', 'Jerome Robbins'], 1962: ['David Lean', 'Frank Perry', 'Pietro Germi', 'Arthur Penn', 'Robert Mulligan'], 1963: ['Elia Kazan', 'Otto Preminger', 'Federico Fellini', 'Martin Ritt', 'Tony Richardson'], 1964: ['George Cukor', 'Peter Glenville', 'Stanley Kubrick', 'Robert Stevenson', 'Michael Cacoyannis'], 1965: ['William Wyler', 'John Schlesinger', 'David Lean', 'Hiroshi Teshigahara', 'Robert Wise'], 1966: ['Fred Zinnemann', 'Michelangelo Antonioni', 'Claude Lelouch', 'Richard Brooks', 'Mike Nichols'], 1967: ['Arthur Penn', 'Stanley Kramer', 'Richard Brooks', 'Norman Jewison', 'Mike Nichols'], 1968: ['Carol Reed', 'Gillo Pontecorvo', 'Anthony Harvey', 'Franco Zeffirelli', 'Stanley Kubrick'], 1969: ['John Schlesinger', 'Arthur Penn', 'George Roy Hill', 'Sydney Pollack', 'Costa-Gavras'], 1970: ['Franklin J. Schaffner', 'Federico Fellini', 'Arthur Hiller', 'Robert Altman', 'Ken Russell'], 1971: ['Stanley Kubrick', 'Norman Jewison', 'Peter Bogdanovich', 'John Schlesinger',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   'William Friedkin'], 1972: ['Bob Fosse', 'John Boorman', 'Jan Troell', 'Francis Ford Coppola', 'Joseph L. Mankiewicz'], 1973: ['George Roy Hill', 'George Lucas', 'Ingmar Bergman', 'William Friedkin', 'Bernardo Bertolucci'], 1974: ['Francis Ford Coppola', 'Roman Polanski', 'Francois Truffaut', 'Bob Fosse', 'John Cassavetes'], 1975: ['Federico Fellini', 'Stanley Kubrick', 'Sidney Lumet', 'Robert Altman', 'Milos Forman'], 1976: ['Alan J. Pakula', 'Ingmar Bergman', 'Sidney Lumet', 'Lina Wertmuller', 'John G. Avildsen'], 1977: ['Steven Spielberg', 'Fred Zinnemann', 'George Lucas', 'Herbert Ross', 'Woody Allen'], 1978: ['Hal Ashby', 'Warren Beatty', 'Buck Henry', 'Woody Allen', 'Alan Parker', 'Michael Cimino'], 1979: ['Bob Fosse', 'Francis Coppola', 'Peter Yates', 'Edouard Molinaro', 'Robert Benton'], 1980: ['David Lynch', 'Martin Scorsese', 'Richard Rush', 'Roman Polanski', 'Robert Redford'], 1981: ['Louis Malle', 'Hugh Hudson', 'Mark Rydell', 'Steven Spielberg', 'Warren Beatty'], 1982: ['Wolfgang Petersen', 'Steven Spielberg', 'Sydney Pollack', 'Sidney Lumet', 'Richard Attenborough'], 1983: ['Peter Yates', 'Ingmar Bergman', 'Mike Nichols', 'Bruce Beresford', 'James L. Brooks'], 1984: ['Woody Allen', 'Roland Joffe', 'David Lean', 'Robert Benton', 'Milos Forman'], 1985: ['Hector Babenco', 'John Huston', 'Akira Kurosawa', 'Peter Weir', 'Sydney Pollack'], 1986: ['David Lynch', 'Woody Allen', 'Roland Joffe', 'James Ivory', 'Oliver Stone'], 1987: ['Bernardo Bertolucci', 'Adrian Lyne', 'John Boorman', 'Norman Jewison', 'Lasse Hallstrom'], 1988: ['Barry Levinson', 'Charles Crichton', 'Martin Scorsese', 'Alan Parker', 'Mike Nichols'], 1989: ['Woody Allen', 'Peter Weir', 'Kenneth Branagh', 'Jim Sheridan', 'Oliver Stone'], 1990: ['Francis Ford Coppola', 'Martin Scorsese', 'Stephen Frears', 'Barbet Schroeder', 'Kevin Costner'], 1991: ['John Singleton', 'Barry Levinson', 'Oliver Stone', 'Ridley Scott', 'Jonathan Demme'], 1992: ['Clint Eastwood', 'Neil Jordan', 'James Ivory', 'Robert Altman', 'Martin Brest'], 1993: ['Jim Sheridan', 'Jane Campion', 'James Ivory', 'Robert Altman', 'Steven Spielberg'], 1994: ['Woody Allen', 'Quentin Tarantino', 'Robert Redford', 'Krzysztof Kieslowski', 'Robert Zemeckis'], 1995: ['Chris Noonan', 'Tim Robbins', 'Mike Figgis', 'Michael Radford', 'Mel Gibson'], 1996: ['Anthony Minghella', 'Joel Coen', 'Milos Forman', 'Mike Leigh', 'Scott Hicks'], 1997: ['Peter Cattaneo', 'Gus Van Sant', 'Curtis Hanson', 'Atom Egoyan', 'James Cameron'], 1998: ['Roberto Benigni', 'John Madden', 'Terrence Malick', 'Peter Weir', 'Steven Spielberg'], 1999: ['Spike Jonze', 'Lasse Hallstrom', 'Michael Mann', 'M. Night Shyamalan', 'Sam Mendes'], 2000: ['Stephen Daldry', 'Ang Lee', 'Steven Soderbergh', 'Ridley Scott', 'Steven Soderbergh'], 2001: ['Ridley Scott', 'Robert Altman', 'Peter Jackson', 'David Lynch', 'Ron Howard'], 2002: ['Rob Marshall', 'Martin Scorsese', 'Stephen Daldry', 'Pedro Almodovar', 'Roman Polanski'], 2003: ['Fernando Meirelles', 'Sofia Coppola', 'Peter Weir', 'Clint Eastwood', 'Peter Jackson'], 2004: ['Martin Scorsese', 'Taylor Hackford', 'Alexander Payne', 'Mike Leigh', 'Clint Eastwood'], 2005: ['Ang Lee', 'Bennett Miller', 'Paul Haggis', 'George Clooney', 'Steven Spielberg'], 2006: ['Alejandro Gonzaalez Inarritu', 'Clint Eastwood', 'Stephen Frears', 'Paul Greengrass', 'Martin Scorsese'], 2007: ['Julian Schnabel', 'Jason Reitman', 'Tony Gilroy', 'Paul Thomas Anderson', 'Joel Coen', 'Ethan Coen'], 2008: ['David Fincher', 'Ron Howard', 'Gus Van Sant', 'Stephen Daldry', 'Danny Boyle'], 2009: ['James Cameron', 'Quentin Tarantino', 'Lee Daniels', 'Jason Reitman', 'Kathryn Bigelow'], 2010: ['Darren Aronofsky', 'David O. Russell', 'David Fincher', 'Ethan Coen', 'Joel Coen', 'Tom Hooper']}
winners = {1931: ['Norman Taurog'], 1932: ['Frank Borzage'], 1933: ['Frank Lloyd'], 1934: ['Frank Capra'], 1935: ['John Ford'], 1936: ['Frank Capra'], 1937: ['Leo McCarey'], 1938: ['Frank Capra'], 1939: ['Victor Fleming'], 1940: ['John Ford'], 1941: ['John Ford'], 1942: ['William Wyler'], 1943: ['Michael Curtiz'], 1944: ['Leo McCarey'], 1945: ['Billy Wilder'], 1946: ['William Wyler'], 1947: ['Elia Kazan'], 1948: ['John Huston'], 1949: ['Joseph L. Mankiewicz'], 1950: ['Joseph L. Mankiewicz'], 1951: ['George Stevens'], 1952: ['John Ford'], 1953: ['Fred Zinnemann'], 1954: ['Elia Kazan'], 1955: ['Delbert Mann'], 1956: ['George Stevens'], 1957: ['David Lean'], 1958: ['Vincente Minnelli'], 1959: ['William Wyler'], 1960: ['Billy Wilder'], 1961: ['Jerome Robbins', 'Robert Wise'], 1962: ['David Lean'], 1963: ['Tony Richardson'], 1964: ['George Cukor'], 1965: ['Robert Wise'], 1966: ['Fred Zinnemann'], 1967: ['Mike Nichols'], 1968: ['Carol Reed'], 1969: ['John Schlesinger'], 1970: ['Franklin J. Schaffner'], 1971: [
    'William Friedkin'], 1972: ['Bob Fosse'], 1973: ['George Roy Hill'], 1974: ['Francis Ford Coppola'], 1975: ['Milos Forman'], 1976: ['John G. Avildsen'], 1977: ['Woody Allen'], 1978: ['Michael Cimino'], 1979: ['Robert Benton'], 1980: ['Robert Redford'], 1981: ['Warren Beatty'], 1982: ['Richard Attenborough'], 1983: ['James L. Brooks'], 1984: ['Milos Forman'], 1985: ['Sydney Pollack'], 1986: ['Oliver Stone'], 1987: ['Bernardo Bertolucci'], 1988: ['Barry Levinson'], 1989: ['Oliver Stone'], 1990: ['Kevin Costner'], 1991: ['Jonathan Demme'], 1992: ['Clint Eastwood'], 1993: ['Steven Spielberg'], 1994: ['Robert Zemeckis'], 1995: ['Mel Gibson'], 1996: ['Anthony Minghella'], 1997: ['James Cameron'], 1998: ['Steven Spielberg'], 1999: ['Sam Mendes'], 2000: ['Steven Soderbergh'], 2001: ['Ron Howard'], 2002: ['Roman Polanski'], 2003: ['Peter Jackson'], 2004: ['Clint Eastwood'], 2005: ['Ang Lee'], 2006: ['Martin Scorsese'], 2007: ['Ethan Coen', 'Joel Coen'], 2008: ['Danny Boyle'], 2009: ['Kathryn Bigelow'], 2010: ['Tom Hooper']}

# Question 1A: Create dictionary with the count of Oscar nominations for each director
nom_count_dict = {}
# Add your solution code below before line 10. Add more lines for your code as needed.
for year, list_dir in nominated.items():
    for director in list_dir:
        if director not in nom_count_dict:
            nom_count_dict[director] = 1
        else:
            nom_count_dict[director] += 1


print("nom_count_dict = {}\n".format(nom_count_dict))
###################################################################################################################
###################################################################################################################

# Question 1B: Create dictionary with the count of Oscar wins for each director
win_count_dict = {}
# Add your solution code below before line 20. Add more lines for your code as needed.
for year, winnerlist in win_count_dict.items():
    for winner in winnerlist:
        win_count_dict[winner] = win_count_dict.get(winner, 0) + 1

print("win_count_dict = {}".format(win_count_dict))

# ------------------------------------------------------------------------------------------------------------------------------------------------

print("\nFUNCTIONS IN PYTHON\n")

# this prints something, but does not return anything


def population_density(population, land_area):
    return population / land_area


test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))

# -----------------------#


def readable_timedelta(days):
    weeks = days // 7

    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)


# test your function
print(readable_timedelta(34))

# --------------------------------------------------------------------------------------------------------------

print('\nEJERCICIO 1')

egg_count = 0


def buy_eggs(count):
    return count + 12


egg_count = buy_eggs(egg_count)
print(egg_count)

# -----------------------#
"""hola, esto es un docstring"""


def multiply(x, y): return x * y


print(multiply(20, 3))

# ------------------------#

numbers = [
    [34, 63, 88, 71, 29],
    [90, 78, 51, 27, 45],
    [63, 37, 85, 46, 22],
    [51, 22, 34, 11, 18]
]
# Expresion lambda

averages = list(map(lambda x: sum(x) / len(x), numbers))
print(averages)

# --------------------------#

cities = ["New York City", "Los Angeles",
          "Chicago", "Mountain View", "Denver", "Boston"]

short_cities = list(filter(lambda x: len(x) < 10, cities))
print(short_cities)

print("\n")


def greeting(name):
    print("Hello! How are you today {}?".format(name.title()))


greeting("Daniela")


# -------------------------------------------------------------------------------------------------------------------------------------------------


f = open('borrarlo.txt', 'r')
file_data = f.read()
f.close()

print(file_data)
# ----------#
# Esta 'with'palabra clave le permite abrir un archivo, realizar operaciones en él y cerrarlo automáticamente después de ejecutar el código sangrado, en este caso, leyendo el archivo. ¡Ahora, no tenemos que llamar a f.close()! Solo puede acceder al objeto de archivo, f, dentro de este bloque sangrado.
with open('borrarlo.txt', 'r') as f:
    file_data = f.read()
# ---------------------------- ---------------------------------------------------------------------------------------

f1 = open("camelot.txt", 'r')
file_data1 = f1.read()
f1.close()
print(file_data1)

camelot_lines = []

with open("camelot.txt", 'r') as f1:
    for line in f1:
        camelot_lines.append(line.strip())

print(camelot_lines)
# -------------------------------------------------------------------------------------------------

print("\nEJERCICIO 2")


def create_cast_list(filename):
    cast_list = []
    # use with to open the file filename
    with open(filename) as f:
        # use the for loop syntax to process each line
        for line in f:
            name = line.split(",")[0]
        # and add the actor name to cast_list
            cast_list.append(name)

        return cast_list


cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
# --------------------------------------------------------------------------------------------

print('\nEJERCICIO 3')

# TODO: First import the `random` module

# We begin with an empty `word_list`
word_file = "words.txt"
word_list = []

# We fill up the word_list from the `words.txt` file
with open(word_file, 'r') as words:
    for line in words:
        # remove white space and make everything lowercase
        word = line.strip().lower()
        # don't include words that are too long or too short
        if 3 < len(word) < 8:
            word_list.append(word)

# TODO: Add your function generate_password below


def generate_password():
    # It should return a string consisting of three random words
    # concatenated together without spaces
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)


print(generate_password())
# ---------------------------------------------------------------------------------------------------------------
