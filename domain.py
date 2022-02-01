import socket 
print("-"*30)
a = 0
while a < 5:
    a+= 1
    domain  = input('domain giriniz: ')
    islem = socket.gethostbyname(domain)
    print("-->", islem)
