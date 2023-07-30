import requests
from t import list as l
def check_proxy(proxy,user):
    try:
        response = requests.get(f"https://t.me/{user}", proxies={"http": proxy, "https": proxy})
        if response.status_code == 200:return True
        else:return False
    except:return False
  
