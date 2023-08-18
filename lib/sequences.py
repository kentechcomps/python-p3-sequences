#!/usr/bin/env python3

def print_fibonacci(length):
 if length<= 0 :
   return []
 elif length == 1 :
   return [0]
 elif length == 2:
   return [0 , 1]
 else :
   seq = [0 , 1]
   for i in range (2 , length):
     next_num = seq[i -1] + seq[i-2]
     seq.append(next_num)
 print(seq)
   