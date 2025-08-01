print("\"MUSIC\"")
print("welcome to quiz")
print("simple game,question will be asked options will be given every correct option increases the money")
input("press enter for start: ")
def over(z):
   print("wrong answer the right answer is",z)
def total(a1,a2,a3,a4,a5,):
    print(a1+a2+a3+a4+a5)
def calmon(i):
 return 500*i
Q1=["Q1:","What ","is","the", "capital","of","france","?"]
print(' '.join(Q1))
q1a=["a)new delhi","toronto"," c)new york","d)paris"]
print(' '.join(q1a))
ans=str(input("lock your answer: "))
if(ans=="d"):
    print("right indeed",q1a[3],"is the right answer")
    sum1=calmon(1)
else:
    over(q1a[3])
    sum1=calmon(0)
print("you won",sum1,"in this question")
input("press enter for start: ")
Q2=["What", "is","the", "chemical", "symbol", "for", "water","?"]
print(' '.join(Q2))
q2a=["a)H2O","b)N2","c)NaCl","d)HCl"]
print(' '.join(q2a))
ans=str(input("lock your answer: "))
if(ans=="a"):
    print("right indeed",q2a[0],"is the right answer")
    sum2=calmon(2)
else:
    over(q2a[0])
    sum2=calmon(0)
print("you won",sum2,"in this question")
input("press enter for start: ")
Q3=["What","is","the","largest","mammal","on","earth","?"]
print(' '.join(Q3))
q3a=["a)Elephant","b)blue whale","c)giraffe","d)gorilla"]
print(' '.join(q3a))
ans=str(input("lock your answer: "))
if(ans=="b"):
    print("right indeed",q3a[1],"is the right answer")
    sum3=calmon(3)
else:
    over(q3a[1])
    sum3=calmon(0)
print("you won",sum3,"in this question")
input("press enter for start: ")
Q4=["Who", "painted","the","Mona","Lisa","?"]
print(' '.join(Q4))
q4a=["a)leonardo di caprio","b)adolf hitler","c)shakesphere","d)leonardo da vinci"]
print(' '.join(q4a))
ans=str(input("lock your answer: "))
if(ans=="d"):
    print("right indeed",q4a[3],"is the right answer")
    sum4=calmon(4)
else:
    over(q4a[3])
    sum4=calmon(0)
print("you won",sum4,"in this question")
input("press enter for start: ")
Q5=["What", "is", "the", "hardest", "natural", "substance", "on", "Earth","? "]
print(' '.join(Q5))
q5a=["a)copper","b)diamond","c)gold","d)titanium"]
print(' '.join(q5a))
ans=str(input("lock your answer: "))
if(ans=="b"):
    print("right indeed",q5a[1],"is the right answer")
    sum5=calmon(5)
else:
    over(q5a[1])
    sum5=calmon(0)
print("you won",sum5,"in this question")
input("press enter: ")
print("the total money you won is:")
total(sum1,sum2,sum3,sum4,sum5)


    
