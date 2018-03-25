# cellsize_pdb
On Linux machine,

Check the existence the database file named sorteddb.gz on the same directory.

Add right of execution to the program

chmod u+x ./cellsize_pdb.py 

Run program
./cellsize_pdb.py

The example of running on Mac is shown below.
-----------------------------------
yoshimurMBk-Air:testpy yoshimur$ ls

  cellsize_pdb.py	sorteddb.gz

yoshimurMBk-Air:testpy yoshimur$ chmod u+x cellsize_pdb.py 

yoshimurMBk-Air:testpy yoshimur$ ./cellsize_pdb.py 

reading data....

a = ?  135 

nearest cell size is  

CRYST1  135.000   37.100   38.500  90.00  92.60  90.00 C 1 2 1       4          1jlm I-DOMAIN FROM INTEGRIN CR3, MN2+ BOUND

b = ?  261 

nearest cell size from db 

CRYST1  135.415  260.694  148.691  90.00 100.94  90.00 P 1 21 1     28          1mnf DOMAIN MOTIONS IN GROEL UPON BINDING OF AN OLIGOPEPTIDE 

c = ?  275 
 
==================================================================== 

it may be 
diff. distance =     6.02 

CRYST1  135.619  259.710  280.848  90.00  90.00  90.00 P 21 21 21   56          4wgl A GROEL D83A/R197A DOUBLE MUTANT

--------------------------------------------------------------------
the other nearest cell sizes 
diff. distance =     7.43 

CRYST1  136.240  261.830  282.280  90.00  90.00  90.00 P 21 21 21   56          4hel STRUCTURE ANALYSIS OF APO-GROEL STRUCTURE
 
diff. distance =     8.08 

CRYST1  130.690  260.300  281.800  90.00  90.00  90.00 P 21 21 21   16          4acq ALPHA-2 MACROGLOBULIN
 
diff. distance =    12.89 

CRYST1  135.676  260.954  287.872  90.00  90.00  90.00 P 21 21 21   56          3e76 WILD-TYPE GROEL WITH BOUND THALLIUM IONS
 
diff. distance =    70.19 

CRYST1  138.500  240.860  207.850  90.00  90.00  90.00 C 2 2 21     48          4lnk B. SUBTILIS GLUTAMINE SYNTHETASE STRUCTURES REVEAL LARGE ACTIVE SITE2 CONFORMATIONAL CHANGES AND BASIS FOR ISOENZYME SPECIFIC REGULATION:3 GS-GLUTAMATE-AMPPCP COMPLEX




---------------------------------------------------------------------------
# sorteddb.gz
The file is small database extracted from PDBj in 2017 Autumn.

From the pdb files, CRYST line and TITLE line were extracted and gattherd into one file.
Then, it was sorted by cell size and from small to large  in order c , b and a.
Finaly it was gzipped in Linux PC.

 