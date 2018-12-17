from itertools import combinations 

n = 1000

a = []
final = []
final2 = []
final3 = []
final4 = []
final5 = []
for i in range(0, n):
  a.append(i)

for i in range(2, n+1):
  final.append(list(combinations(a, i)))

for j in final:
  for g in j:
    if (0 in g):
      final2.append(g)

for r in final2:
  holder = r[1]-r[0]
  flip = True
  for t in range(2, len(r)):
    if (r[t]-r[t-1] != holder):
      flip = False
  if (flip == True):
    final3.append(r)
    final4.append(holder)



for h in range (0, len(final3)):
  if ((final3[h][len(final3[h])-1]+final4[h])%(n) in final3[h]):
    final5.append(final3[h])

print(final5)
