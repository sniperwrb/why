# -*- coding: utf-8 -*-
"""
Created now, today

@author: me
"""

import numpy as np

def n():
    consonants=['k','g','s','z','sh','j','d','t','ch','ts','z','h','f','b',
                'n','m','y','r','w']
    cv_avail  =[ 31, 31, 23, 23,   8,  8, 19, 19,   8,   4,  4, 27,  4, 31,
                 31, 31, 21, 31, 16]
    vowels    =['a','i','u','e','o']
    p         =[0, 0,0,0,2,1,2,0,0]
    p=p/np.sum(p)
    r=np.random.choice(len(p),1,p=p)[0]
    pc=np.ones(len(consonants))
    pc=pc/np.sum(pc)
    pv=np.ones(len(vowels))
    pv=pv/np.sum(pv)
    if (r%2==1):
        rv=np.random.choice(len(pv),1,p=pv)[0]
        x=vowels[rv]
    else:
        x=''
    for i in range(1,r,2):
        rc=np.random.choice(len(pc),1,p=pc)[0]
        rv=np.random.choice(len(pv),1,p=pv)[0]
        while (cv_avail[rc]&(2**(len(vowels)-1-rv))==0):
            rc=np.random.choice(len(pc),1,p=pc)[0]
            rv=np.random.choice(len(pv),1,p=pv)[0]
        x=x+consonants[rc]+vowels[rv]
    x=chr(ord(x[0])-32)+x[1:]
    return x


def v(layer=0):
    p1=[2**layer, 1]
    #work,talk
    p2=[2, 1]
    #  vi,vt
    p3=[2, 1]
    #tosb,noto
    p4=[1, 1]
    # adv,noadv
    p1=p1/np.sum(p1)
    r1=np.random.choice(len(p1),1,p=p1)
    p2=p2/np.sum(p2)
    r2=np.random.choice(len(p2),1,p=p2)
    p3=p3/np.sum(p3)
    r3=np.random.choice(len(p3),1,p=p3)
    p4=p4/np.sum(p4)
    r4=np.random.choice(len(p4),1,p=p4)
    if (r1==0)and(r2==0):
        w,p=vi()
    elif (r1==0)and(r2==1):
        w,p=vt()
    elif (r1==1)and(r2==0):
        w,p=vi_that()
    elif (r1==1)and(r2==1):
        w,p=vt_that()
    p=p/np.sum(p)
    r=np.random.choice(len(p),1,p=p)[0]
    x=w[r]
    if (r2==1):
        x=x+' '+n()
    if (r3==1):
        x=x+' '+adv_phrase()
    if (r4==1):
        x=x+' '+adv()
    if (r1==1):
        x=x+' that '+why(layer=layer+1)
    return x

def vi_that():
    w=["said", "indicated", "claimed"]
    p=np.ones(len(w))
    return w,p

def vt_that():
    w=["told"]
    p=np.ones(len(w))
    return w,p

def vi():
    w=["exploded", "died", "disappeared"]
    p=np.ones(len(w))
    return w,p

def vt():
    w=["terminated", "killed", "ate"]
    p=np.ones(len(w))
    return w,p


def adv():
    w=["quickly", "slowly", "happily", "angrily"]
    p=np.ones(len(w))
    p=p/np.sum(p)
    r=np.random.choice(len(p),1,p=p)[0]
    x=w[r]
    return x

def adv_phrase():
    x=prep()+' '+n()
    return x

def prep():
    w=["to", "from", "with", "at", "on", "in", "behind", "under"]
    p=np.ones(len(w))
    p=p/np.sum(p)
    r=np.random.choice(len(p),1,p=p)[0]
    x=w[r]
    return x


def why(layer=0):
    x=n()+' '+v(layer)
    return x

if __name__=="__main__":
    print(why())
