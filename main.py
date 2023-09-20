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
notLocated = 1
#Definitions!!!

def find_itL(images1, images2, images3, images4, clicks):
    global notLocated
    notLocated = 1
    position = pt.locateCenterOnScreen(images1, confidence=.75)
    if position is None:
        print("L1 not found 1")
        position = pt.locateCenterOnScreen(images2, confidence=.75)
    else:
        notLocated = 0
        print("Not located is zero 1")
        pt.moveTo(position, duration=.1)
        pt.click(clicks=clicks, interval=.3)
        return notLocated

    if position is None:
        print("L1 not found 2")
        position = pt.locateCenterOnScreen(images3, confidence=.75)
    else:
        notLocated = 0
        print("Not located is zero 2")
        pt.moveTo(position, duration=.1)
        pt.click(clicks=clicks, interval=.3)
        return notLocated

    if position is None:
        print("L1 not found 3")
        position = pt.locateCenterOnScreen(images4, confidence=.75)
    else:
        notLocated = 0
        print("Not located is zero 3")
        pt.moveTo(position, duration=.1)
        pt.click(clicks=clicks, interval=.3)
        return notLocated

    if position is None:
        print("L1 not found 4")

    else:
        notLocated = 0
        print("Not located is zero 4")
        pt.moveTo(position, duration=.1)
        pt.click(clicks=clicks, interval=.3)
        return notLocated

# Fishing
def finditR2(imagesGUI1, clicks):
    position = pt.locateCenterOnScreen(imagesGUI1, confidence=.95)
    if position is None:
        print('image not foundR2')
        return 0
    else:
        global y
        print('Find Fish successful!')
        y = y + 1
        pt.click(button='right', clicks=clicks, interval=.3)
        print(y, "/", z)
        sleep(1)
        pt.click(button='right', clicks=clicks, interval=.3)

def Inptake():
    global z
    z=elpepe.get()
    print("Celkem: ", z)

def change_text():
    pakito['text'] = "Working..."
    try:
        print('3')
        sleep(1)
        print('2')
        sleep(1)
        print('1')
        #Starts the search for the Back to game button
        sleep(.5)
        while(notLocated == 1):
            sleep(.5)
            find_itL('images/startSize1.png', 'images/startSize2.png', 'images/startSize3.png', 'images/startSize4.png', 2)

        sleep(0.5)
        #First right click for the fishing to start
        pt.click(button='right')

        while True:
            finditR2('images/SplashV4.png', 1)
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
        ladygaga = customtkinter.CTkLabel(gugu, text="Please input numbers only", text_color="red", text_font=("Comic Sans MS", 20))
        ladygaga.pack()
        gugu.mainloop()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Window
window = customtkinter.CTk()
window.title("F.b.")
window.geometry('1x1+20+200')
window.minsize(260, 260)
window.iconbitmap('icons/Fish.ico')
window.resizable(False, False)

grug = customtkinter.CTkLabel(window, text="Hold your Fishing Rod!", text_color="red", text_font=("Roboto", 18))
grug.pack()

text2 = customtkinter.CTkLabel(window, text="Number of Fish: ")
text2.pack()

elpepe = customtkinter.CTkEntry(window, width=69)
elpepe.configure()
elpepe.pack(pady=5)
elpepe.get()

pakito2 = customtkinter.CTkButton(window, text="Save Input", bg_color="#3c3b3c", corner_radius=0, command=Inptake)
pakito2.pack(pady=3.5)

pakito = customtkinter.CTkButton(window, fg_color="#E7A642", hover_color="#BF7708", text="Start!", corner_radius=0, bg_color="#E7A642", command=change_text)
pakito.pack(pady=3.5)

text1 = customtkinter.CTkLabel(window, text="Made by Toiletman")
text1.pack(pady=15)

window.mainloop()    #Cycle
