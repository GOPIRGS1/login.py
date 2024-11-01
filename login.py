from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
db_connection=pymysql.connect(
    host='localhost',
    user='root',
    password='Velavan@2019',
    database='database' 
    )
my_database = db_connection.cursor()
print("connected sucessfully")
admin_list = []
database_list=[]
root = Tk()
root.title("CRM")
root.geometry("1200x800")
root.configure(background="beige")
def admin_signin():
    name = e.get()
    password = E.get()
    if not name  or not password:
        messagebox.showerror("error")
        return
    else:
        sql_statement="INSERT INTO admin_register (name,password) values(%s,%s) "
        values=(name,password)
        my_database.execute(sql_statement,values)
        db_connection.commit()
        admin_list.append({'name':name,'password':password})
        messagebox.showinfo("sucess","admin registered sucessfully")
    

t=Frame(root,bg="navy blue",height=600,width=500)
t.pack(fill=X)
w=Label(root,text="Login Page",font=("Algerian",20,"italic"),bg="navy blue",fg="white")
n=Label(root,text="Username",font=("Algerian",20,"italic"),bg="navy blue",fg="white")
d=Label(root,text="Don't have account? ",font=("Algerian",20,"italic"),bg="navy blue",fg="white")
P=Label(root,text="Password",font=("Algerian",20,"italic"),bg="navy blue",fg="white")
e=Entry(root,text="",font=("Algerian",20,"italic"),bg="white",fg="black")
E=Entry(root,show="*",font=("Algerian",20,"italic"),bg="white",fg="black")
w.place(x=500,y=20)
n.place(x=300,y=100)
P.place(x=300,y=180)
d.place(x=300,y=500)
e.place(x=500,y=100)
E.place(x=500,y=180)
b=Button(root,text="Login",font=("Algerian",20,"italic"),bg="green",fg="white",activebackground="aqua",activeforeground="white",command=admin_signin)
#B=Button(root,text="Sign in",font=("Algerian",20,"italic"),bg="orange",fg="white",activebackground="green",activeforeground="white")
b.place(x=500,y=300)
#B.place(x=700,y=500)
