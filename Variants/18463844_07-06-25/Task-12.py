mini = 1_000_000
for c1 in range(0,30):
  for c2 in range(0,30):
    for c3 in range(0,30):
        for c4 in range(0,30):
          if (c1*0 + c2*1 + c3*0 + c4*2 == 40 and c1*1 + c2*0 + c3*2 + c4*0 > 50 and 2*c1 + c3 == 2*c2 + c4):
              if (c1*1 + c2*0 + c3*2 + c4*0) < mini:
                  mini = c1*1 + c2*0 + c3*2 + c4*0
print(mini)