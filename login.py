from tkinter import *
from tkinter import messagebox as mb
import sqlite3 as sql
import main
import _thread

class login:
    def __init__(self):

    #def login():
        try:
            reg.destroy()
        except:
            pass
        global log
        log = Tk()
        log.title('Login Page')
        log.geometry('420x450+220+170')
        log.configure(bg='powder blue')
        log.resizable(0,0)

        bg = PhotoImage(file ="resources/background.png")

        canvas1 = Canvas(log,width=420,height=450)
        canvas1.pack(fill ="both", expand =True)
        canvas1.create_image(0,0,image =bg,anchor ="nw")

        canvas1.create_text(200,40,text="MEETZONE",font=('Comic Sans MS',40,'bold'),fill='dark blue',activefill='blue')
        canvas1.create_text(80,100,text='UserName',font=('Comic Sans MS',20,'bold'),fill='dark blue',activefill='blue')

        # log_label = Label(log, text='MEETZONE',bg='powder blue', width=20, height=1, font=('Comic Sans MS',40,'bold'),fg='indigo')
        # log_label.pack()

        # u = Label(log, text='Username :', font=('Comic Sans MS',14,'bold'),bg='powder blue',fg='indigo')
        # u.place(x=10,y=80)
        
        user_entry = Entry(log, font=('Arial Black',10,'bold'),  width=25,bg='white')
        user_entry.place(x=30, y=120)

        canvas1.create_text(80,180,text='Password ',font=('Comic Sans MS',20,'bold'),fill='dark blue',activefill='blue')


        # p = Label(log, text='Password :', font=('Comic Sans MS',14,'bold'),bg='powder blue',fg='indigo')
        # p.place(x=10,y=160)
        
        pass_entry = Entry(log,show='*', font=('Arial Black',10,'bold'),  width=25,bg='white')
        pass_entry.place(x=30, y=200)

        resp = Label(log, text='',font=('Arial Black',10,'bold'),bg='powder blue')
        resp.place(x=30, y=290)
        
        def log_func(*args):

            data_base = sql.connect('login_app.db')
            c = data_base.cursor()

            user = user_entry.get()
            password = pass_entry.get()

            try:
                c.execute(f'select Password from LOG_DETAILS where Username = "{user}" ')

                b = c.fetchall()

                for i in b:
                    passw = i[0]

                    if password == passw:
                        c.execute(f'select name from LOG_DETAILS where Username= "{user}"')
                        b = c.fetchall()[0][0]
                        username_name = b
                        resp.configure(text=f'Login Successful\n Welcome {b} ', fg='green')
                        log.destroy()
                        f = open('isLog.txt','w')
                        to_write = 'logged in,'+b
                        f.write(to_write)
                        f.close()
                        main.main_loop(b)

                    else:
                        resp.configure(text='Wrong Password', fg='red')
                    
            except UnboundLocalError:
                resp.configure(text=f'Username {user} Does Not Exist', fg='red')


        submit = Button(log, text='Log-in',font=('Comic Sans MS',10,'bold'), width=14, command=log_func,bd=0,fg='indigo')
        submit.place(x=30, y=260)

        canvas1.create_text(160,360,text='Click On Register If You Don\'t Have An Account.',font=('Comic Sans MS',9,'italic'),fill='dark blue',activefill='blue')

        # Label(log, text='Click On Register If You Don\'t Have An Account.',font=('Courier',10,'italic'),bg='powder blue',fg='dark blue').place(x=50,y=350)

        Button(log,text='Register',font=('',10,'underline','italic'),bg='powder blue',command=register,fg='blue').place(x=60,y=370)

        log.bind('<Return>', log_func)

        log.mainloop()

class register:
    def __init__(self):

