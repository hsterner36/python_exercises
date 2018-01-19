'''
Vi laver nogle små øvelser:
1. Gæt et tal
import random
import math as m

n=int(random.randrange(1,101))
nbruger = int(input("Gæt et tal mellem 1 og 100: "))
while n!=nbruger:
	if n>nbruger:
		print("Du gættede sgu forkert ", m.fabs(nbruger-n))
		print("Du skal gætte på et større tal")
	else:
		print("Du gættede sgu forkert ", m.fabs(nbruger-n))
		print("Du skal gætte på et mindre tal")
	nbruger = int(input("Gæt et tal mellem 1 og 100: "))
print("Tillykke du gættede rigtigt.")

#2. Summen af alle tal fra 1 til 100.
sum = 0
#while-variant
i = 0
while(i<101):
	sum = sum + i
	i = i + 1
print("Summen af tallen 1 til 100 er ", sum)

#for-variant
for i in range(101):
	sum = sum + i
print("Summen af tallen 1 til 100 er ", sum)
'''

'''
3. Summen af alle lige tal

sum = 0 
for i in range(0,101,2):
	sum = sum + i 
'''
'''
4. Er et tal et primtal

def isPrime(n):
	for i in range(2,n):
		if(n%i==0):
			#print(n, " er ikke et primtal, da ", i, " er primtalsfaktor")
			return False
	#print(n, "er et PRIMTAL. JUHUU.")
	return True
listPrimes=[]
for i in range(1,1000000,2):
	if isPrime(i):
		listPrimes.append(i)
		print(i)
print(listPrimes)


'''
'''
5. Det største tal i en liste

import random
listeaftal=[]
for i in range(100):
	listeaftal.append(random.randint(0,1000))
print("Herunder en usorteret liste af tal: ")
print(listeaftal)

#vi finder herunder det største element
def maxNumber(listeaftal):
	tempmax = 0
	for x in listeaftal:
		if x>tempmax:
			tempmax = x
	print("Største tal i listen er: ", tempmax)
	return tempmax

maxNumber(listeaftal)
'''

	