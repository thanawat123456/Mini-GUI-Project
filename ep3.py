from tkinter import *
from tkinter import ttk, messagebox #PopUp Error
import csv
from datetime import datetime



GUI =Tk()
GUI.title('โปรแกรมคำนวณค่าใช้จ่ายการเดินทาง')
GUI.geometry('900x700+500+300')



Tab = ttk.Notebook(GUI) #เอา Notebook ไปใส่ใน GUI
T1 = Frame(Tab) #เอา Frame ไปใส่ใน Tab ขยาย => T1 = Frame(Tab,width=400,height=400)
T2 = Frame(Tab)  #เอา Frame ไปใส่ใน Tab
Tab.pack(fill=BOTH,expand=1) #x มาจาก import * ขยายเต็มจอ

icon_t1 = PhotoImage(file='insert.png')#.subsample(2) = ย่อรูปตามขนาดเท่า
icon_t2 = PhotoImage(file = 'list.png')
icon_t3 = PhotoImage(file = 'save.png')
icon4 = PhotoImage(file = 't4.png')



Tab.add(T1,text= f'{"เพิ่มค่าใช้จ่าย":^{30}}',image = icon_t1,compound='left') #ทำให้ Tab ยาวเท่ากัน จาก 30 ตัวอักษร
Tab.add(T2,text= f'{"ค่าใช้จ่าทั้งหมด":^{30}}',image = icon_t2,compound='left') #ทำให้ Tab ยาวเท่ากัน จาก 30 ตัวอักษร


f1 =Frame(T1)

f1.pack() 
MainIcon = Label(f1,image= icon4,heigh='100',width='150')
MainIcon.pack(pady=7)

FONT1 = (None,20)

days = {'Mon':'จันทร์',
        'Tue':'อังคาร',
        'Wed':'พุธ',
        'Thu':'พฤหัสบดี',
        'Fri':'ศุกร์',
        'Sat':'เสาร์',
        'Sun':'อาทิตย์'}

def Save(event=None):
        city = v_city.get()
        days = v_days.get()
        spending = v_spending.get()
        if city=='' :
                print('No Data')
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
            text = 'จังหวัด: {} \nจำนวนวัน: {} \nค่าใช้จ่ายทั่วไป: {} $ \nค่าการเดินทางทั้งหมด: {} $\n'.format(city,days,spending,total)   
            d = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            stamp = datetime.now()
            dt = stamp.strftime('%Y-%m-%d %H:%M:%S')
            transactionID = stamp.strftime('%Y%m%d%H%M%f')

            v_result.set(d+'\n'+text)
            v_city.set(' ')
            v_days.set(' ')
            v_spending.set(' ')

            with open('save3.csv','a' ,encoding='utf-8',newline='') as  f:  
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
                v_city.set(' ')
                v_days.set(' ')
                v_spending.set(' ')

# ทำให้สามารถกด enter ได้
GUI.bind('<Return>', Save) #ต้องพิมใน def Save(event=None) ด้วย

def hotel_cost(ninghts):
    return 450*ninghts

def plan_ride_cost(city):
    if city == 'เชียงใหม่':
       return 790
    elif city == 'น่าน':
       return 690
    elif city == 'เลย':
       return 690
    elif city == 'สกลนคร':
       return 690
    elif city == 'ร้อยเอ็ด':
       return 690
    elif city == 'นครพนม':
       return 690    
    elif city == 'หาดใหญ่':
       return 690
    elif city == 'เชียงราย':
       return 690     
    elif city == 'ภูเก็ต':
       return  690  
    elif city == 'กระบี่':
       return  690  
    elif city == 'บุรีรัมย์':
       return  590  
    elif city == 'อุดรธานี':
       return  590    
    elif city == 'ตรัง':
       return  590 
    elif city == 'อุบลราชธานี':
       return  590       
    elif city == 'ขอนแก่น':
       return  590    
    elif city == 'พิษณุโลก':
       return  590       
    else:
       return 'Nope'

def rental_car_cost(days):
    rent_cost =650
    if days>=7:
        return rent_cost*days-1000
    elif days>=3:
        return rent_cost*days-500
    else:
        return rent_cost*days

def trip_cost(city,days,spending_money):
    return plan_ride_cost(city)+rental_car_cost(float(days))+hotel_cost(float(days)-1)+spending_money           




L = Label(f1,text='จังหวัด (เครื่องบิน)',font=FONT1).pack()
v_city = StringVar()
E1 = ttk.Entry(f1,textvariable = v_city,font= FONT1)
E1.pack()

L = Label(f1,text='จำนวนวัน (ค่าเช่ารถ,ค่าโรงแรม)',font=FONT1).pack()
v_days = StringVar()
E2 = ttk.Entry(f1,textvariable=v_days,font=FONT1)
E2.pack()

L = Label(f1,text='ค่าใช้จ่ายทั่วไป',font=FONT1).pack()
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


##################### TAB2 #####################

def read_csv():
        with open('save3.csv',newline="",encoding="utf-8") as f: #ให้เปิดไฟล์ csv ตัวนี้ขึ้นมาแล้วต้องชื่อเล่นมันว่า f
            fr = csv.reader(f)
        
            data = list(fr)
            
        return data
            


L = Label(T2,text = 'ตารางแสดงผลลัพธ์', font=FONT1,).pack()

header = ['รหัสรายการ','วัน-เวลา','จังหวัด','จำนวนวัน','ค่าใช้จ่ายทั่วไป','ค่าการเดินทางทั้งหมด']
reuslttabel = ttk.Treeview(T2,columns=header,show='headings',heigh=50) # เอาไปใส่ใน tab2 headings คือเพื่อให้ไม่มีการย่อลงมาได้ Treeview ตาราง
reuslttabel.pack()



for h in header: 
        reuslttabel.heading(h,text=h)


headerwidth = [140,150,100,60,80,80] 
for h,w in zip(header,headerwidth): 
        reuslttabel.column(h,width=w)



def DeleteRecord():
        check = messagebox.askyesno('confirm?','คุณต่้องการลบข้อมูลใช่หรือไม่')
        print('Yes/No',check)
        

        if check==True:
           print('delete')     
           select = reuslttabel.selection()
           #print(select)
           data = reuslttabel.item(select) #เรียกดูข้อมูลใน reuslttabel
           data = data['values'] #values เป็น key
           transactionID= data[0] #ค้นหาข้อมูลตำแหน่งที่ 0
           #print(transactionID)
           del alltransaction[str(transactionID)] #delete data in dict
           #print(alltransaction)
           updateCSV()
           update_table()
        else:
                print('cencel')

BDeldata = ttk.Button(T2,text='delete',command=DeleteRecord) #เอาไปใส่ใน T2 command คือการเรียกใช้ฟังกันอะไร
BDeldata.place(x=50,y=550)



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
           
           alltransaction[d[0]] = d # d[0] = transactionID
           reuslttabel.insert('',0,value=d) #เพิ่ม data ตำแหน่งแรก
       
    except Exception as e:
        print('No File')

update_table()


rightcclixk = Menu(T2,tearoff=0) # ไม่ต้องดึงออกมาได้  
rightcclixk.add_command(label='Edit')
rightcclixk.add_command(label='Delete')


def menupopup(event):
        print(event.x_root, event.y_root)
reuslttabel.bind('<Button-3>',menupopup)


GUI.bind('<Tab>',lambda x: E2.focus())
GUI.mainloop()
