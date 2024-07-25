"""
A 
B B 
C C C 
D D D D 
E E E E E 
"""

n=5
alpha = 65
for i in range(n):
    for j in range(i+1):
        print(chr(alpha), end=" ")
    alpha= alpha + 1
    print()

