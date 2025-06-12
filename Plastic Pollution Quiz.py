'''Quiz  Program on Plastic Pollution by Hunter Phillips'''

rerun = True
while rerun:
    
#Rerun allows the code to be repeated. This function may be disabled by the user
#at the end of the quiz when asked whether they would like to repeat it or not.
#If the user doesn't want to repeat the quiz, rerun will become false ending the
#loop.
    
    print("Hello and welcome to this quiz about plastic pollution.\n" 
    "It will consist of 10 questions that will test your knowledge and \n" 
    "help you learn more about plastic pollution. When answering a question, you will be shown a list of possible answers.")
    
    #This dictionary contains the questions along with the users options
    ques = {
    "1. What is the most common plastic waste found in the ocean?":
        "a) Plastic bags b) Plastic straws c) Cigarette butts d) Fishing nets",
    "2. Approximately how many metric tons of plastic enter the worlds oceans each year?":
        "a) 800,000 b) 1 million c) 8 million d) 20 million",
    "3. Which marine animals are most at risk from ingesting plastic debris?":
        "a) Dolphins b) Sea turtles c) Whales d) All of the above",
    "4. What is the Great Pacific Garbage Patch?":
        "a) A new marine species b) An island made of sand c) A large area of floating plastic debris d) A coral reef",
    "5. Which of the following is NOT a way plastic pollution harms wild life?":
        "a) Entanglement b) Ingestion of plastic c) Providing shelter d) Chemical contamination",
    "6. Microplastics are defined as plastic particles smaller than:":
        "a) 1 meter b) 5 millimeters c) 1 centimeter d) 10 centimeters",
    "7. What percentage of seabirds are estimated to have plastic in their stomachs?":
        "a) 5% b) 20% c) 60% d) 90%",
    "8. Which human activity contributes most to plastic pollution in oceans?":
        "a) Fishing b) Littering on land c) Oil drilling c) Whale watching",
    "9. What are microplastics?":
        "a) Large plastic objects b) Tiny plastic particles formed from the breakdown of larger plastics c) A type of fish d) Natural ocean minerals",
    "10. Which international agreement aims to reduce plastic waste in the oceans?":
        "a) Paris agreement b) MARPOL Convention c) Antartic Treaty d) Geneva Convention"
}
    #Contains the answers to each of the questions above
    ans = {
    "1. What is the most common plastic waste found in the ocean?":
        "c",
    "2. Approximately how many metric tons of plastic enter the worlds oceans each year?":
        "c",
    "3. Which marine animals are most at risk from ingesting plastic debris?":
        "d",
    "4. What is the Great Pacific Garbage Patch?":
        "c",
    "5. Which of the following is NOT a way plastic pollution harms wild life?":
        "c",
    "6. Microplastics are defined as plastic particles smaller than:":
        "b",
    "7. What percentage of seabirds are estimated to have plastic in their stomachs?":
        "d",
    "8. Which human activity contributes most to plastic pollution in oceans?":
        "b",
    "9. What are microplastics?":
        "b",
    "10. Which international agreement aims to reduce plastic waste in the oceans?":
        "b"
}
    #The valid options the user can input
    valid=['1','2','3','4','5']
    print(ques)
    print(ans)
    points = 0
    
    
    
    
    
    
    
    choice=input("Please enter your answer here: ")