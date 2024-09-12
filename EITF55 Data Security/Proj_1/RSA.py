#phi(n) (p-1)*(q-1) N=p*q e är ett värde jag sätter 
from Euclidean import Euclidean
import random

def getPQ(fileName):
    with open(fileName, 'r') as file:
        p = int(file.readline().strip('\n'))
        q = int(file.readline().strip('\n'))
    return p, q

s2 = 71274583086677085595510589319132870058776443580937815122335718895734813207215482506115152447009359489878226256921097433310910048198805359542948532277123872879363057858578340491840823636248581466510568848779316864003323268400771736852770242143572115673507302374431916973825729951516785561692076125912983421167
#file_name = "512_2.txt"
ec = Euclidean()
p = 11143076682725028852778344581329990554374768844307130664795171165666977116065951289807531452265140419747245808652641484171803380793398396497650288897105129
q = 12949289789084083120792060577048528169964383029590469110076698871712278201961641489685698436589896059237056280725324047804836993084407957030872193327939861
N = p*q
phiN = (p-1) * (q-1)
e = pow(2, 16) + 1
d = ec.findD(e, phiN)
s = random.randrange(2, N - 1)

c = pow(s2, e, N)
z = pow(c, d, N)

print("Value for s: ", s2)
print("Value for c: ", c)
print("Value for z: ", z)

print(s2== z)