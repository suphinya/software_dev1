class checkdata() :               
    
    def __init__(self,data) :           # สร้างเมธอดข้อมูลขึ้นมา
        self.data = data                # ข้อมูลเริ่มต้นที่อ่านมา
        self.boo = []                   # ลิสว่างที่เอาไว้ใส่ข้อมูลหลังจากเช็คและเปลี่ยนค่าตัวแปรแล้ว

    def checkntrans(self) :     # เมธอดในการแปลงสมการ ให้เป็นตัวแปรที่ต้องการ                                     

        for i in range(len(self.data)):
            if self.data[i] == 'I' and self.data[i+1] in '0123456789': # แปลงให้เป็น I0,I1ต่างๆ หรือ !I0,!I1 ต่างๆ โดยจับคู่ I กับเลข หรือจับคู่กับเลขและ !
                if self.data[i-1] == '!':
                    self.boo += ['!'+self.data[i]+self.data[i+1]]
                elif self.data[i-2] == '!' and self.data[i-1] == '('and self.data[i+2] == ')':
                    self.boo += ['!'+self.data[i]+self.data[i+1]]
                else:
                    self.boo += [self.data[i]+self.data[i+1]]
                
            elif self.data[i] in '01' and self.data[i-1] != 'I': # ถ้าเป็นเลขเปล่าๆไม่มี I ประกบ ให้ค่าได้เลย
                self.boo += self.data[i]
                
            elif self.data[i] in '+!&()' :                
                if self.data[i] in '+&':              # เครื่องหมายต่างๆให้ค่าได้ ยกเว้น ! และ () ต้องดูอีกที
                    self.boo += self.data[i]
                elif self.data[i] =='(' :                                   # กรณีของ (
                    if self.data[i+2] == ')' or self.data[i+3] == ')':      # กรณีที่ภายใน () มีค่าเดียวหรือไม่มีเครื่องหมายภายในวงเล็บ ให้ผ่าน
                        pass
                    else :
                        self.boo += self.data[i]                            # นอกจากนั้นให้ค่า ( ตามปกติ
                elif self.data[i] == ')':                                   # กรณีของ )
                    if self.data[i-2] == '(' or self.data[i-3] == '(':      # กรณีที่ภายใน () มีค่า้ดียวหรือไม่มีเครื่องหมายในวงเล็บ ให้ผ่าน (เหมือนกับกรณี'(')
                        pass
                    else :
                        self.boo += self.data[i]                            # นอกจากนั้นให้ค่า ) ตามปกติ
                elif self.data[i] in '!':               # กรณีของ ! 
                    if self.data[i+1] == '(' and self.data[i+3] in '+&':
                        self.boo += self.data[i]
                    elif self.data[i+1] == '(' and self.data[i+4] in '+&':
                        self.boo += self.data[i]
                    elif self.data[i+1] == '(' and self.data[i+2] in '!':
                        self.boo += self.data[i]
                    else :
                        pass

        return self.boo


#------------------------------------------Test class checkdata--------------------------------------------------------------------------

#"!(1+0)"                               ['!', '(', '1', '+', '0', ')']   
#"!(!(0+I0&1))"                         ['!', '(', '!', '(', '0', '+', 'I0', '&', '1', ')', ')']
#"(I0+!I1+!(I2))&(!I0+I1+I2)"           ['(', 'I0', '+', '!I1', '+', '!I2', ')', '&', '(', '!I0', '+', 'I1', '+', 'I2', ')']
#"!(I0&I1)+!(I1+I2)"                    ['!', '(', 'I0', '&', 'I1', ')', '+', '!', '(', 'I1', '+', 'I2', ')']
#"(((I0&I1&!I2)+!I1)+I3)"               ['(', '(', '(', 'I0', '&', 'I1', '&', '!I2', ')', '+', '!I1', ')', '+', 'I3', ')']

datainput = "(I0+!I1+!(I2))&(!I0+I1+I2)" 
notspace = datainput.replace(" ", "")
print(notspace)

