#!/usr/bin/env python
# Copyright 2018 Masato Yoshimura all rights reserved 
import os
import sys
from string import *
from operator import itemgetter, attrgetter
import gzip 
INTRACTIVE = False



if __name__ == '__main__':
   
   if len(sys.argv) == 1:
     INTRACTIVE = True
   elif len(sys.argv) == 4:
     a_inp,b_inp,c_inp = map(float,sys.argv[1:4])
   elif len(sys.argv) == 5: 
     a_inp,b_inp,c_inp = map(float,sys.argv[2:5])
   else:
     print "Usage "
     print "Prepare gzipped data base named sorteddb.gz"
     print "Input cell sizes a and b and c in Angstrom like  "
     print "./cellsize_pdb.py --input 76. 76 30.555 "
     print "Or just type command  "
     print "./cellsize_pdb.py "
     quit()

   if not INTRACTIVE: print " a = %8.3f"%a_inp," b = %8.3f"%b_inp," c = %8.3f"%c_inp
   file=gzip.open("./sorteddb.gz","r")
   print "reading data...."
   line=" "
   db=[]
   while line :     
     line=file.readline()
     strs=line.split()
     if len(strs) > 3:
        a = float(strs[1])
        b = float(strs[2])
        c = float(strs[3])
        al = float(strs[4])
        be = float(strs[5])
        ga = float(strs[6])
        item = (a,b,c,line)
        db.append(item)
   file.close()
   dbsize=len(db)

   if INTRACTIVE : a_inp=float(raw_input('a = ?  '))
   ja = 0
   while db[ja][0] < a_inp:
     ja += 1
   prev_d_a,next_d_a = abs(db[ja-1][0]-a_inp),abs(db[ja][0]-a_inp)
   if prev_d_a < next_d_a :
      ja =  ja - 1
   ja_cen=ja
   if INTRACTIVE :    print "nearest cell size is "
   if INTRACTIVE :    print db[ja_cen][3],
   low_a_inp,high_a_inp = 0.95*a_inp,1.05*a_inp # +-5% region of input a
   low_ja = ja - 500 if ja > 500 else 0;      # +-500 region of input a
   high_ja = ja + 500 if ja + 500 < dbsize else dbsize-1; 
   if db[low_ja][0] < low_a_inp: # compare 5% and 500, choose broader criteria 
       low_ja2 = low_ja
   else:
       ja = 0
       while db[ja][0] < low_a_inp:
         ja += 1
       low_ja2 = ja-1

   if db[high_ja][0] < high_a_inp: # compare 5% and 500, choose broader  
       ja = ja_cen
       while db[ja][0] < high_a_inp:
         ja += 1
       high_ja2 = ja-1
   else:
       high_ja2 = high_ja

   newdb = db[low_ja2:high_ja2]
#   print "extracted region N = ",len(newdb),"     lower and higher"
#   print newdb[0][3],
#   print newdb[-1][3],
   if INTRACTIVE : b_inp=float(raw_input('b = ?  '))
   newdbr=[]
   for a,b,c,line in newdb:
     r = ( (a-a_inp)**2 + (b-b_inp)**2 )**0.5
     newdbr.append((a,b,c,line,r))
   sortdbr=sorted(newdbr,key=itemgetter(4))
   
   if INTRACTIVE: print "nearest cell size from db"
   if INTRACTIVE: print sortdbr[0][3]

   sortdbr2 = filter(lambda x: x[4]<30,sortdbr)
   #print "extracted to N = ",len(sortdbr2)

   newdbfinal=[]
   if INTRACTIVE: c_inp=float(raw_input('c = ?  '))
   for a,b,c,line,r in sortdbr2:
     r = ( (a-a_inp)**2 + (b-b_inp)**2 + (c-c_inp)**2 )**0.5
     newdbfinal.append((a,b,c,line,r))
   sortdbfinal=sorted(newdbfinal,key=itemgetter(4))

   print ""
   sys.stdout.flush()
   print "===================================================================="

   cellmin=min(a_inp,b_inp,c_inp)
   r_min = sortdbfinal[0][4]

   if r_min < cellmin*0.03: # shortest_cell 3%
     print "it must be " 
   elif cellmin*0.03 < r_min < cellmin*0.1 :  # shortest_cell 3% to 20%
     print "it may be "
   else:
     print "the nearest is "
   print "diff. distance = %8.2f"%sortdbfinal[0][4]
   print  sortdbfinal[0][3]
   print "--------------------------------------------------------------------"
   print "the other nearest cell sizes "
   for itemp,temp in enumerate( sortdbfinal[1:] ):
     print "diff. distance = %8.2f"%temp[4] 
     print temp[3]
     if temp[4] > cellmin*0.25 or itemp >= 10:  # list up 10 or  25%
        break
