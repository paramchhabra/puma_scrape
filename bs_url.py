from bs4 import BeautifulSoup
import requests
from rich import print

# query = "cap"
# offset hardcoded for now
def save_ids_get_url(query):
    url = f"https://in.puma.com/in/en/search?q={query}&offset=24"

    proxy = "http://bab9fae56e593e516aac:ff79e32368110bf2@gw.dataimpulse.com:823"
    proxies = {"http":proxy, "https":proxy}
    response = requests.get(url=url, proxies=proxies)
    response = BeautifulSoup(response.content, 'html5lib')

    with open("file.txt","a") as f:
        i = response.find('ul', id="product-list-items")

        count = 0
        url = "https://in.puma.com"
        for j in i.descendants:
            url += j.find("a")["href"]
            break
        for j in i.descendants:
            if j.name!="li":
                continue
            count+=1
            f.write(str(j["data-product-id"])[0:6])
            f.write('\n')
        print(count)
        f.close()
    print("done")

    return url