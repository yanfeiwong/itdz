#Task 4
import datetime
Average_life=80
while 1:
    
        print("Please enter your birthday")
        yy=input("Yaer:")
        mm=input("Month:")
        dd=input("Day:")
        hh=input("Hours:")
        mi=input("Minute:")
        bd=yy+"-"+mm+"-"+dd+" "+hh+":"+mi+":01"
        bd=datetime.datetime.strptime(bd, '%Y-%m-%d %H:%M:%S')
        now=datetime.datetime.now()
        lvd=now-bd
        print("You lived:"+str(lvd.days)+" days "
              +str(int(lvd.seconds/3600))+" hours "+
              str(int((lvd.seconds-int(lvd.seconds/3600)*3600)/60))+"minute")
        delta = datetime.timedelta(days=Average_life*365)
        n_days = bd + delta
        lvd=n_days-now
        print("Time remaining:"+str(lvd.days)+" days "
              +str(int(lvd.seconds/3600))+" hours "+
              str(int((lvd.seconds-int(lvd.seconds/3600)*3600)/60))+"minute")
        break

        
        
