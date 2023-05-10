from colorama import init,Fore
from time import sleep
init()

cl=None

def A_char():
    # # A 
    rows=7
    among_i=rows//2+1
    ch_arr=[]
    for i in range(1,rows+1):
        char_arr=[]
        for j in range(1,rows):
                if (i!=1 and(j==1 or j==rows-1)) or i==among_i or (i==1 and(j!=1 and j!=rows-1)):
                    char_arr.append('#')    
                else:
                    char_arr.append(' ')
        ch_arr.append(char_arr)  
    
    return ch_arr     

def B_char():
    # # B
    rows=7
    among_i=rows//2+1
    ch_arr=[]
    for i in range(1,rows+1):
        char_arr=[]
        for j in range(1,rows):
            if (i==1 and j!=rows-1) or (i==among_i and j!=rows-1) or (i==rows and j!=rows-1):
                char_arr.append('#')
            elif (i!=1 and i!=among_i and i!=rows and (j==1 or j==rows-1)):
                char_arr.append('#')    
            else:
                char_arr.append(' ') 
        ch_arr.append(char_arr)
            
    return ch_arr
def C_char():
   # # C
    rows=7
    among_i=rows//2+1
    ch_arr=[]
    for i in range(1,rows+1):
        char_arr=[]
        for j in range(1,rows):
            if ((i==1 or i==rows) and (j!=1 and j!=rows-1)):
                char_arr.append('#')
            elif ((i==2 or i==rows-1) and (j==1 or j==rows-1)):
                char_arr.append('#')
            elif (i>2 and i<rows-1 and j==1):
                char_arr.append('#')
            else:
                char_arr.append(' ')
        ch_arr.append(char_arr)
    return ch_arr
def D_char():
    # D
    rows=7
    among_i=rows//2+1
    ch_arr=[]
    for i in range(1,rows+1):
        char_arr=[]
        for j in range(1,rows):
            if ((i==1 or i== rows) and j!=rows-1):
                char_arr.append('#')
            elif (i>1 and i<rows and (j==1 or j==rows-1)):
                char_arr.append('#')
            else:
                char_arr.append(' ')
        ch_arr.append(char_arr)
    return ch_arr
    
def E_char():
    # # E
    rows=7
    among_i=rows//2+1
    ch_arr=[]
    for i in range(1,rows+1):
        char_arr=[]
        for j in range(1,rows):  
            if i==1 or i==rows :
                char_arr.append('#')
            elif i==among_i and j!=rows-1:
                char_arr.append('#')
            elif (i!=1 and i!=among_i and i!=rows and j==1):
                char_arr.append('#')
            else:
                char_arr.append(' ')
        ch_arr.append(char_arr)
    return ch_arr    

def F_char():
    # F
    rows=7
    among_i=rows//2+1
    ch_arr=[]
    for i in range(1,rows+1):
        char_arr=[]
        for j in range(1,rows):  
            if i==1  :
                char_arr.append('#')
            elif i==among_i and j!=rows-1:
                char_arr.append('#')
            elif (i!=1 and i!=among_i and j==1):
                char_arr.append('#')
            else:
                char_arr.append(' ')
        ch_arr.append(char_arr)
    return ch_arr
    
def G_char():
    # G
    rows=7
    among_i=rows//2+1
    ch_arr=[]
    for i in range(1,rows+1):
        char_arr=[]
        for j in range(1,rows):
            if ((i==1 or i==rows) and (j!=1 and j!=rows-1)):
                char_arr.append('#')
            elif i==among_i and (j==1 or j>=rows-3) :
                char_arr.append('#')
            elif i==among_i-1 and j==1:
                char_arr.append('#')
            elif i==among_i+1 and (j==1 or j==rows-1 or j==rows-3):
                char_arr.append('#')
            elif (i==2 or i==rows-1 )and (j==1 or j==rows-1):
                char_arr.append('#')
            else:
                char_arr.append(' ')
        ch_arr.append(char_arr)
    return ch_arr
    
def H_char():
    # H
    rows=7
    ch_arr=[]
    among_i=rows//2+1
    for i in range(1,rows+1):
        char_arr=[]
        for j in range(1,rows):
            if i==among_i:
                char_arr.append('#')
            elif i!=among_i and (j==1 or j==rows-1):
                char_arr.append('#')
            else:
                char_arr.append(' ')
        ch_arr.append(char_arr)
    return ch_arr
     
