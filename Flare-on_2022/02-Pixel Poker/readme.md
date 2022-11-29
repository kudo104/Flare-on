# Pixel Poker
## Tổng quan 
 - File 32 bit
 - File PE có 2 .rsrc tại Bitmaps đã bị mã hóa
 - Chạy bài này thì click vào 10 điểm nhưng chưa biết để làm gì
## Phân tích
- Phân tích file thì mỗi lần click thì sẽ giải mã tại điểm đó bằng RC4
- Key phụ thuộc vào tọa độ của điểm ảnh

![alt](https://github.com/kudo104/Flare-on/blob/main/Flare-on_2022/02-Pixel%20Poker/picture/1.png)

|| Giải mã File

```

from PIL import Image

def rc4(key,data):
	array = []
	for i in range(256):
		array.append(i)
	num = 0
	for i in range(256):
		num = (num + array[i] + ord(key[i % len(key)])) % 256
		num2 = array[i]
		array[i] = array[num]
		array[num] = num2
	num = 0
	k = 0
	out = [None] * 3
	c = 2
	for i in range(3):
		k = (k + 1)%256
		num = (num + array[k]) % 256
		num3 = array[k]
		array[k] = array[num]
		array[num] = num3
		num4 = array[(array[k] + array[num]) % 256]
		out[c] = data[c] ^ num4
		c = c - 1
	return out

im = Image.open("Bitmap133.bmp")
d = im.load()
print(d[641,0])
size = im.height * im.width
h = im.height
pixels = []
dec = []
print(im.height,im.width)
for i in range(im.height):
	for j in range(im.width):
		k = "PixelPoker ({},{})".format(j,i)
		t = d[j,i]
		t = tuple(rc4(k,t))
		d[j,i] = t


im.save("out.bmp")

```

    Flag:w1nN3r_W!NneR_cHick3n_d1nNer@flare-on.com



