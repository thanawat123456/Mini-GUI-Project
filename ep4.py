from tkinter import *
from tkinter import ttk, messagebox #PopUp Error
import csv
from datetime import datetime



GUI =Tk()
GUI.title('โปรแกรมคำนวณค่าใช้จ่ายการเดินทาง')
GUI.geometry('900x900+500+100')


 
Tab = ttk.Notebook(GUI) 
T1 = Frame(Tab)
T2 = Frame(Tab) 
Tab.pack(fill=BOTH,expand=1) 

icon_t1 = PhotoImage(file='insert.png')
icon_t2 = PhotoImage(file = 'list.png')
icon_t3 = PhotoImage(file = 'save.png')
icon4 = PhotoImage(file = 't4.png')



Tab.add(T1,text= f'{"เพิ่มค่าใช้จ่าย":^{30}}',image = icon_t1,compound='left') #ทำให้ Tab ยาวเท่ากัน จาก 30 ตัวอักษร
Tab.add(T2,text= f'{"ค่าใช้จ่าทั้งหมด":^{30}}',image = icon_t2,compound='left') 


f1 =Frame(T1)

f1.pack() 
MainIcon = Label(f1,image= icon4,heigh='100',width='150')
MainIcon.pack(pady=7)

FONT1 = (None,20)


      

def Save(event=None):
        city = v_city.get()
        days = v_days.get()
        days2 = v_days22.get()
        city2 = v_city5.get()
        city3 = v_city3.get()
        
        spending = v_spending.get()

        if city=='' :
                print('No Data')
                messagebox.showwarning('Error','กรุณากรอกใส่ข้อมูล')
                return
        elif days =='':
                messagebox.showwarning('Error','กรุณากรอกใส่ข้อมูล')
                return
        elif spending == '':
                messagebox.showwarning('Error','กรุณากรอกใส่ข้อมูล')              
                return

        try: 
            total = trip_cost(city,city2,city3,float(days),float(days2),float(spending)) 
            tdays = int(days)+int(days2)
            pl = plan(city,city2,city3)
            sd = str(tdays)
            d1=int(days)
            d2=int(days2)
            print(total)
            
            #text = 'จังหวัดเริ่มต้น: {} \nจำนวนวัน: {} \nค่าใช้จ่ายทั่วไป: {} $ \nค่าการเดินทางทั้งหมด: {} $\n'.format(city,days,spending,total)   
            text = 'แผนการเดินทาง \n{} -> {} -> {}\nจำนวนวันที่อยู่ {}: {} วัน\nจำนวนวันที่อยู่ {}: {} วัน\nจำนวนวันที่ใช้เดินทางทั้งหมด: {} วัน \n ค่าใช้จ่ายทั่วไป: {} บาท\nค่าเครื่องบินทั้งหมด: {} บาท\n ค่าใช้จ่ายการเดินทางทั้งหมด: {} บาท'.format(city,city2,city3,city2,d1,city3,d2,sd,spending,pl,total)
            d = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            stamp = datetime.now()
            dt = stamp.strftime('%Y-%m-%d %H:%M:%S')
            transactionID = stamp.strftime('%Y%m%d%H%M%f')

            v_result.set(d+'\n'+text)
            v_city.set('เลือกเมือง')
            v_city3.set('เลือกเมือง')
            v_city5.set('เลือกเมือง')
            v_days.set(' ')
            v_days22.set(' ')
            v_spending.set(' ')

            with open('save3.csv','a' ,encoding='utf-8',newline='') as  f:  
              fw = csv.writer(f) 
              data =  [city,city2,city3,tdays,spending,total]
              fw.writerow(data)

        
            E1.focus()
            update_table() 
        except:
                print('Error')               
                messagebox.showwarning('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')               
                v_city.set(' ')
                v_days.set(' ')
                v_spending.set(' ')

# ทำให้สามารถกด enter ได้
GUI.bind('<Return>', Save) 



       


