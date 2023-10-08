# Algoday Workshop 8/10/2023
# Σεμινάριο Προετοιμασίας για IEEEXtreme17.0 και GR-CPC
# "Επίλυση Προβλημάτων Δυναμικού Προγραμματισμού με Python" (Κυριάκος Σγάρμπας)
#
# Fibonacci sequence
# F(0) = 0, F(1) = 1
# F(n) = F(n−1) + F(n−2), for n > 1.
#
# Pos: 0  1  2  3  4  5  6   7   8   9  10  11   12
# Val: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
    
def fib1(n):
    if n==0: return 0
    if n==1: return 1
    return fib1(n-1) + fib1(n-2)
##fib1(12)
##144
##fib1(60)
##..........

def fib2(n):
    if n==0: return 0
    if n==1: return 1
    a,b = 0,1
    for i in range(1,n):
        #c,a,b = a+b, b, c    #(τεστ1: βρείτε το bug)
        c = a+b
        a = b
        b = c
    return c 
##fib2(12)
##144
##fib2(60)
##1548008755920

d = {0:0, 1:1}
def fib3(n):
    #global d    # (τεστ2: χρειάζεται;)
    try: return d[n]
    except:
        z = fib3(n-1) + fib3(n-2)
        d[n] = z
        return z
##fib3(60)
##1548008755920

from functools import cache
@cache
def fib4(n):
    if n==0: return 0
    if n==1: return 1
    return fib4(n-1) + fib4(n-2)
##fib4(60)
##1548008755920

# Άλλο παράδειγμα: Απόσταση Levenshtein (βλ.διαφάνειες)
@cache
def Lev(S,T):
    if S=="": return len(T)
    if T=="": return len(S)
    p1 = Lev(S,T[:-1])+1
    p2 = Lev(S[:-1],T)+1
    p3 = Lev(S[:-1],T[:-1])
    if S[-1] != T[-1]: p3+=1
    return min(p1,p2,p3)
##Lev("gaagctggctaatgtacggatagctag","atgcgagttaactttasgatcgaggaattac")
##16

# -------------------------------------------------
# Απαντήσεις:
# τεστ1: 
# Χρειάζεται να προστεθεί και η αρχική συνθήκη: a,b,c = 0,1,1
# όμως το bug βρίσκεται εδώ: c,a,b = a+b, b, a+b
# H σειρά δεν έχει σημασία, πχ. a,b,c = b, a+b, a+b
#
# τεστ2:
# Όχι, γιατί τα dictionaries είναι mutable. Έτσι μπορούμε και να αλλάξουμε τα
# περιεχόμενα του d μέσα από τη συνάρτηση, όχι μόνο να τα διαβάσουμε.
