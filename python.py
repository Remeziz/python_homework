import requests
from datetime import date
#Our search word, name, and date 
word='Pancetta'  
name='Nikolay Zelinskiy' 
today=date.today() 
d1 = today.strftime("%d/%m/%Y")    
#use try if user inputs not intenger and check if number is more or equal 5
try:
    n = int(input("Enter the number of paragraphs more than 5: "))
    if n<=4:
         print ("Input 5 or more")
    else:
        #Use requests to collect our list and count word Pancetta
         i=0
         Pancetta_repeat=0
         list=[]
         while i<n:
             r = requests.get('https://baconipsum.com/api/?type=meat-and-filler.')
             list.append(r.text)
             if word in list[i]:
                Pancetta_repeat=Pancetta_repeat+1
             print(Pancetta_repeat)
             i=i+1
        #Reverse our list`s indexes
         list.reverse()
        #Create and open file 
         f=open("output.txt", "w+")
        #Write our data to the file 
         f.write("The name of the student "+name+"\n"+"The current date is "+d1+"\n"+"There is the word Pancetta in "+str(Pancetta_repeat)+" paragraphs \n")
        #Write our paragraphs to our file 
         for p in list:
             f.write(p+"\n") 
         f.close

except ValueError:
    print("print number please")
    
 