inclassch = checkdata(notspace)
showlist = inclassch.checkntrans()
print(showlist)

#------------------------------------แบบแยกกันก่อนนะคะ--------------------------------------------------------------------------------

class tree():
    
    def __init__ (self,func):                       # สร้างค่าและลิสต์สำหรับnodetree
        self.func = func
        self.listtree = [''] * 40
        self.complete = [''] * 40
        
       
    def maketree(self):                             
        node = 0                                    # root start
        for i in self.func:                             
            left = ( node * 2 ) + 1                 # node left
            right = ( node * 2 ) + 2                # node right
            back = None                             # back up กันการทับกัน
            
            if i == '(':                            # กรณีของ ( เพื่อใช้ในการจัดค่าของโนดภายในวงเล็บ
                if self.listtree[left] == '' :
                    node = left
                elif self.listtree[left] != '':
                    node = right
                    
            elif i in '+&':                         # กรณีของ การใส่ +,& โดยเช็คการทับกันด้วย
                if self.listtree[node] == '' :      # กรณี root ที่โนดนี้ ว่าง
                    self.listtree[node] = i
                elif self.listtree[node] != '':     # กรณี root ที่โนดนี้ ไม่ว่าง
                    if self.listtree[right] == '':
                        self.listtree[right] = i
                    elif self.listtree[right] != '' :   # กรณี root ไม่ว่างและมีการเกิดการทับกัน
                        back = self.listtree[right]
                        self.listtree[right] = i
                        self.listtree[(right*2)+1] = back
                        del back
                        
            elif i == 'I1' or i == 'I0' or i == 'I2' or i == 'I3' or i in '01' or i == '!I0' or i == '!I1' or i == '!I2' or i == '!I3' : # กรณีการใส่ค่าตัวแปร 
                    if self.listtree[left] == '' :              # เช็คการทับกันทั้งตัวแปรและเครื่องหมาย
                        self.listtree[left] = i
                    elif self.listtree[left] != '' :
                        if self.listtree[right] == '':
                            self.listtree[right] = i
                        elif self.listtree[right] != '':
                            if self.listtree[(right*2)+1] == '':
                                self.listtree[(right*2)+1] = i
                            else:
                                self.listtree[(right*2)+2] = i


            elif i == ')':                          # การปิดวงเล็บเพื่แคำนวนหาโนดที่เชื่อมต่อกับวงเล็บต่อไป
                if node%2 == 1 :
                    node = int((node-1)/2)
                else :
                    node = int((node-2)/2)

        # -------------------------   กรณีของ ! ยังไม่สมบูรณ์ --------------------------------------
            #elif i == '!' :
                #if self.listtree
                #if self.listtree[node] == '':
                    #self.listtree[node] = i
                    #self.listree[right] = 'None'
                #elif self.listtree[node] != '':

        # --------------------------------------------------------------------------------------       
        
        #check  ตำแหน่ง 
        for lenlist in range(len(self.listtree)):           
            if self.listtree[0] == '':                  # กรณี root เริ่มต้น (root = 0) มีค่าว่าง
                if lenlist < 30 :
                    if self.listtree[lenlist] == '' :
                        pass
                    else:
                        self.complete[int(lenlist/2)] = self.listtree[lenlist]
                elif lenlist > 30:
                    if self.listtree[lenlist] == '' :
                        pass
                    else:
                        self.complete[int((lenlist+2)/2)] = self.listtree[lenlist]
                
            else:                                       # กรณีปกติอยู่แล้ว
                self.complete[lenlist] = self.listtree[lenlist]
                
        return self.complete                                                            
        

 
#--------------------------------- test class tree --------------------------------------------
          
inputt = ['(', 'I0', '+', '!I1', '+', '!I2', ')', '&', '(', '!I0', '+', 'I1', '+', 'I2', ')']
inclass = tree(inputt)
completetree = inclass.maketree()
print(completetree)

# 3,5 pass
# เหลือกรณี ! ยังไม่ได้ใส่เงื่อนไข