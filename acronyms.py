#Input the string for short form
phrase = str(input("Enter the phrase:\n"))

#it will split the phrase into list for which it is easy to access the first element of the all the element of list using indexing
text = phrase.split()

#using for loop so that every time a element is access and is added to the variable a
a =''
for i in text:
    a = a+str(i[0]).upper()

print(a)
