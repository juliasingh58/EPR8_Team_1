__author__ = "8072902, Dunkel, 8488705, Singh"

import tkinter as tk

root = tk.Tk()

# This creates the name of the window.
root.title('Club cash register system')

# This creates the headliner of the first window page.
head_login = tk.Label(root, text = "Please authenticate yourself!")
head_login.grid(row=0, column=1)

# The entry widgets for the authentication are getting placed.
tk.Label(text='username:').grid(row=1, column=0)
tk.Label(root, text='password:').grid(row=2, column=0)
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry1.grid(row=1, column=1)
entry2.grid(row=2, column=1)
# A button checks if the authentication was valid.
button1 = tk.Button(text='Login', command = '')
button1.grid(row=3, column=1)

root.mainloop()
