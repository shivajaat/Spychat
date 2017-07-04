from spy_details import spy, Spy, ChatMessage, new_friendlist
from steganography.steganography import Steganography
from termcolor import colored
from datetime import datetime
#Let's start with SpyChat
text=colored('Welcome to SpyChat','cyan')
print text

text1=colored("Lets! Get Started.....",'blue')
print text1
#for message of status...
STATUS_MESSAGES = ['Hi!','Available',' I love food and sleep. If I give you a bit of food or text you all night, that means something.',' We live in the era of smartphones and stupid peoples.']
#For countinue with Default name...
name_exist = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = raw_input(name_exist)
key=raw_input("Enter password for security.If you are Shiva. ")
if key == "1":
    print"password is correct"
elif key >"1" or key<"1":
     print"Wrong Password!"
# This is your Current Status...
show_current_status=raw_input("Do you want to see Default SpyChat starting status...(y/n)?")
if show_current_status == "y":
    current_status = 'Happyness is just state of Mind..(Your current_status)'
    print current_status
else:
    print"Ok! You can Further continue....."
#For Add Friend status you can use add_status function...as below shown...
def add_status():
    updated_status = None
    if spy.current_status != None:
        print 'Your current status is %s\n' % (spy.current_status)
    else:
        print'status is Empty'
        #If you want to choose from some default status you can choose...
    default = raw_input("Do you want to select from older status?..(if yes then please type 'y' if no then type 'n') ")
    if default.upper() == "N":
        new_status = raw_input('What is on your Mind..(Enter your status here)')
        if len(new_status) > 0:
            STATUS_MESSAGES.append(new_status)
            updated_status = new_status
    elif default.upper() == "Y":
         item_position = 1
         for status in STATUS_MESSAGES:
             print"%d. %s", (item_position, status)
             item_position = item_position + 1
         status_selection = int(raw_input("\nPlease choose your from older status as following..."))
         if len(STATUS_MESSAGES) >= status_selection:
            updated_status = STATUS_MESSAGES[status_selection - 1]
    else:
        print'Incorrect option'
    if updated_status:
        print'Your updated status is which is you choosed.....: %s' % (updated_status)
    else:
        print'you did\'n update status'
        #Now status will be update on output of add status...
    print "Loading........"
    return updated_status
#You can also add more friends by add friend function...
def add_friend():
    print"Loading...."
    print"You can easily add a new Friend to your SpyChat!.."
    new_friend = Spy('', '',0, 0.0)
    # for new name
    new_friend.name = raw_input('Please add a new friend Name for SpyChat..')
    if new_friend.name.isalpha():
        print'Hello! What\'s up', new_friend.name
        # len is length...
        a = len(new_friend.name)
        if a == 0:
            print'Hey There.....'+ new_friend.name
        else:
            print"Ok"
    #You will be called my salutation which could be Mister or Miss...
    #New details...
    new_friend.salutation = raw_input("What should i call you.. ")
    if new_friend.salutation.isalpha():
        if new_friend.salutation == "Mr":
            print "Hey! Mr. " + new_friend.name + " What'\s up Welcome to our SpyChat.."
        elif new_friend.salutation == "Ms":
            print "Hey! Ms. " + new_friend.name + " Welcome to our SpyChat.."
        else:
            print"Wrong input Entered!... Please enter a Valid input"
    #for new details
    #to enter name new
    #to enter age..
    new_friend.age = raw_input("Please Enter your Age Which should be greater then 13...?")
    new_friend.age = int(new_friend.age)
    #for enter new rating
    new_friend.rating = raw_input("Spy rating choose from 2,4,5 only?")
    if new_friend.rating .isdigit():
        new_friend.rating = new_friend.rating
        if (new_friend.rating  == 2):
            print'Good'
        elif (new_friend.rating  == 4):
            print'Better'
        elif (new_friend.rating == 5):
            print'Exellent'
    else:
            print'Sorry you are entered wrong rate'
    if len(new_friend.name) > 0 and new_friend.age > 13:
        new_friendlist.append(new_friend)
        print 'Congatulations!..Your new Friend is now Added!..'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
#It will be return the lenght of the new_friendlist
    return len(new_friendlist)
#You can select friend to by Index...(eg:1,2,3,...)....
def select_friend():
    #Fristly.. we will import new_friendlist
    from spy_details import new_friendlist
    item_number = 0
    for new_friend in new_friendlist:
        #Details are...
        print '%d. %s %s is online' % (item_number + 1,new_friend.salutation, new_friend.name),
        print'with Aged is %d and with this Rating %s .' % (new_friend.age,new_friend.rating)
        item_number = item_number + 1
    friend_choice = int(raw_input("Choose from your friends by index"))
    friend_choice_by_position = int(friend_choice) - 1
    print "Welcome  now your friend is selected"
    #it will be retuen friend choise of by its possition(index)....
    return friend_choice_by_position
