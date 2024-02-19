a = 33
b = "33"

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
#The output shows an error as variable "a" is an integer data type 
#and variable "b" is a string data type
#Terminal says : 
#TypeError: '>' not supported between instances of 'str' and 'int'