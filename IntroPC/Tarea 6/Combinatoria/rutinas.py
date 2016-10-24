#! /usr/bin/env python

def factorial(n):
     factorial=1
     i=n
     while i>=1:
          factorial=factorial*i
          i-=1
     return factorial

def combinatoria(L,P):

     fac1=factorial(L)
     fac2=factorial((L-P))
     aux=fac1/fac2
     return aux
