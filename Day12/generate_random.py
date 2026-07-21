import random 
import string

def random_user_id():
  characters = string.ascii_letters + string.digits
  random_id = ''.join(random.choice(characters) for i in range(6))
  return random_id

print(random_user_id())
