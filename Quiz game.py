Questions = ( "How many colours in a rainbow?:",
             "Which animal is the biggest in the world?:",
             "What is the most hardest metal?:"
             " What is included in water?:"
              " Who founded facebook?:"
              " How many  bones are there in human body?:"
              " Which is the biggest country in the world?:"
              " Which team won world cup 2022?:"
              " How many bytes in 1Mb?")

Choices = ( ( "A.5, B.6, C.7 "),
            ( "A.Blue Whale, B.Megalodon, C.Dinosaur "),
            ( "A.Iron, B.Steel, C.Diamond " ),
            ( "A.H2 and O2, B.H2 and Co2, C.O2 and N2"),
            ( "A.Bill Gates,B.Mark Zuckerberg, C.Elon Musk" ),
            ( "A.206, B.200,C.400"),
            ( "A. USA, B.China, C.Russia"),
            ( "A.Brazil,B.France,C. Argentina"),
            ( "A.1024, B.2024,C.1million"))


Answers = ( "C","A", "C", "A", "B","A","C","C","A")
Guesses_for_ans = []
score = 0
question_num = 0

for quiz in Questions:
   print ( "---------")
   print ( quiz)
   for option in Choices[question_num]:
      print (option )

   guess = input ( "Enter(A,B,C):").upper()
   Guesses_for_ans.append(guess)
   if guess == Answers[question_num]:
      score += 1
      print( " It's correct!")
   else:
      print ( "It's incorrect!")
      print ( f"{Answers[question_num]}is the correct answer")
   question_num += 1

print ("-------------")
print (" This is Your Results   ")
print ("_____________")

print ( " Answers:",end='')
for answer in Answers:
   print( answer,end='')
print()

print ( "guess:", end='')
for guess in Guesses_for_ans:
   print ( guess,end='')
print()

score= (score /len(Questions) * 100)
print (f'Your point is: {score}%')
