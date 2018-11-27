lists = []
N = 8
target = "hellfuck"
base = []
ff = open("hash.txt")
for line in ff.read().splitlines():
    sp = line.split(" ")
    crc = sp[0]
    ss = " ".join(sp[1:])
    if len(ss) != 8: 
        print("!!!!!!!", len(ss))
    crc = int(crc, 16)
    # print(crc, ' -> ' , ss)
    base += [(ss, crc)]

# target_crc = zlib.crc32(target.encode())
# exit()

def str2int(ss):
    sum = 0
    for ch in ss:
        sum *= 256
        sum += ord(ch)
    return sum
base2 = [(str2int(ss), crc) for ss, crc in base]

the_sum = 0
the_crc = 0x09209ac5b5e2365e

lists = base2.copy()
while the_crc != 0:
    ss = None
    cc = None
    for sum, crc in lists:
        if crc % 2 == 1:
            # print(sum, crc)
            ss = sum
            cc = crc

    newlists = []
    for sum, crc in lists:
        if crc % 2 == 1:
            sum ^= ss
            crc ^= cc
        crc >>= 1
        if crc != 0:
            newlists += [(sum, crc)]
        elif sum != 0:
            pass
            # print(sum)
            # print("-------")
    lists = newlists.copy()
    if the_crc % 2 == 1:
        if cc == None:
            print("fuck!!")
        the_sum ^= ss
        the_crc ^= cc
    the_crc >>= 1
sss = ''

for i in range(N):
    sss += chr((the_sum % 256))
    the_sum //= 256

print(sss[::-1])