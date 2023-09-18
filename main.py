import pyautogui
import pyautogui as pt
from time import sleep
import customtkinter
#Variables
screenWidth, screenHeight = pyautogui.size()
#pyautogui.moveTo(1920, 1080)
x=0
z=0
y: int=0
#Definitions!!!

def find_itL(images, clicks, off_x=0, off_y=0):
    position = pt.locateCenterOnScreen(images, confidence=.75)
    if position is None:
        print('image not foundL')


        return 0
    else:
        pt.moveTo(position, duration=.1)
        pt.moveRel(off_x, off_y, duration=.1)
        pt.click(clicks=clicks, interval=.3)

# Fishing
def finditR2(images, clicks, off_x=0, off_y=0):
    position = pt.locateCenterOnScreen(images, confidence=.50)
    if position is None:
        print('image not foundR2')
        return 0
    else:
        global y
        print('Find Fish successful!')
        y = y + 1
        pt.moveTo(position, duration=.1)
        pt.moveRel(off_x, off_y, duration=.1)

        pt.click(button='right', clicks=clicks, interval=.3)
        print(y, "/", z)
        sleep(.5)
        pt.click(button='right', clicks=clicks, interval=.3)

def Inptake():
    global z
    z=elpepe.get()
    print("Celkem: ", z)

def change_text():
    pakito["text"] = "Working..."
    try:
        print('3')
        sleep(1)
        print('2')
        sleep(1)
        print('1')

        find_itL('images/StartV2.png', 2)
        sleep(0.5)
        #First right click for the fishing to start
        pt.click(button='right')

        while True:
            finditR2('images/SplashV2.png', 1)
            if y==int(z):
                print("The end!")
                break

    except ValueError:
        print("That isn't a number")
        gugu = customtkinter.CTk()
        gugu.geometry(f"{500}x{500}")
        gugu.geometry(f"{450}x{160}+{900}+{520}")
        gugu.title("ERROR!")
        gaga = customtkinter.CTkLabel(gugu, text="Input Error", text_color="red", text_font = ("Comic Sans MS", 60))
        gaga.pack()
        ladygaga = customtkinter.CTkLabel(gugu, text="Please input numbers only", text_color="red", text_font=("Comic Sans MS", 10))
        ladygaga.pack()
        gugu.mainloop()

#def change text():

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Window

window = customtkinter.CTk()
window.title("F.b.")
window.geometry('1x1+20+200')
window.minsize(260, 260)
window.iconbitmap('icons/Fish.ico')
window.resizable(False, False)


grug = customtkinter.CTkLabel(window, text="Hold your Fishing Rod!", text_color="red", text_font=("Bebas Neue", 14))
grug.pack()


text2 = customtkinter.CTkLabel(window, text="Number of Fish: ", bg="#3c3b3c", fg=("#FF813E"))
text2.pack()


elpepe = customtkinter.CTkEntry(width=69, bg="#5A5A5A", fg="#FF7420")
elpepe.config()
elpepe.pack(pady=5)
elpepe.get()


pakito2 = customtkinter.CTkButton(text="Save Input", bg="#3c3b3c", command=Inptake)
pakito2.pack(pady=3.5)


pakito = customtkinter.CTkButton(fg_color="#E7A642", hover_color="#FF0000", text="Start!", bg="#E7A642", command=change_text)
pakito.pack(pady=3.5)


text1 = customtkinter.CTkLabel(window, text="Made by Toiletman", bg="#3c3b3c", relief="sunken") #tkinter.Label , bg fg text , Font size type(Bold italic)
text1.pack(pady=15)


window.mainloop()    #Cycle
