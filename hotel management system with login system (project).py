from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk,ImageOps,ImageChops  
import os 
from tkinter import messagebox
import mysql.connector
from matplotlib import image
import time
import datetime
import random
from hotelmaangement import HotelManagementSystem




def main():
    root = Tk()
    app = login_window(root)
    root.mainloop()


class login_window :
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

          # Background image


        image = Image.open(
            r"C:\Users\HP\login_form\bg_new.jpg"
        )
        image = image.resize((1550,800))
        self.bg = ImageTk.PhotoImage(image)

    #lable

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        # ================= Title =================
        lblTitle = Label(
            self.root,
            text="HOTEL MANAGEMENT SYSTEM",
            font=("times new roman", 35, "bold"),
            bg="black",
            fg="yellow"
        )
        lblTitle.place(x=0, y=0, width=1550, height=50)

    # frame

        frame = Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

    #profile logo 

        image1 = Image.open(
            r"C:\Users\HP\login_form\real_logo.webp")
        image1 = image1.resize((100,100),Image.Resampling.LANCZOS)
        self.profile_logo = ImageTk.PhotoImage(image1)

        lbl_profile = Label(frame,image=self.profile_logo,bg="black",borderwidth=0)
        lbl_profile.place(x=120,y=13,width=100,height=100)


        #get started 
        get_str = Label(frame,text="Get started",font=("times of new roman",15,"bold"),fg="white",bg="black")
        get_str.place(relx=0.5,y = 129 ,anchor=CENTER)                          #(x=95,y=145)

        # lable2
        username=lbl=Label(frame,text="Username",font=("times of new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=165)

        self.txtuser = ttk.Entry(frame,font=("times of new roman",15,))
        self.txtuser.place(x=40,y=195,width=270)

        #pass
        password=lbl=Label(frame,text="Password",font=("times of new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=235)

        self.txtpass = ttk.Entry(frame,font=("times of new roman",15,))
        self.txtpass.place(x=40,y=265,width=270)


        image2  = Image.open(
                    r"C:\Users\HP\login_form\real_logo.webp")
        image2 = image2.resize((25,25))
        self.username_logo = ImageTk.PhotoImage(image2)

        lbl_username = Label(frame,image=self.username_logo,bg="black",borderwidth=0)
        lbl_username.place(x=43,y=165,width=25,height=25)


        image3   = Image.open(
            r"C:\Users\HP\login_form\aaa.png")
        image3 = image3.resize((25,25))
        self.password_logo = ImageTk.PhotoImage(image3)

        lbl_security = Label(frame,image=self.password_logo,bg="black",borderwidth=0)
        lbl_security.place(x=43,y=236,width=25,height=25)

        # loginbtn
        loginbtn = Button(frame,command=self.login,text = "Login",font=("times of new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=330,width=120,height=35)

        # regiseterbtn
        # Register button image

        registerbtn = Button(
    frame,
    text="New User Register",
    command=self.register_window,
    font=("times of new roman",10,"bold"),
    borderwidth=0,
    fg="white",
    bg="black",
    activeforeground="white",
    activebackground="black"
)

        registerbtn.place(
    x=15,
    y=387,
    width=160
)


        # forgetpassbtn
        forgetbtn = Button(frame,text = "Forget Password",command=self.forgot_password_window ,font=("times of new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetbtn.place(x=10,y=410,width=160)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)



    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
                messagebox.showerror("Error","All fields are required")
        elif self.txtuser.get() == "admin" and self.txtpass.get() == "admin":
                messagebox.showinfo("Success","Welcome to the system")
                self.new_window = Toplevel(self.root)
                self.app = HotelManagementSystem(self.new_window)
        else:

            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Abhi@123",
                database="myproject_1"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM my_data WHERE email=%s AND password=%s", (self.txtuser.get(), self.txtpass.get()))
            row = cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Username or Password")
            else:
                open_main = messagebox.askyesno("YesNo", "Do you want to open the main page?")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return


            conn.commit()
            conn.close()
            # ==================reset pass======
    def reset_password(self):


        if self.combo_security.get() == "Select":
            messagebox.showerror(
                "Error",
                "Please select the security question",parent=self.root2
            )

        elif self.txtsec_ans.get() == "":
            messagebox.showerror(
                "Error",
                "Please enter the answer",
                parent=self.root2
            )

        elif self.txtnew_pass.get() == "":
            messagebox.showerror(
                "Error",
                "Please enter the new password",parent=self.root2
            )

        else:

         conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Abhi@123",
            database="myproject_1"
        )

        my_cursor = conn.cursor()

        query = """
        SELECT * FROM my_data
        WHERE email=%s
        AND secu_question=%s
        AND secu_answer=%s
        """

        value = (
            self.txtuser.get(),
            self.combo_security.get(),
            self.txtsec_ans.get()
        )

        my_cursor.execute(query, value)

        row = my_cursor.fetchone()

        if row is None:

            messagebox.showerror(
                "Error",
                "Please enter correct Answer",parent=self.root2
            )

        else:

            query = """
            UPDATE my_data
            SET password=%s
            WHERE email=%s
            """

            value = (
                self.txtnew_pass.get(),
                self.txtuser.get()
            )

            my_cursor.execute(query, value)

            conn.commit()
            conn.close()

            messagebox.showinfo(
                "Info",
                "Your password has been reset, please login with new password",parent=self.root2
            )

            self.root2.destroy()



# ==============forgot pass=======================

    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter the email address to reset your password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Abhi@123", database="myproject_1")
            cursor = conn.cursor()
            query= "SELECT * FROM my_data WHERE email=%s"
            value = (self.txtuser.get(),)
            cursor.execute(query,value)
            row = cursor.fetchone()

            # print(row)
            if row is None:
                messagebox.showerror("MY ERROR,", "Please enter the correct email address")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("400x400+610+170")


                l = Label(
                    self.root2,
                    text="Forgot Password",
                    font=("times of new roman", 15, "bold"),
                    fg="red"
                )
                l.place(relx=0.5, y=35, anchor="center")


                security = Label(
                    self.root2,
                    text="Security Question",
                    font=("times of new roman", 15, "bold"),
                    fg="black",
                    bg="white"
                )
                security.place(relx=0.30, y=90, anchor="center")


                self.combo_security = ttk.Combobox(
                    self.root2,
                    font=("times of new roman", 10, "bold"),
                    state="readonly"
                )

                self.combo_security["values"] = (
                    "Select",
                    "Your Birth Place",
                    "Your Pet Name",
                    "Your Best Friend Name"
                )

                self.combo_security.current(0)

                self.combo_security.place(
                    relx=0.34,
                    y=106,
                    width=210,
                    height=30,
                    anchor="n"
                )


                sec_ans = Label(
                    self.root2,
                    text="Security Answer",
                    font=("times of new roman", 15, "bold"),
                    fg="black",
                    bg="white"
                )
                sec_ans.place(
                    relx=0.28,
                    y=176,
                    anchor="center"
                )


                self.txtsec_ans = ttk.Entry(
                    self.root2,
                    font=("times of new roman", 15)
                )

                self.txtsec_ans.place(
                    relx=0.34,
                    y=190,
                    width=210,
                    height=30,
                    anchor="n"
                )
                # ====new password label and entry field

                new_pass = Label(
                self.root2,
                text="New Password",
                font=("times of new roman",15,"bold"),
                fg="black",
                bg="white"
                )
                new_pass.place(relx=0.26, y=255, anchor=CENTER)

                self.txtnew_pass = ttk.Entry(
                    self.root2,
                    font=("times of new roman",15),
                    show="*"
                )
                self.txtnew_pass.place(
                    relx=0.34,
                    y=271,
                    width=210,
                    height=30,
                    anchor="n"
                )


                # ====RESET BUTN=====

                RESET_BUT = Button(
                                    self.root2,
                                    text="Reset",
                                    command=self.reset_password,
                                    font=("times of new roman", 15, "bold"),
                                    fg="WHITE",
                                    bg="GREEN"
                                )
                RESET_BUT.place(
                            relx=0.5,
                            y=340,
                            anchor="center"
                        )




class Register :
    def __init__(self,root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")


        # =========variable===========
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_security = StringVar()
        self.var_sec_ans = StringVar()
        self.var_passwd = StringVar()
        self.var_confpasswd = StringVar()


        # =========bg imae ===

        self.bg = ImageTk.PhotoImage(file=r"C:\Users\HP\login_form\new_reg_ph_bg.jpg")
        self.bg_image = Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        image = Image.open(r"C:\Users\HP\login_form\new_reg_ph_bg.jpg")
        image = image.resize((1550, 800), Image.Resampling.LANCZOS)

        self.bg = ImageTk.PhotoImage(image)

        self.bg_image = Label(self.root, image=self.bg)
        self.bg_image.place(x=0, y=0, width=1550, height=800)

# ======== left image ======

        self.left = ImageTk.PhotoImage(file=r"C:\Users\HP\login_form\aaawaw.jpg")
        self.left_image = Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

        frame1 = Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)


        # =======lable=========
        register_lbl = Label (frame1,text="REGISTER HERE",font=("times of new roman",15,"bold"),fg="green",bg="white")
        register_lbl.place(x=50,y=30)


        #====labe and entry ==

        fname = Label(frame1,text="First Name",font=("times of new roman",15,"bold"),fg="black",bg="white")
        fname.place(x=50,y=100)

        self.txtfname = ttk.Entry(frame1,font=("times of new roman",15,),textvariable=self.var_fname)
        self.txtfname.place(x=50,y=130,width=200)


        # ===lastname=======
        lastnm = Label(frame1,text="Last Name",font=("times of new roman",15,"bold"),fg="black",bg="white")
        lastnm.place(x=370,y=100)   

        self.txtlastnm = ttk.Entry(frame1,font=("times of new roman",15,),textvariable=self.var_lname)
        self.txtlastnm.place(x=370,y=130,width=200)

        # contact===========
        contact = Label(frame1,text="Contact",font=("times of new roman",15,"bold"),fg="black",bg="white")
        contact.place(x=50,y=170)   

        self.txtcontact = ttk.Entry(frame1,font=("times of new roman",15,),textvariable=self.var_contact    )
        self.txtcontact.place(x=50,y=200,width=200)


        # ==== email===
        email = Label(frame1,text="Email",font=("times of new roman",15,"bold"),fg="black",bg="white")
        email.place(x=370,y=170)

        self.txtemail = ttk.Entry(frame1,font=("times of new roman",15,),textvariable=self.var_email)
        self.txtemail.place(x=370,y=200,width=200)

        # ====security===
        security = Label(frame1,text = "Security Question",font=("times of new roman",15,"bold"),fg="black",bg="white")
        security.place(x=50,y=240)

        security.combo_security = ttk.Combobox(frame1,font=("times of new roman",10,"bold"),state="readonly",textvariable=self.var_security)
        security.combo_security["values"] = ("Select","Your Birth Place","Your Pet Name","Your Best Friend Name")
        security.combo_security.place(x=50,y=270,width=200,height=30)
        security.combo_security.current(0)


        # ===secu ans++

        sec_ans = Label(frame1,text = "security answer",font=("times of new roman",15,"bold"),fg="black",bg="white")
        sec_ans.place(x=370,y=240)

        self.txtsec_ans = ttk.Entry(frame1,font=("times of new roman",15 ,),textvariable=self.var_sec_ans)
        self.txtsec_ans.place(x=370,y=270,width=200)


        # ===passrd====
        passwd = Label(frame1,text = "password",font=("times of new roman",15,"bold"),fg="black",bg="white")
        passwd .place(x=50,y=310)

        self.txtpasswd = ttk.Entry(frame1,font=("times of new roman",15,),textvariable=self.var_passwd  )
        self.txtpasswd.place(x=50,y=340,width=200)     


        confpasswd = Label(frame1,text = "Confirm Password",font=("times of new roman",15,"bold"),fg="black",bg="white")
        confpasswd.place(x=370,y=310)

        self.confpasswd = ttk.Entry(frame1,font=("times of new roman",15 ,),textvariable=self.var_confpasswd)
        self.confpasswd.place(x=370,y=340,width=200)


        # ==============cehckbox=/
        self.cheackbox_var = IntVar()
        checkbox = Checkbutton(frame1,variable=self.cheackbox_var,text="I Agree The Terms & Conditions",font=("times of new roman",7,"bold"),fg="black",bg="light grey")
        checkbox.place(x=50,y=380)

# Register button image

      # ============= Register Button Image =============
      # ============= Register Button Image =============

        reg_img = Image.open(
         r"C:\Users\HP\login_form\register.png"
).convert("RGB")

# White space remove
        gray = ImageOps.grayscale(reg_img)
        bg = Image.new("L", gray.size, 255)
        diff = ImageChops.difference(gray, bg)

# Small difference ignore karo
        diff = diff.point(lambda p: 255 if p > 10 else 0)

        bbox = diff.getbbox()

        if bbox:

         reg_img = reg_img.crop(bbox)

# Final button size
        reg_img = reg_img.resize(
    (203, 40),
    Image.Resampling.LANCZOS
)

        self.reg_img = ImageTk.PhotoImage(reg_img)

        reg_btn = Button(
    frame1,
    command=self.register_data,
    image=self.reg_img,
    borderwidth=0,
    cursor="hand2",
    bg="white",
    activebackground="white"
)

        reg_btn.place(
    x=210,
    y=415,
    width=200,
    height=40
)


#  ===before login========

        login_btn = Button(
    frame1,
    text=" Login now > ",
    command=self.return_logic,
    font=("times of new roman", 10, ),
    fg="red",
    bg="white",
    borderwidth=0,
    cursor="hand2",
    activebackground="white",
    activeforeground="red"
)

        login_btn.place(
    x=210,
    y=452,
    width=200,
    height=20
)


# ========already have an account========
        already_account = Button(frame1,text="Already have an account?",command=self.return_logic,font=("times of new roman",10,"bold"),fg="black",bg="white",
        activebackground="white",activeforeground="black",borderwidth=0,cursor="hand2")
        already_account.place(x=210,y=470,width=200,height=20)



# =========functiion============
    def register_data(self):

     print("Register button clicked")

     if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_security.get() == "Select":
        messagebox.showerror(
            "Error",
            "All fields are required",
            parent=self.root
        )

     elif self.var_passwd.get() != self.var_confpasswd.get():
        messagebox.showerror(
            "Error",
            "Password & Confirm Password must be same",
            parent=self.root
        )

     elif self.cheackbox_var.get() == 0:
        messagebox.showerror(
            "Error",
            "Please agree to our terms and conditions",
            parent=self.root
        )

     else:


        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Abhi@123",
            database="myproject_1"
        )

        my_cursor = conn.cursor()

        query = "SELECT * FROM my_data WHERE email=%s"
        value = (self.var_email.get(),)

        my_cursor.execute(query, value)

        result = my_cursor.fetchone()

        if result:

            messagebox.showerror(
                "Error",
                "Email already exists",
                parent=self.root
            )

        else:

            insert_query = """
            INSERT INTO my_data
            (f_name, l_name, contact, email, secu_question, secu_answer, password)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            insert_values = (
                self.var_fname.get(),
                self.var_lname.get(),
                self.var_contact.get(),
                self.var_email.get(),
                self.var_security.get(),
                self.var_sec_ans.get(),
                self.var_passwd.get()
            )

            my_cursor.execute(insert_query, insert_values)

            conn.commit()

            messagebox.showinfo(
                "Success",
                "Registered Successfully",
                parent=self.root
            )

        conn.close()


    def return_logic(self):
        self.root.destroy()





class Hotel:
    def __init__(self, root):
        self.root = root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1540x800+0+0")
        self.root.configure(background="powder blue")

        # ================= Title =================
        lblTitle = Label(
            self.root,
            text="HOTEL MANAGEMENT SYSTEM",
            font=("times new roman", 35, "bold"),
            bg="black",
            fg="yellow"
        )
        lblTitle.place(x=0, y=0, width=1540, height=50)

        # ================= Main label =================
        lbl = Label(
            self.root,
            text="Welcome to Hotel Management System",
            font=("times new roman", 25, "bold"),
            bg="powder blue",
            fg="black"
        )
        lbl.place(relx=0.5, y=180, anchor="center")


if __name__ == "__main__":
    main()
