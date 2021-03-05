from paramètres import *
from intersectionarc import *
from calculrayoncourbure import *


def cibleatteignable2(segments,p,v):
    [positioninit1,positioninit2,orientationinit1,orientationinit2,vinit1,vinit2,deltat,amaxlat,epsilonmax,amax,amin,tsb,l,larg,vmax,N,rv,m,alpha,lanti]=params()
    Rminamaxlat=v**2/amaxlat
    Rminepsilonmax=tsb*v**2/(epsilonmax*pi/180)+l/(epsilonmax*pi/180)
    Rmin=max(Rminamaxlat,Rminepsilonmax)
    Rmax=abs(calculrayoncourbure(p))/4
    xp=p[0]
    yp=p[1]
    Ns=len(segments)
    
    Rminajuste=Rmin
    K=0
    if xp!=0:
        K=yp/xp
        b=abs(K/2)
        c=-1/2
        delta=b**2-4*c
        sintheta=(-b+sqrt(delta))/2
        theta=asin(sintheta)
        Rminajuste=v*3*deltat/theta
    Rmin=max(Rminajuste,Rmin)
     
        
    
    
    sgyp=1
    if yp<0:
        sgyp=-1
        
    if Rmin>Rmax:
        return(0,Rmax,sgyp,Rmin)
        
    R=[]
    Nr=100
    i=0
    while i<Nr:
        R.append(Rmin+i*(Rmax-Rmin)/(Nr-1))
        i+=1
        

    i=0
    while i<Nr:
        r=R[i]
        yc=sgyp*r
        
        if yp==0:
            return(1,Rmax,1) #on va en ligne dte
        if xp!=0:
            xinter=(-2*K*yc)/(1+K**2)
            yinter=K*xinter
            #print('xp',xp)
            #print('yp',yp)
            #print('xinter',xinter)
            #print('yinter',yinter)
            #print('r',r)
            
            j=0
            while j<Ns and intersectionarc([xinter,yinter],segments[j])!=1:
                j+=1
            if j==Ns:
                return(1,r,sgyp,Rmin)
            return(0,r,sgyp,Rmin)    
            
        xinter=0
        yinter=sgyp*2*r
        theta=180
        j=0
        while j<Ns and intersectionarc([xinter,yinter],segments[j])!=1:
            j+=1
        if j==Ns:
            return(1,r,sgyp,Rmin)
        return(0,r,sgyp,Rmin)
        i+=1