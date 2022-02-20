import json
from urllib.parse import urljoin

#opening the json file containtig the json response to read from it
with open('response.json','r', encoding='utf8') as f :
    data = json.load(f)

#list of the final product info
products = []

for item in data['appendix']['SearchResults']['content']:
    data = {}
    # adding https://www.walmart.com.mx to productSeoUrl
    link = urljoin('https://www.walmart.com.mx', item['productSeoUrl'])
    price = round(item['skuPrice'], 2) #price to float round 2
    #final json strucutre
    data = {'name': item['skuDisplayName'], 'price': price, 'url':link,'brand':item['brandName']}
    #append all product list
    products.append(data)

#save product info to a json file
with open("runner.json", "w", encoding='utf8') as outfile:
    json.dump(products, outfile)
