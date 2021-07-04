import random as r
maxP=int(input("Enter no of participants: "))
Part=[x for x in input("names with spaces counted as 1 participant: ").split()[:maxP]]
ran=r.randint(0, maxP-1) 
print("winner of lucky draw:",Part[ran])
