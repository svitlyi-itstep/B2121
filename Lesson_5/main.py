import requests

response = requests.get('https://www.whenisthenextmcufilm.com/api')

print(response)
if response.ok:
    as_json = response.json()
    print(as_json['title'])
    print(as_json['overview'])
    print(f"{} releases in {} days!")
else:
    print(f'{response.status_code=}')