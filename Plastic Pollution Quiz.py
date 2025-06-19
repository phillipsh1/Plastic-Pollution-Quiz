'''Quiz  Program on Plastic Pollution by Hunter Phillips'''

rerun = True
while rerun:
    
#Rerun allows the code to be repeated. This function may be disabled by the user
#at the end of the quiz when asked whether they would like to repeat it or not.
#If the user doesn't want to repeat the quiz, rerun will become false ending the
#loop.
    
    print("Hello and welcome to this quiz about plastic pollution.\n" 
    "It will consist of 10 questions that will test your knowledge and \n" 
    "help you learn more about plastic pollution. When answering a question, you will be shown a list of possible answers. \n"
    "Once you have chosen the answer you believe is correct, you then enter the answers corresponding letter (a,b,c or d)")
    
    #This dictionary contains the questions along with the users options
    ques = {
    1.: "What is the most common plastic waste found in the ocean? \n"
            "a) Plastic bags \n"
            "b) Plastic straws \n"
            "c) Cigarette butts \n"
            "d) Fishing nets",
    2.:  "Approximately how many metric tons of plastic enter the worlds oceans each year? \n"
            "a) 800,000 \n"
            "b) 1 million \n"
            "c) 8 million \n"
            "d) 20 million",
    3.:  "Which marine animals are most at risk from ingesting plastic debris? \n"
            "a) Dolphins \n"
            "b) Sea turtles \n"
            "c) Whales \n"
            "d) All of the above",
    4.:  "What is the Great Pacific Garbage Patch? \n"
            "a) A new marine species \n"
            "b) An island made of sand \n"
            "c) A large area of floating plastic debris \n"
            "d) A coral reef",
    5.:  "Which of the following is NOT a way plastic pollution harms wild life? \n"
            "a) Entanglement \n"
            "b) Ingestion of plastic \n"
            "c) Providing shelter \n"
            "d) Chemical contamination",
    6.:  "Microplastics are defined as plastic particles smaller than: \n"
            "a) 1 meter \n"
            "b) 5 millimeters \n"
            "c) 1 centimeter \n"
            "d) 10 centimeters",
    7.:  "What percentage of seabirds are estimated to have plastic in their stomachs? \n"
            "a) 5% \n"
            "b) 20% \n"
            "c) 60% \n"
            "d) 90%",
    8.:  "Which human activity contributes most to plastic pollution in oceans? \n"
            "a) Fishing \n"
            "b) Littering on land \n"
            "c) Oil drilling \n"
            "c) Whale watching",
    9.:  "What are microplastics? \n"
            "a) Large plastic objects \n"
            "b) Tiny plastic particles formed from the breakdown of larger plastics \n"
            "c) A type of fish \n"
            "d) Natural ocean minerals",
    10.: "Which international agreement aims to reduce plastic waste in the oceans? \n"
            "a) Paris agreement \n"
            "b) MARPOL Convention \n"
            "c) Antartic Treaty \n"
            "d) Geneva Convention"
}
    #Contains the answers to each of the questions above
    ans = {
    1:
        "c", # Cigarette butts
    2:
        "c", # 8 million
    3: 
        "d", # All of the above
    4: 
        "c", # A large area of floating plastic debris
    5: 
        "c", # Providing shelter
    6: 
        "b", # 5 millimeters
    7: 
        "d", # 90%
    8: 
        "b", # Littering on land
    9: 
        "b", # Tiny plastic particles formed from the breakdown of larger plastics
    10: 
        "b" # MARPOL Convention
}
    #The valid options the user can input
    valid=['a','b','c','d']
    print(ques[1])
    points = 0
    correct = 0 

    
    def user_correct(x,y):
                print(f"You have selected the answer {x}")
                print(f"{x} is correct! You now have {y} points!")
    
    def user_wrong(x,y):
        print("You have selected the answer {x}")
        print(f"{x} is incorrect! You still have {y} points :(")


    
    for key, value in ques.items():
        print(key, value)
        choice = input("Please enter your answer here: ")
        while choice not in valid:
            print("Your answer was not valid, your answer must be either: A, B, C, or D")
            choice = input("Please enter your answer here: ")
        if choice == ans[key]: 
            points += 1           
            user_correct(choice, points)

            print(points)
        if choice != ans[key]:
            user_wrong(choice, points)

    

    
    



    
    retake = input("Would you like to take the quiz again? Answer with Yes or No: ")
    while retake not in ["yes", "no", "Yes", "No"]:
        retake = input("That is an invalid answer. Please answer with 'Yes' or 'No': ")
    
    if retake == "yes" or retake == "Yes":
        print(f"Thank you for taking this quiz! You were able to get a total of {points}/10 points, which is {correct} answers correct. Goodluck on your next attempt!")
        rerun = True
    else:  
        rerun = False 
        
        print(f"Thank you for taking this quiz! You were able to get a total of {points}/10 points, which is {correct} answers correct.")   