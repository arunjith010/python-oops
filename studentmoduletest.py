# This python file  is for test all fuctions in the student class 
# this is for testing real life scenarios and many functions used in the file 

from modules.student.Student import studentClass

# step 1:student registration test

email = input("Enter your email : ")  
password=input("Enter your password : ") 

s1=studentClass()
s1.setuserNameandPassword(email, password)
