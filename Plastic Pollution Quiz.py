'''Quiz Program on Plastic Pollution by Hunter Phillips'''

#This dictionary contains the questions along with the users options
ques = {
    "1.": "What is the most common plastic waste found in the ocean? \n"
            "a) Plastic bags \n"
            "b) Plastic straws \n"
            "c) Cigarette butts \n"
            "d) Fishing nets",
    "2.":  "Approximately how many metric tons of plastic enter the worlds oceans each year? \n"
            "a) 800,000 \n"
            "b) 1 million \n"
            "c) 8 million \n"
            "d) 20 million",
    "3.":  "Which marine animals are most at risk from ingesting plastic debris? \n"
            "a) Dolphins \n"
            "b) Sea turtles \n"
            "c) Whales \n"
            "d) All of the above",
    "4.":  "What is the Great Pacific Garbage Patch? \n"
            "a) A new marine species \n"
            "b) An island made of sand \n"
            "c) A large area of floating plastic debris \n"
            "d) A coral reef",
    "5.":  "Which of the following is NOT a way plastic pollution harms wild life? \n"
            "a) Entanglement \n"
            "b) Ingestion of plastic \n"
            "c) Providing shelter \n"
            "d) Chemical contamination",
    "6.":  "Microplastics are defined as plastic particles smaller than: \n"
            "a) 1 meter \n"
            "b) 5 millimeters \n"
            "c) 1 centimeter \n"
            "d) 10 centimeters",
    "7.":  "What percentage of seabirds are estimated to have plastic in their stomachs? \n"
            "a) 5% \n"
            "b) 20% \n"
            "c) 60% \n"
            "d) 90%",
    "8.":  "Which human activity contributes most to plastic pollution in oceans? \n"
            "a) Fishing \n"
            "b) Littering on land \n"
            "c) Oil drilling \n"
            "c) Whale watching",
    "9.":  "What are microplastics? \n"
            "a) Large plastic objects \n"
            "b) Tiny plastic particles formed from the breakdown of larger plastics \n"
            "c) A type of fish \n"
            "d) Natural ocean minerals",
    "10.": "Which international agreement aims to reduce plastic waste in the oceans? \n"
            "a) Paris agreement \n"
            "b) MARPOL Convention \n"
            "c) Antartic Treaty \n"
            "d) Geneva Convention"
}
    #Contains the answers to each of the questions above
ans = {
    "1.":
        "C", # Cigarette butts
    "2.":
        "C", # 8 million
    "3.": 
        "D", # All of the above
    "4.": 
        "C", # A large area of floating plastic debris
    "5.": 
        "C", # Providing shelter
    "6.": 
        "B", # 5 millimeters
    "7.": 
        "D", # 90%
    "8.": 
        "B", # Littering on land
    "9.": 
        "B", # Tiny plastic particles formed from the breakdown of larger plastics
    "10.": 
        "B" # MARPOL Convention
}

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
    
    #The list of valid options the user can choose from. When an invalid option (not in this list) is input, it isnt accepted.
    valid_ans=['A','B','C','D']
    
    amount=0
    points = 0
    correct = 0 

    #Functions for when the user gets a question correct or incorrect. 
    #They display to the user their answer (A,B,C or D) and whether they are correct or incorrect.
    #The users points are also shown.
    def user_correct(x,y):
        print(f"You have selected the answer {x}")
        print(f"{x} is correct! You now have {y} points!")
    
    def user_wrong(x,y):
        print(f"You have selected the answer {x}")
        print(f"{x} is incorrect! You still have {y} points")
        print("Better luck on your next question!!")
    #The proccess of asking the user questions, getting their response, and seeing if they are correct or incorrect.
    for key, value in ques.items():
        print(key, value)
        choice = input("Please enter your answer here: ")
        choice = choice.capitalize()
        while choice not in valid_ans:
            print("Your answer was not valid, your answer must be either: A, B, C, or D")
            choice = input("Please enter your answer here: ")
            choice = choice.capitalize()
        if choice == ans[key]: 
            points += 1           
            correct += 1
            user_correct(choice, points)
        if choice != ans[key]:
            user_wrong(choice, points)
    
    print(f"Thank you for taking this quiz! You were able to get a total of {points} points, which is {correct} answers correct.")
    #The code below is responsible for the rerun function located at the top of the code.
    #The user has the option to either repeat the quiz or end it. 
    #The code will repeat if the user enters "Yes" and will end if the user enters "No"
    #Any invalid answers (eg. "hello") will result in the user being asked to enter a valid answer (Yes or no) until they input a valid answer.
    retake = input("Would you like to take the quiz again? Answer with Yes or No: ")
    while retake not in ["yes", "no", "Yes", "No"]:
        retake = input("That is an invalid answer. Please answer with 'Yes' or 'No': ")
    
    if retake == "yes" or retake == "Yes":
        print("Goodluck on your next attempt!")
        rerun = True
    else:  
        rerun = False 
        print("Goodbye!")   


    valid_num=['1','2','3','4']
    valid_response=['Yes','yes','No','no']

    print("Now that you have successfully completed the given questions, you may now submit your own question.")
    user_choice = input("Do you wish to add your own question to the quiz? Answer with 'Yes' or 'No': ")
    user_choice = user_choice.strip().lower()
    while user_choice not in valid_response:
        print("That is an invalid answer. Please answer again with either 'Yes' or 'No': ")
        user_choice = input("Do you wish to add your own question to the quiz? Answer with 'Yes' or 'No': ")
        user_choice = user_choice.strip().lower()
    print(user_choice)
    if user_choice == 'yes':
        user_ques = input("Please enter your selected question: ")
        opt_A = input("Enter option A: ")
        opt_B = input("Enter option B: ")
        opt_C = input("Enter option C: ")
        opt_D = input("Enter option D: ")
        user_ans = input("Which of the 4 options given is the correct answer? (A, B, C, or D): ")
        user_ans = user_ans.strip().upper()
        print(user_ans)
        while user_ans not in valid_ans:
            print("That is an invalid answer. Please select a letter out of A, B, C, or D")
            user_ans = input("Which of the 4 options given is the correct answer? (A, B, C, or D): ")
            user_ans = user_ans.strip().upper()
        user_choice = input("Do you want to create another question? Answer with 'Yes' or 'No' ")

        new_ques = user_ques + "\n" + opt_A + "\n" + opt_B + "\n" + opt_C + "\n" + opt_D
        new_ans = user_ans
        print(new_ques)

        ques.update({"11.": (new_ques)})
        ans.update({"11.": (new_ans)})
    else:
        print("bye")
