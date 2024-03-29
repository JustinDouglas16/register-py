# form.py
import tkinter as tk
import tkinter.messagebox as mb
from validate_email import validate_email
from db import User

class UserForm:
    def __init__(self, root, session):
        self.session = session
        self.create_widgets(root)

    def create_widgets(self, root):
        # Create labels and input fields
        self.firstname_label = tk.Label(root, text="First Name")
        self.firstname = tk.Entry(root)
        self.firstname.bind("<KeyRelease>", lambda event: self.adjust_width(self.firstname))
        self.lastname_label = tk.Label(root, text="Last Name")
        self.lastname = tk.Entry(root)
        self.lastname.bind("<KeyRelease>", lambda event: self.adjust_width(self.lastname))
        self.email_label = tk.Label(root, text="Email")
        self.email = tk.Entry(root)
        self.email.bind("<KeyRelease>", lambda event: self.adjust_width(self.email))

        # Place labels and input fields on the window
        self.firstname_label.place(relx=0.5, rely=0.1, anchor='center')
        self.firstname.place(relx=0.5, rely=0.2, anchor='center')
        self.lastname_label.place(relx=0.5, rely=0.3, anchor='center')
        self.lastname.place(relx=0.5, rely=0.4, anchor='center')
        self.email_label.place(relx=0.5, rely=0.5, anchor='center')
        self.email.place(relx=0.5, rely=0.6, anchor='center')

    # Add the rest of your methods here
    
# Create submit button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        self.submit_button.place(relx=0.5, rely=0.8, anchor='center')
        
def adjust_width(self, entry):
        entry.config(width=max(20, len(entry.get())))

def submit(self):
        fn = self.firstname.get().strip()
        ln = self.lastname.get().strip()
        em = self.email.get().strip()

        if fn.isalpha() and ln.isalpha() and validate_email(em):
            existing_user = self.session.query(User).filter_by(firstname=fn, lastname=ln, email=em).first()
            if existing_user is None:
                user = User(firstname=fn, lastname=ln, email=em)
                self.session.add(user)
                self.session.commit()
                mb.showinfo("Success", "User registered successfully")
            else:
                mb.showerror("Error", "User with the same information already exists")
        else:
            mb.showerror("Error", "Invalid input")