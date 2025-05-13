from tkinter import *

# Create the main window
root = Tk()
root.geometry("800x600")  # Set the window size to 800x600 pixels


################################# ROOT CODE ####################################################
'''MODEL'''

# Create a red frame (a screen) and place it in the top-left corner
# It covers the entire window, but only becomes visible when raised
red_frame = Frame(root, bg="indianred")
red_frame.place(x=0, y=0, width=800, height=600)

# Create a blue frame (another screen)
blue_frame = Frame(root, bg="light blue")
blue_frame.place(x=0, y=0, width=800, height=600)

# Create a teal landing frame (this is the home screen). It is displayed on top because it created last.
landing_frame = Frame(root, bg="teal")
landing_frame.place(x=0, y=0, width=800, height=600)

# This function brings a frame to the front (top of the stack)
def raise_frame(frame):
    frame.tkraise()

################################# LANDING PAGE #################################################
'''MODEL'''
# No data stored here yet; this screen just navigates to other pages

'''CONTROLLER'''
# Create a button that switches to the red frame
red_button = Button(
    landing_frame,  # Button goes on the landing frame
    text="RED", fg="indianred", bg="teal", font=("Arial", 30),
    command=lambda: raise_frame(red_frame))  # When clicked, show red_frame
red_button.place(x=150, y=375, width=200, height=50)

# Create a button that switches to the blue frame
blue_button = Button(
    landing_frame,
    text="BLUE", fg="light blue", bg="teal",font=("Arial", 30),
    command=lambda: raise_frame(blue_frame))  # When clicked, show blue_frame
blue_button.place(x=450, y=375, width=200, height=50)

'''VIEW'''
# Add a title label to the landing frame
landingpage_title = Label( landing_frame, text="Landing Page", fg="white", bg="teal", font=("Arial", 30))
landingpage_title.place(x=200, y=20, width=400, height=50)

################################# BLUE PAGE #################################################
'''MODEL'''
# No data here yet — just a display screen

'''CONTROLLER'''
# Home button to return to the landing page
home = Button( blue_frame, text="HOME", fg="white", bg="light blue",font=("Arial", 30),command=lambda: raise_frame(landing_frame))
home.place(x=300, y=530, width=200, height=50)

'''VIEW'''
# Title label for the blue page
blue_title = Label( blue_frame, text="Blue Page", fg="white", bg="light blue",font=("Arial", 30))
blue_title.place(x=200, y=20, width=400, height=50)

################################# RED PAGE #################################################
'''MODEL'''
# No data here yet either

'''CONTROLLER'''
# Home button to return to the landing page
home = Button( red_frame, text="HOME", fg="white", bg="indianred", font=("Arial", 30),command=lambda: raise_frame(landing_frame))
home.place(x=300, y=530, width=200, height=50)

'''VIEW'''
# Title label for the red page
red_title = Label( red_frame, text="Red Page", fg="white", bg="indianred",font=("Arial", 30))
red_title.place(x=200, y=20, width=400, height=50)

# Start by showing the landing page
raise_frame(landing_frame)

# Keep the window open and running
root.mainloop()