def I_char():
    # # I
    rows=7
    among_j=(rows-1)//2
    ch_arr=[]
    for i in range(1,rows+1):
        char_arr=[]
        for j in range(1,rows-1):
            if i==1 or i==rows:
                char_arr.append('#')
            elif j==among_j:
                char_arr.append('#')
            else:
                char_arr.append(' ')
        ch_arr.append(char_arr)
    return ch_arr
     
def J_char():
    # J
    rows=7
    among_j=(rows-1)//2
    ch_arr=[]
    for i in range(1,rows+1):
        char_arr=[]
        for j in range(1,rows-1):
            if i==1:
                char_arr.append('#')
            elif (i!=1 and i!=rows) and (j==among_j):
                char_arr.append('#')
            elif i==rows and j==among_j-1:
                char_arr.append('#') 
            elif i==rows-1 and j==among_j-2:
                char_arr.append('#')       
            else:
                char_arr.append(' ')
        ch_arr.append(char_arr)
    return ch_arr            

def K_char():
    # K
    rows=7
    among_i=rows//2+1
    ch_arr=[]
    for i in range(1,rows+1):
        char_arr=[]
        for j in range(1,rows):
            if j==1 or j==i-2 or j==(rows-1)-i:
                char_arr.append('#') 
            else:
                char_arr.append(' ') 
        ch_arr.append(char_arr)
    return ch_arr
      
def L_char():
    # # L
    rows=7
    among_i=rows//2+1
    ch_arr=[]
    for i in range(1,rows+1):
        char_arr=[]
        for j in range(1,rows):
            if j==1 or i==rows:
                char_arr.append('#') 
            else:
                char_arr.append(' ') 
        ch_arr.append(char_arr)
    return ch_arr
    
def M_char():
    # M
    rows=7
    among=rows//2+1
    ch_arr=[]
    for i in range(1,rows+1):
        char_arr=[]
        for j in range(1,rows+1):
            if j==1 or j==rows:
                char_arr.append('#') 
            elif (i<=among and (j==i or j==(rows+1)-i) ):
                char_arr.append('#') 
            else:
                char_arr.append(' ') 
        ch_arr.append(char_arr)
    return ch_arr
     
def N_char():
    # N
    rows=7
    among=rows//2+1
    ch_arr=[]
    for i in range(1,rows+1):
        char_arr=[]
        for j in range(1,rows+1):
            if j==1 or j==rows or j==i:
                char_arr.append('#') 
            else:
                char_arr.append(' ') 
        ch_arr.append(char_arr)
    return ch_arr
       
def O_char():
    # # O
    rows=7
    among=rows//2+1
    ch_arr=[]
    for i in range(1,rows+1):
        char_arr=[]
        for j in range(1,rows):
            if (i==1 or i==rows)and j!=1 and j!=rows-1:
                char_arr.append('#') 
            elif (i!=1 and i!=rows) and (j==1 or j==rows-1):
                char_arr.append('#') 
            else:
                char_arr.append(' ') 
        ch_arr.append(char_arr)
    return ch_arr
     
def P_char():
    # P
    rows=7
    among_i=rows//2+1
    ch_arr=[]
    for i in range(1,rows+1):
        char_arr=[]
        for j in range(1,rows):
            if (i==1 or i==among_i) and j!=rows-1:
                char_arr.append('#')
            elif i>1 and i<among_i and (j==1 or j==rows-1):
                char_arr.append('#')
            elif i>among_i and j==1:
                char_arr.append('#')
            else:
                char_arr.append(' ')
        ch_arr.append(char_arr)
    return ch_arr
    
def Q_char():
    # Q
    rows=7
    among_i=rows//2+1
    ch_arr=[]
    for i in range(1,rows+1):
        char_arr=[]
        for j in range(1,rows):
            if (i==1 ) and (j!=1 and j!=rows-1):
                char_arr.append('#')
            elif (i>1 and i<=among_i) and (j==1 or j==rows-1) :
                char_arr.append('#') 
            elif (i== among_i+1 ) and (j%2==0 and j!=2 or j==1)  :
                char_arr.append('#')  
            elif i==among_i+2 and (j==1 or j==rows-2):
                char_arr.append('#') 
            elif i==rows and j!=1 and j!=rows-2:
                char_arr.append('#')         
            else:
                char_arr.append(' ')
        ch_arr.append(char_arr)
    return ch_arr
    
