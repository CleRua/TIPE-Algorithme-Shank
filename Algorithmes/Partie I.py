# -*- coding: utf-8 -*-
"""
Created on Fri May 15 17:28:25 2015

@author: clement

TIPE : Partie I
"""


from random import *

def algo_Euclide_etendu(a,b): 
    r1=a
    u1=1
    v1=0
    r2=b
    u2=0
    v2=1
    while r2!=0 : #Invariants de boucle : r1=u1*a+v1*b et r2=u2*a+v2*b
        q=r1//r2
        rs=r1 ; us=u1 ; vs=v1 #Variables de sauvegarde
        r1=r2 ; u1=u2 ; v1=v2
        r2 = rs - q*r2 # r2 <- Reste de la division euclidienne de r1 par r2
        u2 = us - q*u2
        v2 = vs - q*v2
    return(r1,u1,v1) #On prend le dernier reste non nul.
    
def inverse_modulaire(a,p):
    (r,u,v) = algo_Euclide_etendu(a,p)
    #Si r=1, a*u + v*p = 1 donc a*u = 1 mod p. Donc u = a**(-1).
    while u<0:
        u = (u+p)%p
    return(u)

def mod_pow(x,e,p): #Calcule (x**e)%p .
    x = x % p
    R = 1
    while e > 0 :
        if (e%2) == 1 :
            R = (R*x) % p
        e = e//2
        x = (x*x) % p 
    return(R)

def public_key(p,g,s):
    h = mod_pow(g,s,p)
    return(p,g,h)
    
def encrypt(p,g,h,m):
    k = int (p*random())
    c1 = mod_pow(g,k,p)
    c2 = (m*mod_pow(h,k,p))%p
    return(c1,c2)
        
def decrypt(c1,c2,s,p):
    c3 = inverse_modulaire(mod_pow(c1,s,p),p)
    m = (c2*c3)%p
    return(m)
    
def algo_naif(y,g,p):
    k=0
    A=1
    while y != A:
        A=(A*g)%p
        k = k+1
    return(k)   
    
    
def algo_Shank(y,g,p):
    n = int(p**(1/2)) + 1 #1: On choisit n.
    T = creer_table()
    A=1
    for i in range(n): #2: Baby-step.
        inserer(T,(i,A))
        A = A*g
    #En sortie de boucle, A = g**n .
    B = inverse_modulaire(A,p) #3: Algorithme d'Euclide étendu.
    q=0
    C=y
    (r,_) = chercher(T,C)
    while r == (-1): #4: Giant-step.
        (r,_) = chercher(T,C*B)
    k = n*q + r #5: y*g**(-n*q) = g**r donc y = g**(n*q + r)
    return(k)
