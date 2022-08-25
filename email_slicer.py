
#NObel Cs cluB

email = input("Enter Your Email: ")

username = email[0:email.index("@")]
domain_name = email[email.index("@")+1: ]

print(f'Your username is {username} and your domain name is {domain_name}')