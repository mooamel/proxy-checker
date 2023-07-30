from check import *
input("I Can Run? : ")

for proxy in l:
    user = "vv111"
    if check_proxy(proxy,user) == True:
        with open("Good.txt", "a") as file:
            file.write(proxy + "\n")
        print(f"Proxy {proxy} True \n")
    else:
        print(f"Proxy {proxy} False \n")
