import ctypes
import keyboard
from tkinter import *
import json#don't forget this, it is essential
from PyInstaller.compat import is_win, is_darwin, is_linux
from PIL import ImageTk, Image
import platform
import sys
import tkinter as tk
from cefpython3 import cefpython as cef
import time
# platforms
WINDOWS = 'Windows'
#LINUX = platform.system() == 'Linux'
#MAC = platform.system() == 'Darwin'
app_url="https://www.fireeye.com/cyber-map/threat-map.html"
from loginwindow import userid, passcode


transparency_counter=0.8
is_py2 = False
def main():
    
    root = tk.Tk()
    root.title("Secured Space")
    
    root.iconbitmap('C:\\Users\\Administrator\\Documents\\TEST\\Tkinter_space\\spaceicon.ico')
    
    root.state("zoomed")
    root.configure(bg="#1D3F49")

    ##########################################################title bar
    def move_window(event):
        root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

    root.overrideredirect(True) # turns off title bar, geometry
    root.geometry('200x2') # set new geometry

    # make a frame for the title bar
    title_bar = Frame(root, bg='#1D3F49', relief='raised', bd=2)

    #button icon for close button
    closebutton_image = Image.open("C:\\Users\\Administrator\\Documents\\TEST\\Tkinter_space\\Appicons\\close1.png") #img accessed/defined
    resize_image = closebutton_image.resize((19,19)) #img resized
    closebutton_app_image = ImageTk.PhotoImage(resize_image) #resized img accessed/defined
    

    # put a close button on the title bar
    close_button = Button(title_bar, image=closebutton_app_image, command=root.destroy, bd=0, activebackground="#1D3F49", bg="#1D3F49")
    # pack the widgets
    title_bar.pack(expand=0, fill=X)
    close_button.pack(side=RIGHT)

    # bind title bar motion to the move window function
    title_bar.bind('<B1-Motion>', move_window)
    ##########################################################

    ###############################################################################################33wallet image
    id_image = Image.open("C:\\Users\\Administrator\\Documents\\TEST\\Tkinter_space\\Appicons\\id1.png") #img accessed/defined
    resize_image = id_image.resize((40,40)) #img resized
    id_app_image = ImageTk.PhotoImage(resize_image) #resized img accessed/defined

    ###############################################################################################
    ###############################################################################################33wallet image
    passcode_image = Image.open("C:\\Users\\Administrator\\Documents\\TEST\\Tkinter_space\\Appicons\\password1.png") #img accessed/defined
    resize_image = passcode_image.resize((40,40)) #img resized
    passcode_app_image = ImageTk.PhotoImage(resize_image) #resized img accessed/defined

    ###############################################################################################
    def send_id():
       keyboard.write(userid)
    def send_pass():
        keyboard.write(passcode)












    
    ###############################################################################################33wallet image
    wallet_image = Image.open("C:\\Users\\Administrator\\Documents\\TEST\\Tkinter_space\\Appicons\\Wallet1.png") #img accessed/defined
    resize_image = wallet_image.resize((40,40)) #img resized
    wallet_app_image = ImageTk.PhotoImage(resize_image) #resized img accessed/defined

    ###############################################################################################
    
    account_balance=str(500)
    title_frame= LabelFrame(root,  padx=280, pady=7, bd=0.2)
    title_frame.pack(padx=2)
    title_frame.configure(bg="#1D3F49")
    label1=Label(title_frame,text="Welcome to Secured Space",bd=0, relief=SUNKEN, bg="#1D3F49",font=("Orbitron",13),fg="#ff9988").pack(side="left",padx=450)
    Button_wallet=Button(title_frame,image=wallet_app_image,bd=0,background = "#4AF3F8",activebackground="#1D3F49", bg="#1D3F49").pack(side="right",fill=X)
    user_id_icon=Button(title_frame,image=id_app_image,bd=0,background = "#4AF3F8",activebackground="#1D3F49", bg="#1D3F49", command=send_id).pack(side="right",fill=X)
    user_passcode_icon=Button(title_frame,image=passcode_app_image,bd=0,background = "#4AF3F8",activebackground="#1D3F49", bg="#1D3F49",command=send_pass).pack(side="right",fill=X)


    ##########################################################################                              App frame

    apps_frame= LabelFrame(root,  padx=150, pady=7, bd=0)
    apps_frame.pack(side="bottom")
    apps_frame.configure(bg="#1D3F49")

    
    music_image = Image.open("C:\\Users\\Administrator\\Documents\\TEST\\Tkinter_space\\Appicons\\music7.png") #img accessed/defined
    resize_image = music_image.resize((60,60)) #img resized
    music_app_image = ImageTk.PhotoImage(resize_image) #resized img accessed/defined

    shows_image = Image.open("C:\\Users\\Administrator\\Documents\\TEST\\Tkinter_space\\Appicons\\Shows.png") #img accessed/defined
    resize_image = shows_image.resize((60,60)) #img resized
    shows_app_image = ImageTk.PhotoImage(resize_image) #resized img accessed/defined

    games_image = Image.open("C:\\Users\\Administrator\\Documents\\TEST\\Tkinter_space\\Appicons\\Games.png") #img accessed/defined
    resize_image = games_image.resize((60,60)) #img resized
    games_app_image = ImageTk.PhotoImage(resize_image) #resized img accessed/defined

    browser_image = Image.open("C:\\Users\\Administrator\\Documents\\TEST\\Tkinter_space\\Appicons\\Browser1.png") #img accessed/defined
    resize_image = browser_image.resize((60,60)) #img resized
    browser_app_image = ImageTk.PhotoImage(resize_image) #resized img accessed/defined

    school_image = Image.open("C:\\Users\\Administrator\\Documents\\TEST\\Tkinter_space\\Appicons\\School.png") #img accessed/defined
    resize_image = school_image.resize((60,60)) #img resized
    school_app_image = ImageTk.PhotoImage(resize_image) #resized img accessed/defined

    apps_image = Image.open("C:\\Users\\Administrator\\Documents\\TEST\\Tkinter_space\\Appicons\\Apps.png") #img accessed/defined
    resize_image = apps_image.resize((60,60)) #img resized
    apps_app_image = ImageTk.PhotoImage(resize_image) #resized img accessed/defined

    social_image = Image.open("C:\\Users\\Administrator\\Documents\\TEST\\Tkinter_space\\Appicons\\Social.png") #img accessed/defined
    resize_image = social_image.resize((60,60)) #img resized
    social_app_image = ImageTk.PhotoImage(resize_image) #resized img accessed/defined

    store_image = Image.open("C:\\Users\\Administrator\\Documents\\TEST\\Tkinter_space\\Appicons\\Store1.png") #img accessed/defined
    resize_image = store_image.resize((60,60)) #img resized
    store_app_image = ImageTk.PhotoImage(resize_image) #resized img accessed/defined

    news_image = Image.open("C:\\Users\\Administrator\\Documents\\TEST\\Tkinter_space\\Appicons\\News.png") #img accessed/defined
    resize_image = news_image.resize((60,60)) #img resized
    news_app_image = ImageTk.PhotoImage(resize_image) #resized img accessed/defined

    settings_image = Image.open("C:\\Users\\Administrator\\Documents\\TEST\\Tkinter_space\\Appicons\\Settings.png") #img accessed/defined
    resize_image = settings_image.resize((60,60)) #img resized
    settings_app_image = ImageTk.PhotoImage(resize_image) #resized img accessed/defined

    




    #defining the button_functions
    '''
    def transparent_window_plus(]
        ):
        #global transparency_counter
        root.attributes('-alpha',0.8)
        #root.wm_attributes('-transparentcolor','black')
    '''




    def music_page():
        global e
        global app_url
        app_url="https://soundcloud.com"
        e.destroy()
        e=BrowserFrame()
        e.pack(fill='both', expand=1, padx=5, pady=5)
     
    def shows_page():
        global e
        global app_url

        #app_url="https://sepiasearch.org/"#https://sd.keepcalms.com/i/keep-calm-we-are-working-on-it--11.png
        app_url="https://yomovies.pm/"
        e.destroy()
        e=BrowserFrame()
        e.pack(fill='both', expand=1, padx=5, pady=5)
        
    def games_page():
        global e
        global app_url
        app_url="https://unlockedpiratebay.com/"
        e.destroy()
        e=BrowserFrame()
        e.pack(fill='both', expand=1, padx=5, pady=5)
        
    def browser_page():
        global e
        global app_url
        app_url="https://www.fireeye.com/cyber-map/threat-map.html"
        e.destroy()
        e=BrowserFrame()
        e.pack(fill='both', expand=1, padx=5, pady=5)
        
    def school_page():
        global e
        global app_url
        app_url="https://www.freecodecamp.org/"
        e.destroy()
        e=BrowserFrame()
        e.pack(fill='both', expand=1, padx=5, pady=5)
        
    def apps_page():
        global e
        global app_url
        app_url="https://www.google.com/"
        e.destroy()
        e=BrowserFrame()
        e.pack(fill='both', expand=1, padx=5, pady=5)
        
    def social_page():
        global e
        global app_url
        app_url="https://pixelfed.social/"
        e.destroy()
        e=BrowserFrame()
        e.pack(fill='both', expand=1, padx=5, pady=5)
        
    def store_page():
        global e
        global app_url
        app_url="https://binance.com"
        #app_url="chrome://flags/#extension-mime-request-handling"
        e.destroy()
        e=BrowserFrame()
        e.pack(fill='both', expand=1, padx=5, pady=5)
        
    def news_page():
        global e
        global app_url
        app_url="https://bbc.com"
        e.destroy()
        e=BrowserFrame()
        e.pack(fill='both', expand=1, padx=5, pady=5)
        
    def settings_page():
        global e
        global app_url
        app_url="https://cds.cern.ch/images/CERN-HOMEWEB-PHO-2019-004-1/file?size=large"
        e.destroy()
        e=BrowserFrame()
        e.pack(fill='both', expand=1, padx=5, pady=5)
        

    Button1=Button(apps_frame,image=music_app_image,bd=0,command=music_page,background = "#4AF3F8",activebackground="#1D3F49", bg="#1D3F49").pack(side="left",padx=4,pady="0")
    Button2=Button(apps_frame,image=shows_app_image,bd=0,command=shows_page,background = "#4AF3F8",activebackground="#1D3F49", bg="#1D3F49").pack(side="left",padx=4,pady="0")
    Button3=Button(apps_frame,image=games_app_image,bd=0,command=games_page,background = "#4AF3F8",activebackground="#1D3F49", bg="#1D3F49").pack(side="left",padx=4,pady="0")
    Button4=Button(apps_frame,image=browser_app_image,bd=0,command=browser_page,background = "#4AF3F8",activebackground="#1D3F49", bg="#1D3F49").pack(side="left",padx=4,pady="0")
    Button5=Button(apps_frame,image=school_app_image,bd=0,command=school_page,background = "#4AF3F8",activebackground="#1D3F49", bg="#1D3F49").pack(side="left",padx=4,pady="0")
    Button6=Button(apps_frame,image=apps_app_image,bd=0,command=apps_page,background = "#4AF3F8",activebackground="#1D3F49", bg="#1D3F49").pack(side="left",padx=4,pady="0")
    Button7=Button(apps_frame,image=social_app_image,bd=0,command=social_page,background = "#4AF3F8",activebackground="#1D3F49", bg="#1D3F49").pack(side="left",padx=4,pady="0")
    Button8=Button(apps_frame,image=store_app_image,bd=0,command=store_page,background = "#4AF3F8",activebackground="#1D3F49", bg="#1D3F49").pack(side="left",padx=4,pady="0")
    Button9=Button(apps_frame,image=news_app_image,bd=0,command=news_page,background = "#4AF3F8",activebackground="#1D3F49", bg="#1D3F49").pack(side="left",padx=4,pady="0")
    Button10=Button(apps_frame,image=settings_app_image,bd=0,command=settings_page,background = "#4AF3F8",activebackground="#1D3F49", bg="#1D3F49").pack(side="left",padx=4,pady="0")
    settings = {}
    '''
    if MAC:
        settings["external_message_pump"] = True
    '''
    cef.Initialize(settings=settings)
    global e
    e=BrowserFrame()
    e.pack(fill='both', expand=1, padx=5, pady=5)
    #e.pack_forget()

    #root.bind('<Control-C>',transparent_window_plus)
    root.attributes('-alpha',1)#0.82
    #root.wm_attributes('-transparentcolor','black')
    root.mainloop()
    cef.Shutdown()






