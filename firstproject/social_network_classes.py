# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
import json
import os
class SocialNetwork:
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        with open('data.json', 'w') as f:
            d = json.dumps([person.to_dict() for person in self.list_of_people], indent=2, sort_keys=True)
            f.write(d)
        
    def reload_social_media(self):
        if os.path.exists('data.json') and os.path.getsize('data.json') > 0:
            with open('data.json', 'r') as f:
                d = f.read()
                if d:  # add this to check if the file is not empty
                    d = json.loads(d)
                    for i in d:
                        self.fast_create(i['name'], i['age'],i['friendlist'],i['blocklist'],i['messagelist'])
        else:
            print("No data to load.")
    def __init__(self):
        self.list_of_people = [] 
        self.current_person = Person("", 0, [], [], [])
    
    def  create_account(self):
        print("Creating ...")
        name = input("Enter in your name: ")
        age = input("Enter in your age: ")
        person = Person(name, age, [], [], [])
        self.list_of_people.append(person)
        self.save_social_media()
        pass

    def fast_create(self, name, age, friendlist, blocklist, messagelist):
        p = Person(name, age, friendlist, blocklist, messagelist)
        self.list_of_people.append(p)

    def findUser(self, user):
        for x in range(len(self.list_of_people)):
            if self.list_of_people[x].get_name() == user:
                self.save_social_media()
                return True
        return False
    
    def getUser(self, user):
        for x in range(len(self.list_of_people)):
            if self.list_of_people[x].get_name() == user:
                self.save_social_media()
                return self.list_of_people[x]
    
    def setCurrentUser(self, user):
         for x in range(len(self.list_of_people)):
            if self.list_of_people[x].get_name() == user:
                self.save_social_media()
                self.current_person = self.list_of_people[x]
    
    def getCurrentUser(self):
        self.save_social_media()
        return self.current_person
    
    def send_message(self):
        friend = input("Enter a person you want to message: ")
        for x in range(len(self.list_of_people)):
            if self.list_of_people[x].get_name() == friend:
                for y in range(len(self.list_of_people[x].get_blocked_list())):
                    if self.current_person == self.list_of_people[x].get_blocked_list()[y]:
                        print("This person has blocked you")
                message = self.current_person.get_name()
                message += ": "
                message += input("Enter your message: ")
                self.list_of_people[x].message(message)
        self.save_social_media()
    
    def __str__(self) -> str:
        output = ""
        for x in range(len(self.list_of_people)):
            output += "\n"
            output += self.list_of_people[x].get_name()
            output += " "
            output += str(self.list_of_people[x].get_age())
        return output

class Person:
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    #     self.friendlist = []
    #     self.blocklist = []
    #     self.messagelist = []

    def __init__(self, name, age, friendlist, blocklist, messagelist):
        self.name = name
        self.age = age
        self.friendlist = friendlist
        self.blocklist = blocklist
        self.messagelist = messagelist


    def add_friend(self, person_object):
        self.friendlist.append(person_object)
        pass

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    
    def set_name(self, name):
        self.name = name
    def set_age(self, age):
        self.age = age

    def block(self, friend):
        for x in range(len(self.friendlist)):
            if friend == self.friendlist[x].get_name():
                self.blocklist.append(self.friendlist[x])
                return True
        return False

    def message(self, message):
        self.messagelist.append(message)
    
    def delete_message(self, message_index):
        self.messagelist.pop(message_index)

    def __str__(self):
        output = "Name : " +  self.name + "\n Age : " + str(self.age) + "\n Friends list: "
        for x in range(len(self.friendlist)):
            output += self.friendlist[x]
            output += "\n"
        output += "Blocked list: "
        for x in range(len(self.blockedlist)):
            output += self.blockedlist[x]
            output += "\n"
        return output
    def get_friends_list(self):
        return self.friendlist
    def get_blocked_list(self):
        return self.blocklist
    
    def view_details(self):
         output = "Name : " + self.name + "\n Age : " + str(self.age)
         return output
    def view_friends(self):
        output = "Friends list: \n"
        for x in range(len(self.friendlist)):
            blocked = False
            for y in range(len(self.blocklist)):
                if self.friendlist[x] == self.blocklist[y]:
                    blocked = True
            output += self.friendlist[x].get_name()
            output += f" age: {self.friendlist[x].get_age()}"
            if blocked: 
                output += " (BLOCKED)"  
            output += "\n"
        return output
    def view_blocked(self):
        output = "Blocked list: \n"
        for x in range(len(self.blocklist)):
            output += self.blocklist[x].get_name()
            output += f" age: {self.blocklist[x].get_age()}"
            output += "\n"
        return output
    def view_messages(self):
        output = "Messages: "
        for x in range(len(self.messagelist)):
            output += self.messagelist[x]
            output += "\n"
        return output
    
    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'friendlist': [friend.to_dict() for friend in self.friendlist],  # Convert each friend to dict
            'blocklist': [blocked.to_dict() for blocked in self.blocklist],  # Convert each blocked person to dict
            'messagelist': self.messagelist
        }