#def register():
        try:
           log.destroy()
        except:
           pass

                
        global reg
        reg = Tk()
        reg.title('Register Page')
        reg.configure(bg='powder blue')
        reg.geometry('420x450+220+170')
        reg.resizable(0,0)

        bg = PhotoImage(file ="resources/background.png")

        canvas2 = Canvas(reg,width=420,height=450)
        canvas2.pack(fill ="both", expand =True)
        canvas2.create_image(0,0,image =bg,anchor ="nw")

        canvas2.create_text(200,40,text="MEETZONE",font=('Comic Sans MS',40,'bold'),fill='dark blue',activefill='blue')


        # reg_label = Label(reg, text='MEETZONE', width=20, height=1, font=('Comic Sans MS',40,'bold'),bg='powder blue',fg='indigo')
        # reg_label.pack()


        canvas2.create_text(90,100,text='Full Name ', font=('Comic Sans MS',20,'bold'),fill='dark blue',activefill='blue')

        # n = Label(reg, text='Please Enter Your Name :', font=('Comic Sans MS',14,'bold'),bg='powder blue', fg ='indigo')
        # n.place(x=10,y=80)
                
        name_entry = Entry(reg, font=('Arial Black',10,'bold'),  width=25,bg='white')
        name_entry.place(x=40,y=120)

        canvas2.create_text(90,180,text='UserName', font=('Comic Sans MS',20,'bold'),fill='dark blue',activefill='blue')



        # u = Label(reg, text='Please Enter Your Username :', font=('Comic Sans MS',14,'bold'),bg='powder blue',fg='indigo')
        # u.place(x=10,y=160)
                
        user_entry = Entry(reg, font=('Arial Black',10,'bold'),  width=25,bg='white')
        user_entry.place(x=40, y=200)

        canvas2.create_text(110,260,text='New Password', font=('Comic Sans MS',20,'bold'),fill='dark blue',activefill='blue')


        # p = Label(reg, text='Please Enter New Password :', font=('Comic Sans MS',14,'bold'),bg='powder blue', fg='indigo')
        # p.place(x=10,y=240)
                
        pass_entry = Entry(reg,show='*', font=('Arial Black',10,'bold'),  width=25,bg='white')
        pass_entry.place(x=40, y=280)


        def reg_func(*args):

           
            data_base = sql.connect('login_app.db')
            c = data_base.cursor()

            name = name_entry.get().title()
            user = user_entry.get()
            password = pass_entry.get()

            if name != '' and user != '' and password != '':

                c.execute('select Username from LOG_DETAILS')

                l = c.fetchall()
                ex_t = False
                for i in l:
                    if user == i[0]:
                        ex_t = True
                        break
                    else:
                        ex_t = False
                        
                if ex_t == True:
                    mb.showerror('Register',f'{user} Already Exist.')
                else:                
                    c.execute(f'insert into LOG_DETAILS values("{name}","{user}","{password}","0.png")')
                    data_base.commit()
                    name_entry.delete(0, END)
                    user_entry.delete(0, END)
                    pass_entry.delete(0, END)
                    global username_name
                    username_name = name
                    reg.destroy()
                    f = open('isLog.txt','w')
                    to_write = 'logged in,'+username_name
                    f.write(to_write)
                    f.close()
                    main.main_loop(username_name)
            else:
                mb.showerror('Register','Please Fill All The Fields.')

        submit = Button(reg, text='Register',font=('Comic Sans MS',10,'bold'), width=14, bg='powder blue', command=reg_func,bd=0,fg='indigo')
        submit.place(x=40, y=320)

        canvas2.create_text(110,380,text='Already Have An Account.',font=('Comic Sans MS',9,'italic'),fill='dark blue',activefill='blue')

        # Label(reg, text='Already Have An Account.',font=('Courier',10,'italic'),bg='powder blue',fg='dark blue').place(x=50,y=375)

        Button(reg,text='Log_In',font=('',10,'underline','italic'),bg='powder blue',fg='blue',command=login).place(x=60,y=390)

        reg.bind('<Return>', reg_func)


        reg.mainloop()



##register()


