sub1= int(input ("Enter the first Subject marks: \n"))
sub2= int(input ("Enter the Seconed Subject marks:\n"))
sub3= int(input ("Enter the Third Subject marks: \n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail")

    if(sub1+sub2+sub3)/3<40:
        print("You are fail due to total percentage less than 40")
else:
 print(" Congratulations You  passed  The Exam")