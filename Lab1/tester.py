from Record import Record
from FCFS import executeFCFS
from SJF import  executeSJF
from SRTF import executeSRTF
from RR import executeRR
import copy


t1 = Record(1, 10)
t1.setAT(0)

# print(t1)
# print("-----")
t2 = Record(2, 14, 1)
t3 = Record(3, 2, 2)
t4 = Record(4, 7, 3)
t5 = Record(5, 4, 4)
t6 = Record(6, 9, 5)
t7 = Record(7, 1, 6)

l = [t1, t2, t3, t4, t5, t6, t7]

print(*l, sep='\n')

k = copy.deepcopy(l)
executeFCFS(k)
print(*k, sep='\n')

j = copy.deepcopy(l)
executeSJF(j)
print(*j, sep='\n')

h = copy.deepcopy(l)
executeSRTF(h)
print(*h, sep='\n')


