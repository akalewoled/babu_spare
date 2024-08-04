# use cases 

we have to create two seprate boot
        1  the first one is a  bot to upload items
             it consists 
                    1 autentication and query(file) uploading steps

                    2 and checking the responses of of its query 
        2 selling bot to sell items 
                clicking on the bot he have and uploading its reponse  with the photo and the price 

we have to sotore the file in our data base and   send   it from one boot to another 
 


 # for this we would follow object oriented python 

# first create he objects 
 class User:
    def __init__(self, user_id, name):
        self.user_type=use_type #seller or buyer
        self.user_id = user_id
        self.name = name
        self.location= location
        self.type=type #indivisual  or cmpany 
        self.balance = 0.0  # Default balance

    def update_name(self, new_name):
        self.name = new_name

    def update_balance(self, amount):
        self.balance += amount

    def __str__(self):
        return f'User(id={self.user_id}, name={self.name}, balance={self.balance})'
class  Item:
    def __init__(self,uploader,name,discription,photo,price):
        self.uploader=uploader # this links to the person required this item 
        self.object_ID=objectid
        self.name
        self.discription
        slef.photo
# second implement the bot handler classimport telebot
 # dont forget the stae management and try to delete the  messages after a certain step 

class BotHandler:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        self.users = {}

        # Register bot commands
        self.bot.message_handler(commands=['start'])(self.start)
        self.bot.message_handler(commands=['create'])(self.create_user)
        self.bot.message_handler(commands=['read'])(self.read_user)
        self.bot.message_handler(commands=['update'])(self.update_user)
        self.bot.message_handler(commands=['delete'])(self.delete_user)

    def start(self, message):
        self.bot.reply_to(message, "Welcome to the CRUD Bot! Use /create to create a new user.")

    def create_user(self, message):
        user_id = message.from_user.id
        if user_id not in self.users:
            self.users[user_id] = User(user_id, message.from_user.first_name)
            self.bot.reply_to(message, f"User {message.from_user.first_name} created!")
        else:
            self.bot.reply_to(message, "User already exists.")

    def read_user(self, message):
        user_id = message.from_user.id
        if user_id in self.users:
            user = self.users[user_id]
            self.bot.reply_to(message, str(user))
        else:
            self.bot.reply_to(message, "User not found.")

    def update_user(self, message):
        user_id = message.from_user.id
        if user_id in self.users:
            # For simplicity, we'll just update the user's name
            new_name = message.text.split(maxsplit=1)[1]
            self.users[user_id].update_name(new_name)
            self.bot.reply_to(message, f"User name updated to {new_name}.")
        else:
            self.bot.reply_to(message, "User not found.")

    def delete_user(self, message):
        user_id = message.from_user.id
        if user_id in self.users:
            del self.users[user_id]
            self.bot.reply_to(message, "User deleted.")
        else:
            self.bot.reply_to(message, "User not found.")

    def run(self):
        self.bot.polling()
# third implement the data base handling 

    


