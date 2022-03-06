
import requests
import csv

url = 'http://api.coincap.io/v2/assets'

headers = {
    
    'Accept': 'application/json',
    'content-type': 'application/json'
}

response = requests.request('GET', url, headers=headers,data={})

myjason = response.json()
ourdata=[]

for x in myjason['data']:
    listing=[x['symbol'],x['name'],x['marketCapUsd'],x['priceUsd'],x['volumeUsd24Hr'],x['changePercent24Hr']]
    ourdata.append(listing)
with open('crypto.csv', 'w',encoding='UTF8',newline='') as csvfile:
     writer = csv.writer(csvfile)

     writer.writerow(['symbol','name','marketCapUsd','priceUsd','volumeUsd24Hr','changePercent24Hr'])
     writer.writerows(ourdata)
print('done')