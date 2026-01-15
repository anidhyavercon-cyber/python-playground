questions = ["How many planet are in solar system? : ",
            "How many bones are in human body? :",
            "How many colour are in rainbow? : ",
            "How many wheel are in a rickshaw? :",
            "Which is most abonded gas in atmosphere"]

options = [("A.12" , "B.13" , "C.8" , "D.9 "),
            ("A.208" , "B.207", "C.209" , "D.206 "),
            ("A.3" , "B.7" , "C.9" , "D.4"),
            ("A.20" , "B.8", "C.3" , "D.1 "),
            ("A.Nitrogen" , "B.Oxygen" , "C.Carbon-Dioxide", "D.Sulphur ")]

answers = ("C", "D", "B", "C", "A")

Guesses = []
score = 0
question_num = 0


for question in questions:
    print ("----------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)


    guess = input ("Enter (A,B,C,D) : ").upper()
    
    Guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print ("CORRECT")
    else:
        print ("INCORRECT")
        print (f"Correct answer is {answers[question_num]}")
    question_num = question_num + 1

print ("------------------")
print ("      RESULT      ")


print("Answers : " , end = "")
for answer in answers:
    print (answer, end=" ")
print ()
print("Guesses : " , end= "")
for guess in Guesses:
    print (guess, end=" ")
print ()

score = score / len(questions) * 100
print(f"Your score is {score}%")

print ("------------------")
