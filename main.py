import pyautogui
import pyautogui as pt
from time import sleep
import customtkinter
import threading
from tkinter import font
#Variables
screenWidth, screenHeight = pyautogui.size()
#pyautogui.moveTo(1920, 1080)
x=0
user_input_variable: int = 0
current_fish_amount: int = 0
not_located: bool = True
thread_switch = True
#Definitions!!!
print(threading.activeCount())
print(threading.enumerate())
def find_itL(images1, images2, images3, images4, clicks):
    global not_located
    not_located = True
    position = pt.locateCenterOnScreen(images1, confidence=.75)
    if position is None:
        print("L1 not found 1")
        position = pt.locateCenterOnScreen(images2, confidence=.75)
    else:
        not_located = False
        print("Not located is zero 1")
        pt.moveTo(position, duration=.1)
        pt.click(clicks=clicks, interval=.3)
        return not_located

    if position is None:
        print("L1 not found 2")
        position = pt.locateCenterOnScreen(images3, confidence=.75)
    else:
        not_located = False
        print("Not located is zero 2")
        pt.moveTo(position, duration=.1)
        pt.click(clicks=clicks, interval=.3)
        return not_located

    if position is None:
        print("L1 not found 3")
        position = pt.locateCenterOnScreen(images4, confidence=.75)
    else:
        not_located = False
        print("Not located is zero 3")
        pt.moveTo(position, duration=.1)
        pt.click(clicks=clicks, interval=.3)
        return not_located

    if position is None:
        print("L1 not found 4")

    else:
        not_located = False
        print("Not located is zero 4")
        pt.moveTo(position, duration=.1)
        pt.click(clicks=clicks, interval=.3)
        return not_located
# Fishing
def finditR2(imagesGUI1, clicks):
    print(threading.enumerate())
    position = pt.locateCenterOnScreen(imagesGUI1, confidence=.95)
    if position is None:
        print('image not foundR2')
        return 0
    else:
        global current_fish_amount
        print('Find Fish successful!')
        current_fish_amount += 1
        pt.click(button='right', clicks=clicks, interval=.3)
        print(current_fish_amount, "/", user_input_variable)
        sleep(1)
        pt.click(button='right', clicks=clicks, interval=.3)
        sleep(1.4)
def user_input():
    print(threading.enumerate())
    global user_input_variable
    try:
        user_input_variable = int(user_input_window.get())
        print(f"Total Fish to be caught: {user_input_variable}")
    except ValueError:
        user_input_window.delete(0, 999999999)
        print("That isn't a number")
        error_message = customtkinter.CTkLabel(root, text="Error: Input whole numbers only", text_font=("Roboto", 12), text_color="red")
        error_message.pack(pady=5)
def start_button():
#Starts the search for the Back to game button

    while not_located:
        sleep(.5)
        find_itL('images/startSize1.png', 'images/startSize2.png', 'images/startSize3.png', 'images/startSize4.png', 2)

    sleep(0.5)
        #First right click for the fishing to start
    pt.click(button='right')

    while True:
        finditR2('images/SplashV4.png', 1)
        if current_fish_amount == int(user_input_variable):
            print("The end!")
            thread_switch = True
            break

def user_input2():
    user_input_thread = threading.Thread(target=user_input, args=())
    user_input_thread.start()
def start_button2():
    global thread_switch
    start_button_thread = threading.Thread(target=start_button, args=())
    if(thread_switch):
        thread_switch = False
        start_button_thread.start()
    else:
        print("start button thread already running")
    return thread_switch
#-----------------------------------------------------------------------------------------------------------------------------------------------
#Window
root = customtkinter.CTk()
root.title("F.b.")
root.geometry('1x1+20+200')
root.minsize(260, 260)
root.iconbitmap('icons/Fish.ico')
root.resizable(False, False)

hold_fishing_rod_text = customtkinter.CTkLabel(root, text="Hold your Fishing Rod!", text_color="red", text_font=("Roboto", 16))
hold_fishing_rod_text.pack()

number_of_fish = customtkinter.CTkLabel(root, text="Number of Fish: ")
number_of_fish.pack()

user_input_window = customtkinter.CTkEntry(root, width=69)
user_input_window.configure()
user_input_window.pack(pady=5)
user_input_window.get()

save_user_input_button = customtkinter.CTkButton(root, text="Save Input", bg_color="#3c3b3c", corner_radius=0, command=user_input2)
save_user_input_button.pack(pady=3.5)

start_button_on_GUI = customtkinter.CTkButton(root, fg_color="#E7A642", hover_color="#BF7708", text="Start!", corner_radius=0, bg_color="#E7A642", command=start_button2)
start_button_on_GUI.pack(pady=3.5)

bottom_text = customtkinter.CTkLabel(root, text="Made by Toiletman")
bottom_text.pack(pady=15)

root.mainloop()    #Cycle
