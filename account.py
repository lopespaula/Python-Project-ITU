

# import mysql.connector as mysql
import sqlite3 as mysql

from tkinter import *
from tkinter import messagebox as mb

def account_func(username):
    
    db = mysql.connect('login_app.db')
    c = db.cursor()

    def change_info(arg):
        c.execute(f'select password from log_details where name = "{username}"')
        p = c.fetchone()[0]
        print(p)
        print(cur_pass.get(), 'done')

        if cur_pass.get() == p:
            req = req_pass.get()
            c.execute(f'update log_details set {arg} = "{req}" where name="{username}"')
            mb.showinfo('Done',f'{arg} Updated.\n Please Logout and login again to see changes.')
            db.commit()
        else:
            mb.showerror('Failed','Password Is Incorrect')

    def change_avatar():

        def set_av(no):
            av.destroy()
            no = str(no)
            c.execute(f'update log_details set avatar = "{no}.png" where name="{username}"')
            db.commit()
            c.execute(f'select avatar from log_details where name = "{username}"')
            avar_no = c.fetchone()[0]
            avatar = PhotoImage(file=f'avatars/{avar_no}')
            av_button.configure(image=avatar)
            mb.showinfo('success','Avatar Changed. Please logout and log back again!')
            pro.destroy()





        bg = 'Powder Blue'
        av = Toplevel()
        av.geometry('560x650')
        av.resizable(0,0)
        av.title('Choose Avatar')
        av.configure()

        bacg = PhotoImage(file ="resources/background.png")


        
        frame=Frame(av,width=560,height=650)
        frame.pack(expand=True, fill=BOTH)

        canvas1 = Canvas(frame)
        canvas1.pack(fill ="both", expand =True)
        canvas1.create_image(0,0,image =bacg,anchor ="nw")







        canvas1.create_text(200,20,text='Choose Avatar',font=('Comic Sans MS',40,'bold'),fill='dark blue',activefill='blue')





        img_0 = PhotoImage(file='avatars/0.png')
        av_button0 = Button(av, image=img_0,bg=bg,command=lambda : set_av(0),width=126,height=139,bd=0,borderwidth=0)
        av_button0.place(x=10,y=50)

        img_1 = PhotoImage(file='avatars/1.png')
        av_button1 = Button(av, image=img_1,bg=bg,command=lambda : set_av(1),width=126,height=139,bd=0,borderwidth=0)
        av_button1.place(x=140,y=50)

        img_2 = PhotoImage(file='avatars/2.png')
        av_button2 = Button(av, image=img_2,bg=bg,command=lambda : set_av(2),width=126,height=139,bd=0,borderwidth=0)
        av_button2.place(x=270,y=50)

        img_11 = PhotoImage(file='avatars/11.png')
        av_button11 = Button(av, image=img_11,bg=bg,command=lambda : set_av(11),width=126,height=139,bd=0,borderwidth=0)
        av_button11.place(x=400,y=50)


        img_3 = PhotoImage(file='avatars/3.png')
        av_button3 = Button(av, image=img_3,bg=bg,command=lambda : set_av(3),width=126,height=139,bd=0,borderwidth=0)
        av_button3.place(x=10,y=200)

        img_4 = PhotoImage(file='avatars/4.png')
        av_button4 = Button(av, image=img_4,bg=bg,command=lambda : set_av(4),width=126,height=139,bd=0,borderwidth=0)
        av_button4.place(x=140,y=200)

        img_5 = PhotoImage(file='avatars/5.png')
        av_button5 = Button(av, image=img_5,bg=bg,command=lambda : set_av(5),width=126,height=139,bd=0,borderwidth=0)
        av_button5.place(x=270,y=200)

        img_12 = PhotoImage(file='avatars/12.png')
        av_button12 = Button(av, image=img_12,bg=bg,command=lambda : set_av(12),width=126,height=139,bd=0,borderwidth=0)
        av_button12.place(x=400,y=200)

        img_6 = PhotoImage(file='avatars/6.png')
        av_button6 = Button(av, image=img_6,bg=bg,command=lambda : set_av(6),width=126,height=139,bd=0,borderwidth=0)
        av_button6.place(x=10,y=350)

        img_7 = PhotoImage(file='avatars/7.png')
        av_button7 = Button(av, image=img_7,bg=bg,command=lambda : set_av(7),width=126,height=139,bd=0,borderwidth=0)
        av_button7.place(x=140,y=350)

        img_8 = PhotoImage(file='avatars/8.png')
        av_button8 = Button(av, image=img_8,bg=bg,command=lambda : set_av(8),width=126,height=139,bd=0,borderwidth=0)
        av_button8.place(x=270,y=350)

        img_13 = PhotoImage(file='avatars/13.png')
        av_button13 = Button(av, image=img_13,bg=bg,command=lambda : set_av(13),width=126,height=139,bd=0,borderwidth=0)
        av_button13.place(x=400,y=350)


        img_9 = PhotoImage(file='avatars/9.png')
        av_button9 = Button(av, image=img_9,bg=bg,command=lambda : set_av(9),width=126,height=139,bd=0,borderwidth=0)
        av_button9.place(x=10,y=500)

        img_10 = PhotoImage(file='avatars/10.png')
        av_button10 = Button(av, image=img_10,bg=bg,command=lambda : set_av(10),width=126,height=139,bd=0,borderwidth=0)
        av_button10.place(x=140,y=500)

        img_14 = PhotoImage(file='avatars/14.png')
        av_button14 = Button(av, image=img_14,bg=bg,command=lambda : set_av(14),width=126,height=139,bd=0,borderwidth=0)
        av_button14.place(x=270,y=500)

        img_15 = PhotoImage(file='avatars/15.png')
        av_button15 = Button(av, image=img_15,bg=bg,command=lambda : set_av(15),width=126,height=139,bd=0,borderwidth=0)
        av_button15.place(x=400,y=500)






        
        av.mainloop()

    def del_func():
        res = mb.askquestion('Confirm', 'Are You Sure That You Want To Delete Your Account.',icon='error')
        if res == 'yes':
            c.execute(f'delete from log_details where name = "{username}"')
            db.commit()
        pro.destroy()
        





    def name_func(arg):

        name = Tk()
        name.geometry('250x200')
        name.title(f'Change {arg}')
        name.configure(bg=bg)
        name.resizable(0,0)


       
        Label(name, text=f'Change {arg}',font=('Comic Sans MS',20,'bold'),bg='powder blue',fg='dark blue').pack()

        Label(name, text='Enter Your Current Password',font=('Comic Sans MS',13),bg='powder blue',fg='dark blue').place(x=5,y=40)

        global cur_pass
        cur_pass = Entry(name,font=('Calibri Light',10,'bold'),show='*')
        cur_pass.place(x=5,y=70)

        Label(name, text=f'Enter {arg} You Want To Set',font=('Comic Sans MS',13),bg='powder blue',fg='dark blue').place(x=5,y=100)

        global req_pass
        req_pass = Entry(name,font=('Calibri Light',10,'bold'))
        req_pass.place(x=5,y=130)

        Button(name, text='Apply Changes',bd=0,bg='White',fg='dark blue',font=('Comic Sans MS',10,'bold'),command=lambda:change_info(arg)).place(x=50,y=170)

    


    bg = 'Powder Blue'

    pro = Toplevel()
    pro.geometry('420x450+220+170')
    pro.resizable(0,0)
    pro.title('Account Settings')
    pro.configure()

    bacg = PhotoImage(file ="resources/background.png")

    canvas1 = Canvas(pro,width=420,height=500)
    canvas1.pack(fill ="both", expand =True)
    canvas1.create_image(0,0,image =bacg,anchor ="nw")



    c.execute(f'select avatar from log_details where name = "{username}"')

    avar_no = c.fetchone()[0]

    avatar = PhotoImage(file=f'avatars/{avar_no}')

    av_button = Button(pro, image=avatar,bg=bg,command=change_avatar,width=126,height=139,bd=0,borderwidth=0)
    av_button.place(x=10,y=30)



    c.execute(f'select username from log_details where name = "{username}"')
    user = c.fetchone()[0]

    pencil = PhotoImage(file='resources/pencil-32.png')

    canvas1.create_text(280,100,text='@'+user,font=('Comic Sans MS',16,'bold'),fill='dark blue',activefill='blue')
    canvas1.create_text(280,80,text=username.title(),font=('Comic Sans MS',20,'bold'),fill='dark blue',activefill='blue')
    canvas1.create_text(120,230,text='Change Account Name',font=('Comic Sans MS',20,'bold'),fill='dark blue',activefill='blue')


    Button(pro, image=pencil,bg=bg,bd=0,width=30,height=30,command=lambda : name_func('Name'),fg='white').place(x=280,y=220)


    canvas1.create_text(100,280,text='Change UserName',font=('Comic Sans MS',20,'bold'),fill='dark blue',activefill='blue')

    Button(pro, image=pencil,bg=bg,bd=0,width=30,height=30,command=lambda : name_func('Username'),fg='white').place(x=280,y=270)

    canvas1.create_text(95,330,text='Change Password',font=('Comic Sans MS',20,'bold'),fill='dark blue',activefill='blue')



    Button(pro, image=pencil,bg=bg,bd=0,width=30,height=30,command=lambda : name_func('Password'),fg='white').place(x=280,y=320)

    canvas1.create_text(100,380,text='Delete Account',font=('Comic Sans MS',20,'bold'),fill='dark blue',activefill='blue')


  
    delete = PhotoImage(file='resources/delete-32.png')

    Button(pro, image=delete,bg=bg,bd=0,width=30,height=30,command=del_func,fg='white').place(x=280,y=370)
    

    pro.mainloop()


