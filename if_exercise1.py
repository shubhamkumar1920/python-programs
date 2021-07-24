# number guessing game
# make a variable,like winning and assign any number to it
# ask user to guess a anumber
# if user gussed correctly then print"you win
# if user didn't gussed correctly then
# if user gussed lower than actual number then print "too low"
# if user gussed higher than actual number then  print "too high"

# google "how to generate random number in python" to generate random
# winning number

# soln:-

winning_number =27
user_input = input("guess a number b/w 1 and 100: ")
user_input = int(user_input)
if user_input==winning_number:
    print("you win!!!")
else:
    if user_input < winning_number:
        print("too low")
    else:
        print("too high")