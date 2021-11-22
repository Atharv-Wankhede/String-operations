a=input("enter string--")
b=input("enter the word you want to search--")
c=input("Enter substring--")
d=a.split()
e = -1
for i in d:
    	if len(i) > e:
    		e= len(i)
    		res = i 
print("Maximum length string is : " + res)
count=0
for i in range(0,len(a)):
			if(a[i]==b):
				count=count+1
print("Number of times word occured--",count)
c=""
for i in a:
    c=i+c
print("Reversed string:",c)
if(c==a):
			print("entered string is palindrome")
else:
			print("entered string is not pallindrome")
if(c in a):
	print("Substring is present in string")
else:
	print("Substring is not present")

													
					
			