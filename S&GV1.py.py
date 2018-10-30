import pyodbc
import time

class db:

    

    def __init__(self, query, command, command2):
        self.query = query
        self.command = command
        self.command2 = command2
        
    
    
    def dbconn(self):
        
        conn = pyodbc.connect('Driver={SQL Server};SERVER=localhost\SQLEXPRESS;DATABASE=UNIS;UID=unisuser;PWD=unisamho')
        sql = self.query
        curs = conn.cursor()
        if self.command2==1:
            shift = curs.execute(sql)
        if self.command == 1:
            result = shift.fetchall()
            return result
        elif self.command == 2:
            result = shift.fetchone()
            return result
        elif self.command2==2:
            shift = curs.execute(shifts)
            unis.commit()
        conn.close()

class sort:
       
    def ed(self,data):
        lst=[]
        for x in data:
            lst.append(x)
            

        lst1 = []
        for x in lst:
            for x in x:
                lst1.append(str(x))
        return lst1



class ngp:

    def __init__(self,numd):
        self.numd = numd


    def pattern(self,ng,v,leap):

        if leap == 1:
            feb=29
        elif leap == 0:
            feb=28
        a = ng
        ngv = {1:31,3:31,5:31,7:31,8:31,10:31,12:31,4:30,6:30,9:30,11:30,2:feb}

          
        vicg = ngv[ng]
        if ng+1<12:
            ving = ngv[ng+1]
    
        elif ng+1>12:
            ving=ngv[(ng+1)%12]
            a =0
        elif ng+1==12:
            ving=31
        

        #print dinm
        nv = v              # v is the ast digit of previous pattern.
        values=[]
        
        
                
        for x in range(1,self.numd+1):
            if v+x <= vicg:
                    if ng<10:
                        if nv+x<10:
                            values.append(str(0)+str(ng)+str(0)+str(nv+x))
                        elif nv+x>10:
                            values.append(str(0)+str(ng)+str(nv+x))
                    elif ng>=10:
                        if nv+x<10:
                            values.append(str(ng)+str(0)+str(nv+x))
                        elif nv+x>=10:
                            values.append(str(ng)+str(nv+x))
                                
                            
                            
                    
            elif v+x == vicg+ving:
                if a+1<10:
                    values.append(str(0)+str(a+1)+str(ving))
                elif a+1>=10:
                    values.append(str(a+1)+str(ving))
                    
                
            elif v+x>vicg+ving:
                if a+2<10:
                    if (v+x)%(vicg+ving)<10:
                        values.append(str(0)+str(a+2)+str(0)+str((v+x)%(vicg+ving)))
                    elif (v+x)%(vicg+ving)>=10:
                        values.append(str(0)+str(a+2)+str((v+x)%(vicg+ving)))
                elif a+2>=10:
                    if (v+x)%(vicg+ving)<10:
                        values.append(str(a+2)+str(0)+str((v+x)%(vicg+ving)))
                    elif (v+x)%(vicg+ving)>=10:
                        values.append(str(a+2)+str((v+x)%(vicg+ving)))
                    
                        

            elif v+x>vicg:
                    if a+1<10:
                        if (nv-vicg+x)%ving <10:
                            values.append(str(0)+str(a+1)+str(0)+str((nv-vicg+x)%ving))
                        elif (nv-vicg+x)%ving >=10:
                            values.append(str(0)+str(a+1)+str((nv-vicg+x)%ving))
                    elif a+1>=10:
                        if (nv-vicg+x)%ving <10:
                            values.append(str(a+1)+str(0)+str((nv-vicg+x)%ving))
                        elif (nv-vicg+x)%ving >=10:
                            values.append(str(a+1)+str((nv-vicg+x)%ving))
                            
                            
                            

                 
        return values

