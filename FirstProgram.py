#FirstProgram.py
#Name: Pierce Limbo
#Date: 8/31/2025
#Assignment: Lab 1

from datetime import date, datetime


def main():
  print("First Program")
  #Say hello
  print("Hello")
  #Ask for the user's name
  user = input("Please enter your name: ")
  #Use the user's name in the program.
  print("Hello ", user)
  #Ask the user for their age.
age = input("How old are you?")
  #Tell the user what year they were born in.
  #Assume that they have not had their birthday yet this year.
birth = datetime.now().year - age
print("You were born in", birth)

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
