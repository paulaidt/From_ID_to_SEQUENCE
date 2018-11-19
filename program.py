import sys
import re
db=sys.argv[1]
file=sys.argv[2]

class Seq:
    def __init__(self):
        self.id="x"
    def __init__(self):
        self.seq="y"
    def __init__(self):
        self.features="z"
        
def readseq (fname):
    seqlist={}
    record=[]
    nrec=-1
    inseq=0
    with open(fname) as f:
      for line in f:
        if re.match ( r'^>', line):
            nrec+=1
            record.append(Seq())
            mobj=re.match ( r'^>(\S*)\s*(.*)', line)

            if (mobj):
                record[nrec].id=mobj.group(1)
                record[nrec].features=mobj.group(2)
            inseq=0
        else :
            if inseq==0 :
                inseq=1
                record[nrec].seq=line
            else:
                cstring=record[nrec].seq+line
                record[nrec].seq=cstring
                
    seqlist={}       
    for x in range (0,nrec+1):
        record[x].seq=re.sub (r'[ \n\t\r]',"",record[x].seq)
        seqlist[record[x].id]=record[x].seq

    return seqlist 
    
db=readseq(db)


c=0
l=[]
with open(file) as f:
	while c<20:
		l.append(f.readline().split('	')[1])
		c+=1

d={}
for x in l:
		for i in db.keys():
			if x==i:
				d[x]=db[i]
				
for x in l:
	print('>', end='')
	print(x)
	print(d[x])
