import hashlib
from arc4 import ARC4
import base64
from pwn import * 
s = "TdQdBRa1nxGU06dbB27E7SQ7TJ2+cd7zstLXRQcLbmh2nTvDm1p5IfT/Cu0JxShk6tHQBRWwPlo9zA1dISfslkLgGDs41WK12ibWIflqLE4Yq3OYIEnLNjwVHrjL2U4Lu3ms+HQc4nfMWXPgcOHb4fhokk93/AJd5GTuC5z+4YsmgRh1Z90yinLBKB+fmGUyagT6gon/KHmJdvAOQ8nAnl8K/0XG+8zYQbZRwgY6tHvvpfyn9OXCyuct5/cOi8KWgALvVHQWafrp8qB/JtT+t5zmnezQlp3zPL4sj2CJfcUTK5copbZCyHexVD4jJN+LezJEtrDXP1DJNg=="

s1 = "F1KFlZbNGuKQxrTD/ORwudM8S8kKiL5F906YlR8TKd8XrKPeDYZ0HouiBamyQf9/Ns7u3C2UEMLoCA0B8EuZp1FpwnedVjPSdZFjkieYqWzKA7up+LYe9B4dmAUM2lYkmBSqPJYT6nEg27n3X656MMOxNIHt0HsOD0d+"

h_k = 0

def utf(kr):
    data = []
    kr_u = 0
    i = 0
    for k in kr:
        if(i == 0):
            kr_u = (kr_u + ord(k)) << 8
            i = i + 1
        else:
            kr_u = ((kr_u << 8) + ord(k)) << 8
    key = kr_u.to_bytes(64,"big")
    return key



def conv(i,j,k,l,m):
    key = 0x46004f003900
    key = ((key << 8) + i) << 8
    key = ((key << 8) + j) << 8
    key = ((key << 8) + k) << 8
    key = ((key << 8) + l) << 8
    key = ((key << 8) + m) << 8
    return key 

cipher = 0x610068006F007900
cipher = cipher.to_bytes(8,"big")
plant1 = b'ydN8BXq16RE='


for i in range(0x30,0x3A,1):
    for j in range(0x30,0x3A,1):
        for k in range(0x30,0x3A,1):
            for l in range(0x30,0x3A,1):
                for m in range(0x30,0x3A,1):
                    key = conv(i,j,k,l,m)
                    key = key.to_bytes(16,"big")
                    r = hashlib.md5(key)
                    key_rc4 = utf(r.hexdigest())
                    arc4 = ARC4(key_rc4)
                    dec_rc4 = arc4.encrypt(cipher)
                    b64_r = base64.b64encode(dec_rc4)
                    # print(b64_r)
                    if(b64_r == plant1 ):
                        print("FO9{}{}{}{}{}".format(chr(i),chr(j),chr(k),chr(l),chr(m)))
                        print("found")




            