def R_char():
    # R
    rows=7
    among_i=rows//2+1
    ch_arr=[]
    for i in range(1,rows+1):
        char_arr=[]
        for j in range(1,rows):
            if (i==1 or i == among_i) and j!=rows-1:
                char_arr.append('#')
            elif i>1 and i<among_i and (j==1 or j==rows-1):
                char_arr.append('#')    
            elif i> among_i and (j==1 or j==i-1) :
                char_arr.append('#')        
            else:
                char_arr.append(' ')
        ch_arr.append(char_arr)
    return ch_arr
    
def S_char():
    # S
    rows=7
    among_i=rows//2+1
    ch_arr=[]
    for i in range(1,rows+1):
        char_arr=[]
        for j in range(1,rows):
            if i==1 and j!=1 and j!=rows-1:
                char_arr.append('#')
            elif (i>1 and i<among_i) and j==1:
                char_arr.append('#')
            elif i==among_i and (j!=1 and j!=rows-1):
                char_arr.append('#')
            elif (i>among_i and i<rows) and j==rows-1:
                char_arr.append('#')
            elif i==rows and j!=rows-1 and j!=1:
                char_arr.append('#')
            else:
                char_arr.append(' ')
        ch_arr.append(char_arr)
    return ch_arr
    
def T_char():
    # T
    rows=7
    among_j=(rows//2) +1
    ch_arr=[]
    for i in range(1,rows+1):
        char_arr=[]
        for j in range(1,rows+1):
            if i==1 or j==among_j:
                char_arr.append('#')
            else:
                char_arr.append(' ')
        ch_arr.append(char_arr)
    return ch_arr
    
def U_char():
    # # U
    rows=7
    among_j=(rows//2) +1
    ch_arr=[]
    for i in range(1,rows+1):
        char_arr=[]
        for j in range(1,rows):
            if i>=1 and i<rows and (j==1 or j==rows-1):
                  char_arr.append('#')
            elif i==rows and j!=1 and j!=rows-1:
                 char_arr.append('#')      
            else:
                 char_arr.append(' ')
        ch_arr.append(char_arr)
    return ch_arr

def V_char():
    # V
    rows=7
    among=rows//2+1
    ch_arr=[]
    for i in range(1,rows+1):
        char_arr=[]
        for j in range(1,rows):
            if i<=among+1:
                if j==1 or j==rows-1:
                    char_arr.append('#')
                else:
                    char_arr.append(' ')    
            else:
                if j == among-(rows+1-i) or j == among+(rows-i):
                    char_arr.append('#')
                else:
                    char_arr.append(' ')
        ch_arr.append(char_arr)
    return ch_arr
      
def W_char():
    # W
    rows=7
    among=rows//2+1
    ch_arr=[]
    for i in range(1,rows+1):
        char_arr=[]
        for j in range(1,rows+1):
            if j==1 or j==rows:
                char_arr.append('#')
            elif (i>=among and (j==i or j==(rows+1)-i) ):
                char_arr.append('#')
            else:
                char_arr.append(' ')
        ch_arr.append(char_arr)
    return ch_arr
    

def X_char():
    # X
    rows=7
    among=rows//2+1
    ch_arr=[]
    for i in range(1,rows+1):
        char_arr=[]
        for j in range(1,rows+1):
            if j==i or j==(rows+1)-i:
                char_arr.append('#')
            else:
                char_arr.append(' ')
        ch_arr.append(char_arr)
    return ch_arr
    
def Y_char():
    # Y
    rows=7
    among_i=rows//2+1
    ch_arr=[]
    for i in range(1,rows+1):
        char_arr=[]
        for j in range(1,rows+1):
            if i>=among_i:
                if j==among_i:
                    char_arr.append('#')
                else:
                    char_arr.append(' ')
            else:
                if j==i or j==rows+1-i:
                    char_arr.append('#')
                else:
                    char_arr.append(' ')
        ch_arr.append(char_arr)
    return ch_arr
     
def Z_char():
    # Z
    rows=7
    among_i=rows//2+1
    ch_arr=[]
    for i in range(1,rows+1):
        char_arr=[]
        for j in range(1,rows):
            if i==1 or i==rows or j==rows-i:
                char_arr.append('#')
            else:
                char_arr.append(' ')
        ch_arr.append(char_arr)
    return ch_arr    

def get_color(cl):
    color=None
    if cl=='blue':
       color=Fore.BLUE
    elif cl=='black':
        color=Fore.BLACK
    elif cl=='yellow':
        color=Fore.YELLOW
    elif cl=='red':
        color=Fore.RED
    elif cl=='white':
        color=Fore.WHITE
    elif cl=='green':
        color=Fore.GREEN
    elif cl=='cyan':
        color=Fore.CYAN  
    return color          

               
main_arr=[]
def set_arr(arr):
    arr_inside={}
    for i in range(0,len(arr)):
             arr_inside[i]=arr[i]     
    main_arr.append(arr_inside)


def make_inside_dic(arr):
    char=''
    for ch in arr:
        char+=ch
    return char

def make_char():
    global main_arr,cl
    ch0=''
    ch1=''
    ch2=''
    ch3=''
    ch4=''
    ch5=''
    ch6=''
    ch7=''
    for every_dic in main_arr:
        
        for key in every_dic.keys():
            if key==0:
                ch0+=" "+make_inside_dic(every_dic[0])
            elif key==1:
                ch1+=" "+make_inside_dic(every_dic[1])
            elif key==2:
                ch2+=" "+make_inside_dic(every_dic[2])
            elif key==3:
                ch3+=" "+make_inside_dic(every_dic[3])
            elif key==4:
                ch4+=" "+make_inside_dic(every_dic[4])
            elif key==5:
                ch5+=" "+make_inside_dic(every_dic[5])
            elif key==6:
                ch6+=" "+make_inside_dic(every_dic[6])
            elif key==7:
                ch6+=" "+make_inside_dic(every_dic[7])    
    print(cl)
    print(ch0)        
    print(ch1)        
    print(ch2)        
    print(ch3)        
    print(ch4)        
    print(ch5)        
    print(ch6)        
    print(ch7)        
        
def make_space():
    ch_arr=[]
    for i in range(0,7):
        char_arr=[]
        for j in range(0,3):
            char_arr.append(' ')
        ch_arr.append(char_arr)
    return ch_arr        


def alpha_char(name,color):
    global cl
    cl=get_color(color.lower())   
    for n in name:
        n=str(n).lower()
        if n=="a":
            set_arr(A_char())
        elif n=="b":
            set_arr(B_char())
        elif n=='c':
            set_arr(C_char())    
        elif n=='d':
            set_arr(D_char())    
        elif n=='e':
            set_arr(E_char())  
        elif n=='f':
            set_arr(F_char())  
        elif n=='g':
            set_arr(G_char())  
        elif n=='h':
            set_arr(H_char())          
        elif n=='i':
            set_arr(I_char())  
        elif n=='j':
            set_arr(J_char())
        elif n=='k':
            set_arr(K_char())
        elif n=='l':
            set_arr(L_char())
        elif n=='m':
            set_arr(M_char())
        elif n=='n':
            set_arr(N_char())
        elif n=='o':
            set_arr(O_char())
        elif n=='p':
            set_arr(P_char())
        elif n=='q':
            set_arr(Q_char())
        elif n=='r':
            set_arr(R_char())
        elif n=='s':
            set_arr(S_char())
        elif n=='t':
            set_arr(T_char())
        elif n=='u':
            set_arr(U_char())
        elif n=='v':
            set_arr(V_char())
        elif n=='w':
            set_arr(W_char())
        elif n=='x':
            set_arr(X_char())
        elif n=='y':
            set_arr(Y_char())
        elif n=='z':
            set_arr(Z_char())   
        elif n==' ':
            set_arr(make_space())
    make_char()        
            
                                                                                 
      

if __name__=="__main__":
    alpha_char('mohsen abbasi','red')
    # make_char()
