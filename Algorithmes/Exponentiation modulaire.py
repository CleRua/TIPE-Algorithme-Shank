# -*- coding: utf-8 -*-
"""
Created on Thu May 21 19:13:08 2015

@author: clement

Exponentiation modulaire
"""

"""
De nombreuses fois les puissances calculées en cryptographies forment
des nombres très grands qui occupent trop de place en mémoire.
Cependant on peut tirer profit du fait qu'on travaille sur des groupes cycliques.
Ainsi, l'exponentiation modulaire vise a calculer (a**b)%c sans calculer 
directement a**b qui serait un nombre trop grand.
"""

def mod_pow(x,e,p):#Calcule (x**e)%p .
    x = x % p
    R = 1
    while e > 0 :
        if (e%2) == 1 :
            R = (R*x) % p
        e = e//2
        x = (x*x) % p 
    return(R)