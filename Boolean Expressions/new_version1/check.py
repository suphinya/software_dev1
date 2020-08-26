class checkdata() :               
    
    def __init__(self,data) :           # สร้างเมธอดข้อมูลขึ้นมา
        self.data = data.replace(" ", "")                # ข้อมูลเริ่มต้นที่อ่านมาที่แยกช่องว่างแล้ว
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


#--------------------------------------------------------------


