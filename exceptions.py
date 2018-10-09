#python exceptions let you deal with
#unexpected results

try:
	print(a)	#this will throw an exception since a is not defind
except:
	print("a is not defined!")
	
#there are specific erros to help with cases
try:
	print(a)
except NameError:
	print("a is still not defined!")
except:
	print("Something else went wrong.")
	
print(a)