from chatbot_functions import *
from tkinter import *
import time

root = Tk()

# change icon
p1 = PhotoImage(file='GUI/ensias.png')
root.iconphoto(False, p1)

#title of the window
root.title('ENSIBOT')
#dimensions
root.geometry("1357x690")

 #load images
start = PhotoImage(file='GUI/start.png').subsample(1,1)
img1 = PhotoImage(file='GUI/backg2.gif')
img2 = PhotoImage(file = "GUI/bg2.gif" )
send = PhotoImage(file='GUI/sendm.png').subsample(4,4)
audiopic = PhotoImage(file='GUI/audio.png').subsample(3,3)
speakerpic = PhotoImage(file = 'GUI/speak.png').subsample(4,4)

global tospeech
tospeech = ''
#tkinter functions
def envoyer():
    msg = UserField.get("1.0",'end-1c').strip()
    UserField.delete("0.0",END)

    if msg != '':
        chat.config(state=NORMAL)
        chat.tag_configure("even", foreground = "green", font = ("Comic Sans MS", 12))
        chat.tag_configure("odd")
        tag = "even"
        chat.insert(END, "Vous:   " + msg + '\n\n', tag)
        #chat.config(foreground="#442265", font=("Verdana", 12 ))
        res = reponse_chatbot(msg)
        tag = "odd"
        chat.insert(END, "EnsiBot: " + res + '\n\n' , tag)
        chat.config(state=DISABLED)
        chat.yview(END)
        global tospeech
        tospeech = res



def record():
    res = audio()
    chat.config(state=NORMAL)
    if res[0] != '':
        chat.tag_configure("even", foreground = "green", font = ("Comic Sans MS", 12))
        chat.tag_configure("odd")
        tag = "even"
        chat.insert(END, "Vous : " + res[0] + '\n\n', tag)
        tag = "odd"
        chat.insert(END, "EnsiBot: " + res[1] + '\n\n', tag)
        chat.config(state=DISABLED)
    chat.yview(END)
    global tospeech
    tospeech = res[1]

def speaker():
    speak(tospeech)


def begin():
    time.sleep(0.5)
    start_button.destroy()
    canvas.itemconfig(backgr, image=img2)

    # Place all components on the screen
    scrollbar.place(x=1284, y=70, height=490)
    chat.place(x=831, y=65, height=500, width=460)
    label.place(x=880, y=564)
    UserField.place(x=890, y=572)
    SendButton.place(x=831, y=573)
    audiobutton.place(x=1270, y=570)
    speakerbutton.place(x=660, y=150)


#background
canvas = Canvas(root , width = 1357 , height = 690  )
canvas.pack()
backgr = canvas.create_image(0, 0 ,anchor = NW, image=img1)

#new
#start button
start_button = Button(root , image = start, border = '0' , command = begin)
start_button.place( x= 700, y = 250)

#Create Chat window
chat = Text(root, bd=5,height="8", width="50", font="Arial")
chat.config(state = DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(root, command=chat.yview, cursor="heart")
chat['yscrollcommand'] = scrollbar.set


#Create Buttons
SendButton = Button(root, image = send , border = '0', command = envoyer )
audiobutton = Button(root, image = audiopic , border = '0', command = record )
speakerbutton = Button(root, image = speakerpic , border = '0' , command = speaker)

#Create the box to enter message
# Text Field
TextFieldImg = PhotoImage(file='GUI/text.png')
label = Label( image = TextFieldImg )
UserField = Text(root, fg='black', bg='#38B6FF', font=('Montserrat', 10), width=52, height = 2, bd = 0 )







root.mainloop()


