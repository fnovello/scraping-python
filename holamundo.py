import requests
from bs4 import BeautifulSoup


# page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
url = "https://www.booking.com/reviews/ar/hotel/mint-hostel.en-gb.html?aid=304142;label=gen173nr-1DCAsoDEILbWludC1ob3N0ZWxICVgEaAyIAQGYAS7CAQp3aW5kb3dzIDEwyAEM2AED6AEB-AEEkgIBeagCAw;sid=85143f177573d2d6aeab4c777b49814c";
# url = "https://www.infobae.com";
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
# parsed_html = BeautifulSoup(page, "lxml")
encode = soup.encode('UTF-8')
# last = soup.find("div")
# last = soup.find(class_='review_item_review_container lang_ltr');
# print(last.encode('UTF-8'))

# items_reviews = soup.find_all(class_='review_item_review_container lang_ltr');
items_reviews = soup.find_all(class_='review_item clearfix ');
for item in items_reviews:
	review_item_reviewer = item.find(class_='review_item_reviewer')
	t = review_item_reviewer.find('span', attrs={'itemprop':'nationality'})
	# print(review_item_reviewer.encode('UTF-8'))
	print(t.text.encode('UTF-8')) #pais
	# print(item.encode('UTF-8'))



# print(last)
# last = encode.find(class_='review_list')

# print(last)

# a = last.find_all('a')


# for b in a:
#      names = b.contents[0]
#      print(names)


#     print(names)
# encode = parsed_html.encode('UTF-8')



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


