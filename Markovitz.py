
import numpy as np
from math import *
import pandas
import matplotlib.pyplot as plt


file=file="C:\\Users\\33611\\Downloads\\Composants_CAC40\\Composants_CAC40\\";

CAC=["ACA","AI","AIR","ALSO","AXA","BN","BNP","CA","CAP","DG","DSY","EL","EN","ENGI","ERF","GLE","HO","KER","LR","MC","ML","MT","OR","ORA","PUB","RI","RMS","RNO","SAF","SAN","SGO","STLA","STM","SU","TEP","TTE","VIE","VIV","WLN"]

company=["BN","ALSO","ORA"]
#,"STLA","ERF"

def recuperationprice(file,n):
    sortie = pandas.read_csv(file, usecols=['Dernier'])
    return(float(sortie.iloc[n]['Dernier']))

def nbprice(file):
    sortie = pandas.read_csv(file, usecols=['Dernier'])
    return(516)
    #return(len(sortie))

def Rentabilite(x,file,nbprice,recuperationprice):
    f=file+x+".PA.csv"
    R=[]
    for i in range(nbprice(f)-1):
        r=(recuperationprice(f,i+1)-recuperationprice(f,i))/recuperationprice(f,i)
        R.append(r)
    return(R)


def Variance(x,file,nbprice,recuperationprice,Rentabilite):
    f=file+x+".PA.csv"
    R=Rentabilite(x,file,nbprice,recuperationprice)
    m=0
    v=0
    for i in range(len(R)):
        m+=R[i]
    m=m/len(R)
    for i in range(len(R)):
        v+=(R[i]-m)**2
    v=v/len(R)
    return(v,m)

def Covariance(x,y,file,nbprice,recuperationprice,Rentabilite):
    R1=Rentabilite(x,file,nbprice,recuperationprice)
    R2=Rentabilite(y,file,nbprice,recuperationprice)
    m1=0
    m2=0
    v=0
    if(len(R1)<=len(R2)):
        n=len(R1)
    else:
        n=len(R2)
    for i in range(n):
        m1+=R1[i]
        m2+=R2[i]
    m1=m1/n
    m2=m2/n
    for i in range(n):
        v+=(R1[i]-m1)*(R2[i]-m2)
    return(v/n)


def PoidsAleatoire(n):
    W=np.random.dirichlet(np.ones(n),size=1)
    return(W)


def Marko(company,file,nbprice,recuperationprice,Rentabilite,Variance,Covariance):
    V=[]
    n=len(company)
    for i in range(n):
        for j in range(n):
            if(i==j):
                V.append(Variance(company[i],file,nbprice,recuperationprice,Rentabilite)[0])
            else:
                V.append(Covariance(company[i],company[j],file,nbprice,recuperationprice,Rentabilite))
    Vp = np.array(V,dtype=float)
    Vp = Vp.reshape((n,n))
    return(Vp)


def markovitz(company,file,nbprice,recuperationprice,Rentabilite,Variance,Covariance,PoidsAleatoire):
    V=[]
    R=[]
    n=len(company)
    for i in range(n):
        for j in range(n):
            if(i==j):
                V.append(Variance(company[i],file,nbprice,recuperationprice,Rentabilite)[0])
            else:
                V.append(Covariance(company[i],company[j],file,nbprice,recuperationprice,Rentabilite))
    Vp = np.array(V,dtype=float)
    Vp = Vp.reshape((n,n))
    W = np.array(PoidsAleatoire(n))
    tW = np.transpose(W)
    VV=((np.dot(W,Vp)).dot(tW))
    for i in range(n):
        R.append(Variance(company[i],file,nbprice,recuperationprice,Rentabilite)[1])
    E=np.array(R,dtype=float)
    Ep=np.dot(E,tW)
    return(Ep[0],VV[0,0])

def MonteCarlo(Marko,company,file,nbprice,recuperationprice,Rentabilite,Variance,Covariance,PoidsAleatoire,N):
    Risque=[]
    Rendement=[]
    R=[]
    n=len(company)
    Vp=Marko(company,file,nbprice,recuperationprice,Rentabilite,Variance,Covariance)
    print("Vp",Vp,"\n")
    for i in range(n):
        R.append(Variance(company[i],file,nbprice,recuperationprice,Rentabilite)[1])
    E=np.array(R,dtype=float)
    print("E",E,"\n")
    for i in range(N):
        W = np.array(PoidsAleatoire(n))
        tW = np.transpose(W)
        VV=((np.dot(W,Vp)).dot(tW))
        Ep=np.dot(W,np.transpose(E))
        Rendement.append(Ep[0])
        Risque.append(sqrt(VV)*sqrt(365))
    plt.plot(Risque,Rendement,'*')
    plt.xlabel('Risk')
    plt.ylabel('Return')
    plt.grid(True)
    plt.show()