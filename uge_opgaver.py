# LIX Beregner
# LIX = O/P + L*100/O
# O antal ord
# P antal punktummer
# L antal lange ord > end 6 bogstaver
def computeLIX(s):
	Otemp	= s.replace("."," ")
	Otemp	= s.replace(","," ")
	words	= Otemp.split(" ")
	O		= len(Otemp)
	P		= s.count(".")
	L		= 0
	for w in words:
		if len(w)>6:
			L = L + 1
	if P==0:
		P=1
	LIX		= (O/P) + (L*100/O)
	#responder i fht LIX
	if LIX>55:
		print("Meget tung faglitteratur")
	elif LIX>45:
		print("Tung faglitteratur")
	elif LIX>35:
		print("Middel")
	elif LIX>25:
		print("Let for dygtige")
	else:
		print("Let tekst for alle")

computeLIX("HEJ MED DIG")