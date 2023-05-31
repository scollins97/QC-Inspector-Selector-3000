#import the tkinter.  a standard library in python for GUI's
import functions
import tkinter as tk


#this is initialises the window
root = tk.Tk()
root.title("QC Inspector Selector 3000")

#set the icon 
#this will have to implemented after it gets put on the O drive
#root.iconbitmap("")

#set the background to navy blue
root.configure(bg="#020257")

#tell it to open in full screen
root.attributes("-fullscreen", True)

#set the size it will be when not fullscreen? might just delete this
root.geometry("1000x550")


# Create a label widget and set its text and background color... and font
label = tk.Label(text="hello, click next", bg="white", font=("Arial", 64))

# Create a button widget and set its text.
next_button = tk.Button(text="Next", command=functions.chooseTheSelector(),
                         font=("Arial", 25))

# Create a button widget and set its text.
skip_button = tk.Button(text="Skip", command=lambda: print("testing"), font=("Arial", 25))

# Create a button widget and set its text.
quit_button = tk.Button(text="Quit", command=root.quit, font=("Arial", 25))


# Center the label horizontally
label.place(relx=0.5, rely=0.35, anchor="center")

# Pack the next button to the right of the label widget.
next_button.pack(side="right", padx= 20)

# Pack the skip button to the left of the label widget.
skip_button.pack(side="left", padx= 20)

# Pack the quit button at the bottom of the screen.
quit_button.pack(side="bottom", pady= 20)




#start the main loop
root.mainloop()