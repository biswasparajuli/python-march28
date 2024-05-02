import requests

url = "https://www.onlinekhabar.com/smtm/home/trending"
r = requests.get(url=url)
if r.status_code == 200:
    c = 0
    data = r.json()['response']
    for i in data:
        if i['percentage_change']>0:
            print(f'{i['ticker_name']} Percentage Changes Today: {i['percentage_change']}')
    print(f'________________________________________________-')

    c = len(data)
    print(f'Total Number of listed Company is {c}')


else:
    print(f'Error Occured')
