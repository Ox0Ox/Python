# print('hello world')
# for i in range(2):
#     i = input('Enter something: ')
#     print(i + ' was inputted')



# h = 'hiiii'
# h[1] = 'o'

# print(h)




# import sys
# import requests
# import json
# def main():
#       coin = price(5)
#       coin_price(coin)
# def price(n):
#         return n

# def coin_price(l):
#       x = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
#       y = x.json()
#       z = ((float(price(5)))*(float(y["bpi"]["USD"]["rate_float"])))
#       print(f"${z:,.4f}")

# main()


import sys
import requests
import json
def main():
      coin = price()
      coin_price(coin)
def price():
        if len(sys.argv) == 2 :
                try:
                    if float(sys.argv[1]):
                           return sys.argv[1]
                except ValueError:
                    sys.exit("Command-line argument is not a number")
        else:
              sys.exit("Missing command-line argument")

def coin_price(coin):
      x = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
      y = x.json()
      z = ((float(sys.argv[1]))*(float(y["bpi"]["USD"]["rate_float"])))
      print(f"${z:,.4f}")

main()