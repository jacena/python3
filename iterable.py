from collections import Iterable
l = isinstance('abc',Iterable)
print(l)

L=list(range(1,11))
print(L)

L2 = [x * x for x in range(1,20)]
print(L2)

L3 = [m + n for m in 'abc' for n in 'hkl']
print(L3)

import os
L4 = [d for d in os.listdir('.')]
print('all dir',L4)

L5 = ['Hello','World',18,'Apple',None]
L6 = [s.lower() for s in L5 if isinstance(s,str)]
print(L6)


L7 = ['Hello','World',18,'Apple',None]
L8 = [s.lower() if isinstance(s,str) else s for s in L7]
print(L8)









