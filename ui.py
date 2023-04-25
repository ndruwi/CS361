from tkinter import *
import time
from tkinter import ttk

def search():
    # create loading bar window
    loading_window = Toplevel(root)
    loading_window.geometry("200x50")
    loading_window.title("Loading...")
    loading_bar = ttk.Progressbar(loading_window, orient='horizontal', mode='determinate', maximum=100, value=0)
    loading_bar.pack()

    # simulate search delay using after()
    def simulate_search():
        for i in range(101):
            loading_bar['value'] = i
            loading_window.update_idletasks()
            time.sleep(0.02)
        loading_window.destroy()

    root.after(10, simulate_search)

def show_more_info():
    more_window = Toplevel(root)
    more_window.geometry("300x100")
    more_window.title("Learn more")
    moreInsLabel1 = Label(more_window, text="Dates must be in the form of month/day")
    moreInsLabel2 = Label(more_window, text="Places are limited to the 50 biggest cities in USA")
    moreInsLabel1.pack()
    moreInsLabel2.pack()

# set default size
root = Tk()
root.geometry("500x200")

insWords = ["Enter", "date", "city", "or", "university"]
insColours = ["black", "red", "blue", "black", "green"]

# create a frame to hold the labels and entry widget
frame_labels = Frame(root)
frame_labels.pack(fill=BOTH, expand=1)

# add extra space to the left and right of the frame
frame_labels.grid_columnconfigure(0, weight=1)
frame_labels.grid_columnconfigure(len(insWords)+1, weight=1)

for index, word in enumerate(insWords):
    insLabel = Label(frame_labels, text=word, fg=insColours[index])
    if index == 0:
        insLabel.grid(column=1, row=0)
    else:
        insLabel.grid(column=index+1, row=0)
entry = Entry(frame_labels)
entry.grid(column=1, row=1, pady=10, columnspan=len(insWords))
moreIns= Label(frame_labels, text= "Learn More", cursor= "hand2")
moreIns.grid(column=1, row=2, pady=10, columnspan=len(insWords))
moreIns.bind("<Button-1>", lambda event: show_more_info())

# create a frame to hold the buttons
frame_buttons = Frame(root)
frame_buttons.pack(side=RIGHT, padx=10)

searchButton = Button(frame_buttons, text="Search", command=search)
exitButton = Button(frame_buttons, text="Exit", command=root.quit)
searchButton.pack(side=LEFT, padx=5)
exitButton.pack(side=LEFT, padx=5)

root.mainloop()
