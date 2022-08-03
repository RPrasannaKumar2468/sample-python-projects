# #Taking input from user and storing it in string
user_input = str(input("Enter a Phrase: "))
#spliting the phrase using split function
text = user_input.split()
#declaring new variable "a"
a = " "
#using for loop condition 
for i in text:
    a = a+str(i[0]).upper()
print(a)