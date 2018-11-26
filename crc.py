import zlib
import random
import string
lists = []
N = 4
target = "hell"
read = "a" * N
for i in range(160):
    ss =''.join(random.choice(string.ascii_lowercase) for _ in range(N))
    lists += [ss]

base = []
for ss in lists:
    base += [(ss, zlib.crc32(ss.encode()))]

read_crc = zlib.crc32(read.encode())
target_crc = zlib.crc32(target.encode())
target_crc ^= read_crc

def str2int(ss):
    sum = 0
    for ch in ss:
        sum *= 256
        sum += ord(ch)
    return sum
read_sum = str2int(read)
base2 = [(str2int(ss) ^ read_sum, crc^read_crc) for ss, crc in base]

the_sum = 0
the_crc = target_crc

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

the_sum ^= read_sum
for i in range(N):
    sss += chr((the_sum % 256))
    the_sum //= 256

print(sss[::-1])