def playgame():
  print("Welcome to the choice game. At the end, you will get your final message and a list of your choices.")
  choice1 = input("You arrive at school. Where do you go? Type A for classroom and B for locker.")
  if choice1 == "A":
      choice2 = input("What class are you going to? Type A for English and B for math.")
      if choice2 == "B":
        choice4 = input("Was class fun today? Type A for yes and B for no.")
        if choice4 == "A":
            print("Great! Have a good day.")
            list1 = ["A", "B", "A"]
            print (list1)
        else: 
            print("Too bad. Maybe tomorrow.")
            list2 =  ["A", "B", "B"]
            print (list2)
      if choice2 == "A":
        choice3 = input("Was class fun today? Type A for yes and B for no.")
        if choice3 == "A":
            print("Great! Have a good day.")
            list3 = ["A", "A", "A"]
            print (list3)
        else: 
            print("Too bad. Maybe tomorrow.")
            list4 = ["A", "A", "B"]
        


  if choice1 == "B":
        choiceA = input("What do you do at your locker? Type A for getting a book and B for putting a book away.")
        if choiceA == "A":
            choiceB = input("What do you do now? Type A for catching up with friends and B for going to class.")
            if choiceB == "A":
                print("Great! Have fun with your friends.")
                list5 = ["B", "A", "A"]
                print (list5)
            else:
                print("Great! Have fun at class.")
                list6 = ["B", "A", "B"]
                print (list6)
        if choiceA == "B":
            choiceC = input("What do you do now? Type A for going to class and B for going to the library.")
            if choiceC == "A":
                print("Great! Have fun at class.")
                list7 = ["B", "B", "A"]
                print (list7)
            else:
                print("Great! Have fun at the library.")   
                list8 = ["B", "B", "B"]
                print(list8)   

playgame()