#################################################################33brwoser_frame_defnintion

class BrowserFrame(tk.Frame):
    global app_url
    def __init__(self,master=None, **kw):
        super().__init__(master,**kw)
        self.browser = None
        self.bind('<Configure>', self.on_configure)

    def get_window_handle(self):
        '''
        if MAC:
            from AppKit import NSApp
            import objc
            return objc.pyobjc_id(NSApp.windows()[-1].contentView())
        '''
        if self.winfo_id() > 0:
            return self.winfo_id()
        else:
            raise Exception('Could not obtain window handle!')

    def on_configure(self, event):
        #global cef_winfo
        global cef_winfo
        if self.browser is None:
            # create the browser and embed it in current frame
            rect = [0, 0, self.winfo_width(), self.winfo_height()]
            cef_winfo = cef.WindowInfo()
            win_id = self.get_window_handle()
            cef_winfo.SetAsChild(win_id, rect)
            #print("win info is: "+ str(cef_winfo))
            self.browser = cef.CreateBrowserSync(cef_winfo, url=app_url)

            # start the browser handling loop
            self.cef_loop()

        # resize the browser
        if WINDOWS:
            ctypes.windll.user32.SetWindowPos(
                self.browser.GetWindowHandle(), 0,
                0, 0, event.width, event.height, 0x0002)
        '''
        elif LINUX:
            self.browser.SetBounds(0, 0, event.width, event.height)
        '''

    def cef_loop(self):
        cef.MessageLoopWork()
        self.after(10, self.cef_loop)


































################################main_calling_statements
if __name__ == '__main__':
    main()