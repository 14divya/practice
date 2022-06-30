#Operations on strings and tuples
print("Enter 1 for operations on string, 2 for operations on tuples and 'q' for exiting:")
while True:
	ch=input("Enter your choice:")
	if ch=="1":
		print("Operations on strings")
		print('''1. Concatenation of two strings\n2. Repetition of a string\n3. Reversing a string\n4. Extracting an element\
from the string\n5. Extracting a range of elements from the string\n6. Counting the number of occurences of an\
element in the string\n7. Converting a string to uppercase\n8. Converting a string to lowercase\n9. Determining\
length of the string\n10. Iterating the string\nEnter 'q' to exit.''')
		while True:
			c=input("Enter your choice:")
			if c=="1":
				string1=input("Enter first string:")
				string2=input("Enter second string:")
				print("After concatenation=",string1+string2)
			elif c=="2":
				string=input("Enter a string:")
				n=int(input("Enter the number of times the above string has to be repeated:"))
				print("After repetition=",string*n)
			elif c=="3":
				string=input("Enter the string to be reversed:")
				print("After reversing=",string[::-1])
			elif c=="4":
				string=input("Enter a string:")
				n=int(input("Enter the index of the element to be extracted:"))
				if n<len(string):
					print("The element at position",n,"=",string[n])
				else:
					print("Invalid index.")
			elif c=="5":
				string=input("Enter a string:")
				i=int(input("Enter the first index range of elements:"))
				j=int(input("Enter the second index range of elements:"))
				if i<len(string) and j<len(string):
					print("After extracting=",string[i:j])
				else:
					print("Invalid index.")
			elif c=="6":
				string=input("Enter a string:")
				n=input("Enter the character to be counted:")
				if n in string:
					print("The character",n,"has been repeated",string.count(n),"number of times.")
				else:
					print("Invalid character.")
			elif c=="7":
				string=input("Enter a string:")
				print("After converting to uppercase=",string.upper())
			elif c=="8":
				string=input("Enter a string:")
				print("After converting to lowercase=",string.lower())
			elif c=="9":
				string=input("Enter a string:")
				print("Length of the string=",len(string))
			elif c=="10":
				string=input("Enter a string:")
				for i in string:
					print(i)
			elif c=="q":
				print("Exiting, thank you.")
				exit()
			else:
				print("Enter a valid choice!")
	elif ch=="2":
		print("Operations on tuples")
		list1=[]
		n=int(input("Enter hte size:"))
		for i in range(n):
			a=int(input("enter the elements:"))
			list1.append(a)
		tuple1=tuple(list1)
		list1=[]
		n=int(input("Enter hte size:"))
		for i in range(n):
			a=int(input("enter the elements:"))
			list1.append(a)
		tuple2=tuple(list1)
		print('''1. Concatenation of two tuples\n2. Repetition of a tuple\n3. Reversing a tuple\n4. Extracting an element\
from the tuple\n5. Extracting a range of elements from the tuple\n6. Counting the number of occurences of an\
element in the tuple\n7.Creation of a new empty tuple\n8. Finding if an element is present in the tuple\n9.\
Determining length of the tuple\n10. Iterating the tuple\nEnter 'q' to exit.''')
		while True:
			c=input("Enter your choice:")
			if c=="1":
				print("After concatenation=",tuple(tuple1+tuple2))
			elif c=="2":
				a=int(input("Enter the tuple for using:"))
				if a==1:
					tup=tuple1
				else:
					tup=tuple2
				n=int(input("Enter the number of times the above tuple has to be repeated:"))
				print("After repetition=",tup*n)
			elif c=="3":
				tup=tuple(input("Enter the tuple to be reversed:").split(" "))
				print("After reversing=",tup[::-1])
			elif c=="4":
				tup=tuple(input("Enter a tuple:").split(" "))
				n=int(input("Enter the index of the element to be extracted:"))
				if n<len(tup):
					print("The element at position",n,"=",tup[n])
				else:
					print("Invalid index.")
			elif c=="5":
				tup=tuple(input("Enter a tuple:").split(" "))
				i=int(input("Enter the first index range of elements:"))
				j=int(input("Enter the second index range of elements:"))
				if i<len(tup) and j<len(tup):
					print("After extracting=",tup[i:j])
				else:
					print("Invalid index.")
			elif c=="6":
				tup=tuple(input("Enter a tuple:").split(" "))
				n=input("Enter the element to be counted:")
				if n in tup:
					print("The element",n,"has been repeated",tup.count(n),"number of times.")
				else:
					print("Invalid element.")
			elif c=="7":
				tup=tuple()
				print("The new tuple=",tuple(tup))
			elif c=="8":
				tup=tuple(input("Enter a tuple:").split(" "))
				n=input("Enter the element to be checked:")
				if n in tup:
					print(n,"is present")
				else:
					print(n,"is not present")
			elif c=="9":
				tup=tuple(input("Enter a tuple:").split(" "))
				print("Length of the tuple=",len(tup))
			elif c=="10":
				tup=tuple(input("Enter a tuple:").split(" "))
				for i in tup:
					print(i)
			elif c=="q":
				print("Exiting, thank you.")
				exit()
			else:
				print("Enter a valid choice!")
	elif ch=="q":
		print("Exiting...Thank you")
		exit()
	else:
		print("Enter a valid choice:")
