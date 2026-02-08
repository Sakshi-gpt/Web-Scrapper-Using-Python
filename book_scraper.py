import requests
from bs4 import BeautifulSoup
import csv
import sqlite3 as db
import time
from urllib.parse import urljoin

base_url="https://books.toscrape.com/catalogue/"


def get_soup(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    return soup


def get_book_links(page_url):
    soup=get_soup(page_url)
    book_links=[]
    link=soup.select('article.product_pod h3 a')
    for article in link:
        rel_url=article.get('href')
        full_url=urljoin(base_url,rel_url)
        book_links.append(full_url)
    return book_links


def parse_book_page(book_url):
    soup=get_soup(book_url)

    title=soup.h1.text.strip()

    price=soup.select_one('p.price_color').text.strip()

    availability=soup.select_one('p.instock.availability').text.strip()

    description=soup.select_one('div#product_description')
    description_text=""
    if description:
        description_text=description.find_next_sibling("p").text.strip()
    else:
        description_text="No Description"

    category=soup.select('ul.breadcrumb li')[-2].text.strip()

    rating=soup.select_one('p.star-rating')["class"][1]
   
    return{
    "Title":title,
    "Price":price,
    "Availability":availability,
    "Rating":rating,
    "Description":description_text,
    "Category":category,
    "URL":book_url
    }   


def scrape_all_books():
    all_books_dict=[]
    limit=int(input("How many pages you want to scrape:"))
    print("Scraping in progress")

    for i in range(1,limit+1):
        page_url=f"{base_url}page-{i}.html"
        book_links=get_book_links(page_url)
        for desc_link in book_links:
            book_detail=parse_book_page(desc_link)
            all_books_dict.append(book_detail)
            time.sleep(0.5)
    return all_books_dict


def save_to_db(books,db_name="books.db"):
    conn=db.connect(db_name)
    cur=conn.cursor()
    qry='''create table if not exists books
    (
    title Text,
    price Text,
    availability Text,
    rating Text,
    description Text,
    category Text,
    url Text
    )'''
    cur.execute(qry)
    cur.execute("delete from books")
    conn.commit()
    for book in books:
        cur.execute('''insert into books values(?,?,?,?,?,?,?)''', (book["Title"],book["Price"],book["Availability"],book["Rating"],book["Description"],book["Category"],book["URL"]))
        conn.commit()


def save_to_csv(books, filename="books.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Title', 'Price', 'Availability', 'Rating', 'Description', 'Category', 'URL'])
        writer.writeheader()
        writer.writerows(books)


if __name__=="__main__":
   books=scrape_all_books()
   save_to_db(books)
   save_to_csv(books)
   print("Data saved to database and CSV successfully.")