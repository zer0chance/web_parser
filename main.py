import requests
from bs4 import BeautifulSoup

url = 'https://coinmarketcap.com/'

def find_currencies():
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    rows = soup.find_all(class_ = "cmc-table-row")
    currencies = {}     # dictionary, to store currencies                                  

    for i in range(25):
        name_and_price = rows[i].find_all("a")      # find all links, because name and price is links
        market_cup = rows[i].find_all(class_ = "")[1].get_text()
        currencies[name_and_price[0].get_text()] = [name_and_price[1].get_text(), market_cup]   # key - name 
                                                                                                # value - list of [price, market_cup]    
    return currencies 

if __name__ == "__main__":
    currencies = find_currencies()

    while(True):
        print("Type cryptocurrency`s name or \"exit\":", end=" ")
        name = input()
        if name == "exit":
            break
        elif name in currencies:
            print("\n Price:      " + currencies[name][0])
            print(" Market cap: " + currencies[name][1], end="\n\n")
        else:
            print("\n No such cryptocurrency in top 25 \n")    
