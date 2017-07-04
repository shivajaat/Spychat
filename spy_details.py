#In this firstly date and time wil be import...
from datetime import datetime
#class of spy is used here below...
#My  is used as refrence....
class Spy:
    def __init__(My, name, salutation, age, rating):
        My.name = name
        My.salutation = salutation
        My.age = age
        My.rating = rating
        My.is_online = True
        My.chats = []
        My.current_status = None
#here other chatmessages class is added...
class ChatMessage:
    def __init__(My,message,sent_by_me):
        My.message = message
        My.time = datetime.now()
        My.sent_by_me = sent_by_me
#Spy is details of any person and it is uses in short as shown below...
spy = Spy('Shiva', 'Mr.', 18, 5)
#other friends are available for slections easily
friend_one = Spy('Maxwell', 'Mr.', 5, 27)
friend_two = Spy('Priya', 'Ms.', 4, 21)
#list of available friends are shown below...
new_friendlist = [friend_one, friend_two]