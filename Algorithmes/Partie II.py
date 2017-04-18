# -*- coding: utf-8 -*-
"""
Created on Wed May 27 22:39:40 2015

@author: clement

Partie II
"""
from random import random
import numpy as np

def creer_th(l):
    return([[]]*l)
    
def inserer_th(u,T,h):
    T[h(u)].append(u)

def rechercher_th(u,T,h):
    return(u in T[h(u)])
    
def h_opt(u,l):
    return(int(((u*0.6180339887498949) % 1) * l)) #((5**(1/2))-1)/2 = 0.6180339887498949
    

    
#Test de h_teta sans resultat concluant ...
    
def h_teta(u,teta,l):
    return(int(((u*teta) % 1) * l))
    
def test_h_teta(l,N,p):
    fichier = open('C:/Users/clement/Desktop/test_h_teta_'+str(l)+'_'+str(p)+'.txt','a')
    L = np.linspace(0,1,111)
    for teta in L:
        S = 0 #S -> Variable qui compte le nombre de collisions.
        T = [True]*l #T[i] = True -> la case est vide. T[i] = False -> la case n'est pas vide.
        for i in range(N):
            u = int(random() * p)
            s = h_teta(u,0.6180339887498949,l)
            if T[s]:
                T[s] = False
            else:
                S = S + 1
        fichier.write(str(teta)+" "+str(S)+";")
    fichier.close()