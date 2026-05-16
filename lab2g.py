#!/usr/bin/env python3

#Author: Rence Michael Valerio
#Author ID: rmvalerio
#Date Created: 2026/05/15

import sys

timer = 3

if len(sys.argv) > 1 :
    timer = int(sys.argv[1])
    while timer != 0:
        print (timer)
        timer = timer - 1
    print('blast off!')

else:
    while timer != 0:
        print (timer)
        timer = timer - 1
    print('blast off!')