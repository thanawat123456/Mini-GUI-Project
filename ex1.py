from tkinter import *
from tkinter import ttk, messagebox
import csv
from datetime import datetime

GUI = Tk()
GUI.title('โปรแกรมคำนวณค่าใช้จ่ายการเดินทาง')
GUI.geometry('800x700+500+200')

bg = PhotoImage(file='travel2.png')
icon1 = PhotoImage(file = 't4.png')
icon3 = PhotoImage(file = 'list.png')
icon4 = PhotoImage(file = 'insert.png')

Tab = ttk.Notebook(GUI)

T1 = Frame(Tab)
T2 = Frame(Tab)
Tab.pack(fill=BOTH,expand=1)
#im.PhotoImage(Image.open('travel2.png').resize((600,600)))

f1 =Frame(T1)
f1.pack()





MainIcon = Label(f1,image= icon1,heigh='100',width='150')
MainIcon.pack(pady=7)

Tab.add(T1,text='เพิ่มค่าใช้จ่าย',image = icon4,compound='left')
Tab.add(T2,text='ข้อมูลทั้งหมด',image = icon3,compound='left')

FONT1 = (None,20)

L = Label(f1,text='City',font=FONT1).pack()
v_city = StringVar()
E1 = ttk.Entry(f1,textvariable = v_city,font= FONT1)
E1.pack()

L = Label(f1,text='Days',font=FONT1).pack()
v_days = StringVar()
E2 = ttk.Entry(f1,textvariable=v_days,font=FONT1)
E2.pack()

L = Label(f1,text='Spending',font=FONT1).pack()
v_spending = StringVar()
E3 = ttk.Entry(f1,textvariable=v_spending,font=FONT1)
E3.pack()



def Save(event=None):
        city = v_city.get()
        days = v_days.get()
        spending = v_spending.get()
        if city=='' :
                print('No Dara')
                messagebox.showwarning('Error','กรุณากรอกเมือง')
                return
        elif days =='':
                messagebox.showwarning('Error','กรุณากรอกวัน')
                return
        elif spending == '':
                messagebox.showwarning('Error','กรุณากรอกค่าใช้จ่าย')              
                return

        try:
            total = trip_cost(city,float(days),float(spending)) 
            print(total)
            text = 'City: {} \nDays: {} \nSpending Money: {} $ \nTrip cost: {} $\n'.format(city,days,spending,total)   
            d = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            stamp = datetime.now()
            dt = stamp.strftime('%Y-%m-%d %H:%M:%S')
            transactionID = stamp.strftime('%Y%m%d%H%M%f')

            v_result.set(d+'\n'+text)
            v_city.set(' ')
            v_days.set(' ')
            v_spending.set(' ')

            with open('save.csv','a' ,encoding='utf-8',newline='') as  f:  
              fw = csv.writer(f) 
              data =  [transactionID,dt,city,days,spending,total]
              fw.writerow(data)

        
            E1.focus()
            update_table() 
        except:
                print('Error')
                # messagebox.showerror('Error','กรุณากรอกข้อมูลให่ คุณกรอกตัวเลขผิด')
                messagebox.showwarning('Error','กรุณากรอกข้อมูลให่ คุณกรอกตัวเลขผิด')
                #messagebox.showinfo('Error','กรุณากรอกข้อมูลให่ คุณกรอกตัวเลขผิด')
                v_expense.set(' ')
                v_price.set(' ')
                v_emt.set(' ')

    
GUI.bind('<Return>', Save)    	

def hotel_cost(ninghts):
    return 140*ninghts

def plan_ride_cost(city):
    if city == 'Charlottle':
       return 183
    elif city == 'Tampa':
       return 220
    elif city == 'Pitt':
       return 222
    elif city == 'Los':
       return 475
    else:
       return 'Nope'

def rental_car_cost(days):
    rent_cost =40
    if days>=7:
    	return rent_cost*days-50
    elif days>=3:
        return rent_cost*days-20
    else:
        return rent_cost*days

def trip_cost(city,days,spending_money):
    return plan_ride_cost(city)+rental_car_cost(float(days))+hotel_cost(float(days)-1)+spending_money        	

v_result = StringVar()
v_result.set('----Result----')
result = Label(f1,textvariable = v_result,font=FONT1,fg = 'green')
result.pack(pady=20)

icon2 = PhotoImage(file='save.png')
b2 = ttk.Button(f1,text=f'{"Save": >{7}}',image=icon2,compound='left',command=Save) 
b2.pack(ipadx=20,ipady=10,pady=20) 



###############TAB2#################
# f2 = Label(T2,text='sdfsdf',image=bg).pack() 
# c =Canvas(f2)
# b =Label(f2,image=bg)
#c.pack()


def read_csv():
        with open('save2.csv',newline="",encoding="utf-8") as f: 
            fr = csv.reader(f)
        
            data = list(fr)
           
        return data


L = Label(T2,text='ตารางแสดงข้อมูล',font=FONT1).pack()
header = ['ID','Time','City','Days','Spending','Total']
tabel = ttk.Treeview(T2,columns=header,show='headings',heigh=50)
tabel.pack()

for h in header:
	tabel.heading(h,text=h)

headerwidth =[140,150,150,90,90,90]
for h,w in zip(header,headerwidth):
    tabel.column(h,width=w)	

alltransaction = {}

def DeleteRecord():
        check = messagebox.askyesno('confirm?','คุณต่้องการลบข้อมูลใช่หรือไม่')
        print('Yes/No',check)
        

        if check==True:
           print('delete')     
           select = tabel.selection()
           #print(select)
           data = tabel.item(select) 
           data = data['values'] 
           transactionID= data[0] 
           
           del alltransaction[str(transactionID)]
          
           updata()
           updata_table()
        else:
                print('cencel')

BDeldata = ttk.Button(T2,text='delete',command=DeleteRecord) 
BDeldata.place(x=50,y=550)

def updata():
	with open('save2.csv','w',newline='',encoding='utf-8') as f:
		fw = csv.writer(f)
		data = list(alltransaction.values())
		fw.writerow(data)
		print('Table was updated')

def updata_table():
    tabel.delete(*tabel.get_children())
    try:   
       data = read_csv()
       for d in data:
           alltransaction[d[0]]
           tabel.insert('',0,value=d)
       print(alltransaction)
    except Exception as e:
       print('No File')   	

updata_table()       

GUI.bind('<Tab>',lambda x: E2.focus())
GUI.mainloop()