import random
import numpy as np



def get_level(s_x,s_y,fake):
    global level,way
    while 1:
        way=[]
        try:
            size=s_x,s_y
            level=np.zeros(size)
            start_x=random.randint(0,s_x-1)
            start_y=random.randint(0,s_y-1)
            level[start_x,start_y]=1
            way.append(str(start_x)+","+str(start_y))
            get_way(s_x,s_y,start_x,start_y,8,0)
            for i in range(fake):
                start_x,start_y=fake_start(s_x,s_y,8)
                #print(start_x,start_y)
                if level[start_x,start_y]!=8:
                   level[start_x,start_y]=5
                way.append(str(start_x)+","+str(start_y))
                get_way(s_x,s_y,start_x,start_y,5,1)
            #print(level)
            break
        except:
            get_level(s_x,s_y,fake)
    return level


def get_way(s_x,s_y,start_x,start_y,mark,isfake):
    global level,way
    moved=''
    while 1:
        move=[]
        non=0
        if start_x>=1 and level[start_x-1,start_y]==0:
            if start_x>=2 and level[start_x-2,start_y]!=0:
                non=1
            if start_y==0 and level[start_x-1,start_y+1]==0 and non!=1:
                move.append("up")
            elif start_y==s_y-1 and level[start_x-1,start_y-1]==0 and non!=1:
                move.append("up")
            elif level[start_x-1,start_y+1]==0 and level[start_x-1,start_y-1]==0 and non!=1:
                move.append("up")
        non=0        
        if start_y>=1 and level[start_x,start_y-1]==0:
            if start_y>=2 and level[start_x,start_y-2]!=0:
                non=1
            if start_x==0 and level[start_x+1,start_y-1]==0 and non!=1:
                move.append("left")
            elif start_x==s_x-1 and level[start_x-1,start_y-1]==0 and non!=1:
                move.append("left")
            elif level[start_x-1,start_y-1]==0 and level[start_x+1,start_y-1]==0 and non!=1:
                move.append("left")
        non=0    
        if start_x<(s_x-2) and level[start_x+1,start_y]==0:
            if start_x<(s_x-3) and level[start_x+2,start_y]!=0:
                non=1
            if start_y==0 and level[start_x+1,start_y+1]==0 and non!=1:
                move.append("down")
            elif start_y==s_y-1 and level[start_x+1,start_y-1]==0 and non!=1:
                move.append("down")
            elif level[start_x+1,start_y+1]==0 and level[start_x+1,start_y-1]==0 and non!=1:
                move.append("down")
        non=0        
        if start_y<(s_y-2) and level[start_x,start_y+1]==0:
            if start_y<(s_y-3) and level[start_x,start_y+2]!=0:
                non=1
            if start_x==0 and level[start_x+1,start_y+1]==0 and non!=1:
                move.append("right")
            elif start_x==s_x-1 and level[start_x-1,start_y+1]==0 and non!=1:
                move.append("right")
            elif level[start_x-1,start_y+1]==0 and level[start_x+1,start_y+1]==0 and non!=1:
                move.append("right")
                
        if len(move)!=0:
            go=move[random.randint(0,len(move)-1)]
            if go=="up":
                start_x=start_x-1
            elif go=="down":
                start_x=start_x+1
            elif go=="left":
                start_y=start_y-1
            elif go=="right":
                start_y=start_y+1
            level[start_x,start_y]=mark
            way.append(str(start_x)+','+str(start_y))
            go=''
        else:
            if isfake==0:
                level[start_x,start_y]=3
            break
        
def fake_start(s_x,s_y,mark):
    while 1:       
        fakepoint=way[random.randint(0,len(way)-1)]
        i=int(fakepoint.split(",")[0])
        j=int(fakepoint.split(",")[1])
        move=[]
        if j<=s_x-2 and level[i,j+1]==0:
            move.append("r")
        if j>=1 and level[i,j-1]==0:
            move.append("l")
        if i<=s_y-2 and level[i+1,j]==0:
            move.append("d")
        if i>=1 and level[i-1,j]==0:
            move.append("u")
        if len(move)!=0:
            move=move[random.randint(0,len(move)-1)]
            if move=="r":
                j=j+1
            elif move=="l":
                j=j+1
            elif move=="u":
                i=i-1
            else:
                i=i+1
            break
        else:
            pass
    return i,j



#get_level(20,20,1)
