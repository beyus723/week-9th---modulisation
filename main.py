import fill_list, displayList as Display, datetime, random

continueLoop = True
while continueLoop == True:

  userDetails = list()
  userDetails = fill_list.GetDetails(userDetails)

  Display.DisplayDetails(userDetails)

  date = datetime.datetime.now()
  print("\n", date.strftime("%d/%m/%y"))

  choice = input("\nAre you happy with these? Y or N")

  if choice.lower() == "y":
    print("Thanks...\n\n")
    continueLoop == False
    
    randomName = random.randint(0,9)
    print((userDetails[0] + " ") * randomName)

    
    
  elif choice.lower() == "n":
    print("\n\nTry again...\n\n")
          
  else:
    print("\n\n\nAn error occured. Try again\n")