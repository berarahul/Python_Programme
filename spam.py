text= input("Enter the Text:: \n")
# spam = False
if("Make a lot of money" in  text):
    Spam = True
elif("Buy Now"in text):
    Spam = True

elif("Click This"in text):
    Spam = True
elif("Subscribe this "in text):
    Spam = True     
else:
    Spam=False
    if(Spam):
        print ("This text is  spam!")
    else:
        print ("This text is  not spam!")