op= [
   'เลือกเมือง',
   'นิวยอร์ก',
   'วอชิงตัน',
   'ลอสแอนเจลิส',
   'ออนแทรีโอ',
   'นวร์ก',
   'โคลัมบัส',
   'ไมอามี',
   'ชาร์ลอตต์',
   'ชิคาโก',
   'แอตแลนตา',
   'ฟลอริดา',
   'ฮูสตัน'
]



L = Label(f1,text='เมืองเริ่มต้น (เครื่องบิน)',font=FONT1).pack()
v_city = StringVar()
#E1 = ttk.Entry(f1,textvariable = v_city,font= FONT1)
v_city = ttk.Combobox(f1,value=op)
v_city.current(0)
v_city.bind('<<ComboboxSelected>>')
v_city.pack()





v_cityy = StringVar()

#E1 = ttk.Entry(f1,textvariable = v_city,font= FONT1)

E1 = ttk.Entry(f1,textvariable = v_cityy)
#E1.pack()


L = Label(f1,text='เมืองระหว่างทาง (เครื่องบิน)',font=FONT1).pack()
v_city5 = StringVar()
#E1 = ttk.Entry(f1,textvariable = v_city,font= FONT1)
v_city5 = ttk.Combobox(f1,value=op)
v_city5.current(0)
v_city5.bind('<<ComboboxSelected>>')
v_city5.pack()

 
L = Label(f1,text='จำนวนวันที่อยู่เมืองระหว่างทาง',font=FONT1).pack()
v_days = StringVar()
E5 = ttk.Entry(f1,text='sdfsdf',textvariable=v_days,font=FONT1)
E5.pack()

L = Label(f1,text='เมืองสิ้นสุด (เครื่องบิน)',font=FONT1).pack()
v_city3 = StringVar()
v_city3 = ttk.Combobox(f1,value=op)
v_city3.current(0)
v_city3.bind('<<ComboboxSelected>>')
v_city3.pack()
#E1 = ttk.Entry(f1,textvariable = v_city3,font= FONT1)
#E1.pack()






L = Label(f1,text='จำนวนวันที่อยู่เมืองสิ้นสุด',font=FONT1).pack()
v_days22 = StringVar()
E2 = ttk.Entry(f1,textvariable=v_days22,font=FONT1)
E2.pack()




L = Label(f1,text='ค่าใช้จ่ายทั่วไป',font=FONT1).pack()
v_city2=StringVar()  
v_spending = StringVar()
E3 = ttk.Entry(f1,textvariable=v_spending,font=FONT1)
E3.pack()



v_result = StringVar()  
v_result.set('----ผลลัพธ์----')
result = Label(f1,textvariable = v_result,font=FONT1,fg = 'green')
result.pack(pady=20)
icon2 = PhotoImage(file='save.png')
b2 = ttk.Button(f1,text=f'{"Save": >{7}}',image=icon2,compound='left',command=Save) 
b2.pack(ipadx=20,ipady=10,pady=20)    




def hotel_cost(ninghts):
    return 450*ninghts

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



  

def plan(city_1,city_2,city_3):
    if city_1=='นิวยอร์ก' and city_2 == 'วอชิงตัน' and city_3  =='แอตแลนตา':
        return 2915
    elif city_1=='วอชิงตัน' and city_2 == 'ชาร์ลอตต์' and city_3  =='ฟลอริดา':
        return 3740
    elif city_1=='ลอสแอนเจลิส' and city_2 == 'ชาร์ลอตต์' and city_3  =='นิวยอร์ก':
        return 2270
    elif city_1=='วอชิงตัน' and city_2 == 'ชาร์ลอตต์' and city_3  =='โคลัมบัส':
        return 3215
    elif city_1=='ออนแทรีโอ' and city_2 == 'ชิคาโก' and city_3  =='นิวยอร์ก':
        return 2820
    elif city_1=='ลอสแอนเจลิส' and city_2 == 'แอตแลนตา' and city_3  =='ไมอามี':
        return 3210
    elif city_1=='นวร์ก' and city_2 == 'ชาร์ลอตต์' and city_3  =='แอตแลนตา':
        return 2440 
    elif city_1=='ลอสแอนเจลิส' and city_2 == 'ไมอามี' and city_3  =='ชิคาโก':
        return 3070
    elif city_1=='ชิคาโก' and city_2 == 'ไมอามี' and city_3  =='นิวยอร์ก':
        return 2725
    elif city_1=='ฮูสตัน' and city_2 == 'ชาร์ลอตต์' and city_3  =='นิวยอร์ก':
        return 2800                  
    else:
       return 'ไม่มีสายการบิน'                          

