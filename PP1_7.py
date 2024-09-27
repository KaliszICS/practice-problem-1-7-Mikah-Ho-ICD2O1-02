'''
  Lesson: Booleans
  Author: Mikah Ho
  Date Created: Sept 25, 2024
  Date Last Modified: Sept 26, 2024
'''

def q1():
  #Write code here
  boolean = True
  print(boolean)

def q2():
  #Write code here
  integer = input("Input an integer: ")
  integer = int(integer) > 5
  print(integer)

def q3():
  #Write code here
  letter = input("Input the letter a: ")
  letter = letter == "a"
  print(letter)

def q4():
  #Write code here
  word = input("Input a word earlier in the dictionary than google: ")
  word = word < "google"
  print(word)

def q5():
  #Write code here
  integer1 = input("Input an integer: ")
  integer2 = input("Input another integer: ")
  product = int(integer1) * int(integer2)
  product = product > 40
  print("Your numbers multiplied together are greater than 40: ", end="")
  print(product)

#Do edit the code below
#Comment the lines below when running your tests

# q1()
# q2()
# q3()
# q4()
# q5()
