from tkinter import *

root = Tk()
root.geometry("600x400")

def getvals():
    print("Accepted")

Label(root, text="Python Registration_Login Form", font="arial 15 bold").grid(row=0, column=3)

name =   Label(root, text='Name')
age =    Label(root, text='Age')
gender = Label(root, text='Gender')
phone =  Label(root, text="Phone")
address = Label(root, text="Address")
email =  Label(root, text="Email")

name.grid(row=1, column=2)
age.grid(row=2, column=2)
gender.grid(row=3, column=2)
phone.grid(row=4, column=2)
address.grid(row=5, column=2)
email.grid(row=6, column=2)

namevalue = StringVar()
agevalue = StringVar()
gendervalue = StringVar()
phonevalue = StringVar()
addressvalue = StringVar()
emailvalue = StringVar()  # Corrected: use StringVar instead of IntVar

nameentry = Entry(root, textvariable=namevalue)
ageentry = Entry(root, textvariable=agevalue)
genderentry = Entry(root, textvariable=gendervalue)
phoneentry = Entry(root, textvariable=phonevalue)
addressentry = Entry(root, textvariable=addressvalue)
emailentry = Entry(root, textvariable=emailvalue)  # Corrected: use emailentry instead of emailvalue

nameentry.grid(row=1, column=3)
ageentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
phoneentry.grid(row=4, column=3)
addressentry.grid(row=5, column=3)
emailentry.grid(row=6, column=3)

button = Checkbutton(root, text="Remember me?", variable=IntVar())
button.grid(row=7, column=3)

Button(root, text='Submit', command=getvals).grid(row=8, column=3)  # Changed row number

root.mainloop()
