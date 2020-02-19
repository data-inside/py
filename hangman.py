#hangman
import random
pics=[' ',
    '''
=========||
    |    ||
         ||
         ||
         ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
         ||
         ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
    |    ||
         ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
   /|    ||
         ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
   /|\   ||
         ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
   /|\   ||
   /     ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
   /|\   ||
   / \   ||
         ||
         || ''',
]
f1=open("twl06.txt","r")
word=f1.read()
word=word.lower()
word=word.split()
def getWord(WordList):
    Index=random.randint(0,len(WordList)-1)
    return WordList[Index]
def display(Correct,Missed,SecretWord):
    print (pics[len(Missed)])
    print("Here is the list of letters you missed ")
    for Letter in Missed+Correct:
        print (Letter,end=' ')
    Blanks='_'*len(SecretWord)
    for i in range(len(SecretWord)):
        if SecretWord[i] in Correct:
            Blanks=Blanks[:i]+SecretWord[i]+Blanks[i+1:]
    print ("\nHere is the secret word...\n")
    print("The word is ",end='')
    print(len(SecretWord),end=' ')
    print("characters long")
    for i in range (0,len(Blanks)):
        print (Blanks[i],end=' ')
    print()
    ch=''
    if Blanks == SecretWord:
        print("Congrats!!!!Word guessed!!!")
        print("Play again???y/n ")
        ch=input()
        guess(ch)
    elif Blanks !=SecretWord and len(Missed)==7:
        print("You lose\n")
        print ("The word was ",end='')
        print(SecretWord)        
        print("Play again???y/n ")
        ch=input()
        guess(ch)        
def guess(Choice):
    if Choice=='y':
        print('Welcome to HANGMAN!\n')
        Missed=''
        Correct=''
        SecretWord=getWord(word)
        print('_ '*len(SecretWord))
        while len(Missed)<len(pics)-1 :
            print('Please guess a letter...\n')
            letter=input()
            flag=checkLetter(letter,Missed,Correct)
            if flag == 1 and letter in SecretWord:
                Correct=Correct+letter
                display(Correct,Missed,SecretWord)
            elif flag==1 and letter not in SecretWord:
                Missed=Missed+letter
                display(Correct,Missed,SecretWord)
    else:
        exit("\nthank you for playing")
def checkLetter(letter,Missed,Correct):
    UnForbidden='abcdefghijklmnopqrstuvwxyz'
    if letter in UnForbidden and len(letter) == 1 and letter not in Missed+Correct:
        return 1
    elif letter not in UnForbidden:
        print("Enter only alphabets\n")
        return 2
    elif len(letter) !=1:
        print("Only one character allowed\n")
        return 3
    elif letter in Missed+Correct:
        print("Already used\n")
        return 4
guess('y')
