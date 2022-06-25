from backend import studentresult
from tkinter import *
#from PIL import Image, ImageTk
import tkinter.messagebox as tmsg
root=Tk()
st=studentresult()
root.title("SRMS")
root.geometry("700x500")
tmsg.showinfo("NOTE","WELCOME , IN SRMS ")

def student():
    top=Toplevel()
    top.geometry("400x300")
    top.title("LOGIN")
    def insert_user():
        try:
            st.login(userid.get(),password.get(),2)
            def login():
                #print("sneh")
                sm=studentresult()
                sm.student_details(enrollment.get())
            def marks():
                sm=studentresult()
                sm.cheak_marks(enrollment.get())
            def atte():
                sm=studentresult()
                sm.cheak_attendance(enrollment.get())
            def cgpa():
                sm=studentresult()
                sm.cheak_cgpa(enrollment.get())
            
            #print("hello")
            top=Toplevel()
            top.geometry("400x300")
            top.title("STUDENT")
            Label(top,text="WELCOME",pady=5,font="comicsansms 13 bold").grid(row=0,column=4)
            enrollment=Label(top,text="ENROLLMENT NO").grid(row=1,column=3)
            enrollment=StringVar()
            useridentry=Entry(top,textvariable=enrollment).grid(row=1,column=4)
            Button(top,text="About",command=login).grid(row=2,column=4)
            Button(top,text="marks",command=marks).grid(row=3,column=4)
            Button(top,text="attendance",command=atte).grid(row=4,column=4)
            Button(top,text="cgpa",command=cgpa).grid(row=5,column=4)
            
            
        except Exception as e:
            print(e)
    Label(top,text=" LOGIN PAGE",pady=5,font="comicsansms 13 bold").grid(row=0,column=3)
    userid=Label(top,text="ENROLLMENT NO").grid(row=1,column=2)
    name=Label(top,text="DATE OF BIRTH").grid(row=2,column=2)
    
    password=Label(top,text="PASSWORD").grid(row=3,column=2)
    userid=StringVar()
    name=StringVar()
    
    password=StringVar()
    useridentry=Entry(top,textvariable=userid).grid(row=1,column=3)
    nameentry=Entry(top,textvariable=name).grid(row=2,column=3)
    
    passwordenttry=Entry(top,textvariable=password).grid(row=3,column=3)
    Button(top,text="submit",command=insert_user).grid(row=4,column=3)
def faculty():
    top=Toplevel()
    top.geometry("400x300")
    top.title("LOGIN")
    def insert_user():
        try:
            st.login(userid.get(),password.get(),1)
            def login():
                #print("sneh")
                sm=studentresult()
                sm.student_details(enrollment.get())
                #sm.faculty_details(userid2.get())
            def marks():
                sm=studentresult()
                sm.update_marks(enrollment.get(),se.get(),lqt.get(),coa.get())
            def atte():
                sm=studentresult()
                sm.update_attendance(enrollment.get(),se.get(),lqt.get(),coa.get())
            #def cgpa():
                #sm=studentresult()
                #sm.cheak_cgpa(enrollment.get())
            #print("hello")
            top=Toplevel()
            top.geometry("400x300")
            top.title("ADMIN")
            Label(top,text="WELCOME",pady=5,font="comicsansms 13 bold").grid(row=0,column=4)
            enrollment=Label(top,text="USER ID").grid(row=1,column=3)
            userid2=StringVar()
            useri1dentry=Entry(top,textvariable=userid2).grid(row=1,column=4)
            enrollment=Label(top,text="ENROLLMENT NO").grid(row=2,column=3)
            enrollment=StringVar()
            useridentry=Entry(top,textvariable=enrollment).grid(row=2,column=4)
            se=Label(top,text="marks of SE").grid(row=3,column=3)
            se=IntVar()
            user2identry=Entry(top,textvariable=se).grid(row=3,column=4)
            lqt=Label(top,text="Marks of LQT").grid(row=4,column=3)
            lqt=IntVar()
            useri3dentry=Entry(top,textvariable=lqt).grid(row=4,column=4)
            coa=Label(top,text="Marks of COA").grid(row=5,column=3)
            coa=IntVar()
            useri4dentry=Entry(top,textvariable=coa).grid(row=5,column=4)
            Button(top,text="ABOUT",command=login).grid(row=6,column=4)
            Button(top,text="marks",command=marks).grid(row=7,column=4)
            Button(top,text="attendance",command=atte).grid(row=8,column=4)
            #Button(top,text="cgpa",command=cgpa).grid(row=8,column=3)
            
            
        except Exception as e:
            print(e)
    Label(top,text=" LOGIN PAGE",pady=5,font="comicsansms 13 bold").grid(row=0,column=3)
    userid=Label(top,text="USER ID").grid(row=1,column=2)
    name=Label(top,text="DATE of BIRTH").grid(row=2,column=2)
    
    password=Label(top,text="PASSWORD").grid(row=3,column=2)
    userid=StringVar()
    name=StringVar()
    
    password=StringVar()
    useridentry=Entry(top,textvariable=userid).grid(row=1,column=3)
    nameentry=Entry(top,textvariable=name).grid(row=2,column=3)
    
    passwordenttry=Entry(top,textvariable=password).grid(row=3,column=3)
    Button(top,text="submit",command=insert_user).grid(row=4,column=3)
    
def password():
    tmsg.showinfo("SRMS","Password , for password mail to singhsneh58@gmail.com")




f0 = Frame(root, width=400, height=70,bg="red")
Label(f0, text="STUSENT RESULT MANAGEMENT SYSTEM", font="lucida 25 bold").pack()
f0.pack()
f1 = Frame(root, width=400, height=195, pady=14)
Label(f1, text=" HOME  ", font="lucida 15 bold").pack()
Button(f1,text="     STUDENT     ",command=student).pack(pady=10)

Button(f1,text=" FACULTY ",command=faculty).pack(pady=10)

Button(f1,text="FORGATE PASS",command=password).pack(pady=10)


f1.pack()
f2 = Frame(root, width=400, height=195, pady=14, padx=22)
Label(f2, text="BY", font="lucida 18 bold").pack()
Label(f2, text="191B261 191B262 191B263", font="lucida 20 bold").pack()

f2.pack()


root.mainloop()

            
