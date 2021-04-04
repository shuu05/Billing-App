from tkinter import *
import math,random,os
from tkinter import messagebox


class Bill_app:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing system")
        bg_color = "#b7d962"
        f_color = "#3a3b39"
        title = Label(self.root, text="Billing Software",bd=3,relief=GROOVE,bg=bg_color,fg=f_color,font=("Ariael",30,"bold"),pady=3).pack(fill=X)
        
        #======================Variables=========================
            #==============starter===============
        self.momo=IntVar()
        self.sw=IntVar()
        self.piz=IntVar()
        self.ff=IntVar() 
        self.vr=IntVar()
        self.gb=IntVar()
            #=================Drinks========================
        self.coffee=IntVar()
        self.tea=IntVar()
        self.coke=IntVar()
        self.lemonade=IntVar()
        self.juice=IntVar()
        self.mojito=IntVar()
            #================Sweets===============
        self.cc=IntVar()
        self.p=IntVar()
        self.waffle=IntVar()
        self.pastry=IntVar()
        self.brownies=IntVar()
        self.cake=IntVar()
        #=========================tax==========================
        self.GST=StringVar()
        self.SGST=StringVar()
        self.CGST=StringVar()
        #===============total of section====================
        self.total_starter=StringVar()
        self.total_drinks=StringVar()
        self.total_sweets=StringVar()
        #=====================customer data==================
        self.cname=StringVar()
        self.cphn=StringVar()     
        
        self.cbill=StringVar()
        x=random.randint(1000,9999)
        self.cbill.set(str(x))
        self.sbill=StringVar()
        #=============CUSTOMER DETAIL FRAME======================
        f1 = LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="#C70039",bg=bg_color)
        f1.place(x=0,y=70,relwidth=1)
        
        cname_label=Label(f1,text="Customer Name",bg=bg_color,fg=f_color,font=("times new roman",18,"bold")).grid(row=0, column=0,padx=20,pady=8)
        cname_text=Entry(f1,width=15,textvariable=self.cname,font=("arial",15),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=8,padx=10)
        
        cphn_label=Label(f1,text="Phone no.",bg=bg_color,fg=f_color,font=("times new roman",18,"bold")).grid(row=0, column=2,padx=20,pady=8)
        cphn_text=Entry(f1,width=15,textvariable=self.cphn,font=("arial",15),bd=5,relief=SUNKEN).grid(row=0,column=3,pady=8,padx=10)
        
        cbill_label=Label(f1,text="Bill Number",bg=bg_color,fg=f_color,font=("times new roman",18,"bold")).grid(row=0, column=4,padx=20,pady=8)
        cbill_text=Entry(f1,width=15,textvariable=self.sbill,font=("arial",15),bd=5,relief=SUNKEN).grid(row=0,column=5,pady=8,padx=10)
        
        bill_btn = Button(f1,text="Search",command=self.find_bill,width=10,bd=7,font=("arial 12 bold")).grid(row=0,column=6,padx=10,pady=10)
        
        #==========================starter=================================
        f2=LabelFrame(self.root,text="Starters",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="#C70039",bg=bg_color)
        f2.place(x=5,y=175,width=320,height=380)
        
        momo_label = Label(f2,text="Momos",bg=bg_color,fg=f_color,font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=10)
        momo_text = Entry(f2,width=10,textvariable=self.momo,font=("arial 15 bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        
        sw_label = Label(f2,text="Sandwitch",bg=bg_color,fg=f_color,font=("times new roman",15,"bold")).grid(row=1,column=0,padx=10,pady=10)
        sw_text = Entry(f2,width=10,textvariable=self.sw,font=("arial 15 bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        
        pizza_label = Label(f2,text="pizza",bg=bg_color,fg=f_color,font=("times new roman",15,"bold")).grid(row=2,column=0,padx=10,pady=10)
        pizza_text = Entry(f2,width=10,textvariable=self.piz,font=("arial 15 bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        
        ff_label = Label(f2,text="French Fries",bg=bg_color,fg=f_color,font=("times new roman",15,"bold")).grid(row=3,column=0,padx=10,pady=10)
        ff_text = Entry(f2,width=10,textvariable=self.ff,font=("arial 15 bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        
        vr_label = Label(f2,text="Veggi Wrap",bg=bg_color,fg=f_color,font=("times new roman",15,"bold")).grid(row=4,column=0,padx=10,pady=10)
        vr_text = Entry(f2,width=10,textvariable=self.vr,font=("arial 15 bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        
        gb_label = Label(f2,text="Garlic Bread",bg=bg_color,fg=f_color,font=("times new roman",15,"bold")).grid(row=5,column=0,padx=10,pady=10)
        gb_text = Entry(f2,width=10,textvariable=self.gb,font=("arial 15 bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
     #==========================starter=================================
        f3=LabelFrame(self.root,text="Drinks",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="#C70039",bg=bg_color)
        f3.place(x=330,y=175,width=320,height=380)
        
        coffee_label = Label(f3,text="Coffee",bg=bg_color,fg=f_color,font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=10)
        coffee_text = Entry(f3,width=10,textvariable=self.coffee,font=("arial 15 bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        
        tea_label = Label(f3,text="Tea",bg=bg_color,fg=f_color,font=("times new roman",15,"bold")).grid(row=1,column=0,padx=10,pady=10)
        tea_text = Entry(f3,width=10,textvariable=self.tea,font=("arial 15 bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        
        coke_label = Label(f3,text="Coke",bg=bg_color,fg=f_color,font=("times new roman",15,"bold")).grid(row=2,column=0,padx=10,pady=10)
        coke_text = Entry(f3,width=10,textvariable=self.coke,font=("arial 15 bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        
        lemonade_label = Label(f3,text="Lemonade",bg=bg_color,fg=f_color,font=("times new roman",15,"bold")).grid(row=3,column=0,padx=10,pady=10)
        lemonade_text = Entry(f3,width=10,textvariable=self.lemonade,font=("arial 15 bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        
        juice_label = Label(f3,text="Juice",bg=bg_color,fg=f_color,font=("times new roman",15,"bold")).grid(row=4,column=0,padx=10,pady=10)
        juice_text = Entry(f3,width=10,textvariable=self.juice,font=("arial 15 bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        
        mojito_label = Label(f3,text="Mojito",bg=bg_color,fg=f_color,font=("times new roman",15,"bold")).grid(row=5,column=0,padx=10,pady=10)
        mojito_text = Entry(f3,width=10,textvariable=self.mojito,font=("arial 15 bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
        #==========================sweets=================================
        f4=LabelFrame(self.root,text="Sweets",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="#C70039",bg=bg_color)
        f4.place(x=655,y=175,width=320,height=380)
        
        cc_label = Label(f4,text="cotton candy",bg=bg_color,fg=f_color,font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=10)
        cc_text = Entry(f4,width=10,textvariable=self.cc,font=("arial 15 bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        
        p_label = Label(f4,text="Pancakes",bg=bg_color,fg=f_color,font=("times new roman",15,"bold")).grid(row=1,column=0,padx=10,pady=10)
        p_text = Entry(f4,width=10,textvariable=self.p,font=("arial 15 bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        
        waffle_label = Label(f4,text="Waffle",bg=bg_color,fg=f_color,font=("times new roman",15,"bold")).grid(row=2,column=0,padx=10,pady=10)
        waffle_text = Entry(f4,width=10,textvariable=self.waffle,font=("arial 15 bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        
        Pastry_label = Label(f4,text="Pastry",bg=bg_color,fg=f_color,font=("times new roman",15,"bold")).grid(row=3,column=0,padx=10,pady=10)
        Pastry_text = Entry(f4,width=10,textvariable=self.pastry,font=("arial 15 bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        
        cake_label = Label(f4,text="Cake",bg=bg_color,fg=f_color,font=("times new roman",15,"bold")).grid(row=4,column=0,padx=10,pady=10)
        cake_text = Entry(f4,width=10,textvariable=self.cake,font=("arial 15 bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        
        Brownies_label = Label(f4,text="Brownies",bg=bg_color,fg=f_color,font=("times new roman",15,"bold")).grid(row=5,column=0,padx=10,pady=10)
        Brownies_text = Entry(f4,width=10,textvariable=self.brownies,font=("arial 15 bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
        
        #==========================Bill Area=================================
        f5=Frame(self.root,bd=10,relief=GROOVE)
        f5.place(x=980,y=175,width=350,height=380)
        
        bill_title=Label(f5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(f5,orient=VERTICAL)
        self.txtarea=Text(f5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        
        
        #====================button frame===================================
        f6=LabelFrame(self.root,text="Bill Menu",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="#C70039",bg=bg_color)
        f6.place(x=0,y=560,relwidth=1,height=190)
        m1_lbl=Label(f6,text="Total Starter Price",bg=bg_color,fg=f_color,font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(f6,width=18,textvariable=self.total_starter,font=("arial 10 bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
        
        m2_lbl=Label(f6,text="Total Drinks Price",bg=bg_color,fg=f_color,font=("times new roman",15,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(f6,width=18,font=("arial 10 bold"),textvariable=self.total_drinks,bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=5)
        
        m3_lbl=Label(f6,text="Total Sweets Price",bg=bg_color,fg=f_color,font=("times new roman",15,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(f6,width=18,font=("arial 10 bold"),textvariable=self.total_sweets,bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)
        
        m4_lbl=Label(f6,text="GST",bg=bg_color,fg=f_color,font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        m4_txt=Entry(f6,width=18,font=("arial 10 bold"),bd=7,textvariable=self.GST,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)
        
        m5_lbl=Label(f6,text="SGST",bg=bg_color,fg=f_color,font=("times new roman",15,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        m5_txt=Entry(f6,width=18,font=("arial 10 bold"),bd=7,textvariable=self.SGST,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=5)
        
        m6_lbl=Label(f6,text="CGST",bg=bg_color,fg=f_color,font=("times new roman",15,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        m6_txt=Entry(f6,width=18,font=("arial 10 bold"),textvariable=self.CGST,bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)
        
        
        btn_f=Frame(f6,bd=7,relief=GROOVE)
        btn_f.place(x=670,width=650,height=110)
        
        total_btn=Button(btn_f,text="Total",command=self.total,bg=bg_color,fg=f_color,bd=5,pady=11,width=11,font=("arial 15 bold")).grid(row=0,column=0,padx=5,pady=5)
        
        gb_btn=Button(btn_f,text="Generate Bill",command=self.bill_area,bg=bg_color,fg=f_color,bd=5,pady=11,width=11,font=("arial 15 bold")).grid(row=0,column=1,padx=5,pady=5)
        
        clear_btn=Button(btn_f,text="Clear",command=self.clear_data,bg=bg_color,fg=f_color,bd=5,pady=11,width=11,font=("arial 15 bold")).grid(row=0,column=2,padx=5,pady=5)
        
        exit_btn=Button(btn_f,text="Exit",command=self.exit_app,bg=bg_color,fg=f_color,bd=5,pady=11,width=11,font=("arial 15 bold")).grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()
        
    def total(self):
        self.momo_T=self.momo.get()*60
        self.sw_T=self.sw.get()*90
        self.piz_T=self.piz.get()*320
        self.ff_T=self.ff.get()*120
        self.vr_T=self.vr.get()*150
        self.gb_T=self.gb.get()*110
        self.total_starter_price=float(
            self.momo_T+
            self.sw_T+
            self.piz_T+
            self.ff_T+
            self.vr_T+
            self.gb_T
               )
        self.total_starter.set("Rs. "+str(self.total_starter_price))
        self.gsttax=round((self.total_starter_price*0.18),2)
        self.GST.set("Rs."+str(self.gsttax))
        
        self.coffee_T=self.coffee.get()*40
        self.tea_T=self.tea.get()*40
        self.coke_T=self.coke.get()*110
        self.lemonade_T=self.lemonade.get()*120
        self.juice_T=self.juice.get()*150
        self.mojito_T=self.mojito.get()*110
       
        self.total_drinks_price=float(
            self.coffee_T+
            self.tea_T+
            self.coke_T+
            self.lemonade_T+
            self.juice_T+
            self.mojito_T
               )
        self.total_drinks.set("Rs. "+str(self.total_drinks_price))
        self.sgsttax=round((self.total_drinks_price*0.18),2)
        self.SGST.set("Rs."+str(self.sgsttax))
        
        self.cc_T=self.cc.get()*30
        self.p_T=self.p.get()*120
        self.waffle_T=self.waffle.get()*40
        self.pastry_T=self.pastry.get()*90
        self.brownies_T=self.brownies.get()*150
        self.cake_T=self.cake.get()*350
        
        self.total_sweets_price=float(
            self.cc_T+
            self.p_T+
            self.waffle_T+
            self.pastry_T+
            self.brownies_T+
            self.cake_T
               )
        self.total_sweets.set("Rs. "+str(self.total_sweets_price))
        self.cgsttax=round((self.total_sweets_price*0.18),2)
        self.CGST.set("Rs."+str(self.cgsttax))
        
        self.totalbill=round(float(self.total_starter_price+
                             self.total_drinks_price+
                             self.total_sweets_price+
                             self.gsttax+
                             self.cgsttax+
                             self.sgsttax),2)
                
       
      
        
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\n\tWELCOME TO SHUU CAFE \n\t---------------------")
        self.txtarea.insert(END,f"\n Bill Number :{self.cbill.get()}")
        self.txtarea.insert(END,f"\n Customer Name:{self.cname.get()} ")
        self.txtarea.insert(END,f"\n Phone Number :{self.cphn.get()} ")
        self.txtarea.insert(END,f"\n--------------------------------------")
        self.txtarea.insert(END,f"\n FoodItems\t\tQTY\t\tPrice")
        self.txtarea.insert(END,f"\n--------------------------------------")
        
        
        
    def bill_area(self):
        if self.cname.get() == "" or self.cphn.get() == "":
            messagebox.showerror("Error","Customer details are must")
        elif self.total_drinks.get() == "Rs. 0.0" and self.total_starter.get() == "Rs. 0.0" and self.total_sweets.get() == "Rs. 0.0" :
            messagebox.showerror("Error","No item has been selected")
        else:
            
            self.welcome_bill()
            #=========================starter===================
            if self.momo.get()!= 0 :
                self.txtarea.insert(END,f"\n Momos\t\t{self.momo.get()}\t   Rs. {self.momo_T}")
            if self.sw.get()!= 0 :
                self.txtarea.insert(END,f"\n Sandwitch\t\t{self.sw.get()}\t   Rs. {self.sw_T}")
            if self.piz.get()!= 0 :
                self.txtarea.insert(END,f"\n Pizza\t\t{self.piz.get()}\t   Rs. {self.piz_T}")
            if self.ff.get()!= 0 :
                self.txtarea.insert(END,f"\n French Fries\t\t{self.ff.get()}\t   Rs. {self.ff_T}")
            if self.vr.get()!= 0 :
                self.txtarea.insert(END,f"\n Veggie wrap\t\t{self.vr.get()}\t   Rs. {self.vr_T}")
            if self.gb.get()!= 0 :
                self.txtarea.insert(END,f"\n Garlic Bread\t\t{self.gb.get()}\t   Rs. {self.gb_T}")
                
            #=========================drinks===================
            if self.coffee.get()!= 0 :
                self.txtarea.insert(END,f"\n Coffee\t\t{self.coffee.get()}\t   Rs. {self.coffee_T}")
            if self.tea.get()!= 0 :
                self.txtarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t   Rs. {self.tea_T}")
            if self.coke.get()!= 0 :
                self.txtarea.insert(END,f"\n Coke\t\t{self.coke.get()}\t   Rs. {self.coke_T}")
            if self.lemonade.get()!= 0 :
                self.txtarea.insert(END,f"\n Lemonade\t\t{self.lemonade.get()}\t   Rs. {self.lemonade_T}")
            if self.juice.get()!= 0 :
                self.txtarea.insert(END,f"\n Juice\t\t{self.juice.get()}\t   Rs. {self.juice_T}")
            if self.mojito.get()!= 0 :
                self.txtarea.insert(END,f"\n Mojito\t\t{self.mojito.get()}\t   Rs. {self.mojito_T}")
            #=========================sweets===================
            if self.cc.get()!= 0 :
                self.txtarea.insert(END,f"\n Cotton candy\t\t{self.cc.get()}\t   Rs. {self.cc_T}")
            if self.p.get()!= 0 :
                self.txtarea.insert(END,f"\n Pancake\t\t{self.p.get()}\t   Rs. {self.p_T}")
            if self.waffle.get()!= 0 :
                self.txtarea.insert(END,f"\n Waffle\t\t{self.waffle.get()}\t   Rs. {self.waffle_T}")
            if self.pastry.get()!= 0 :
                self.txtarea.insert(END,f"\n Pastry\t\t{self.pastry.get()}\t   Rs. {self.pastry_T}")
            if self.brownies.get()!= 0 :
                self.txtarea.insert(END,f"\n Brownies\t\t{self.brownies.get()}\t   Rs. {self.brownies_T}")
            if self.cake.get()!= 0 :
                self.txtarea.insert(END,f"\n Cake\t\t{self.cake.get()}\t   Rs. {self.cake_T}")
                
            self.txtarea.insert(END,f"\n--------------------------------------")
            if self.GST.get() != "0.0": 
                self.txtarea.insert(END,f"\n GST\t\t\t   {self.GST.get()}")
            if self.SGST.get() != "0.0":
                self.txtarea.insert(END,f"\n SGST\t\t\t   {self.SGST.get()}")
            if self.CGST.get() != "0.0": 
                self.txtarea.insert(END,f"\n CGST\t\t\t   {self.CGST.get()}")
            self.txtarea.insert(END,f"\n--------------------------------------")
            self.txtarea.insert(END,f"\n Total\t\t\t   Rs.{self.totalbill}")
            self.save_bill()
        
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.bill_data=self.txtarea.get("1.0",END)
            f1=open("bills/"+str(self.cbill.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Billl no. {self.cbill.get()} saved successfully")
        else:
            return
    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.sbill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete("1.0",END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present == "no":
            messagebox.showerror("ERROR","File not found")
    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really want to clear?")
        if op>0:
            self.momo.set(0)
            self.sw.set(0)
            self.piz.set(0)
            self.ff.set(0)
            self.vr.set(0)
            self.gb.set(0)
                #=================Drinks========================
            self.coffee.set(0)
            self.tea.set(0)
            self.coke.set(0)
            self.lemonade.set(0)
            self.juice.set(0)
            self.mojito.set(0)
                #================Sweets===============
            self.cc.set(0)
            self.p.set(0)
            self.waffle.set(0)
            self.pastry.set(0)
            self.brownies.set(0)
            self.cake.set(0)
            #=========================tax==========================
            self.GST.set("")
            self.SGST.set("")
            self.CGST.set("")
            #===============total of section====================
            self.total_starter.set("")
            self.total_drinks.set("")
            self.total_sweets.set("")
            #=====================customer data==================
            self.cname.set("")
            self.cphn.set("")     
            
            self.cbill.set("")
            x=random.randint(1000,9999)
            self.cbill.set(str(x))
            self.sbill.set("")
            self.welcome_bill()
        
    def exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()
        
            
        
        
root = Tk()
obj = Bill_app(root)
root.mainloop()
