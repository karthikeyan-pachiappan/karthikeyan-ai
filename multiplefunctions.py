class multiplefunctions:
    def OddEven():
        num=int(input("Enter a number:"))
        if(num % 2 == 0):
            print(num,"is Even number")
        else:
            print(num,"is Odd number")
    def Subfields():
        print("Sub-fields in AI are:\nMachine Learning\nNeural Networks\nVision\nRobotics\nSpeech Processing\nNatural Language Processing")
   
    def Elegible():
        gender=input("Your Gender :")
        age=int(input("Your Age :"))
        if(gender == "Male" and age >=21):
            print("ElIGIBLE")
        elif(gender == "Female" and age >=18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")       

    def percentage():
        sub1=int(input("Subject1="))
        sub2=int(input("Subject2="))
        sub3=int(input("Subject3="))
        sub4=int(input("Subject4="))
        sub5=int(input("Subject5="))
        Total=sub1+sub2+sub3+sub4+sub5
        print("Total : ",Total)
        Percentage=float(Total/5)
        print("Percentage : " ,Percentage)

    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        at=(height*breadth)/2
        print ("Area of Triangle:",at)
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        breadth1=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        pt=height1+height2+breadth1
        print("Perimeter of Triangle:",pt)
    
        