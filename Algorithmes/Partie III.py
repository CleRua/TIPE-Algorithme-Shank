# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 23:15:02 2015

@author: clement

Partie III
"""
import time


Nb_p=[10009,50069,100069,200003,300007,400069,500029,600011,700027,800117,900091,1000133,2000003,3000029,4000037,5000201,6000047,7000061,8000009,9000011,10000103,20000003,30000023,40000123,50000063,60000011,70000037,80000069,90000049,100000049,200000033,300000119,400000043,500000057,600000019,700000001,800000063,900000011,1000000097,2000000011,3000000077,4000000007,5000000497,6000000089,7000000013,8000000081,9000000307,10000000019]

Nb_p2=[10009,50069,100069,200003,300007,400069,500029,600011,700027,800117,900091,1000133,2000003,3000029,4000037,5000201,6000047,7000061,8000009,9000011,10000103,20000003,30000023,40000123,50000063,60000011,70000037,80000069,90000049,100000049,200000033,300000119,400000043,500000057,600000019,700000001,800000063,900000011,1000000097,2000000011,3000000077,4000000007,5000000497]
Gen_communs = [11,539,8624]

def h_opt(u,l):
    return(int(((u[1]*0.6180339887498949) % 1) * l))
    
def creer_th(l):
    return([[]]*l)
    
def inserer_th(u,T,h):
    l = len(T)
    v_h = h(u,l)
    T[v_h] = T[v_h] + [u]
    
def rechercher_th(u,T,h):
    l = len(T)
    r = (-1)
    for (j,B) in T[h(u,l)]:
        if B == u[1]:
            r = j
            break
    return(r)
    
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
    
def algo_Shank(y,g,p):
    n = int(p**(1/2)) + 1 #1: On choisit n.
    T = creer_th(n)
    A=1
    for i in range(n): #2: Baby-step.
        inserer_th((i,A),T,h_opt)
        A = (A*g) % p
    #En sortie de boucle, A = g**n .
    B = inverse_modulaire(A,p) #3: Algorithme d'Euclide étendu.
    q=0
    C=y
    r = rechercher_th((0,C),T,h_opt)
    while r == (-1): #4: Giant-step.
        C = (C*B) % p
        q = q+1
        r = rechercher_th((0,C),T,h_opt)
    k = n*q + r #5: y*g**(-n*q) = g**r donc y = g**(n*q + r)
    return(k)

def test_algo_Shank(y,g):
    fichier = open('C:/Users/clement/Desktop/test_Shank'+str(y)+'_'+str(g)+'.txt','a')
    for p in Nb_p:
        temps_debut = time.time() #ou (datetime.now()).microsecond
        k = algo_Shank(y,g,p)
        temps_fin = time.time() #ou (datetime.now()).microsecond
        delta = temps_fin - temps_debut
        fichier.write(str(p)+" "+str(delta)+";")
    fichier.close()
    
def executer_tests_Shank(y,L):
    n = len(L)
    for i in range(n):
        test_algo_Shank(y,L[i])
        

        
