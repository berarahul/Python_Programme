letter = '''Dear <|NAME|>,
Greetings from ABC coding house. I am Happy to tell you about your selection
You  Are Selected!
Have a great day ahead!
Thanks and Regards,
bill
Date: <|DATE|>
'''
name =input("Enter your name::\n")
date =input("Enter Date::\n")



letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)