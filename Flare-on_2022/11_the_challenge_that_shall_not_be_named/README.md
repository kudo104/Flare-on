# the challenge that shall not be named

## 1.Tổng Quan 
Đầu tiên mình ném vào `Detect it easy` để có các thông tin cơ bản, chương trình dùng pyinstaller để đóng gói.

![alt](https://github.com/kudo104/Flare-on/blob/main/Flare-on_2022/11_the_challenge_that_shall_not_be_named/Picture/1.png)

## 2. Unpack và Phân tích
Sử dụng tool có sẵn `PyInstaller Extractor` để unpack,file cần reverse 11.pyc

![alt](https://github.com/kudo104/Flare-on/blob/main/Flare-on_2022/11_the_challenge_that_shall_not_be_named/Picture/2.png)

Sử dụng ```decpmpile3``` hay ```uncompyle6``` để decompile `pyc` thành `py`.

Sau khi decompile thành file py thì chương trình đã bị `pyamor`

![alt](https://github.com/kudo104/Flare-on/blob/main/Flare-on_2022/11_the_challenge_that_shall_not_be_named/Picture/3.png)  

Sau khi chạy file 11.py thì biết cần 1 số thư viện khác thử decompile Crypt.pyc tại vì 11.pyc load thèn này đầu tiên nên mình decompile thèn này,thì thấy thư viện này cũng bị pyamor trong khi python là mã nguồn mở và decompile thì những thèn khác không bị.Do đó Crypt.py đã bị custom.

![alt](https://github.com/kudo104/Flare-on/blob/main/Flare-on_2022/11_the_challenge_that_shall_not_be_named/Picture/4.png) 

Thử tạo 1 file rỗng Crypt.py thì biết được nó dùng ARC4.Chỉ cần tạo 1 class ARC4 và in ra là được flag

![alt](https://github.com/kudo104/Flare-on/blob/main/Flare-on_2022/11_the_challenge_that_shall_not_be_named/Picture/5.png) 

```
class ARC4:
  def __init__(self, name):
    self.name = name

  def encrypt(self,b):
    print(b)
```

## 3. Flag

```Pyth0n_Prot3ction_tuRn3d_Up_t0_11@flare-on.com```

