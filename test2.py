#!/usr/bin/env python3
# -*- coding:Utf-8 -*-

from random import randint
entiers=[]
i=0
while len(entiers)<25 :
	entier = randint(1,100)
	if entier not in entiers:
		entiers.append (entier)
	i=i+1
entiers.sort()
print (i, entiers)