class shiftdates:

    def __init__(self,numd):
        self.numd=numd

    def sd(self,dates):

        if self.numd==54:

            totalcount = 0
            count1 = 0
            count2 = 0

            ssdates=[]

            while totalcount <self.numd:
                if count1<4:
                    ssdates.append(dates[totalcount])
                    totalcount = totalcount+1
                    count1 = count1+1
                elif count1 >=4:
                    totalcount=totalcount+4
                    count1=0
                    count2=count2+1
                if count2 ==5:
                    break

            return ssdates

        elif self.numd==42:

            totalcount =0
            ssdates = []
            while totalcount <self.numd:
                if totalcount <2:
                    totalcount=totalcount+1
                if totalcount >=1 and totalcount<5 :
                    ssdates.append(dates[totalcount])
                    totalcount=totalcount+1
                if totalcount==5:
                    totalcount=totalcount+3
                if totalcount >=7 and totalcount<12:
                    ssdates.append(dates[totalcount])
                    totalcount=totalcount+1
                if totalcount==12:
                    totalcount=totalcount+2
                if totalcount>=14 and totalcount<17:
                    ssdates.append(dates[totalcount])
                    totalcount=totalcount+1
                if totalcount==17:
                    totalcount=totalcount+4
                if totalcount >=21 and totalcount <24:
                    ssdates.append(dates[totalcount])
                    totalcount=totalcount+1
                if totalcount == 24:
                    totalcount=totalcount+6
                if totalcount>=30 and totalcount<34:
                    ssdates.append(dates[totalcount])
                    totalcount=totalcount+1
                if totalcount ==34:
                    totalcount=totalcount+3
                if totalcount >=37 and totalcount<41:
                    ssdates.append(dates[totalcount])
                    totalcount=totalcount+1
                elif totalcount==41:
                    break
                
                    
            return ssdates
                    
                    
                    

                
            


#class 
#while True:
    
leap = 0       

year=int(time.strftime('%Y'))

if year %4==0:
    leap = 1 
if year % 100 == 0 and year %400 ==0:
    leap = 1
elif year %4 >0:
    leap=0

#### create list(s) of users that need to be assigned to special shifts -Identified by worktype 42 or 54 day

s42=[]
s54=[]
d42=db("select L_UID from tEmploye where C_work = (select C_Code from tWorkType where C_Name = 'SS42')",1,1)
d54=db("select L_UID from tEmploye where C_Work= (select C_Code from tWorkType where C_Name = 'SS54')",1,1)

for x in d42.dbconn():
    for y in x:
        if y not in s42:
            s42.append(y)

for x in d54.dbconn():
    for y in x:
        if y not in s54:
            s54.append(y)
            
###Shift start - based on 42 or 54 day shift assignment #####
strt42=[]
strt54=[]

ss42=db("select C_BasicDay from tWorktype where C_Name = 'SS42'",1,1)
ss54=db("select C_BasicDay from tWorktype where C_Name = 'SS54'",1,1)

for x in ss42.dbconn():
            for y in x:
                strt42.append(int(y))

for x in ss54.dbconn():
            for y in x:
                strt54.append(int(y))

n42=ngp(42)
n54=ngp(54)
x54=strt54
y54=str(x54)
x42=strt42
y42=str(x42)

pat42 = n42.pattern(int(y42[5:7]),int(y42[7:9]),leap)
pat54 = n54.pattern(int(y54[5:7]),int(y54[7:9]),leap)

d42=shiftdates(42)
d54=shiftdates(54)
wds54=d54.sd(pat54) # Returns dates - total of 20 - 4day gap over 40days
wds42=d42.sd(pat42)

#### 54 day pattern ####
def f4_day():
    
    days=1
    nights=2
    pat={}
    c=0
    for x in wds54:
        if c <2:
            pat[x]=days
            c=c+1
        elif c >=2:
            pat[x]=nights
            c=c+1
        if c ==4:
            c=0
    return pat

#### 42 Day pattern #####

def f2_day():

    days=1
    nights=2
    pat={}
    c=0
    
    for x in wds42:
        if c <=8:
            pat[x]=nights
            c=c+1
        if c > 8 and c <14:
            pat[x]=days
            c=c+1
        if c >=14:
            pat[x]=days
            c=c+1
        if c==24:
            break

    return pat
            
l42=[]      
for x in s42:
    for y in wds42:
        l=[]
        if y in f2_day():
            l.append(str(x))
            l.append(str(y))
            l.append(str(f2_day()[y]))
            l42.append(l)
            l=[]

l54=[]
for x in s54:
    for y in wds54:
        l=[]
        if y in f4_day():
            l.append(str(x))
            l.append(str(y))
            l.append(str(f4_day()[y]))
            l54.append(l)
            l=[]
            
        
    
    

        
        
        
        
    
    










    
        
    
    
    

    
    
