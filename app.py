
from user import User
from database import Database

Database.initialise(database="learning", user="postgres", password="menliang99", host="localhost")

user2 = User('deer@rsmith.com', 'Genty', 'Smith', None)
user2.save_to_db()

user_from_db = User.load_from_db_by_email('menliang99@gmail.com')
print (user_from_db)


