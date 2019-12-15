from Bio import SeqIO
from pip._vendor.distlib.compat import raw_input
k=int(raw_input("Enter K_mar Size:"))
seq_qy={}
seq=0
for seq_record  in SeqIO.parse("user_seq.fa", "fasta"):
    seq_id =(str(seq_record.id))
    my_seq=(seq_record.seq)
    L = 0
    R = k
    seq+=1
    pos = 0
    seq_qy[seq,pos]={str(seq_record.id)}

    for i in range(len(my_seq)-k-1):
        k_mar=(str(my_seq[L:R]))
        L+=1
        R+=1
        pos += 1
        seq_qy[(seq,pos)]={k_mar}

w = open("Q_seq.txt", "w+")
w.write("SEQ_ID\tPOS\tK_mar\n")
for key, val in seq_qy.items():
    if key[1] == 0:
        val = str(val)
        w.write('%s\t%s\t%s\n' % (key[0],key[1], val[2:-2]))
    else:
        val=str(val)
        w.write('%s\t%s\t%s\n'%(key[0],key[1],val[2:(k+2)]))
w.close()
Database={}
Q_seq={}
count = len(open("K_mar%i.txt"%k).readlines(  ))
r=open("K_mar%i.txt"%k,"r+")
r.seek(0)
k_mar=r.readline()
for i in range(count-1):
    k_mar=str(r.readline()).split()
    Database[(k_mar[0],k_mar[1])]={k_mar[2]}
r.close()

count = len(open("Q_seq.txt").readlines(  ))
r=open("Q_seq.txt","r+")
r.seek(0)
k_mar=r.readline()
for i in range(count-1):
    k_mar=str(r.readline()).split()
    Q_seq[(k_mar[0],k_mar[1])]={k_mar[2]}
r.close()
# result file to save Marching K_mars data
result=open("Result.txt","w+")
result.write("Query Seq_ID\t\t\tQ Start\t\tQ End\t\t Databse Seq_ID\t\t\tD start\t\t D end\n")
for q_key,q_val in Q_seq.items():
    details=str(q_val)

    if (int(q_key[1]) == 0):
        User_ID=details[2:-2]
        print(User_ID)
        continue
    for d_key,d_val in Database.items():
        details = str(d_val)

        if(int(d_key[1])==0):
            Database_ID=details[2:-2]
            continue
        print(([d_val, q_val]))
        if(q_val==d_val):
            result.write('%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\n' % (User_ID,q_key[1],(k),Database_ID,d_key[1],(k)))






