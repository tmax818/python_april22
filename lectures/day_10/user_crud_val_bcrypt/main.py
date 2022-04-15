from flask_app import Bcrypt, app

# print(app)

bcrypt = Bcrypt(app)
print(dir(bcrypt))

my_hash = bcrypt.generate_password_hash("password")
# my_hash1 = bcrypt.generate_password_hash("hansome69")

# print(my_hash, my_hash1)

check = bcrypt.check_password_hash(my_hash, "password123")
print(check)
# check2 = bcrypt.check_password_hash(b'$2b$12$3K/bAxM42VptuEKh7pBEh./EP9bQMm0Of7NRv/iA2FNeBNa7M4IIi', "stinky")

# print(check, check2)