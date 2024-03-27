import os
import random
import tempfile
from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image,ImageTk


class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1370x650+0+0")
        self.root.title("GMS")

        #Variables
        self.c_name=StringVar()
        self.c_phn=StringVar()
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total = StringVar()
        self.tax_input = StringVar()
        self.total = StringVar()

        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)



        #Select Category Subparts
        self.Category=["select option", "fruits", "vegetables", "breads", "milk"]
        
        self.SubCatfruits=["apple", "mango", "banana", "pineapple"]
        self.price_apple=80
        self.price_mango=150
        self.price_banana=80
        self.price_pineapple=100

        self.SubCatvegetables=["tomato", "onion", "cabbage", "lemon"]
        self.price_tomato=60
        self.price_onion=50
        self.price_cabbage=40
        self.price_lemon=100

        self.SubCatbreads=["white bread", "brown bread", "multigrain bread", "atta bread"]
        self.price_whitebread=25
        self.price_brownbread=40
        self.price_multigrainbread=50
        self.price_attabread=40

        self.SubCatmilk=["cow milk", "buffalo milk", "toned milk", "fullcream milk"]
        self.price_cowmilk=56
        self.price_buffalomilk=70
        self.price_tonedmilk=60
        self.price_fullcreammilk=68




        #Grocery Main Heading
        # lbl_title=Label(self.root,text="GROCERY MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="black")
        lbl_title1=Label(self.root,text="GROCERY",font=("times new roman",30,"bold"),bg="white",fg="steelblue4")
        lbl_title2=Label(self.root,text="MANAGEMENT",font=("times new roman",30,"bold"),bg="white",fg="steelblue4")
        lbl_title3=Label(self.root,text="SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="steelblue4")
        # lbl_title.place(width=1370,height=85)
        lbl_title1.place(x=220, width=280,height=85)
        lbl_title2.place(x=500, width=350,height=85)
        lbl_title3.place(x=830, width=300,height=85)




        #CUSTOMER LABEL BOX
        #Customer Heading
        Cust_Frame=LabelFrame(self.root,text="Customer",font=("times new roman",20,"bold"),bg="white",fg="orange2")
        Cust_Frame.place(x=2,y=75,width=320,height=150)
        #Customer Subparts
        self.lblCustName=Label(Cust_Frame,text="Name ",font=("times new roman",15,"bold"),bg="white",fg="steelblue4")
        self.lblCustName.grid(row=0, column=0,sticky=W,padx=5,pady=2)
        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("times new roman", 12, "bold"), width=26)
        self.txtCustName.grid(row=0, column=1)

        self.lbl_mob=Label(Cust_Frame,text="Phno. ",font=("times new roman",15,"bold"),bg="white",fg="steelblue4")
        self.lbl_mob.grid(row=1, column=0,sticky=W,padx=5,pady=2)
        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phn,font=("times new roman", 12, "bold"), width=26)
        self.entry_mob.grid(row=1, column=1)

        self.lblEmail=Label(Cust_Frame,text="Email ",font=("times new roman",15,"bold"),bg="white",fg="steelblue4")
        self.lblEmail.grid(row=2, column=0,sticky=W,padx=5,pady=2)
        self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("times new roman", 12, "bold"), width=26   )
        self.txtEmail.grid(row=2, column=1)
        



        #PRODUCT LABEL BOX
        #Product Heading
        Product_Frame=LabelFrame(self.root,text="Product",font=("times new roman",20,"bold"),bg="white",fg="orange2")
        Product_Frame.place(x=320,y=75,width=600,height=150)
        #Product Subparts
        self.lblCategory=Label(Product_Frame,text="Select Category ",font=("times new roman",15,"bold"),bg="white",fg="steelblue4",bd=4  )
        self.lblCategory.grid(row=0, column=0,sticky=W,padx=5,pady=2)
        self.Combo_Category=ttk.Combobox(Product_Frame,font=("times new roman",15,"bold"),value=self.Category,width=17,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0, column=1, sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>", self.Categories)

        self.lblproduct=Label(Product_Frame,text="Product Name",bd=4,font=("times new roman",15,"bold"),bg="white",fg="steelblue4")
        self.lblproduct.grid(row=1, column=0, sticky=W,padx=5,pady=2)
        self.ComboProduct=ttk.Combobox(Product_Frame,textvariable=self.product,font=("times new roman",15,"bold"),width=17,state="readonly")
        self.ComboProduct.grid(row=1, column=1, sticky=W,padx=5,pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)

        self.lblPrice=Label(Product_Frame,text="Price",bd=4,font=("times new roman",15,"bold"),bg="white",fg="steelblue4")
        self.lblPrice.grid(row=0, column=2, sticky=W,padx=5,pady=2)
        self.ComboPrice=ttk.Combobox(Product_Frame,textvariable=self.prices,font=("times new roman",15,"bold"),width=10,state="readonly")
        self.ComboPrice.grid(row=0, column=3, sticky=W,padx=5,pady=2)

        self.lblQty=Label(Product_Frame,text="Qty",bd=4,font=("times new roman",15,"bold"),bg="white",fg="steelblue4")
        self.lblQty.grid(row=1, column=2, sticky=W,padx=5,pady=2)
        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=("times new roman",15,"bold"),width=10)
        self.ComboQty.grid(row=1, column=3, sticky=W,padx=5,pady=2)
        



        #BILL AREA BOX
        #Bill Area Heading
        RightLabelFrame=LabelFrame(self.root,text="Bill Area",font=("times new roman",20,"bold"),bg="white",fg="green4")
        RightLabelFrame.place(x=920,y=125,width=435,height=440)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="black",font=("times new roman",10,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)




        #SEARCH BILL AREA
        Search_Frame=Frame(self.root,bd=2,bg="white")
        Search_Frame.place(x=920,y=75)

        self.lblBill=Label(Search_Frame,text="Bill Number",font=("times new roman",15,"bold"),bg="white",fg="green4")
        self.lblBill.grid(row=0,column=0,padx=1,sticky=W)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("times new roman",15,"bold"),width=20)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)

        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=("times new roman",11,"bold"),bg="orange2",fg="white",width=11,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)
        




        #BILL COUNTER
        #Bill Counter Heading
        Bottom_Frame=LabelFrame(self.root,text="Bill Counter",font=("times new roman",20,"bold"),bg="white",fg="orange2")
        Bottom_Frame.place(x=2,y=225,width=915,height=290)
        #Bill Counter Subparts
        self.lblSubTotal = Label(Bottom_Frame, text="Sub Total", font=("times new roman", 15, "bold"), bg="white", fg="steelblue4", bd=4)
        self.lblSubTotal.grid(row=0, column=0, sticky=W, padx=5, pady=2)
        self.EntySubTotal = ttk.Entry(Bottom_Frame, textvariable=self.sub_total, font=("times new roman", 15, "bold"))
        self.EntySubTotal.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.lbl_tax = Label(Bottom_Frame, text="Tax", font=("times new roman", 15, "bold"), bg="white", fg="steelblue4", bd=4)
        self.lbl_tax.grid(row=1, column=0, sticky=W, padx=5, pady=2)
        self.txt_tax = ttk.Entry(Bottom_Frame, textvariable=self.tax_input, font=("times new roman", 15, "bold"))
        self.txt_tax.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.lbl_tax = Label(Bottom_Frame, text="Total Amount", font=("times new roman", 15, "bold"), bg="white", fg="steelblue4", bd=4)
        self.lbl_tax.grid(row=2, column=0, sticky=W, padx=5, pady=2)
        self.txt_tax = ttk.Entry(Bottom_Frame, textvariable=self.total, font=("times new roman", 15, "bold"))
        self.txt_tax.grid(row=2, column=1, sticky=W, padx=5, pady=2)




        #BUTTONS
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=440,y=0)

        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,text="Add to Cart",font=("times new roman",15,"bold"),bg="green4",fg="white",width=15,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0,padx=7,pady=1)

        self.Btngenerate_bill=Button(Btn_Frame,command=self.gen_bill,text="Generate Bill",font=("times new roman",15,"bold"),bg="orange2",fg="white",width=15,cursor="hand2")
        self.Btngenerate_bill.grid(row=0,column=1,padx=7,pady=1)

        self.BtnSave=Button(Btn_Frame,command=self.save_bill,text="Save Bill",font=("times new roman",15,"bold"),bg="green4",fg="white",width=15,cursor="hand2")
        self.BtnSave.grid(row=1,column=0,padx=7,pady=1)

        self.BtnPrint=Button(Btn_Frame,command=self.iprint,text="Print Bill",font=("times new roman",15,"bold"),bg="orange2",fg="white",width=15,cursor="hand2")
        self.BtnPrint.grid(row=1,column=1,padx=7,pady=1)

        self.BtnClear=Button(Btn_Frame,command=self.clear,text="Clear",font=("times new roman",15,"bold"),bg="green4",fg="white",width=15,cursor="hand2")
        self.BtnClear.grid(row=2,column=0,padx=7,pady=1)

        self.BtnExit=Button(Btn_Frame,command=self.root.destroy,text="Exit",font=("times new roman",15,"bold"),bg="orange2",fg="white",width=15,cursor="hand2")
        self.BtnExit.grid(row=2,column=1,padx=7,pady=1)
        self.welcome()



        # BUTTON FUNCTIONING
        # ADD TO CART FUNCTION
        self.l=[]
    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("error", "please select the product")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str("Rs.%.2f"%(sum(self.l))))
            self.tax_input.set(str("Rs.%2f"%((((sum(self.l))-(self.prices.get()))*Tax)/100)))
            self.total.set(str("Rs.%.2f"%(((sum(self.l))+((((sum(self.l))-(self.prices.get())*Tax)/100))))))

        # GENERATE BIL FUNCTION 
    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("error", "please add to cart product")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END, text)
            self.textarea.insert(END,"\n ==========================================================")
            self.textarea.insert(END,f"\nSUB AMOUNT:\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\nTAX AMOUNT:\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\nTOTAL AMOUNT:\t\t{self.total.get()}")
            self.textarea.insert(END,"\n ==========================================================")
       
        # SAVE BIL FUNCTION
    def save_bill(self):
        op=messagebox.askyesno("SAVE BILL", "DO YOU WANT TO SAVE THE BILL")
        if op>0:
            self.bill_data=self.textarea.get(1.0, END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            op=messagebox.showinfo("SAVED",f"BILL NUMBER: {self.bill_no.get()} SAVED SUCCESSFULLY")
            f1.close()
            
        # PRINT BUTTON FUNCTION
    def iprint(self):
        q = self.textarea.get(1.0, "end-1c")
        temp_dir = "D:/DESKTOP/Bill Project/bills"  # Replace with your desired directory
        filename = tempfile.mktemp(".txt", dir=temp_dir)
        open(filename, 'w').write(q)
        os.startfile(filename, "print")
        
        # SEARCH BUTTON FUNCTION
    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split(".")[0]==self.search_bill.get():
                f1=open(f"bills/{i}", "r")
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=="no":
            messagebox.showerror("error", "invalid bill")
        
        # CLEAR BUTTON FUNCTION
    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phn.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.welcome()




        #BILL AREA BOX CONTENT FUNCTION
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,f"\n BILL NUMBER: {self.bill_no.get()}")
        self.textarea.insert(END,f"\n CUSTOMER NAME: {self.c_name.get()}")
        self.textarea.insert(END,f"\n MOBILE NO: {self.c_phn.get()}")
        self.textarea.insert(END,f"\n EMAIL: {self.c_email.get()}")

        self.textarea.insert(END,"\n ==========================================================\n")
        self.textarea.insert(END,f"\n PRODUCTS\t\tQUANTITY\t\tPRICE")
        self.textarea.insert(END,"\n ==========================================================")

        #CATEGORIES BOX FUNCTION
    def Categories(self,event=""):
        if self.Combo_Category.get()=="fruits":
            self.ComboProduct.config(value=self.SubCatfruits)
            self.ComboProduct.current(0)
        if self.Combo_Category.get()=="vegetables":
            self.ComboProduct.config(value=self.SubCatvegetables)
            self.ComboProduct.current(0)
        if self.Combo_Category.get()=="breads":
            self.ComboProduct.config(value=self.SubCatbreads)
            self.ComboProduct.current(0)
        if self.Combo_Category.get()=="milk":
            self.ComboProduct.config(value=self.SubCatmilk)
            self.ComboProduct.current(0)

        #PRICE BOX FUNCTION
    def price(self,event=""):
        if self.ComboProduct.get()=="apple":
            self.ComboPrice.config(value=self.price_apple)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="mango":
            self.ComboPrice.config(value=self.price_mango)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="banana":
            self.ComboPrice.config(value=self.price_banana)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="pineapple":
            self.ComboPrice.config(value=self.price_pineapple)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="tomato":
            self.ComboPrice.config(value=self.price_tomato)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="onion":
            self.ComboPrice.config(value=self.price_onion)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="cabbage":
            self.ComboPrice.config(value=self.price_cabbage)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="lemon":
            self.ComboPrice.config(value=self.price_lemon)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="white bread":
            self.ComboPrice.config(value=self.price_whitebread)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="brown bread":
            self.ComboPrice.config(value=self.price_brownbread)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="multigrain bread":
            self.ComboPrice.config(value=self.price_multigrainbread)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="atta bread":
            self.ComboPrice.config(value=self.price_attabread)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="cow milk":
            self.ComboPrice.config(value=self.price_cowmilk)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="buffalo milk":
            self.ComboPrice.config(value=self.price_buffalomilk)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="toned milk":
            self.ComboPrice.config(value=self.price_tonedmilk)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="fullcream milk":
            self.ComboPrice.config(value=self.price_fullcreammilk)
            self.ComboPrice.current(0)
            self.qty.set(1)
        






if __name__== '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()
