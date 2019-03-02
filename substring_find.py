string = raw_input('Enter String : ')
substring = raw_input('Search String : ')
 
if substring in string:
	print ("Your substring was found!")
else:
	print("NOT find the substring!")