#You can easily send messages to your Friends.... by choose from  new_friendlist...
def send_message():
    #we select a friend which is stored in friend choice...
    friend_choice = select_friend()
    #for raw input image path
    SAVE_ME='You can help me to save my time'
    original_image = raw_input('What is name/path of your image file')
    #for enter output path...
    output_path = 'output.jpg'
    #to write secrete messages...
    secret_text = raw_input("What\'s on your Mind")
    if secret_text=='SAVE_ME':
        # To hide text on image we using encoding....
        print'You can again action perform of to add path by enter again'
        original_image_other = raw_input('enter again name/path of the image')
        output_path_other = 'output.jpg'
        Steganography.encode(original_image_other,output_path_other,SAVE_ME)
        new_chat = ChatMessage(secret_text,True)
        new_friendlist[friend_choice].chats.append(new_chat)
    elif secret_text=='SOS':
        print 'You can again action perform of to add message by enter again'
        secret_text_other=raw_input('What\'s on your mind you can add more message')
        Steganography.encode(original_image, output_path,secret_text_other)
        new_chat = ChatMessage(secret_text, True)
        new_friendlist[friend_choice].chats.append(new_chat)
    elif len(secret_text) == None or secret_text==None:
        print'Empty secret messages not allowed...So please Try again letter'
    else:
        Steganography.encode(original_image, output_path,secret_text)
        new_chat = ChatMessage(secret_text, True)
        new_friendlist[friend_choice].chats.append(new_chat)

    #messages will be saved...on output
    print "Your secret message is ready!"
#to read messages we can use read messages function
def read_message():
    #firstly we selecting friend..
    sender = select_friend()
    #to input
    output_path = raw_input("What is the name/path of the file?")
    output_path='output.jpg'
    #for text
    #decode are use to view hide text from image...
    secret_text = Steganography.decode(output_path)
    new_chat = ChatMessage(secret_text,False)
    #The data will be saved on output....
    new_friendlist[sender].chats.append(new_chat)
    #you can see output..
    print "Your secret message has been saved!"
#You can read the chat history which is action performed..
def read_chat_history():
    #select a friend
            read = select_friend()
            print"\n"
    #we use loop on it....
            for chat in new_friendlist[read].chats:
                if chat.sent_by_me==True:
                    print colored('%s'%chat.time.strftime("%A %d. %B %Y %H:%M:%S"),'blue')
                    print colored('You Said: ','red'),
                    print('%s' % chat.message)
                else:
                    print colored('%s' % chat.time.strftime("%A %d. %B %Y %H:%M:%S"), 'blue')
                    print colored(new_friendlist[read].name, 'red'),
                    print colored('%s' % chat.message)
#You can start chat and choose diffrent menus to perform diffrent actions...
def start_chat(spy):
    spy.name = spy.salutation + " " + spy.name
    if spy.age >= 13:
        #after completion of succesfully details
        print "Authentication complete. Welcome " + spy.name + " age: " + str(spy.age) + " and rating is: " + str(spy.rating)+" Now you are online!!"
        select = raw_input("Do you want to perform more action " + "with Menu " " (Y/N)? ")
        if select == "y":
            #if menu ==true then menu will be shown....
            menu = True
            while menu:
                choose_menu = raw_input("Enter 1 for StatusUpdate.....\n Enter 2 for add Spy.....\n Enter 3 for enter in Friend list.....\nEnter 4 for Send message to your Friend.....\n Enter 5 for Read messages.....\n Enter 6 for Read of chat history.....\n Enter 7 End the program of Selection Processes.....")
                if choose_menu == "1":
                    print"You can  update your status"
                    spy.current_status = add_status()
                    print"Choose from anothers"
                elif choose_menu == "2":
                    print" You can Add Spy"
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif choose_menu == "3":
                    print"You can enter in friend list by index"
                    select_friend()
                elif choose_menu == "4":
                    print"You can Sent message"
                    send_message()
                elif choose_menu == "5":
                    print"You can Read message"
                    read_message()
                elif choose_menu == "6":
                     read_chat_history()
                elif choose_menu == "7":
                    menu = False
                    print"You can close program"
                else:
                    print"wrong input,try again letter"
                    menu = False
        else:
            print'invalid'
    else:
        print"invalid input"
#if you select continues with default name you will be enter in yyes condition otherwise you are entering in else condition....
if existing == "y" or existing == 'Y':
    #Here we are calling StartChat function
    start_chat(spy)
elif existing == "n" or existing == 'N':
         spy = Spy('', '',0,0.0)
         print "Loading...."
         print "Please enter your details First And then you can start further "
         spy.name = raw_input("Welcome to SpyChat!,Enter your Name ")
         spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")
         spy.age = raw_input("What is your age?")
         spy.age = int(spy.age)
         spy.rating = raw_input("What is your spy rating from 2, 4, 5...?")
         spy.rating = int(spy.rating)
         #here we call start chat function
         start_chat(spy)
else:
    print "Wrong input entered"
#Finished... Work