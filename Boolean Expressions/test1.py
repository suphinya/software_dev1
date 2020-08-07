class exptt() :               
    
    def __init__(self,func) :       
        self.func = func           
        self.tree = []
        for i in range(len(func)) :     
            if func[i] == '(' or func[i] == ')' :      
                pass
            else :
                self.tree.append(func[i])         
        i = 0
        while True :           
            if len(self.tree) <= (2**(i))-1 :       
                temp = 2**(i) - 1                  
                break                         
            else :
                i += 1
                pass
        self.mylist = ['None'] * temp           
        

    def trans(self) :                                          
        n = 0

        self.boo = []
        for i in range(len(self.func)):
            if self.func[i] == 'I' and self.func[i+1] == '0' :
                self.boo += ['I0']
                
            if self.func[i] == 'I' and self.func[i+1] == '1' :
                self.boo += ['I1']
                
            if self.func[i] == 'I' and self.func[i+1] == '2' :
                self.boo += ['I2']
                
            if self.func[i] == 'I' and self.func[i+1] == '3' :
                self.boo += ['I3']
                
            if self.func[i] in '01' and self.func[i-1] != 'I':
                self.boo += self.func[i]
                
            if self.func[i] in '+!&()' :
                self.boo += self.func[i]
        

        for i in self.boo :                           
            self.left = (n * 2) + 1                        
            self.right = (n * 2) + 2                      
            if i == '(' :                                
                if self.mylist[self.left] == 'None' :      
                    n = self.left
                else :                                              
                    n = self.right
            elif i == 'I1' or i == 'I0' or i == 'I2' or i == 'I3' or i == '1' or i == '0' :                         
                if self.mylist[self.left] == 'None' :      
                    self.mylist[self.left] = i
                else :
                    self.mylist[self.right] = i
            elif i in '+&' :                                      
                self.mylist[n] = i 
                
            else :                              
                if n%2 == 1 :                   
                    n = int((n-1)/2)
                else :
                    n = int((n-2)/2)             
                    
        return self.mylist
            
            
        
        
f =" ((I1 +I0 ) & (1+I2 )) + (I1 + 0)" 
n = f.replace(" ", "")
test = exptt(n)
show = test.trans()
print(show)