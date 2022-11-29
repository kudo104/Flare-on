# Nur_getraumt
- Đây là 1 file  `Apple DiskCopy 4.2 image`
- Sử dụng tool `macintosh.js` để chạy chương trình và cho sẵn chương trình `super ResEdit` để decompile sau đó mình lấy offset của chương trình

![alt](https://github.com/kudo104/Flare-on/blob/main/Flare-on_2022/10_Nur_getraumt/Picture/1.png)

- Sau khi lấy được offset mình dùng ghidra để tìm đến hàm `decodeFlag()`

![alt](https://github.com/kudo104/Flare-on/blob/main/Flare-on_2022/10_Nur_getraumt/Picture/2.png)

- Hàm decodeFlag chỉ đơn giản là 
```
for(int i = 0; i < strlen(key) ; i ++){
    cipher[i] = cipher[i] ^ key[i % strlen(key)]
}
```
- Tìm lại Key dựa vào chuỗi `@flare-on.com` và các kí tự còn lại ở mình tra google

> Key 

    Hast du etwas Zeit für mich