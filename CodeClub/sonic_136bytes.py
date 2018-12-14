def sonic_how_many_rings_did_you_get(s):
 r=0
 for c in s:
  if'abdepqoDOPQR0469'.count(c):r+=1
  if'gB8'.count(c):r+=2
 return r
