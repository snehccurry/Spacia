from tkinter import *
from PIL import ImageTk, Image
import random
import keyboard
import time


#C:\Users\Administrator\Documents\TEST\Space\icons\account.png
#C:\\Users\\Administrator\\Documents\\TEST\\Space\\icons\\account.png
root=Tk()
root.title("Secured Space")
root.iconbitmap("C:\\Users\\Administrator\\Documents\\TEST\\Tkinter_space\\spaceicon.ico")
#getting screen width and height of display
root.state("zoomed")

#setting tkinter window size
root.configure(bg="#000000")
#root.attributes('-alpha',0.76)
'''
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
'''
'''
root.geometry("1920x1080")
root.attributes('-fullscreen', True)
'''
bg = PhotoImage(file = "C:\\Users\\Administrator\\Documents\\TEST\\Tkinter_space\\Appicons\\login.png")
  
# Show image using label
label1 = Label( root, image = bg, bd=0)
label1.place(relx=0.259,rely=0.25)



Home_frame= LabelFrame(root,  padx=150, pady=60, bg="#000000",bd=0)
Home_frame.pack(padx=10, pady=400)
################################################################################################################

#														Restricting screenshots





###################################################################################################################


#													LOooooooooginnn Page
##########################################################################################################################################

k=3

letters=['a','2','4','7','1','9','5','6','3','8','@','@','@','%','$','4','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
##print(len(letters))
def submit_info(user_id, pass_code):
	global userid, passcode
	#print("reached",userid)
	userid=user_id
	passcode=pass_code
	#os.system("C:\\Users\\Administrator\\Desktop\\surf.pyw")
	root.destroy()
	'''
	if(userid=="sumitgupta" and passcode=="sumitgupta"):
		#print("logged in")
		wrongpass_label=Label(Home_frame,text="Logging in...").grid(row=4,column=3,pady=20)
		time.sleep(1)
		os.system("C:\\Users\\Administrator\\Desktop\\surf.pyw")
		root.destroy()
	else:
		#print("wrong userid/password",passcode)
		wrongpass_label=Label(Home_frame,text="wrong pass").grid(row=4,column=3,pady=20)
	'''
	
def	keyboard_call():
	keyboard.on_press_key("a", lambda _:sendstr(k))
	keyboard.on_press_key("b", lambda _:sendstr(k))
	keyboard.on_press_key("c", lambda _:sendstr(k))
	keyboard.on_press_key("d", lambda _:sendstr(k))
	keyboard.on_press_key("e", lambda _:sendstr(k))
	keyboard.on_press_key("f", lambda _:sendstr(k))
	keyboard.on_press_key("g", lambda _:sendstr(k))
	keyboard.on_press_key("h", lambda _:sendstr(k))
	keyboard.on_press_key("i", lambda _:sendstr(k))
	keyboard.on_press_key("j", lambda _:sendstr(k))
	keyboard.on_press_key("k", lambda _:sendstr(k))
	keyboard.on_press_key("l", lambda _:sendstr(k))
	keyboard.on_press_key("m", lambda _:sendstr(k))
	keyboard.on_press_key("n", lambda _:sendstr(k))
	keyboard.on_press_key("o", lambda _:sendstr(k))
	keyboard.on_press_key("p", lambda _:sendstr(k))
	keyboard.on_press_key("q", lambda _:sendstr(k))
	keyboard.on_press_key("r", lambda _:sendstr(k))
	keyboard.on_press_key("s", lambda _:sendstr(k))
	keyboard.on_press_key("t", lambda _:sendstr(k))
	keyboard.on_press_key("u", lambda _:sendstr(k))
	keyboard.on_press_key("v", lambda _:sendstr(k))
	keyboard.on_press_key("w", lambda _:sendstr(k))
	keyboard.on_press_key("x", lambda _:sendstr(k))
	keyboard.on_press_key("y", lambda _:sendstr(k))
	keyboard.on_press_key("z", lambda _:sendstr(k))
	keyboard.on_press_key(" ", lambda _:sendstr(k))
	keyboard.on_press_key("1", lambda _:sendstr(k))
	keyboard.on_press_key("2", lambda _:sendstr(k))
	keyboard.on_press_key("3", lambda _:sendstr(k))
	keyboard.on_press_key("4", lambda _:sendstr(k))
	keyboard.on_press_key("5", lambda _:sendstr(k))
	keyboard.on_press_key("6", lambda _:sendstr(k))
	keyboard.on_press_key("7", lambda _:sendstr(k))
	keyboard.on_press_key("8", lambda _:sendstr(k))
	keyboard.on_press_key("9", lambda _:sendstr(k))
	keyboard.on_press_key("0", lambda _:sendstr(k))
	keyboard.on_press_key(".", lambda _:sendstr(k))


def sendstr(k):
	if(k==0):							#set the value of k, for the input field, say k=0 will be for id input field, k=1 will be for password field
		ran=random.randint(0,41)
		for i in range(1,ran,1):
			keyboard.write(letters[i])
		time.sleep(0.2)
		e.delete(len(e.get())-ran+1,END)
		
	if(k==1):
		ran=random.randint(0,25)
		for i in range(1,ran,1):
			keyboard.write(letters[i])
		time.sleep(0.2)
		e2.delete(len(e2.get())-ran+1,END)


def id_field():
	global k
	k=0
	e.grid(row=0,column=2)
	e2.grid_forget()


def password_field():
	global k
	k=1
	e.grid_forget()
	e2.grid(row=1,column=2)
	submit_label=Button(Home_frame,bg="#000000",text="Done",fg="#009999",font=("Orbitron",14),activebackground="#009999",bd=0,command=lambda: submit_info(e.get(),e2.get())).grid(row=4,column=2)

keyboard_call()
	

e=Entry(Home_frame, width=35, borderwidth=5, font=("Orbitron",14),bg="#000000",fg="#009999")
e2=Entry(Home_frame, width=35, borderwidth=5, show="*",font=("Orbitron",14),bg="#000000",fg="#009999")

id_button_label=Button(Home_frame,text="Space ID  :",fg="#009999",bg="#000000",font=("Orbitron",14), activebackground="#009999",bd=0,command=id_field).grid(row=0,column=1)
pass_button_label=Button(Home_frame,text="Password:",fg="#009999",bg="#000000",font=("Orbitron",14), activebackground="#009999",bd=0,command=password_field).grid(row=1,column=1)


#####################################################################################################



#																icon definition for apps.

'''
####################for id
image = Image.open("C:\\Users\\Administrator\\Documents\\TEST\\Tkinter_space\\id.jpeg") #img accessed/defined

resize_image = image.resize((40, 25)) #img resized
 
img = ImageTk.PhotoImage(resize_image) #resized img accessed/defined


my_button=Button(Home_frame, image=img,command=id_field, bd=0)#bd or borderwidth=0 to hide the border
my_button.grid(row=0,column=0,pady=20)


'''


'''
######################for password
image = Image.open("password.ico") #img accessed/defined
 
resize_image = image.resize((40, 25)) #img resized
 
img = ImageTk.PhotoImage(resize_image) #resized img accessed/defined


my_button=Button(Home_frame, image=img,command=id_field, bd=0)#bd or borderwidth=0 to hide the border
my_button.grid(row=0,column=0,pady=20)


my_label=Label(Home_frame,text='')
my_label.grid(row=4,column=3,pady=20)

'''







#																	Enddddddd of Logggggin page
######################################################################################################
























































root.mainloop()











