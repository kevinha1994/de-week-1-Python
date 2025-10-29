a = "1"
b = "1"

a_dez = 0
b_dez = 0
for i in range(len(a)):
    a_dez = a_dez + int(a[i]) * 2**(len(a)-i-1)
for i in range(len(b)):
    b_dez = b_dez + int(b[i]) * 2**(len(b)-i-1)
c_dez = a_dez + b_dez
if c_dez != 0:
    c = ""
    x = c_dez
    while x>=2:
        c = c + str(x%2)
        x = x//2
    if x == 1:
        c = c + "1"
    c = c[::-1]
else:
    c = "0"

print(c)

