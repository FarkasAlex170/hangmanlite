name = input("What's your name?: ").upper()
print("\n" * 5 + "Hello " + name + " let's have some fun!" + "\n" * 10 )
name2 = input("Name your rival: ").upper()
print("It's " + name + " against " + name2 + "!")
word = input("What is your word " + name + "?:")
print(len(word) * "-" + "\n" * 11)
guess = input("what is your chosen letter " + name2 + "?:") 
wrong =0
if guess in word:
    print("Hell yeah " + guess + " is correct")
    print(len(word) * "-" +  "\n" * 8 ) 
    guess += word

else:
    'try again'
    print(len(word) * "-" + "\n" * 8)
guess1 = input("what is your following letter? " )  
if guess1 in word:
    print("Not bad " + guess1 + " is correct")
    print(len(word) * "-" + "\n" * 8)
else:
    print("try again")   
    print(len(word) * "-" + "\n" * 8)
guess2 = input("Next one: ")    
if guess2 in word:
    print("Go on! " + guess2 + " is correct too" )
    print(len(word) * "-" + "\n" * 8)
else: 
    print("try again")
    print(len(word) * "-" + "\n" * 8)