number_of_gusses = 1
print("number_of_gusses is limited to only 9 times: ")
while (number_of_gusses <= 9):
     guess_number = int(input("Guess the number: \n"))
     if guess_number < 18:
          print("enter less number pls input greater number\n")
     elif guess_number>18:
          print("enter greater number pls input smaller number\n")
     else:
          print("you won\n")
          print("number_of_guesses, no. of guesses he took to finish")
          break
     print(9-number_of_gusses,"no. of guesses left")
     number_of_gusses = number_of_gusses + 1

if(number_of_gusses > 9):
    print("Game over")
        
