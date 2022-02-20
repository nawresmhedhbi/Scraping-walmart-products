import json
from urllib.parse import urljoin

#open the json file containtig the json reponse to read from it
with open('response.json','r', encoding='utf8') as f :
    data = json.load(f)

#list of the final product info
products = []
product_list = data['appendix']['SearchResults']['content']
#using range to get the ranking
for i in range(len(product_list)):
    item = product_list[i]
    data = {}
    link = urljoin('https://www.walmart.com.mx', item['productSeoUrl'])
    #splitting product_name to extract the exact structure
    keyword =  item['skuDisplayName'].split(" ")
    # final json strucutre
    data = { 'url':link,'rank': i+1 ,'keyword': "".join( keyword[1]+' '+keyword[2]) }
    # append all product list
    products.append(data)

#save product info to a json file
with open("ranking.json", "w", encoding='utf8') as outfile:
    json.dump(products, outfile)
