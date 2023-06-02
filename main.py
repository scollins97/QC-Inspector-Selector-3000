#import the tkinter.  a standard library in python for GUI's
import functions
import tkinter as tk

def chooseTheInspector():
    window.configure(bg=functions.randomcolor())
    # Pack the skip button to the left of the label widget.
    #this means the skip button will not show until after the next button is clicked
    skip_button.pack(side="left", padx= 20)
    return functions.getRandomInspectorWithinReason()
    
def skipThenChooseTheInspector():
    window.configure(bg=functions.randomcolor())
    return functions.skipTheLastInspectorFirst()


#this is initialises the window
window = tk.Tk()
window.title("QC Inspector Selector 3000")

#set the icon 
#this will have to implemented after it gets put on the O drive
#window.iconbitmap("")

#set the background to a random color using the random color function
window.configure(bg=functions.randomcolor())

#tell it to open in full screen
window.attributes("-fullscreen", True)

#set the size it will be when not fullscreen? might just delete this
window.geometry("1000x550")


# Create a label widget and set its text and background color... and font
label = tk.Label(text="hello, click next", font=("Arial", 100))

# Create a button widget and set its text.
#not sure why it has to be a lambda expression but it does 

next_button = tk.Button(text="Next",
                        command=lambda : label.configure(text= str(chooseTheInspector()),
                        font=("Arial, 200")), font=("Arial", 25))

# Create a button widget and set its text.
skip_button = tk.Button(text="Skip",
                        command=lambda : label.configure(text= str(skipThenChooseTheInspector()),
                        font=("Arial, 200")), font=("Arial", 25))

# Create a button widget and set its text.
quit_button = tk.Button(text="Quit", command=window.quit, font=("Arial", 25))


# Center the label horizontally
label.place(relx=0.5, rely=0.35, anchor="center")

# Pack the next button to the right of the label widget.
next_button.pack(side="right", padx= 20)

# Pack the quit button at the bottom of the screen.
quit_button.pack(side="bottom", pady= 20)


#start the main loop
window.mainloop()