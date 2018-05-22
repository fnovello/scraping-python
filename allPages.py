import requests
import json
import sys
from bs4 import BeautifulSoup

p_page=0
ban=True
while(ban):

	p_page+=1
	print(p_page)
	# aid=304142;
	# label=gen173nr-1DCAsoDEILbWludC1ob3N0ZWxICVgEaAyIAQGYAS7CAQp3aW5kb3dzIDEwyAEM2AED6AEB-AEEkgIBeagCAw;
	# sid=ee7daad16ec016539000c9f3ba857bb2;
	# customer_type=total;
	# hp_nav=0;
	# old_page=0;
	# order=completed_asc;
	# page=1;
	# r_lang=all;
	# rows=75&
	
	payload = {
			   'aid': '304142',
			   'label': 'label=gen173nr-1DCAsoDEILbWludC1ob3N0ZWxICVgEaAyIAQGYAS7CAQp3aW5kb3dzIDEwyAEM2AED6AEB-AEEkgIBeagCAw', 
			   'sid': 'ee7daad16ec016539000c9f3ba857bb2',
			   'r_lang':'all',
			   'customer_type':'total',
			   'page': p_page,
			   'rows':'75',
			   'order':'completed_asc'
			   }
	header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
	page = requests.get('https://www.booking.com/reviews/ar/hotel/mint-hostel.en-gb.html', params=payload, headers=header)
	# page = requests.get('https://www.booking.com/reviews/es/hotel/conquistador.es.html', params=payload, headers=header)
	# sys.exit(page.url)
	soup = BeautifulSoup(page.content, 'html.parser')

	bd='https://testvuejs-44f38.firebaseio.com/scoreBooking.json'
	list_datos = list()
	indice = 0

	items_reviews = soup.find_all(class_='review_item clearfix ');
	# sys.exit(items_reviews_archived)
	print(len(items_reviews))
	for item in items_reviews:
		indice= indice + 1
		review_item_reviewer = item.find(class_='review_item_reviewer')
		score = item.find('span', attrs={'class':'review-score-badge'})
		date_write = item.find('meta', attrs={'itemprop':'datePublished'}).get('content')
		try:
			staydate = item.find('p', attrs={'class':'review_staydate'}).text
			pass
		except Exception as e:
			staydate ='not found'
			pass
		contenedor_pais = review_item_reviewer.find('span', attrs={'itemprop':'nationality'})
		pais = contenedor_pais.find('span', attrs={'itemprop':'name'})
		user_age_group = review_item_reviewer.find('div', attrs={'class':'user_age_group'}).text
		
		dato = {
				"nationality":pais.text,
				"page":p_page,
				"score":score.text.strip(),
				"user_age_group": user_age_group.strip(),
				"staydate":staydate.strip(),
				"date_write":date_write.strip()
				}
		
		
		list_datos.append(dato)
		if indice == len(items_reviews):
			headers = {
		    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
		    'Accept': 'application/json, text/javascript, */*; q=0.01',
		    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		    'X-Requested-With': 'XMLHttpRequest'
			}
			
			requests.post(bd, data=json.dumps(list_datos))
			pass
		
if (p_page > 8):
	ban = False
	sys.exit('FIN')


