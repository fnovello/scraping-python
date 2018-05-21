import requests
import json
import sys
from bs4 import BeautifulSoup


# page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
# url = "https://www.booking.com/reviews/ar/hotel/mint-hostel.en-gb.html?aid=304142;label=gen173nr-1DCAsoDEILbWludC1ob3N0ZWxICVgEaAyIAQGYAS7CAQp3aW5kb3dzIDEwyAEM2AED6AEB-AEEkgIBeagCAw;sid=85143f177573d2d6aeab4c777b49814c";
# url = "https://www.booking.com/reviews/es/hotel/las-casas-de-la-juderia.es.html?aid=304142;label=gen173nr-1FCAEoggJCAlhYSDNYBGgMiAEBmAEKwgEKd2luZG93cyAxMMgBDNgBAegBAfgBC5ICAXmoAgM;sid=73ce31bc9e08add33bf198d47a357dc3;customer_type=total;hp_nav=0;old_page=0;order=completed_asc;page=2;r_lang=all;rows=99";

# url2 = "https://www.booking.com/reviews/es/hotel/homesuitehome-cordoba.es.html?aid=304142;label=gen173nr-1FCAEoggJCAlhYSDNYBGgMiAEBmAEKwgEKd2luZG93cyAxMMgBDNgBAegBAfgBC5ICAXmoAgM;sid=73ce31bc9e08add33bf198d47a357dc3";
# https://www.booking.com/reviews/es/hotel/homesuitehome-cordoba.es.html?aid=304142&label=gen173nr-1FCAEoggJCAlhYSDNYBGgMiAEBmAEKwgEKd2luZG93cyAxMMgBDNgBAegBAfgBC5ICAXmoAgM&sid=73ce31bc9e08add33bf198d47a357dc3&r_lang=de&customer_type=total&order=completed_asc
# url2 = "https://www.booking.com/reviews/es/hotel/conquistador.es.html?aid=304142";
# url = "https://www.infobae.com";
payload = {
		   'aid': '304142','label': 
		   'gen173nr-1FCAEoggJCAlhYSDNYBGgMiAEBmAEKwgEKd2luZG93cyAxMMgBDNgBAegBAfgBC5ICAXmoAgM', 
		   'sid': '73ce31bc9e08add33bf198d47a357dc3',
		   'r_lang':'de','customer_type':'total',
		   'page': '5',
		   'rows':'75',
		   'order':'completed_asc'
		   }
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
page = requests.get('https://www.booking.com/reviews/es/hotel/conquistador.es.html', params=payload, headers=header)
# sys.exit(page.url)
soup = BeautifulSoup(page.content, 'html.parser')

# # parsed_html = BeautifulSoup(page, "lxml")
# encode = soup.encode('UTF-8')

# # last = soup.find("div")
# # last = soup.find(class_='review_item_review_container lang_ltr');
# # print(last.encode('UTF-8'))

# # items_reviews = soup.find_all(class_='review_item_review_container lang_ltr');
bd='https://testvuejs-44f38.firebaseio.com/score.json'
list_datos = list()
indice = 0
# archived_separator = soup.find_all(class_='archived_separator');
# sys.exit(archived_separator)
items_reviews = soup.find_all(class_='review_item clearfix ');
# items_reviews_archived = soup.find_all(class_='review_item clearfix archive_item ');
# sys.exit(items_reviews_archived)
print(len(items_reviews))
# print(len(items_reviews_archived))
# for item in items_reviews:
# for item in items_reviews_archived:
	# print(item.encode('UTF-8'))
	# break
	indice= indice + 1
	# print(item2.encode('UTF-8'))
	review_item_reviewer = item.find(class_='review_item_reviewer')
	# print(review_item_reviewer.encode('UTF-8'))
	puntaje = item.find('span', attrs={'class':'review-score-badge'})
	date_write = item.find('meta', attrs={'itemprop':'datePublished'}).get('content')
	date_persist = item.find('p', attrs={'class':'review_staydate'}).text
	# date_persist = '' 
	contenedor_pais = review_item_reviewer.find('span', attrs={'itemprop':'nationality'})
	pais = contenedor_pais.find('span', attrs={'itemprop':'name'})
	# print(pais.text)
	rango_edad = review_item_reviewer.find('div', attrs={'class':'user_age_group'}).text
	# print(rango_edad)
	# continue
	dato = {
			"pais":pais.text,
			"puntaje":puntaje.text.strip(),
			"rango_edad": rango_edad.strip(),
			"date_persist":date_persist.strip(),
			"date_write":date_write.strip()
			}
	# print(json.dumps(dato))
	# break;
	
	list_datos.append(dato)
	if indice == len(items_reviews):
	# if indice == len(items_reviews_archived):
		headers = {
	    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
	    'Accept': 'application/json, text/javascript, */*; q=0.01',
	    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'X-Requested-With': 'XMLHttpRequest'
		}
		# login_data='{"clave":" python","email":"fucking python ","fecha":"17/05/python 01:43","nombre":"python"}'
		# s = requests.Session()
		# print(json.dumps(list_datos))
		# break
		requests.post(bd, data=json.dumps(list_datos))
		# print(list_datos)s
		pass
	
	# print(my_list) #pais
	# print(t.text.encode('UTF-8')) #pais






# page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
# soup = BeautifulSoup(page.text, 'html.parser')

# last_links = soup.find(class_='AlphaNav')
# last_links.decompose()

# artist_name_list = soup.find(class_='BodyText')
# artist_name_list_items = artist_name_list.find_all('a')

# # Use .contents to pull out the <a> tag’s children
# for artist_name in artist_name_list_items:
#     names = artist_name.contents[0]
#     print(names)


# encode = soup.prettify().encode('UTF-8')
# print(encode)
# print(encode.find_all("div", class_='review_item_review'));
# 

# print(soup.prettify().encode('UTF-8'));
# result = soup.encode("utf-8");
# print(result);
# print(soup.encode("utf-8"));
# print(soup.prettify());


