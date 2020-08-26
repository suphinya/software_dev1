class tree():
    
    def __init__ (self,func):           # สร้างค่าและลิสต์สำหรับnodetree
        self.func = func
        self.listtree = [''] * 40
        self.complete = [''] * 40
        
       
    def maketree(self):
        node = 0                        # root start
        for i in self.func:
            left = ( node * 2 ) + 1     # node left
            right = ( node * 2 ) + 2    # node right
            back = None                 # back up กันการทับกัน
            
            if i == '(':                                # กรณีของ ( เพื่อใช้ในการจัดค่าของโนดภายในวงเล็บ
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
                        
            elif i == 'I1' or i == 'I0' or i == 'I2' or i == 'I3' or i in '01' or i == '!I0' or i == '!I1' or i == '!I2' or i == '!I3' :     # กรณีการใส่ค่าตัวแปร
                    if self.listtree[left] == '' :  # เช็คการทับกันทั้งตัวแปรและเครื่องหมาย
                        self.listtree[left] = i
                    elif self.listtree[left] != '' :
                        if self.listtree[right] == '':
                            self.listtree[right] = i
                        elif self.listtree[right] != '':
                            if self.listtree[(right*2)+1] == '':
                                self.listtree[(right*2)+1] = i
                            else:
                                self.listtree[(right*2)+2] = i
 
                        
            elif i == '!' :        # กรณีการทำ !
                
                if self.listtree[node] == '':
                    self.listtree[node] = i
                    self.listtree[right] = 'None'
                elif self.listtree[node] != '':
                    if self.listtree[left] == '':
                        self.listtree[left] = i 
                        self.listtree[(left*2)+2] = 'None'
                    elif self.listtree[left] != '':
                        if self.listtree[right] == '' :
                            self.listtree[right] = i
                            self.listtree[(right*2)+2] = 'None'
                        else :
                            self.listtree[(right*2)+1] = i
                            self.listtree[(((right*2)+1)*2)+2] = 'None'




            elif i == ')':          # การปิดวงเล็บเพื่แคำนวนหาโนดที่เชื่อมต่อกับวงเล็บต่อไป
                if node%2 == 1 :
                    node = int((node-1)/2)
                else :
                    node = int((node-2)/2)
                         
        
        #check position
        for lenlist in range(len(self.listtree)):
            if self.listtree[0] == '':      # กรณี root เริ่มต้น (root = 0) มีค่าว่าง
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
                
            else:   # กรณีปกติอยู่แล้ว
                self.complete[lenlist] = self.listtree[lenlist]
                
        return self.complete
        

 
#------------------------------------------------------------------------
