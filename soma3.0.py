# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 12:53:59 2022

@author: 北山_Besson
"""
import cmath #复数数学库
import math  #数学库
import os    #文件系统库

#第一部分

def medline(x1,z1,x2,z2):            #求中垂线
    a0=2*(x2-x1)
    b0=2*(z2-z1)
    c0=x1**2-x2**2+z1**2-z2**2
    return a0,b0,c0

def lines(x1,z1,x2,z2):               #两点法求直线
    a1=z1-z2
    b1=x2-x1
    c1=x1*z2-x2*z1
    return a1,b1,c1

def point(x0,z0,x1,z1,x2,z2):        #求中垂线和直线交点
    a0,b0,c0=medline(x1,z1,x2,z2)
    a1,b1,c1=lines(x0,z0,x1,z1)
    D=a0*b1-a1*b0
    if D==0:
        return None
    x=(b0*c1-b1*c0)/D
    z=(a1*c0-a0*c1)/D
    return x,z

f1=open("point.txt","r")
list1=[]
for line in f1.readlines():
    line=line.strip('\n')
    list1.append(line.split(','))
f1.close()

f2=open("opoint.txt","w")
x0=int(input("Px的值："))            #输入第一个圆心的x坐标
z0=int(input("Pz的值："))            #输入第一个圆心的z坐标
for i in range(0,len(list1)-1):
    x1,z1=float(list1[i][0]),float(list1[i][1])
    x2,z2=float(list1[i+1][0]),float(list1[i+1][1])
    x0,z0=point(x0,z0,x1,z1,x2,z2)
    f2.write("{0:.10f},{1:.10f}\n".format(x0, z0))
f2.close()

#第二部分

def soma(x1,z1,x2,z2,y,r,way):
    global n
    global list2
    dir="soma"
    if os.path.exists(dir)==False:
        os.mkdir(dir)
    Ra=cmath.polar(complex(x1,z1))[1]       #极坐标的样式是（r,θ），所以我们取第二个参数
    Rb=cmath.polar(complex(x2,z2))[1]
    Da=int(math.degrees(Ra))
    Db=int(math.degrees(Rb))
    c=abs(Da-Db)
    if way=="1":
        if Da>Db:
            name=str(n)
            fp=open(dir+"\\"+name+".mcfunction","w")
            
            for i in range(Da,Db-1,-1):
                rad=math.radians(i)
                xi=cmath.rect(r,rad).real+float(list2[n][0])
                zi=cmath.rect(r,rad).imag+float(list2[n][1])
                fp.write("particle end_rod {0:.10f} {1:.10f} {2:.10f} 0 0 0 0.1 1 force\n".format(xi, y,zi))
            fp.close()
          
        else:
            c=360-c
            name=str(n)
            fp=open(dir+"\\"+name+".mcfunction","w")
            
            for i in range(Da,Da-c-1,-1):
                rad=math.radians(i)
                xi=cmath.rect(r,rad).real+float(list2[n][0])
                zi=cmath.rect(r,rad).imag+float(list2[n][1])
                fp.write("particle end_rod {0:.10f} {1:.10f} {2:.10f} 0 0 0 0.1 1 force\n".format(xi, y,zi))
            fp.close()
           
    else:
        if Db==180:
            Db=-180
        if Da>Db:
            name=str(n)
            fp=open(dir+"\\"+name+".mcfunction","w")
            
            for i in range(Da,Da+c+1):
                rad=math.radians(i)
                xi=cmath.rect(r,rad).real+float(list2[n][0])
                zi=cmath.rect(r,rad).imag+float(list2[n][1])
                fp.write("particle end_rod {0:.10f} {1:.10f} {2:.10f} 0 0 0 0.1 1 force\n".format(xi, y,zi))
            fp.close()
            
        else:
            c=360-c
            name=str(n)
            fp=open(dir+"\\"+name+".mcfunction","w")
            
            for i in range(Da,Da+c+1):
                rad=math.radians(i)
                xi=cmath.rect(r,rad).real+float(list2[n][0])
                zi=cmath.rect(r,rad).imag+float(list2[n][1])
                fp.write("particle end_rod {0:.10f} {1:.10f} {2:.10f} 0 0 0 0.1 1 force\n".format(xi, y,zi))
            fp.close()
            

y=int(input("请输入y的值："))
way=input("请输入方向（0为顺时针，1为逆时针）：")
f2=open("opoint.txt","r")
list2=[]
for line in f2.readlines():
    line=line.strip('\n')
    list2.append(line.split(','))
f2.close()
n=0
for i in range(0,len(list1)-1):
    x1=float(list1[i][0])-float(list2[n][0])
    z1=float(list1[i][1])-float(list2[n][1])
    x2=float(list1[i+1][0])-float(list2[n][0])
    z2=float(list1[i+1][1])-float(list2[n][1])
    r=math.sqrt(x1**2+z1**2)
    soma(x1,z1,x2,z2,y,r,way)
    n+=1
    if 0<n<len(list1)-1:
        if float(list2[n][1])<=float(list2[n-1][1]):
            if way=="1":
                way="0"
            else:
                way="1"