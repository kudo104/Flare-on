import ctypes
import mmap

value = [80, 94, 94, 163, 79, 91, 81, 94, 94, 151, 163, 128, 144, 163, 128, 144, 163, 128, 144, 163, 128, 144, 163, 128, 144, 163, 128, 144, 163, 128, 144, 162, 163, 107, 127, 0]
for i in range(36):
	for j in range(0x20,0x7f,1):
		if((value[i] + j) == 0xc3):
			print(chr(j),end = "")