def rental_car_cost(days):
    rent_cost =650
    if days>=7:
        return rent_cost*days-1000
    elif days>=3:
        return rent_cost*days-500
    else:
        return rent_cost*days

def trip_cost(city_1,city_2,city_3,days,days2,spending_money):
    return plan(city_1,city_2,city_3)+rental_car_cost(float(days))+rental_car_cost(float(days2))+hotel_cost(float(days)-1)+spending_money   


def ttt(city_1,city_2,city_3):
    return plan(city_1,city_2,city_3)            

 


##################### TAB2 #####################

def read_csv():
        with open('save3.csv',newline="",encoding="utf-8") as f: 
            fr = csv.reader(f)
        
            data = list(fr)
            
        return data
            


L = Label(T2,text = 'ตารางแสดงผลลัพธ์', font=FONT1,).pack()

header = ['เมืองเริ่มต้น','เมืองระหว่างทาง','เมืองสิ้นสุด','จำนวนวันทั้งหมด','ค่าใช้จ่ายทั่วไป','ค่าการเดินทางทั้งหมด']
reuslttabel = ttk.Treeview(T2,columns=header,show='headings',heigh=50) 
reuslttabel.pack()



for h in header: 
        reuslttabel.heading(h,text=h)


headerwidth = [100,100,90,60,80,100] 
for h,w in zip(header,headerwidth): 
        reuslttabel.column(h,width=w)



def DeleteRecord():
        check = messagebox.askyesno('confirm?','คุณต่้องการลบข้อมูลใช่หรือไม่')
        print('Yes/No',check)
        

        if check==True:
           print('delete')     
           select = reuslttabel.selection()
           data = reuslttabel.item(select) 
           data = data['values'] 
           transactionID= data[0] #ค้นหาข้อมูลตำแหน่งที่ 0
           del alltransaction[str(transactionID)]
           updateCSV()
           update_table()
        else:
                print('cencel')

BDeldata = ttk.Button(T2,text='delete',command=DeleteRecord) 
BDeldata.place(x=380,y=550)



alltransaction = {} #สร้างเพื่อเก็บ id ของข้อมูลเพื่อเอามาไว้ลบ         

def updateCSV():
        with open('save3.csv','w',newline="",encoding="utf-8") as f: # w เขียนทับข้อมูลที่มีอยู่
            fw = csv.writer(f)
            # เตรียมข้อมูลออกมาจาก alltransaction ให้กลายเป็น list
            data = list(alltransaction.values()) #แปลง dict ให้กลายเป็นลิส
            fw.writerows(data) #ลิสซ้อนลิส [[],[],[]] multiple line from nested list
            print('Table was updated')
            

def update_table():
    reuslttabel.delete(*reuslttabel.get_children()) #ลบข้อมูลก่อนที่จะอัพเดตข้อมูล *เป็นการลบแบบรัวๆ หรือลบแบบ for ลูป
    
    try: 
       data = read_csv()
       for d in data:
           
           alltransaction[d[0]] = d 
           reuslttabel.insert('',0,value=d) #เพิ่ม data ตำแหน่งแรก
       
    except Exception as e:
        print('No File')

update_table()


rightcclixk = Menu(T2,tearoff=0)
rightcclixk.add_command(label='Edit')
rightcclixk.add_command(label='Delete')


def menupopup(event):
        print(event.x_root, event.y_root)
reuslttabel.bind('<Button-3>',menupopup)


GUI.bind('<Tab>',lambda x: E2.focus())
GUI.mainloop()
