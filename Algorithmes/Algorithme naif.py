# -*- coding: utf-8 -*-
"""
Created on Wed May 20 23:18:37 2015

@author: clement

Algorithme naïf
"""

import time
from datetime import datetime

Nb_p2=[10009,50069,100069,200003,300007,400069,500029,600011,700027,800117,900091,1000133,2000003,3000029,4000037,5000201,6000047,7000061,8000009,9000011,10000103,20000003,30000023,40000123,50000063,60000011,70000037,80000069,90000049,100000049,200000033,300000119,400000043,500000057,600000019,700000001,800000063,900000011,1000000097,2000000011,3000000077,4000000007,5000000497,6000000089,7000000013,8000000081,9000000307,10000000019]
Gen_communs = [11,539,8624]

Nb_p=[10009,50069,100069,200003,300007,400069,500029,600011,700027,800117,900091,1000133,2000003,3000029,4000037,5000201,6000047,7000061,8000009,9000011,10000103,20000003,30000023,40000123,50000063,60000011,70000037,80000069,90000049,100000049,200000033,300000119,400000043,500000057,600000019,700000001,800000063,900000011,1000000097,2000000011,3000000077,4000000007,5000000497]
Nb_p_gen=[1009,10009,100069,500029,1000133]

def mod_pow(x,e,p):#Calcule (x**e)%p .
    x = x % p
    R = 1
    while e > 0 :
        if (e%2) == 1 :
            R = (R*x) % p
        e = e//2
        x = (x*x) % p 
    return(R)
    
def elements_generateurs(p):
    L = []
    P = list(set(facteurs(p-1)))
    for g in range(1,p):
        b = True
        for l in P:
            if mod_pow(g,(p-1)/l,p) == 1 : #Propriété compliquée à démontrer
                b = False
                break
        if b:
            L = L + [g]  
    return(L)

def est_generateur(g,p):
    P = list(set(facteurs(p-1)))
    b = True
    for l in P:
        if mod_pow(g,(p-1)/l,p) == 1 : #Propriété compliquée à démontrer
            b = False
            break
    return(b)
    
def test_elements_generateurs():
    fichier = open('C:/Users/clement/Desktop/test_generateurs.txt','a')
    for p in Nb_p_gen:
        temps_debut = time.time() #ou (datetime.now()).microsecond
        L = elements_generateurs(p)
        temps_fin = time.time() #ou (datetime.now()).microsecond
        delta = temps_fin - temps_debut
        fichier.write(str(p)+" "+str(delta)+";")
    fichier.close()
    
def intersect_liste_gen(L,p):
    M = []
    n = len(L)
    for i in range(n):
        if est_generateur(L[i],p):
            M = M + [L[i]]
    return(M)
    
def elements_generateurs_liste(L):
    n = len(L)
    M = elements_generateurs(L[0])
    for i in range(1,n):
        M = intersect_liste_gen(M,L[i])
    return(M)
    
def algo_naif(y,g,p):
    k=0
    A=1
    while y != A:
        A=(A*g)%p
        k = k+1
    return(k)   
        
def test_algo_naif(y,g):
    fichier = open('C:/Users/clement/Desktop/test_'+str(y)+'_'+str(g)+'.txt','a')
    for p in Nb_p:
        temps_debut = time.time() #ou (datetime.now()).microsecond
        k = algo_naif(y,g,p)
        temps_fin = time.time() #ou (datetime.now()).microsecond
        delta = temps_fin - temps_debut
        fichier.write(str(p)+" "+str(delta)+";")
    fichier.close()
    
def executer_tests(y,L):
    n = len(L)
    for i in range(n):
        test_algo_naif(y,L[i])
    test_elements_generateurs()
    


#Programmes pas assez performants.  
    
def nul_elements_generateurs(p):
    L = []
    for g in range(1,p):
        A=1
        M=[]
        while not(A in M):
            M = M + [A]
            A = (A*g)%p
        if len(M)==(p-1):
            L = L + [g]
    return(L)

def nul_est_generateur(g,p):
    M = []
    A = 1
    while not(A in M):
            M = M + [A]
            A = (A*g)%p
    return ((len(M)==(p-1),M))
    

#Programme d'internet.    
    
def facteurs(n): #Source : http://python.jpvweb.com/mesrecettespython/doku.php?id=decomposition_en_facteurs_premiers
    """facteurs(n): décomposition d'un nombre entier n en facteurs premiers"""
    F = []
    if n==1:
        return F
    # recherche de tous les facteurs 2 s'il y en a
    while n>=2:
        x,r = divmod(n,2)
        if r!=0:
            break
        F.append(2)
        n = x
    # recherche des facteurs 1er >2
    i=3
    rn = int(n**(1/2))+1
    while i<=n:
        if i>rn:
            F.append(n)
            break
        x,r = divmod(n,i)
        if r==0:
            F.append(i)
            n=x
            rn = int(n**(1/2))+1
        else:
            i += 2
    return F

