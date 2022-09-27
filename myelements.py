# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 08:03:45 2018

@author: Nirbhay Jain
"""

import numpy as np
from integrationRule import integrateOnQuadrangle as integ


def Shapefunc(Vertex):
    A = np.zeros((4,4))
    for i in np.arange(0,4):
        A[i,:] = [1,Vertex[i,0],Vertex[i,1],(Vertex[i,0])*(Vertex[i,1])]
    
    Coef = np.zeros((4,4))
    for i in np.arange(0,4):
        B= np.zeros(4)
        B[i] = 1
        Coef[i,:] = np.linalg.solve(A,B)

    return Coef

def Stifness(Vertex, conductivity):
    Coeff=Shapefunc(Vertex)
    fdiagonals = [lambda x,y,i=i1:(Coeff[i,1]+(Coeff[i,3])*y)**2+(Coeff[i,2]+(Coeff[i,3])*x)**2 for i1 in range(4)]
    f1 = [lambda x,y,i=i1:(Coeff[0,1]+y*Coeff[0,3])*(Coeff[i+1,1]+y*Coeff[i+1,3])+(Coeff[0,2]+x*Coeff[0,3])*(Coeff[i+1,2]+x*Coeff[i+1,3]) for i1 in range(3)]
    f2 = [lambda x,y,i=i1:(Coeff[1,1]+Coeff[1,3]*y)*(Coeff[i+2,1]+Coeff[i+2,3]*y)+(Coeff[1,2]+Coeff[1,3]*x)*(Coeff[i+2,2]+Coeff[i+2,3]*x) for i1 in range(2)]
    f3 = lambda  x,y: (Coeff[2,1]+Coeff[2,3]*y)*(Coeff[3,1]+Coeff[3,3]*y)+(Coeff[2,2]+Coeff[2,3]*x)*(Coeff[3,2]+Coeff[3,3]*x)    
    
    Ke= np.zeros((4,4))
    for i in range(4):
        Ke[i,i]=integ(Vertex, fdiagonals[i], 0)
    for j in range(3):
        Ke[0,j+1]=integ(Vertex, f1[j], 0)
    for j in range(2):
        Ke[1,j+2]=integ(Vertex, f2[j], 0)   

    Ke[2,3]=integ(Vertex, f3, 0)

    for i in range(3):
        Ke[i+1,0]=Ke[0,i+1]
        
    for i in range(2):
        Ke[i+2,1]=Ke[1,i+2]

    Ke[3,2]=Ke[2,3]
    
    return Ke*conductivity


def Force(Vertex, sourceTerm):          
    Coeff=Shapefunc(Vertex)
    Force= np.zeros(4)
    f = [lambda x,y,i=i1:sourceTerm(x,y)*(Coeff[i1,0]+Coeff[i1,1]*x+Coeff[i1,2]*y+Coeff[i1,3]*x*y) for i1 in range(4)]
    for i in np.arange(0,4):
        Force[i]= integ(Vertex, f[i], 0)

    return Force


