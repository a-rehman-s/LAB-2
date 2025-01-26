import re

email = input("Enter email: ")
pattern = r'^[a-zA-Z0-9_.+-]+@[gmail]+\.[com]+$'
if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")
