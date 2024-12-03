import json
import pandas as pd

with open(r"C:\Users\Elusive\Desktop\Study\Ex\pythonProject\scoring_routes.json", encoding="utf-8") as f:
    data = json.load(f)

print(data)


from_the_city_list = []
for key in data.keys():
    from_the_city_list.append(key)

from_the_city_df = pd.DataFrame(from_the_city_list, columns=['Город'])
print(from_the_city_df)
from_the_city_df.to_excel(r"C:\Users\Elusive\Desktop\Study\Ex\pythonProject\from_the_city.xlsx", index=False)

in_the_city_list = []
for val in data.values():
    for k in val:
        in_the_city_list.append(k)

in_the_city_list = list(set(in_the_city_list))
in_the_city_list_df = pd.DataFrame(in_the_city_list, columns=['Город'])
print(in_the_city_list_df)
in_the_city_list_df.to_excel(r"C:\Users\Elusive\Desktop\Study\Ex\pythonProject\in_the_city.xlsx", index=False)

city = []
count_city = []
for key, val in data.items():
    city.append(key)
    count_city.append(len(val))


city_count_df = pd.DataFrame({'Город': city, 'Количество отправлений': count_city})
city_count_df.sort_values('Количество отправлений', ascending=False, inplace=True)
print(city_count_df)
city_count_df.to_excel(r"C:\Users\Elusive\Desktop\Study\Ex\pythonProject\city_count.xlsx", index=False)