import fill_list, displayList as Display

continueLoop = True
while continueLoop == True:

  userDetails = list()
  userDetails = fill_list.GetDetails(userDetails)

  Display.DisplayDetails(userDetails)

  choice = input("\nAre you happy with these? Y or N")

  if choice.lower() == "y":
    print("Thanks...\n\n")
    continueLoop == False
    
  elif choice.lower() == "n":
    print("\n\nTry again...\n\n")
          
  else:
    print("\n\n\nAn error occured. Try again\n")