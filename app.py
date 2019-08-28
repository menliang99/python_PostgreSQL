
from user import User

user2 = User('roedl@rsmith.com', 'Rolf', 'Smith', None)
user2.save_to_db()

user_from_db = User.load_from_db_by_email('menliang99@gmail.com')
print (user_from_db)


