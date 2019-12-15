from Bio import SeqIO
from pip._vendor.distlib.compat import raw_input
k=int(raw_input("Enter K_mar Size:"))  # insert k_mar size
seq_Db={}   # Dictionary for saving k_mars readed from fasta file
seq=0
for seq_record  in SeqIO.parse("Dseq.fa", "fasta"): # reading fasta file
    seq_id =(str(seq_record.id))
    my_seq=(seq_record.seq)
    L = 0
    R = k
    seq+=1
    pos = 0
    seq_Db[seq,pos]={str(seq_record.id)} #saving seq id in dic at (n,0) key
    for i in range(len(my_seq)-k-1):
        k_mar=(str(my_seq[L:R]))
        L+=1
        R+=1
        pos += 1
        seq_Db[(seq,pos)]={k_mar} #saving data in dic as (seq id , position ) = K_mar

fieldnames=["Seq_id","position","k_mar"]
w = open("K_mar%i.txt" %k, "w+")
w.write("SEQ_ID\tPOS\tK_mar\n")
for key,val in seq_Db.items(): # read values from dic to save in file
    if key[1] == 0:
        val = str(val)
        w.write('%s\t%s\t%s\n' % (key[0],key[1], val[2:-2]))
    else:
        val=str(val)
        w.write('%s\t%s\t%s\n'%(key[0],key[1],val[2:(k+2)]))
w.close()