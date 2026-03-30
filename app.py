# Simple Secure Bank App

print("Welcome to Secure Bank App")

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
    print("Your balance is ₹10,000")
else:
    print("Invalid Credentials")
