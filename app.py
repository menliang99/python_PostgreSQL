
from user import User

user2 = User('rolf@rsmith.com', 'Rolf', 'Smith', None)
user2.save_to_db()

my_user = User.load_from_db_by_email('menliang99@gmail.com')
print (my_user)


