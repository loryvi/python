from itertools import combinations
count =0
for p in combinations("abcdefgh",2):
    print("".join(p))
    count = count +1
print(count)


"""
formula for combination = meaning theres no repetitive element
where n is the number of elements 
== (n(n-1))/ 2
8 x 7 =56 / 2
= 28
"""
ab   ac  ad  ae  af  ag  ah   #notice that there will no be "ba" because it is the same as "ab"
bc  bd  be  bf  bg  bh
cd  ce  cf  cg  ch
de  df  dg  dh
ef  eg  eh
fg  fh
gh
28

"""
if we did permutation
from itertools import permutations
count =0
for p in permutations("abcdefgh",2):
    print("".join(p))
    count = count +1
print(count)
    it will count that there are 56 ways to randomize by 2 characters the 8 characters. 
    where n(n-1)
"""
ab  ac  ad  ae  af  ag  ah 
ba  bc  bd  be  bf  bg  bh
ca  cb  cd  ce  cf  cg  ch
da  db  dc  de  df  dg  dh
ea  eb  ec  ed  ef  eg  eh
fa  fb  fc  fd  fe  fg  fh
ga  gb  gc  gd  ge  gf  gh
ha  hb  hc  hd  he  hf  hg
56
"""
