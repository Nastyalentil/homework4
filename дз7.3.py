# круг
from ctb import place

x = '10', '-10'
up = '-1','0','1'
for num in x:
  for numup in up:
    place(num, numup, 0)
x1 = '9','-9'
up1 = '2','3','4','-4','-3','-2'
for numx1 in x1:
  for numup1 in up1:
    place(numx1, numup1, 0)
x2 = '8','-8'
up2 = '5','6','-6','-5'
for numx2 in x2:
  for numup2 in up2:
    place(numx2, numup2, 0)
x3 = '7','-7'
up3 = '6','7','-7','-6'
for numx3 in x3:
  for numup3 in up3:
    place(numx3, numup3, 0)
x4 = '6','-6'
up4 = '7','8','-8','-7'
for numx4 in x4:
  for numup4 in up4:
    place(numx4, numup4, 0)
x5 = '5','-5'
up5 = '8','-8'
for numx5 in x5:
  for numup5 in up5:
    place(numx5, numup5, 0)
x6 = '4','3','2','-2','-3','-4'
up6 = '9','-9'
for numx6 in x6:
  for numup6 in up6:
    place(numx6, numup6, 0)
x7 = '1','0','-1'
up7 = '10','-10'
for numx7 in x7:
  for numup7 in up7:
    place(numx7, numup7, 0)

