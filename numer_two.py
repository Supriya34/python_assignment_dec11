password="woohoo"

def func(word):
    if (word==password):
        print("The password is correct")
    else:
        print("The password is incorrect")


word=input("Enter the password \n")
func(word)