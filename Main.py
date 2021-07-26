from Reader import Reader
from Article import Article
import requests
import os

list_art = []
init_file = Reader("shisa.product.csv")
new_file = init_file.read(init_file.filepath)

os.mkdir('Articles')
os.chdir("Articles")

# Ok this is dumb , but I couldn't make it more DRY...
# Any hints and critique would be awesome ;(

for (product_code, active, name, price, vat, unit, category, producer, other_price, pkwiu, weight, priority, short_description, description, mainpage, mainpage_priority, stock, stock_warnlevel, availability, delivery, views, rank, rank_votes, images_1, images_2, images_3, images_4, images_5, images_6, images_7, images_8) in new_file.iloc:

    article = Article(product_code=product_code, active=active, name=name, price=price, vat=vat, unit=unit, category=category, producer=producer, other_price=other_price, pkwiu=pkwiu, weight=weight, priority=priority, short_description=short_description, description=description, mainpage=mainpage,
                      mainpage_priority=mainpage_priority, stock=stock, stock_warnlevel=stock_warnlevel, availability=availability, delivery=delivery, views=views, rank=rank, rank_votes=rank_votes, images_1=images_1, images_2=images_2, images_3=images_3, images_4=images_4, images_5=images_5, images_6=images_6, images_7=images_7, images_8=images_8)
    os.mkdir(f'{article.name}')
    list_art.append(article)

# This is ultra DUMB!

for article in list_art:

    print(f'{article.name}')

    try:
        if article:

            r1 = requests.get(article.images_1)
            with open(f"{article.name}/{article.name}-1.jpg", "wb") as f:
                f.write(r1.content)

            r2 = requests.get(article.images_2)
            with open(f"{article.name}/{article.name}-2.jpg", "wb") as f:
                f.write(r2.content)

            r3 = requests.get(article.images_3)
            with open(f"{article.name}/{article.name}-3.jpg", "wb") as f:
                f.write(r3.content)

            r4 = requests.get(article.images_4)
            with open(f"{article.name}/{article.name}-4.jpg", "wb") as f:
                f.write(r4.content)

            r5 = requests.get(article.images_5)
            with open(f"{article.name}/{article.name}-5.jpg", "wb") as f:
                f.write(r5.content)

            r6 = requests.get(article.images_6)
            with open(f"{article.name}/{article.name}-6.jpg", "wb") as f:
                f.write(r6.content)

            r7 = requests.get(article.images_7)
            with open(f"{article.name}/{article.name}-7.jpg", "wb") as f:
                f.write(r7.content)

            r8 = requests.get(article.images_8)
            with open(f"{article.name}/{article.name}-8.jpg", "wb") as f:
                f.write(r8.content)

    except:
        continue
