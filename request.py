import json
import requests

#The url got from XHR and fetch filter
URL = "https://www.walmart.com.mx/api/v2/page/browse/autos-y-llantas/llantas-y-rines/llantas-rin-18?page=0&size=48"

headers = {
  'authority': 'www.walmart.com.mx',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
  'accept': 'application/json',
  'content-type': 'application/json',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.walmart.com.mx/autos-y-llantas/llantas-y-rines/llantas-rin-18?page=0',
  'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7,ar;q=0.6',
  'cookie': 'pxcts=fb69b48b-8f44-11ec-b89a-6b674774497a; _pxvid=fb69a7be-8f44-11ec-b89a-6b674774497a; _gcl_au=1.1.2124928926.1645028662; _gaexp=GAX1.3.oGISqiscRiON0oa7Cd-zdA.19126.1; _ga=GA1.1.1820994232.1645028664; NSC_mc-383446992-1-409917434=ffffffff09ebb29f45525d5f4f58455e445a4a4229a0; _fbp=fb.2.1645028666289.499826000; loggedInUserCookie=guest; FPID=FPID2.3.wGKe%2FCXWfMshya%2BE8O4ImFjqqFXjq2Y5BOOEPudWFYI%3D.1645028664; mtz_visitor_id=e74b5b908f4411ec9c2247f897d712c1; cart-item-count=0; com.silverpop.iMAWebCookie=a1219834-535d-a82d-387a-120be84c8572; wmt.c=0; FPLC=lRVxoygCE6G0nAsBdEITThV9w8lZnPqyXGcnm7oIRuJIX%2F1sHgXe7exls9njtCOwjoSV%2BkNHnVRwKQdu%2FEiitoxfKCsUFZ2NiVOVb9nMPnLsdMbLQxvAbNZm9anGAA%3D%3D; _clck=1pwe937|1|ez3|0; JSESSIONID=Ir58P0n7HDutovJx7FpG9XF0.restapp-267254196-1-1347522392; TS01c7b722=01c5a4e2f922465517f93896a843a2384b38ac047d684949f2942dd6d06411d785d776df25480f2e99148a996e11412c2ec4aeab01; TS014f2e15=01538efd7c3725178bb0afc47ba9597a37a380bb59ee13382f9a39a1883c30ca848a791248ec6ea2a6c01993d9b36e54a29b41e01f; com.silverpop.iMA.session=a1113d4c-71ca-2060-3a26-46adc5e16180; com.silverpop.iMA.page_visit=1611087973:; _uetsid=e74b13008f4411ec816aafcb4731797d; _uetvid=e74b5b908f4411ec9c2247f897d712c1; _px3=f20b0ec3cd4ab9a0e481f002183f51106bca091d4a66b7c874b4c1fdce800af8:NJu9xcEDntvs6WBf0ynj+7TRspk/EsoOLQrGowtOJQtJ6+JOqbTRiiOMMUO94meJAU/xP+vksfhVyTZ4V8mvKA==:1000:o5n81WqsgsBlKv4jSE7OjxNaNgQYHHf4Etg7i6U3OzZ5SB22OBD1VXC32hacCmNZpg1x045XaxDDZRbejApYWHGFZTyKgJ6TZHsyJchvTUV1AhggTD372qmXRUOINaopwqgT7i/5w1rRpwjmhNOnnbA3r63cPQQl+0Hpimo/oAEJFkKkKqZ7yMBWawOcLwzNAzZaWd4+XU9IHfhD2s5YUw==; cto_bundle=UbybVV9pVVVLRDZBbFBHTjIySFJwNVpmRlZLVlhNc1dLRDJKcXZpQW5GWG1DUXNyeFQzcmlzSk9sbTN2UW1ibm41Um52azJpMjRyRFN4dlFpOHdvU1AxYUc1Z2xlWUElMkIlMkJJOGYwcWN0bWRkcE5pczE5THZoa2taJTJGdXBERyUyRm83TE5zMkM0WW51alIlMkZEYlVNVmZlQXVxR3RhbVBBJTNEJTNE; 12901.vst=%7B%22s%22%3A%22178c297e-8a2e-4306-989e-b9590e29bf6c%22%2C%22t%22%3A%22returning%22%2C%22lu%22%3A1645167193381%2C%22lv%22%3A1645167116273%2C%22lp%22%3A0%7D; _pxde=b073f48431f23fbb7ed55c178f30bec565014f02acf5276bd496f99fcf7d61bd:eyJ0aW1lc3RhbXAiOjE2NDUxNjcyNjQ3MDQsImZfa2IiOjAsImlwY19pZCI6W119; _clsk=e4dri3|1645167226365|4|0|f.clarity.ms/collect; akavpau_vp_walmart_ss=1645167566~id=eb65a857c38d4301ddabbcfbbd8a7d81; TS01f4281b=0130aff2323a5ad12c570a63ba5b45bda2cb20dab93917b2411dcada21624c383f29605abb14d7119085fa3c258882c514370abd65; _ga_9C15BZ4SZ5=GS1.1.1645167104.11.1.1645167369.60; _ga_RZERZ9LC4J=GS1.1.1645167104.9.1.1645167369.60; akavpau_vp_walmart_ss=1645167881~id=d5e287e1f4988433bacff7ae096f5914',
  'if-modified-since': 'Fri, 18 Feb 2022 01:02:26 GMT'
}
r = requests.request("GET", URL, headers=headers)
#load the reponse
data = json.loads(r.text)
#observing the reponse : products info
print(data['appendix']['SearchResults']['content'])
