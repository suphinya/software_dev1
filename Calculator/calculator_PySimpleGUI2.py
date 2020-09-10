##############################################
##          Name : Suphinya Wu              ##
##          ID : 6201012630100              ##
##############################################


import PySimpleGUI as sg

# ตั้งค่าธีม
sg.theme("LightBrown7")

# ข้อมูลในหน้าต่าง
layout = [[sg.Text("calculator eiei", size=(16,1))], 
    [sg.Text('', size=(15,1) , background_color='black', font=('Digital-7',58),text_color='#cc1d1d', justification='right', key="input")],
    [sg.Button("%",size=(5,1),font=('Digital-7',40)) , sg.Button("DEL",size=(5,1),font=('Digital-7',40)) , sg.Button("CE",size=(5,1),font=('Digital-7',40)) , sg.Button("/",size=(5,1),font=('Digital-7',40))],
    [sg.Button("7",size=(5,1),font=('Digital-7',40)) , sg.Button("8",size=(5,1),font=('Digital-7',40)) , sg.Button("9",size=(5,1),font=('Digital-7',40)) , sg.Button("*",size=(5,1),font=('Digital-7',40))],
    [sg.Button("4",size=(5,1),font=('Digital-7',40)) , sg.Button("5",size=(5,1),font=('Digital-7',40)) , sg.Button("6",size=(5,1),font=('Digital-7',40)) , sg.Button("-",size=(5,1),font=('Digital-7',40))],
    [sg.Button("1",size=(5,1),font=('Digital-7',40)) , sg.Button("2",size=(5,1),font=('Digital-7',40)) , sg.Button("3",size=(5,1),font=('Digital-7',40)) , sg.Button("+",size=(5,1),font=('Digital-7',40))],
    [sg.Button("0",size=(5,1),font=('Digital-7',40)) , sg.Button(".",size=(5,1),font=('Digital-7',40)) , sg.Button("=",size=(10,1),font=('Digital-7',42), focus = True )]]
    

# สร้างหน้าต่าง
window = sg.Window("test calculator", layout)

# ใช้เก็บค่าหน้าจอแสดงผล
output = ''

while True:
    event, values = window.read()
    print(event)

    if event in ['0','1','2','3','4','5','6','7','8','9','+','-','*','/','.'] : # ใส่ค่าในหน้าจอแสดงผล
        if len(output) < 14 :
            output += event
            window['input'].update(output)
        if len(output) > 14:
            pass

    if event == 'CE' :      # ถ้าปุ่มเป็น CE ให้ลบค่าในจอแสดงผลทั้งหมด
        output = ''
        window['input'].update(output)

    if event == '=' :       # ถ้าปุ่มเป็น  = ให้ทำการคำนวนค่า +,-,*,/ ตามค่าที่แสดงในหน้าจอ (ให้ทศนิยม 4 ตำแหน่ง)
        #output = str(eval(output))
        output = '{:,.2f}'.format(eval(output))
        window['input'].update(output)
       
    if event == '%' :       # ถ้าปุ่มเป็น % ให้หาร 100
        output = str( float(output) / 100 )
        window['input'].update(output)

    if event == 'DEL':      # ถ้าปุ่มเป็น DEL ให้ลบค่าล่าสุด
        output = output[0:-1]
        window['input'].update(output)

    if event == sg.WINDOW_CLOSED:   # ปิดหน้าต่าง
        break
    


window.close()

#################################################################
# ref : https://github.com/israel-dryer/PyDataMath-II/blob/master/calculator_sg.py
# ref : https://pysimplegui.readthedocs.io/en/latest/#button-element