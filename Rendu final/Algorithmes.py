"""
TIPE : Attaque du système de cryptage d'El Gamal.
"""
#PARTIE I

#Recherche d'une liste de nombre premiers possédant des générateurs communs.

def mod_pow(x,e,p):
    """Calcule (x**e)%p par exponentiation modulaire rapide."""
    x = x % p
    R = 1
    while e > 0 :
        if (e%2) == 1 :
            R = (R*x) % p
        e = e//2
        x = (x*x) % p 
    return(R)

def est_generateur(g,p):
    """Renvoie True si g est générateur de (Z/pZ)* et False sinon."""
    P = list(set(facteurs(p-1))) #facteurs(p-1) renvoit la liste des diviseurs premiers de (p-1).
    b = True
    for l in P:
        if mod_pow(g,(p-1)/l,p) == 1 : #Un générateur de vérifie pas cette propriété.
            b = False
            break
    return(b)
    
def elements_generateurs(p):
    """Donne la liste des éléments générateurs de (Z/pZ)*."""
    L = []
    P = list(set(facteurs(p-1))) 
    for g in range(1,p):
        b = True
        for l in P:
            if mod_pow(g,(p-1)/l,p) == 1 :
                b = False
                break
        if b:
            L = L + [g]  
    return(L)
    
def intersect_liste_gen(L,p):
    """Renvoie la liste des éléments de L qui sont générateurs de (Z/pZ)*."""
    M = []
    n = len(L)
    for i in range(n):
        if est_generateur(L[i],p):
            M = M + [L[i]]
    return(M)
    
def elements_generateurs_liste(L):
    """Renvoie la liste des éléments générateurs communs aux nombres premiers dans L."""
    n = len(L)
    M = elements_generateurs(L[0])
    for i in range(1,n):
        M = intersect_liste_gen(M,L[i])
    return(M)
    
#Liste de nombres premiers et leurs générateurs communs.

Nombres_premiers = [10009,50069,100069,200003,300007,400069,500029,600011,700027,800117,900091,1000133,2000003,3000029,4000037,5000201,6000047,7000061,8000009,9000011,10000103,20000003,30000023,40000123,50000063,60000011,70000037,80000069,90000049,100000049,200000033,300000119,400000043,500000057,600000019,700000001,800000063,900000011,1000000097,2000000011,3000000077,4000000007,5000000497,6000000089,7000000013,8000000081,9000000307,10000000019]
Generateurs_communs = [11,539,8624]
    
#Algorithme naïf.
    
def algo_naif(y,g,p):
    "Algorithme naïf de résolution du logarithme discret."""
    k=0
    A=1
    while y != A:
        A=(A*g)%p
        k = k+1
    return(k)
    
    
#PARTIE II
    
#Tables de hachage.
    
def creer_th(l):
    """Crée une table de hachage de taille l."""
    return([[]]*l)
    
def inserer_th(u,T,h):
    """Insère l'élément u dans la table T à l'aide de la fonction h."""
    l = len(T)
    v_h = h(u,l)
    T[v_h] = T[v_h] + [u]
    
def rechercher_th(u,T,h):
    """Recherche l'élément u dans la table T à l'aide de la fonction h. Renvoie (-1) si u n'est pas dans la table et r>=0 sinon."""
    l = len(T)
    r = (-1)
    for (j,B) in T[h(u,l)]:
        if B == u[1]:
            r = j
            break
    return(r)
    
def h_teta(u,teta,l):
    """Fonction de hachage avec teta en paramètres."""
    return(int(((u*teta) % 1) * l))
    
def h_opt(u,l):
    """Fonction de hachage théoriquement optimale."""
    return(int(((u*0.6180339887498949) % 1) * l)) #((5**(1/2))-1)/2 = 0.6180339887498949
    
    
#PARTIE III
    
#Algorithme étendu d'Euclide et inverse modulaire.
    
def algo_Euclide_etendu(a,b): 
    """Renvoie (r,u,v) tels que r = PGCD(a,b) et a*u + b*v = r ."""
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
    """Renvoie l'élément a**(-1) dans (Z/pZ)*."""
    (r,u,v) = algo_Euclide_etendu(a,p)
    #Si r=1, a*u + v*p = 1 donc a*u = 1 mod p. Donc u = a**(-1).
    while u<0:
        u = (u+p)%p
    return(u)
    
#Algorithme de Shank.
    
def algo_Shank(y,g,p):
    """Resout le logarithme discret avec la méthode de Shank."""
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
    k = n*q + r #5: y = g**(n*q + r)
    return(k)
    
#Affichage table de hachage.
    
import matplotlib.pyplot as plt
    
def couleur_case(n):
    """Donne la couleur correspondant au nombre n d'éléments dans l'alvéole."""
    if n==1:
        return('green')
    if n==2:
        return('blue')
    if n==3:
        return('red')
    else:
        return('black')
    

def afficher_th(T):
    """Affichage graphique de la table de hachage."""
    l = len(T)
    N = int((l-1)**(1/2))
    for i in range(l):
        n = len(T[i])
        x = i % N
        y = i // N
        #plt.plot([x,x+1,x+1,x],[y,y,y+1,y+1],'r')
        if n!=0:
            plt.fill([x,x+1,x+1,x],[N-y,N-y,N-y-1,N-y-1],couleur_case(n))
    plt.show()

#ANNEXE

#Algorithmes de test.

import time
import numpy as np
from random import random

def test_algo_naif(y,g):
    fichier = open('test_algo_naif_'+str(y)+'_'+str(g)+'.txt','a')
    for p in Nombres_premiers:
        temps_debut = time.time() 
        k = algo_naif(y,g,p)
        temps_fin = time.time() 
        delta = temps_fin - temps_debut
        fichier.write(str(p)+" "+str(delta)+";")
    fichier.close()
    
def test_h_teta(l,N,p):
    fichier = open('test_h_teta_'+str(l)+'_'+str(p)+'.txt','a')
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
    
def test_algo_Shank(y,g):
    fichier = open('test_algo_Shank_'+str(y)+'_'+str(g)+'.txt','a')
    for p in Nombres_premiers:
        temps_debut = time.time()
        k = algo_Shank(y,g,p)
        temps_fin = time.time()
        delta = temps_fin - temps_debut
        fichier.write(str(p)+" "+str(delta)+";")
    fichier.close()
    
#Algorithme de décomposition en facteurs premiers.
#Auteur :  "tyrtamos".
#Source : http://python.jpvweb.com/mesrecettespython/doku.php?id=decomposition_en_facteurs_premiers
    
def facteurs(n): 
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