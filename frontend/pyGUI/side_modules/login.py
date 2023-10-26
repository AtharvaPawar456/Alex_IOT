from tkinter import ttk
from tkinter import *
import urllib.request
import time
from plyer import notification
import wetherData as wethD
import requests
import readmeCode as rc
from datetime import datetime
import os

def register_user():
    username_info = username.get()
    password_info = password.get()
    path = os.path.join(os.path.dirname(__file__), "../logindata/")

    file = open(path + username_info + ".txt", "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration Success",
          fg="green", font=("calibri", 11)).pack()

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()

    Label(screen1, text="please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username * ").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10,
           height=1, command=register_user).pack()

def login_verify():

    username1in = (username_verify.get())
    password1 = (password_verify.get())
    username_entry2.delete(0, END)
    password_entry2.delete(0, END)

    username1 = username1in + ".txt"
    path = os.path.join(os.path.dirname(__file__), "../logindata/")

    os.chdir(path)
    list_of_files = os.listdir()
    print(list_of_files)
    if username1 in list_of_files:
        with open(username1, 'r') as f:
            data = f.read()
            print(username1)
        verify = data.splitlines()
        print(verify)
        if password1 in verify:
            print("login success")
            Label(screen2, text=username1in+" Login Successful",
                  fg="green", font=("calibri", 11)).pack()
            Label(screen2, text="Note: Do not Close this Tab",
                  height=5, fg="red", font=("calibri", 11)).pack()
            alexIOT()
            # mainSoft()
        else:
            print("Password has not been recognised")
    else:
        print("User not found !")


def login():
    # print("Login session started")
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify
    global username_entry2
    global password_entry2

    username_verify = StringVar()
    password_verify = StringVar()

    Label(screen2, text="Username * ").pack()
    username_entry2 = Entry(screen2, textvariable=username_verify)
    username_entry2.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password * ").pack()
    password_entry2 = Entry(screen2, textvariable=password_verify)
    password_entry2.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10,
           height=1, command=login_verify).pack()


