from requests_html2 import HTMLSession
import pandas

s = HTMLSession()


query = input("Enter the city for which you want to see the weather : ").lower()
url = f'https://www.google.com/search?q=weather+{query}'


r = s.get(url,headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'})

temperature = r.html.find('span#wob_tm')[0].text

unit = r.html.find('div.vk_bk.wob-unit span.wob_t')[0].text

desc = r.html.find('div.VQF4g')[0].find('span#wob_dc')[0].text

precipitation = r.html.find('div.wtsRwe')[0].find('span#wob_pp')[0].text

humidity = r.html.find('div.wtsRwe')[0].find('span#wob_hm')[0].text

wind = r.html.find('div.wtsRwe span.wob_t')[0].find('span#wob_ws')[0].text

print(temp, unit, desc, precipitation, humidity, wind)

#create a dataframe from scratch
data_dict = {
     "temperature" : [f"{temperature} {unit}"],
     "description" : [desc],
     "precipitation" : [precipitation],
     "humidity" : [humidity],
     "wind" : [wind]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv(f"{query}_weather")

