from spy_details import Spy
#for input Name
spy = Spy('', '' , 0 , 0.0 , True )
spy.name = raw_input('Enter Name')
#it will be work when name is in aplha
if spy.name.isalpha():
        print'Hello',spy.name
        #len is lenth
        a=len(spy.name)
        if a == 0:
            print'name should not be empty'
        else:
            print a
#salutation is being used for calling Mister or Miss...
spy.salutation = raw_input("Are you Mr. or Ms. ?")
if spy.salutation.isalpha():
    if spy.salutation == "Mr":
            print "Hi! Mr.",spy.name
    elif spy.salutation == "Ms":
            print "Hi! Ms.",spy.name
    else:
            print"Wrong input Entered"
#for input age
spy.age = raw_input('Please enter your Age')
if not spy.age.isalpha():
  spy.age = int(spy.age)
if (spy.age >= 13) or (spy.age <= 55):
           print 'Your Age is',spy.age
else:
           print 'Invalid Age Please Enter Valid Age'
#in this the rating is in threee ways you can select only by 2,4,5 to give rarting
spy.rating = raw_input('Please Enter Rate from these rates 2,4,5 ....')
if spy.rating.isdigit():
     spy.rating = float(spy.rating)
     if(spy.rating == 2):
        print'Good'
     elif(spy.rating == 4):
        print'Better'
     elif(spy.rating == 5):
        print'Exellent'
     else:
      print'Sorry you are entered wrong rate'
#To make spy is online.
spy.is_online = True
#After completeion of authentication...output will be shown...
print"Loading....."
print"Congratulations....."
print "Authentication complete!!  Welcome " + spy.name + " age: " + str(spy.age) + " and rating is: " + str(spy.rating) + str(spy.is_online) + "Now you are online!!"
