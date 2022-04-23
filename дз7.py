from ctb import place
# грани куба
x = '0123456'
upx = '066'
yx = '066'
for num in x:
  for numup in upx:
    for numy in yx:
      place(num, numup, numy)
y = '0123456'
upy = '0066'
xy = '0606'
for number in y:
  for numberupy in upy:
    for numberxy in xy:
      place(numberxy, numberupy, number)
level = '0123456'
levelx = '0606'
levely = '0066'
for numberlevel in level:
  for numberx in levelx:
    for numbery in levely:
      place(numberx, numberlevel, numbery)

# квадрат
squarex = '3456789'
squarey = '3456789'
for numeric in squarex:
  for num in squarey:
    place(-int(numeric), 0, num)

