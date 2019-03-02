def reverse(s): 
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0] 
  
string = raw_input('Enter String : ')
  
print "The original string  is : ",string

  
print "The reversed string is : ",reverse(string)
