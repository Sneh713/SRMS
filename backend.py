import mysql.connector as connector
class studentresult:
    def __init__(self):
        self.con=connector.connect(user='root', password='sneh@singh111',
                              host='127.0.0.1',
                              database='srms')
        #print(self.con)
        query='create table if not exists faulty(userId varchar(10) primary key not null ,name varchar(30),dateofbirth date not null ,password varchar(20))'
        query1='create table if not exists student(enrollmentno varchar(10) primary key not null ,name varchar(30),dateofbirth date not null ,password varchar(20))'
        query2='create table if not exists faculty_details( userId varchar(10)primary key not null,name varchar(30),email varchar(30), education varchar(20),contect_no varchar(15),areas varchar(100))'
        query3='create table if not exists student_details(enrollmentno varchar(10) primary key not null,name varchar(30),email varchar(30) ,branch varchar(10), year int ,phone varchar(10), rsult_10 varchar(10), result_12 varchar(10))'
        query4='create table if not exists marks(enrollmentno varchar(10) primary key not null,name varchar(30), se int, lqt int, coa int)'
        query5='create table if not exists attendance(enrollmentno varchar(10) primary key not null,name varchar(30),dateof date, se int, lqt int, coa int)'
        cur=self.con.cursor()
        cur.execute(query)
        cur.execute(query1)
        cur.execute(query2)
        cur.execute(query3)
        cur.execute(query4)
        cur.execute(query5)
        #print("created")
    def insert_marks(self,enrollmentno,name,se,lqt,coa):
        query="insert into marks(enrollmentno,name,se,lqt,coa) values('{}','{}',{},{},{})".format(enrollmentno,name,se,lqt,coa)
        #print("sneh")
        #print(query)
        cur=self.con.cursor()
        #print("sneh1")
        #print(cur)
        cur.execute(query)
        #print("sneh3")
        self.con.commit()
        print("sneh ")
    def insert_attendance(self,enrollmentno,name,dateof,se,lqt,coa):
        query="insert into attendance(enrollmentno,name,dateof,se,lqt,coa) values('{}','{}',{},{},{},{})".format(enrollmentno,name,dateof,se,lqt,coa)
        #print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("sneh")
    def update_attendance(self,enrollmentno,se,lqt,coa):
        query=" update attendance set se={},lqt={},coa={} where enrollmentno='{}'".format(se,lqt,coa,enrollmentno)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("sneh")
    def update_marks(self,enrollmentno,se,lqt,coa):
        query=" update marks set se={},lqt={},coa={} where enrollmentno='{}'".format(se,lqt,coa,enrollmentno)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("sneh")
    def student_details(self,enrollmentno):
        query="select * from student_details where enrollmentno='{}'".format(enrollmentno)
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print()
            print("STUDENT DETAILS")
            print("enrollment no :",row[0])
            print("Name :",row[1])
            print("Email:", row[2])
            print("branch :",row[3])
            print("Year:",row[4])
            print("phone:",row[5])
            print("result of 10:",row[6])
            print("result of 12:",row[7])
            print()
    def faculty_details(self,enrollmentno):
        query="select * from faculty_details where userId='{}'".format(userId)
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print()
            print("ADMIN DETAILS")
            print("userId:",row[1])
            print("Name :",row[2])
            print("Email:", row[3])
            print("education :",row[4])
            print("contect_no:",row[5])
            print("areas:",row[6])
            print()
    def cheak_cgpa(self,enrollment):
        query="select enrollmentno,name,(se+lqt+coa)/30 as cgpa from marks where enrollmentno='{}'".format(enrollment)
        cur=self.con.cursor()
        cur.execute(query)
        #print(cur)
        for row in cur:
            print()
            print("Enrollmentno:",row[0])
            print("Name:",row[1])
            print("CGPA:",row[2])
            print()
        
    
    def login(self,number,password,s):
        #print("for fuculty enter 1 or student 2")
        
        if s==1:
            query="select * from faulty where userId='{}' and password='{}'".format(number,password)
            cur=self.con.cursor()
            cur.execute(query)
            #self.con.commit()
            print("login successfull")
        elif s==2:
            query="select * from student where enrollmentno='{}' and password='{}'".format(number,password)
            cur=self.con.cursor()
            cur.execute(query)
            #self.con.commit()
            print("login successfull")
        else:
            print("plese enter valid number, password,id")
    def cheak_marks(self,enrollment):
        query="select enrollmentno,name,se,lqt,coa from marks where enrollmentno='{}'".format(enrollment)
        cur=self.con.cursor()
        cur.execute(query)
        #print(cur)
        for row in cur:
            print()
            print("MARKS")
            print("Enrollmentno:",row[0])
            print("Name:",row[1])
            print("SE:",row[2])
            print("LQT:",row[3])
            print("COA:",row[4])
            print()
    def cheak_attendance(self,enrollment):
        query="select enrollmentno,name,se,lqt,coa from attendance where enrollmentno='{}'".format(enrollment)
        cur=self.con.cursor()
        cur.execute(query)
        #print(cur)
        for row in cur:
            print()
            print("ATTENDANCE")
            print("Enrollmentno:",row[0])
            print("Name:",row[1])
            print("SE:",row[2])
            print("LQT:",row[3])
            print("COA:",row[4])
            print()
        
        
        
            
            
            
                
            
        
student=studentresult()
#student.insert_marks("191B261","Silvi Malik",80,80,80)
#student.insert_attendance("191B261","silvi malik",20/5/2022,100,100,100)
#student.update_attendance("191B262",95,99,98)
#student.update_marks("191B262",90,90,90)
#student.login("191B260","sneh1singh111",2)
#student.student_details("191B262")
#student.faculty_details("111g23")
#student.cheak_cgpa("191B262")
#student.cheak_marks("191B262")
#student.cheak_attendance("191B262")
#student.login("111G23","abcdefgh",1)






