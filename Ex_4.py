import re

# 1) есть строка, где есть какие-то email с разными доменами, давай вытащим все их списком

text_1 = "Контакты: fw.ww@example.com, info@mail.ru и sup@company.org. mian@yandex.ru, sjsd@ma.s.ru"
pattern_1 = r'\b\w+\S*@\w+.\w+\S*\b'
email = re.findall(pattern_1, text_1)
print(email)

# 2) аналогично найдем все url-адреса

text_2 = """
Посетите наши сайты: https://example.com, http://site.org, www.website.ru, ftp://ftp.server.com, https://sub.domain.com, 
http://localhost:8000, https://192.168.0.1, http://10.0.0.1:5000, https://shop.example.net/products?id=12345, 
http://news.site.net/article#top, https://longurl.example.com/path/to/page?query=abc, https://business.site.com, 
http://cdn.site.org/images, www.blog.com, www.news.org, www.portal.co.uk, ftp://download.server.org/file, https://backup.server.io, 
https://wiki.site.net, http://dev.local, https://shop.site.org/cart?id=6789&ref=promo, http://files.site.com/download.php, 
https://update.site.com, www.support.com, https://secure.site.org/login, http://beta.site.net/version, ftp://files.site.ru/upload, 
https://music.site.com/track/123, www.moviesite.com/watch, https://bank.example.com/transfer?id=98765.
"""
pattern_2 = r'\b(?:https?|ftp):\/\/\S+\w+|www\.\w+\.\w+(?:\.\w+)*(?:\/\S*)?'
url = re.findall(pattern_2, text_2)
print(url)


# 3) Посмотрим по датам. Приведем все даты к одному формату (любому, который захочешь)

text_3 = "Дата рождения: 17-05/1995. Выпускной: 30/06.2013. Следующая встреча 09//09/2025."

dates = re.sub(r'[-/.]+', '/', text_3)
print(dates)
pattern = r'\b\d{2}/\d{2}/\d{4}\b'
dates_res = re.findall(pattern, dates)
print(dates_res)

