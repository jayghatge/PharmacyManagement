from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
class PharmacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

        self.addmed_var=StringVar()
        self.refMed_var=StringVar()
        
        self.ref_var=StringVar()
        self.typeMed_var=StringVar()
        self.medName_var=StringVar()
        self.lot_var=StringVar()
        self.issuedate_var=StringVar()
        self.expdate_var=StringVar()
        self.uses_var=StringVar()
        self.sideEffect_var=StringVar()
        self.warning_var=StringVar()
        self.dosage_var=StringVar()
        self.price_var=StringVar()
        self.product_var=StringVar()
        
        
        lbltitle=Label(self.root,text="PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE,bg='white',fg="darkgreen",font=("times new roman",50,"bold"),padx=2,pady=4)

        lbltitle.pack(side=TOP,fill=X)

        img1=Image.open("C:\\Users\\jay\\OneDrive\\Desktop\\pharmacy management system\\mba.jpg")
        img1=img1.resize((80,80),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=70,y=20)
        
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1530,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",fg="darkgreen",font=("arial",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department",fg="darkgreen",font=("arial",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)


        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=520,width=1530,height=65)
        

        btnAddData=Button(ButtonFrame,command=self.add_data,text="Medicine Add",font=("arial",12,"bold"),bg="darkgreen",fg="white")
        btnAddData.grid(row=0,column=0)

        btnUpdateMed=Button(ButtonFrame,command=self.Update,text="UPDATE",font=("arial",13,"bold"),width=14,bg="darkgreen",fg="white")
        btnUpdateMed.grid(row=0,column=1)

        btnDeleteMed=Button(ButtonFrame,command=self.delete,text="DELETE",font=("arial",13,"bold"),width=14,bg="darkgreen",fg="white")
        btnDeleteMed.grid(row=0,column=2)
        
        btnResetMed=Button(ButtonFrame,text="RESET",font=("arial",13,"bold"),width=14,bg="darkgreen",fg="white")
        btnResetMed.grid(row=0,column=3)

        btnExitMed=Button(ButtonFrame,text="Exit",font=("arial",13,"bold"),width=14,bg="darkgreen",fg="white")
        btnExitMed.grid(row=0,column=4)

        lblSearch=Label(ButtonFrame,font=("arial",17,"bold"),text="Search By",padx=2,bg="red",fg="white")
        lblSearch.grid(row=0,column=5,sticky=W)
        
        self.search_var=StringVar()   
        serch_combo=ttk.Combobox(ButtonFrame,textvariable=self.search_var,width=12,font=("arial",17,"bold"),state="readyonly")
        serch_combo["values"]=("Ref","Medicine Name","Lot")
        serch_combo.grid(row=0,column=6)
        serch_combo.current(0)
        
        self.searchTxt_var=StringVar()
        txtSerch=Entry(ButtonFrame,textvariable=self.searchTxt_var,bd=3,relief=RIDGE,width=12,font=("arial",17,"bold"))
        txtSerch.grid(row=0,column=7)

        searchBtn=Button(ButtonFrame,command=self.search_data,text="SEARCH",font=("arial",13,"bold"),width=13,bg="darkgreen",fg="white")
        searchBtn.grid(row=0,column=8)

        showAll=Button(ButtonFrame,text="SHOW ALL",font=("arial",13,"bold"),width=13,bg="darkgreen",fg="white")
        showAll.grid(row=0,column=9)

        lblrefno=Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No.",padx=2)
        lblrefno.grid(row=0,column=0,sticky=W)
        
        conn=mysql.connector.connect(host="localhost",username="root",password="jagnjr10",database="mydata")
        mycursor=conn.cursor()
        mycursor.execute("select Ref from pharma")
        row=mycursor.fetchall()
        
        
        ref_combo=ttk.Combobox(DataFrameLeft,textvariable=self.ref_var,font=("arial",17,"bold"),state="readonly")
        ref_combo["values"]=row
        ref_combo.grid(row=0,column=1)
        ref_combo.current(0)
        
        lblTypeofMedicine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Type Of medicine",padx=2)
        lblTypeofMedicine.grid(row=1,column=0,sticky=W)
        txtTypeofMedicine=Entry(DataFrameLeft,textvariable=self.typeMed_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtTypeofMedicine.grid(row=1,column=1)
 
 
        comTypeofMedicine=ttk.Combobox(DataFrameLeft,textvariable=self.typeMed_var,font=("arial",17,"bold"),state="readonly")
        comTypeofMedicine["values"]=("Tablet","Liquid","Capsules","Topical Medicines","Drops","Inhales","Injections")

        comTypeofMedicine.grid(row=1,column=1)
        comTypeofMedicine.current(0)

        lblMedicineName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medicine Name",padx=2,pady=6)
        lblMedicineName.grid(row=2,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="jagnjr10",database="mydata")
        mycursor=conn.cursor()
        mycursor.execute("select `Medicine Name` from pharma")
        med=mycursor.fetchall()
        
        comMedicineName=ttk.Combobox(DataFrameLeft,textvariable=self.medName_var,font=("arial",17,"bold"),state="readonly")
        comMedicineName["values"]=med
        comMedicineName.grid(row=2,column=1)
        comMedicineName.current(0)

        lblLotNo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot No.",padx=2,pady=6)
        lblLotNo.grid(row=3,column=0,sticky=W)
        txtLotNo=Entry(DataFrameLeft,textvariable=self.lot_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtLotNo.grid(row=3,column=1)

        lblIssueDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date",padx=2,pady=6)
        lblIssueDate.grid(row=4,column=0,sticky=W)
        txtIssueDate=Entry(DataFrameLeft,textvariable=self.issuedate_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtIssueDate.grid(row=4,column=1)

        lblExpDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Exp Date",padx=2,pady=6)
        lblExpDate.grid(row=5,column=0,sticky=W)
        txtExpDate=Entry(DataFrameLeft,textvariable=self.expdate_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtExpDate.grid(row=5,column=1)

        lblUses=Label(DataFrameLeft,font=("arial",12,"bold"),text="Uses:",padx=2,pady=6)
        lblUses.grid(row=6,column=0,sticky=W)
        txtUses=Entry(DataFrameLeft,textvariable=self.uses_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtUses.grid(row=6,column=1)

        lblSideEffect=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=7,column=0,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,textvariable=self.sideEffect_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtSideEffect.grid(row=7,column=1)

        lblprecWarning=Label(DataFrameLeft,font=("arial",12,"bold"),text="Prec&Warning",padx=2,pady=6)
        lblprecWarning.grid(row=0,column=2,sticky=W)
        txtprecWarning=Entry(DataFrameLeft,textvariable=self.warning_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtprecWarning.grid(row=0,column=3)
        
        lblDosage=Label(DataFrameLeft,font=("arial",12,"bold"),text="Dosage:",padx=2,pady=6)
        lblDosage.grid(row=1,column=2,sticky=W)
        txtDosage=Entry(DataFrameLeft,textvariable=self.dosage_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtDosage.grid(row=1,column=3)

        lblPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Tablets Price:",padx=2,pady=6)
        lblPrice.grid(row=2,column=2,sticky=W)
        txtPrice=Entry(DataFrameLeft,textvariable=self.price_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtPrice.grid(row=2,column=3)

        lblProductQt=Label(DataFrameLeft,font=("arial",12,"bold"),text="Product QT:",padx=2,pady=6)
        lblProductQt.grid(row=3,column=2,sticky=W)
        txtProductQt=Entry(DataFrameLeft,textvariable=self.product_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtProductQt.grid(row=3,column=3,sticky=W)
        

        lblhome=Label(DataFrameLeft,font=("arial",12,"bold"),text="stay home stay safe:",padx=2,pady=6,bg="white",fg="red",width=37)
        lblhome.place(x=410,y=140)

        img2=Image.open("C:\\Users\\jay\\OneDrive\\Desktop\\pharmacy management system\\tab.jpg")
        img2=img2.resize((150,135),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        b1.place(x=770,y=330)

        img3=Image.open("C:\\Users\\jay\\OneDrive\\Desktop\\pharmacy management system\\njr.jpg")
        img3=img3.resize((150,135),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(self.root,image=self.photoimg3,borderwidth=0)
        b1.place(x=620,y=330)

        img4=Image.open("C:\\Users\\jay\\OneDrive\\Desktop\\pharmacy management system\\lab.jpg")
        img4=img4.resize((150,135),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(self.root,image=self.photoimg4,borderwidth=0)
        b1.place(x=475,y=330)

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department",fg="darkgreen",font=("arial",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)


        img5=Image.open("C:\\Users\\jay\\OneDrive\\Desktop\\pharmacy management system\\rss.jpg")
        img5=img5.resize((200,75),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(self.root,image=self.photoimg5,borderwidth=0)
        b1.place(x=960,y=160)

        img6=Image.open("C:\\Users\\jay\\OneDrive\\Desktop\\pharmacy management system\\rss.jpg")
        img6=img6.resize((200,75),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b1=Button(self.root,image=self.photoimg6,borderwidth=0)
        b1.place(x=1160,y=160)

        lblrefno=Label(DataFrameRight,font=("arial",12,"bold"),text="Reference No.:",padx=2,pady=6)
        lblrefno.place(x=0,y=80)
        txtrefno=Entry(DataFrameRight,textvariable=self.refMed_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtrefno.place(x=135,y=80)

        lblmedName=Label(DataFrameRight,font=("arial",12,"bold"),text="Medicine Name:",padx=2,pady=6)
        lblmedName.place(x=0,y=110)
        txtmedName=Entry(DataFrameRight,textvariable=self.addmed_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtmedName.place(x=135,y=110)

        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=150,width=290,height=160)
        
        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.medicine_table=ttk.Treeview(side_frame,column=("Ref","Medicine Name"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)
        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("Ref",text="Ref")
        self.medicine_table.heading("Medicine Name",text="Medicine Name")

        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)                     
        
        self.medicine_table.column("Ref",width=100)
        self.medicine_table.column("Medicine Name",width=100)
        
        self.medicine_table.bind("<ButtonRelease-1>",self.Medget_cursor)
        
        down_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="darkgreen")
        down_frame.place(x=330,y=150,width=135,height=160)

        btnAddmed=Button(down_frame,command=self.AddMed,text="Add",font=("arial",12,"bold"),width=12,bg="lime",fg="white",pady=4)
        btnAddmed.grid(row=0,column=0)

        btnUpdatemed=Button(down_frame,command=self.UpdateMed,text="UPDATE",font=("arial",12,"bold"),width=12,bg="purple",fg="white",pady=4)
        btnUpdatemed.grid(row=1,column=0)

        btnDeletemed=Button(down_frame,command=self.DeleteMed,text="DELETE",font=("arial",12,"bold"),width=12,bg="red",fg="white",pady=4)
        btnDeletemed.grid(row=2,column=0)

        btnClearmed=Button(down_frame,command=self.ClearMed,text="CLEAR",font=("arial",12,"bold"),width=12,bg="orange",fg="white",pady=4)
        btnClearmed.grid(row=3,column=0)
        
        Framedetails=Frame(self.root,bd=15,relief=RIDGE)
        Framedetails.place(x=0,y=580,width=1530,height=210)
        
        Table_frame=Frame(Framedetails,bd=15,relief=RIDGE,padx=20)
        Table_frame.place(x=0,y=1,width=1500,height=180)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.pharmacy_table=ttk.Treeview(Table_frame,column=("ref","type","tabletname","lotno","issuedate","expdate","uses","sideeffect","warning","dosage","price","productqt")
                                             ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)
        
        self.pharmacy_table["show"]="headings"
        

        self.pharmacy_table.heading("ref",text="Reference No.")
        self.pharmacy_table.heading("type",text="Type of medicine")
        self.pharmacy_table.heading("tabletname",text="Tablet Name")
        self.pharmacy_table.heading("lotno",text="Lot No.")
        self.pharmacy_table.heading("issuedate",text="Issue Date")
        self.pharmacy_table.heading("expdate",text="Exp Date")
        self.pharmacy_table.heading("uses",text="Uses")
        self.pharmacy_table.heading("sideeffect",text="Side Effect")
        self.pharmacy_table.heading("warning",text="Prec&warning")
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price")
        self.pharmacy_table.heading("productqt",text="Product Qts")
        self.pharmacy_table.pack(fill=BOTH,expand=1)
        
        self.pharmacy_table.column("ref",width=100)
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("tabletname",width=100)
        self.pharmacy_table.column("lotno",width=100)
        self.pharmacy_table.column("issuedate",width=100)
        self.pharmacy_table.column("expdate",width=100)
        self.pharmacy_table.column("uses",width=100)
        self.pharmacy_table.column("sideeffect",width=100)
        self.pharmacy_table.column("warning",width=100)
        self.pharmacy_table.column("dosage",width=100)
        self.pharmacy_table.column("price",width=100)
        self.pharmacy_table.column("productqt",width=100)
        self.fetch_dataMed()
        self.fetch_data()
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)
    #==================Add Medicine functionality Declaration==================
    def AddMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="jagnjr10",database="mydata")
        mycursor=conn.cursor()
        mycursor.execute("insert into pharma(Ref,`Medicine Name`) values(%s,%s)",(
            self.refMed_var.get(),
            self.addmed_var.get()
        ))
        conn.commit()
        self.fetch_dataMed()
        self.Medget_cursor()
        conn.close()
        messagebox.showinfo("Success","Medicine Added",parent=self.root)
        
        
    def fetch_dataMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="jagnjr10",database="mydata")
        mycursor=conn.cursor()
        mycursor.execute("select * from pharma")
        rows=mycursor.fetchall()
        if len(rows)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows :
                self.medicine_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def Medget_cursor(self,event=""):
         cursor_row=self.medicine_table.focus()
         content=self.medicine_table.item(cursor_row)
         row=content.get("values",[])
         if row:
           self.refMed_var.set(row[0])
           if len(row)>1:
             self.addmed_var.set(row[1])
         else:
             self.refMed_var.set("")
             self.addmed_var.set("")
    
    def UpdateMed(self):
        if self.refMed_var.get()=="" or self.addmed_var.get()=="":
            messagebox.showerror("Error","All fields ae Required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="jagnjr10",database="mydata")
            mycursor=conn.cursor()
            mycursor.execute("update pharma set `Medicine Name`=%s where Ref=%s",(
                self.addmed_var.get(),
                self.refMed_var.get(),            
                ))
        conn.commit()
        self.fetch_dataMed()
        conn.close()
        
        messagebox.showinfo("Success","Medicine has been updated")
    
    def DeleteMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="jagnjr10",database="mydata")
        mycursor=conn.cursor()
        
        sql="delete from pharma where Ref=%s"
        val=(self.refMed_var.get(),)
        mycursor.execute(sql,val)
        
        conn.commit()
        self.fetch_dataMed()
        conn.close()
        
    def ClearMed(self):
        self.refMed_var.set("")
        self.addmed_var.set("")
    
    def add_data(self):
        if self.ref_var.get()=="" or self.lot_var.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="jagnjr10",database="mydata")
            mycursor=conn.cursor()
            mycursor.execute("insert into `pharmacy-2` values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.ref_var.get(),
            self.typeMed_var.get(),
            self.medName_var.get(),
            self.lot_var.get(),
            self.issuedate_var.get(),
            self.expdate_var.get(),
            self.uses_var.get(),
            self.sideEffect_var.get(),
            self.warning_var.get(),
            self.dosage_var.get(),
            self.price_var.get(),
            self.product_var.get()
            ))
            
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Data has been inserted")
    
    def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="jagnjr10",database="mydata")
            mycursor=conn.cursor()
            mycursor.execute("select * from `pharmacy-2`")
            row = mycursor.fetchall()
            if len(row)!=0:
                self.pharmacy_table.delete(*self.pharmacy_table.get_children())
                for i in row:
                    self.pharmacy_table.insert("",END,values=i)
                conn.commit()
            conn.close()
    
    def get_cursor(self,ev=""):
         cursor_row=self.pharmacy_table.focus()
         content=self.pharmacy_table.item(cursor_row)
         row=content.get("values",[])
         if row:
           self.ref_var.set(row[0])
           if len(row)>1:
             self.typeMed_var.set(row[1]),
             self.medName_var.set(row[2]),
             self.lot_var.set(row[3]),
             self.issuedate_var.set(row[4]),
             self.expdate_var.set(row[5]),
             self.uses_var.set(row[6]),
             self.sideEffect_var.set(row[7]),
             self.warning_var.set(row[8]),
             self.dosage_var.set(row[9]),
             self.price_var.set(row[10]),
             self.product_var.set(row[11])
         else:
             self.refMed_var.set("")
             self.addmed_var.set("")
    
    def Update(self):
         if self.ref_var.get()=="" or self.lot_var.get()=="":
                messagebox.showerror("Error","All fields ae Required")
         else:
            conn=mysql.connector.connect(host="localhost",username="root",password="jagnjr10",database="mydata")
            mycursor=conn.cursor()
            mycursor.execute("update `pharmacy-2` set Type=%s,medname=%s,lot=%s,issuedate=%s,expdate=%s,uses=%s,sideeffect=%s,warning=%s,dosage=%s,price=%s,product=%s where refno=%s",(
            self.typeMed_var.get(),
            self.medName_var.get(),
            self.lot_var.get(),
            self.issuedate_var.get(),
            self.expdate_var.get(),
            self.uses_var.get(),
            self.sideEffect_var.get(),
            self.warning_var.get(),
            self.dosage_var.get(),
            self.price_var.get(),
            self.product_var.get(),
            self.ref_var.get(),
            
        ))
         conn.commit()
         self.fetch_data()
         conn.close()
         messagebox.showinfo("Success","Record has been updated")
    
    def delete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="jagnjr10",database="mydata")
        mycursor=conn.cursor()
        
        sql="delete from `pharmacy-2` where refno=%s"
        val=(self.ref_var.get(),)
        mycursor.execute(sql,val)
        
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Delete","Info deleted successfully")
        
    def search_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="jagnjr10",database="mydata")
        mycursor=conn.cursor()
        mycursor.execute("select * from `pharmacy-2` where "+str(self.search_var.get())+" LIKE '%"+str(self.searchTxt_var.get()) +"%'")
        
        rows=mycursor.fetchall()
        if len(rows)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
        
root=Tk()
obj=PharmacyManagementSystem(root)
root.mainloop()
