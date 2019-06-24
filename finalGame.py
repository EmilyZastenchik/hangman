import random
import turtle


def stand():
    
	#draw stand
	turtle.left(90)
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(150)
	turtle.left(90)
	turtle.forward(400)
	turtle.left(90)
	turtle.forward(250)
	turtle.pu()
	turtle.goto(0,-60)
	turtle.pd()
def head():
	#head
	turtle.circle(30)
def body():
	#body
	turtle.right(90)
	turtle.forward(150)
def l_arm():
	#left arm
	turtle.pu()
	turtle.goto(0, -125)
	turtle.pd()
	turtle.right(135)
	turtle.forward(55)
def r_arm():
	#right arm
	turtle.pu()
	turtle.pd()
	turtle.goto(0, -125)
	turtle.right(90)
	turtle.forward(55)
def l_foot():
	#left foot
	turtle.pu()
	turtle.goto(0, -210)
	turtle.pd()
	turtle.right(175)
	turtle.forward(65)
def r_foot():
	#right foot
    
	turtle.goto(0, -210)
    
	turtle.left(80)
	turtle.forward(65)
def face():
	print("GAME OVER!")
	#face details
	#eyes
	turtle.pu()
	turtle.goto(-5, -15)
	turtle.pd()
	turtle.right(75)
	turtle.forward(10)
	turtle.pu()
	turtle.goto(-10, -15)
	turtle.pd()
	turtle.left(55)
	turtle.forward(10)
	#turtle.circle(4)

	turtle.pu()
	turtle.goto(15, -20)
	turtle.pd()
	turtle.pd()
	turtle.right(60)
	turtle.forward(10)
	turtle.pu()
	turtle.goto(10, -20)
	turtle.pd()
	turtle.left(55)
	turtle.forward(10)
	#turtle.circle(4)

	#mouth
	turtle.pu()
	turtle.goto(-15, -35)
	turtle.pd()
	turtle.left(55)
	turtle.forward(20)
	#turtle.backward(8)
	turtle.pu()
	turtle.goto(-15, -35)
	turtle.pd()
	turtle.forward(40)
	turtle.backward(20)
	turtle.right(90)
	turtle.forward(10)
	turtle.circle(5, 180)
	turtle.forward(10)
	turtle.left(90)
	turtle.forward(4)
	turtle.left(90)
	turtle.pu()
	turtle.forward(2)
	turtle.pd()
	turtle.forward(7)
	turtle.pu()
	turtle.home()


lineNum = random.randint(0,49)
print(lineNum)

wordBank = open(r"words.txt","r")

#read in word bank list
lines = wordBank.readlines()

#print randomly selected word
#print(lines[lineNum])

word = str(lines[lineNum])

letterCount = len(word)

print(letterCount)
stand()
#list of correct letters in selected word
findWord = list()
#initialize findWord with - dashes
for i in range (0,letterCount-1):
	findWord.append(' _ ')
    
#list of guessed letters
used = list()

#print(findWord)

#counter for guesses (MAX 6)
counter = 0
badguess = 0
#for counter in range(0, 6):
while(badguess<7):
	#prints menu
	print("Guess #", counter)
	print("Word: ", *findWord)
	print("Letters guessed: ", used)
	print("You have ", 6-counter, " more guesses")
	print("What is your guess? ")
	guessLetter = input()
	used.append(guessLetter.lower())
	#print(word.find(guessLetter))
	for position, char in enumerate(word):
    	#correct guess
    	if char == guessLetter:
        	findWord[position] = guessLetter
	#incorrect guess
	if(word.find(guessLetter)== -1):
  	print("Bad guess")
  	badguess+=1
  	print(badguess)
	if(badguess==1):
     	head()
	if(badguess==2):
     	body()
	if(badguess==3):
    	l_arm()
	if(badguess==4):
    	r_arm()
	if(badguess==5):
    	l_foot()
	if(badguess==6):
    	r_foot()
    	face()
     	 
	print("____________________________________________________")
	guessWord = ''.join(findWord)
 
	if(len(word) == len(guessWord)+1):
    	print("Yay! You Won!")
    	break
print(word)





