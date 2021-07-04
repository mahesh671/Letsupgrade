#this is mahesh kumar
#prime number assignment using functions
def PrimeorNot(n):
  for i in range(2,n):
    if n%i==0:
      return False
    else:
      pass
  return True
number = int(input("Enter the number: "))
if PrimeorNot(number):
  print(number,":Number is prime")
else:
  print(number,": is not Prime")
