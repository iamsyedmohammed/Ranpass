import random
import time
user = input("Do you Want to Generate Random Password? yes/no\n").lower()
def play():
    if user != "yes":
        quit()
    lower="abcdefghijklmnopqrstuvwxyz"
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num="0123456789"
    sym="!@#$%^&*(){}_+"
    string=lower+upper+num+sym
    length=int(input("Enter The Length You Want for Your Password:\n"))
    if length >= 8 and length <= 15:
        password="".join(random.sample(string,length))
        time.sleep(1)
        print(f"Your Randomly Password is Generated:\n{password}")
    elif length > 15:
        print("You Password Not Should Contain More Character ")
    elif length < 8:
        print("Please Add More Characters ")
play()
