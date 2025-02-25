import requests

api_key = '8e2f781484aa9b6ab0b70d12973fdf4d'
city = 'bangkok'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city }&appid={api_key}'
url_json = 'https://api.openweathermap.org/data/2.5/weather?q=bangkok&appid=8e2f781484aa9b6ab0b70d12973fdf4d'

result = requests.get(url).json()
print(result)

city = result['name']
country = result ['sys'] ['country']
weather =result ['weather'] [0]['main'] 
description = result ['weather'] [0] ['description']
temp = result ['main'] ['temp'] - 273.15


print(f'เมือง {city} ประเทศ {country}')
print(f'สภาพอากาศวันนี้ {weather} มีลักษณะ {description}')
print(f'อุณหภูมิตอนนี้ {temp:.2f} C ')