def mainSoft():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Alex [--Control Panel--]")
    screen3.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()

    Label(screen3, text="please enter details below").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="Username * ").pack()
    username_entry = Entry(screen3, textvariable=username)
    username_entry.pack()
    Label(screen3, text="Password * ").pack()
    password_entry = Entry(screen3, textvariable=password)
    password_entry.pack()
    Label(screen3, text="").pack()
    Button(screen3, text="Register", width=10,
           height=1, command=register_user).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Alex(IOT)")
    Label(text="IOT", bg="grey", width="300",
          height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
    Label(screen, text="Note: Do not Close this Tab",
          height=5, fg="red", font=("calibri", 11)).pack()

    screen.mainloop()


def alexIOT():
    dtime = 10

    def delay(val):
        time.sleep(val)

    butTextcolor = "yellow"

    # Channel Values
    ch1on = "400"  # set     = 1
    ch1off = "450"  # reset   = 0

    ch2on = "500"
    ch2off = "550"

    ch3on = "600"
    ch3off = "650"

    ch4on = "700"
    ch4off = "750"

    #   ThinkSpeak channel API key
    chann1 = "https://api.thingspeak.com/update?api_key=42J30P59Q38LHIRY&field1="
    chann2 = "https://api.thingspeak.com/update?api_key=42J30P59Q38LHIRY&field2="
    chann3 = "https://api.thingspeak.com/update?api_key=42J30P59Q38LHIRY&field3="

    # Display x Axis values
    xais = 1000
    laxis = 900

    # ON/OFF Values
    on = 'ON '
    off = 'OFF'

    dataColor = '#ACDF87'

    uplink = "https://api.thingspeak.com/update?api_key=YYN5LAINXD8Y6Y4A&field1="
    #################################################################################################################################

    class GuiPart:
        

        def __init__(self, master, ):
            pass

        def iotdht(self):
            urllib.request.urlopen(uplink+"800")
            print("updated filed 1", "800")
            delay(15)

            temData1 = requests.get(
                "https://api.thingspeak.com/channels/1661789/feeds.json?api_key=BWRV718JS99HRK3N&results=2")
            field2 = temData1.json()['feeds'][-1]['field2']
            print("Temprature:- ", field2)
            delay(dtime)

            humData2 = requests.get(
                "https://api.thingspeak.com/channels/1661789/feeds.json?api_key=BWRV718JS99HRK3N&results=3")
            field3 = humData2.json()['feeds'][-1]['field3']
            print("Humidity:- ", field3)
            delay(dtime)

            print("DHT-11 Sensor Data Updated")

            temp.config(text=field2)
            hum.config(text=field3)

        def dhtlabel(self, master):
            temp = Label(master, text='Temp', fg=dataColor,
                         bg="#1A3718", font=('Arial Bold', 12))
            temp.place(x=846, y=210)

            hum = Label(master, text='hum', fg=dataColor, bg="#1A3718")
            hum.place(x=921, y=162)

        def runner(self, master):
            self.CH1 = Label(master, text='CH1:', bg="#1A3718",
                             font=('Arial Bold', 16))
            self.CH1.place(x=laxis, y=400)
            self.button1 = Button(master, text=off, fg="#EC650E", bg="#1A3718",
                                  relief=RAISED, font=('Arial Bold', 10), command=self.ch1)
            self.button1.place(x=xais, y=400)

            self.CH2 = Label(master, text='CH2:', bg="#1A3718",
                             font=('Arial Bold', 16))
            self.CH2.place(x=laxis, y=450)
            self.button2 = Button(master, text=off, fg="#EC650E", bg="#1A3718",
                                  relief=RAISED, font=('Arial Bold', 10), command=self.ch2)
            self.button2.place(x=xais, y=450)

            self.CH3 = Label(master, text='CH3:', bg="#1A3718",
                             font=('Arial Bold', 16))
            self.CH3.place(x=laxis, y=500)
            self.button3 = Button(master, text=off, fg="#EC650E", bg="#1A3718",
                                  relief=RAISED, font=('Arial Bold', 10), command=self.ch3)
            self.button3.place(x=xais, y=500)

            self.CH4 = Label(master, text='CH4:', bg="#1A3718",
                             font=('Arial Bold', 16))
            self.CH4.place(x=laxis, y=550)
            self.button4 = Button(master, text=off, fg="#EC650E", bg="#1A3718",
                                  relief=RAISED, font=('Arial Bold', 10), command=self.ch4)
            self.button4.place(x=xais, y=550)

            self.updatebtn = Button(master, text="Refresh", fg="#EC650E", bg="#1A3718",
                                    relief=RAISED, font=('Arial Bold', 10), command=self.iotdht)
            self.updatebtn.place(x=1030, y=4)

        ##########################################################################################

        def ch1(self):
            global is___on
            # Determine is on or off
            if is___on[0]:

                self.button1.config(text=off, fg="#EC650E")
                is___on[0] = False
                urllib.request.urlopen(uplink+ch1on)
                print("updated filed 1:", ch1on)
                delay(dtime)
            else:
                self.button1.config(text=on, fg=butTextcolor)
                is___on[0] = True
                urllib.request.urlopen(uplink+ch1off)
                print("updated filed 1:", ch1off)
                delay(dtime)

        def ch2(self):
            global is___on
            # Determine is on or off
            if is___on[1]:
                self.button2.config(text=off, fg="#EC650E")
                is___on[1] = False
                urllib.request.urlopen(uplink+ch2on)
                print("updated filed 2:", ch2on)
                delay(dtime)
            else:
                self.button2.config(text=on, fg=butTextcolor)
                is___on[1] = True
                urllib.request.urlopen(uplink+ch2off)
                print("updated filed 2:", ch2off)
                delay(dtime)

        def ch3(self):
            global is___on
            # Determine is on or off
            if is___on[2]:
                self.button3.config(text=off, fg="#EC650E")
                is___on[2] = False
                urllib.request.urlopen(uplink+ch3on)
                print("updated filed 3", ch3on)
                delay(dtime)
            else:
                self.button3.config(text=on, fg=butTextcolor)
                is___on[2] = True
                urllib.request.urlopen(uplink+ch3off)
                print("updated filed 3", ch3off)
                delay(dtime)

        def ch4(self):
            global is___on
            # Determine is on or off
            if is___on[3]:
                # on_button.config(image = off)
                self.button4.config(text=off, fg="#EC650E")
                is___on[3] = False
                urllib.request.urlopen(uplink+ch4on)
                print("updated filed 4:", ch4on)
                delay(dtime)
            else:
                # on_button.config(image = on)
                self.button4.config(text=on, fg=butTextcolor)
                is___on[3] = True
                urllib.request.urlopen(uplink+ch4off)
                print("updated filed 4:", ch4off)
                delay(dtime)

        def DisplayWether(self):
            wethD.wether_data()

        def options(self):
            filemenu = Menu(menu)
            menu.add_cascade(label='Options', menu=filemenu)
            # filemenu.add_command(label='--------', command=nothing)
            filemenu.add_command(label='Wether', command=self.DisplayWether)
            # filemenu.add_command(label='BMI Calculator', command=bmi)
            # filemenu.add_command(label='Wikipedia', command=weki)
            filemenu.add_separator()
            filemenu.add_command(label='Exit', command=lambda: ws.quit())
            # press 2 times to exit...

        def help(self):
            helpmenu = Menu(menu)
            menu.add_cascade(label='Help', menu=helpmenu)
            helpmenu.add_command(label='About', command=rc.all)

    ###############################################################################################

    class ThreadedClient:
        """
        Launch the main part of the GUI and the worker thread. periodicCall and
        endApplication could reside in the GUI part, but putting them here
        means that you have all the thread controls in a single place.
        """

        def __init__(self, master):
            """
            Start the GUI and the asynchronous threads. We are in the main
            (original) thread of the application, which will later be used by
            the GUI. We spawn a new thread for the worker.
            """

            self.master = master
            self.gui = GuiPart(master)

            temp = 28.13
            hum = 12.45

            self.gui.dhtlabel(master)
            # self.gui.iotdht(master)
            self.gui.runner(master)
            self.gui.options()
            self.gui.help()

        def iotreset(self):
            try:
                array_off = [ch1off, ch2off, ch3off, ch4off]
                for abcdef in range(4):
                    iotdata = urllib.request.urlopen(
                        chann1+str(array_off[abcdef]))
                    print(iotdata)
                    print("Channel1 ::  ", array_off[abcdef])
                    time.sleep(100)
            except:
                print("Connect Device to Internet")
                notification.notify(
                    title="Alex-IOT", message=" Connect Device to Internet", timeout=2)

        # def channel1(self, x):
        #     if(x == "on"):
        #         data = urllib.request.urlopen(chann1+str(ch1on))
        #     else:
        #         data = urllib.request.urlopen(chann1+str(ch1off))

    ##############################################################################################################################
    global is___on
    is___on = [True, True, True, True]
    ws = Tk()
    ws.title('Alex [--IOT--]')
    ws.geometry('1092x592')  # h x v =
    ws.config(bg='yellow')
    ws.resizable(False, False)
    canvas = Canvas(ws, bg = "#000000")
    img = PhotoImage(master = canvas, file='alex_ui.png')
    bgimg = Label(ws, image=img)
    bgimg.place(x=0, y=0)
    


    menu = Menu(ws)
    ws.config(menu=menu)

    temp = Label(ws, text="00.00", fg=butTextcolor,
                 bg="#1A3718", font=('Arial Bold', 12))
    temp.place(x=846, y=155)

    hum = Label(ws, text="00.00", fg=butTextcolor, bg="#1A3718")
    hum.place(x=921, y=118)

    ThreadedClient(ws)

    ws.mainloop()

main_screen()