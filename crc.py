import zlib
import random
import string
lists = []
N = 9
target = "hellofuck"
read = "a" * N
for i in range(160):
    ss =''.join(random.choice(string.ascii_lowercase) for _ in range(N))
    lists += [ss]

base = []
for ss in lists:
    base += [(ss, zlib.crc32(ss.encode()))]

read_crc = zlib.crc32(read.encode())
target_crc = zlib.crc32(target.encode())
target_crc = target_crc ^ read_crc

def fuck(ss):
    sum = 0
    for ch in ss:
        sum *= 256
        sum += ord(ch)
    return sum
read_sum = fuck(read)
base2 = [(fuck(ss) ^ read_sum, crc^read_crc) for ss, crc in base]

# the_sum, the_crc = fuck(target, target_crc)
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
            sum = sum ^ ss
            crc = crc ^ cc
        crc = crc >> 1
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
        the_sum = the_sum ^ ss
        the_crc = the_crc ^ cc
    the_crc = the_crc >> 1
sss = ''

the_sum = the_sum ^ read_sum
for i in range(N):
    sss += chr((the_sum % 256))
    the_sum = the_sum // 256

print(sss[::-1])