import requests
from t import list as l
def check_proxy(proxy):
    try:
        response = requests.get("https://t.me/vv111", proxies={"http": proxy, "https": proxy})
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False
    except:return False
  
input("inter FOr RUN")
  
for proxy in l:
    if check_proxy(proxy) == True:
        with open("Good.txt", "a") as file:
            file.write(proxy + "\n")
        print(f"Proxy {proxy} True \n")
    else:
        print(f"Proxy {proxy} False \n")
