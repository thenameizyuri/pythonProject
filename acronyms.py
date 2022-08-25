phrase = str(input("Enter the phrase:\n"))

text = phrase.split()

a =''
for i in text:
    a = a+str(i[0]).upper()

print(a)
