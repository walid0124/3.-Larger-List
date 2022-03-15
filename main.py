L1=[4,10,2,5]
L2=[-10,2,5,10]
N=1
fir= (L1[-N:])
sec= (L2[-N:])
if fir >= sec:
   print ("The last element of the list is : " + str(fir))
else:
   print ("The last element of the list is : " + str(sec))
