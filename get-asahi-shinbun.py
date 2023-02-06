import requests
from bs4 import BeautifulSoup

url = "https://www.asahi.com/"
res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")

# 見出し一面記事の取得
print("【一面記事】")
first_news = soup.select_one(".p-topNews__firstNews a")
print(first_news.getText())
print("\n")

# 見出し関連記事
print("関連記事：")
related_news_titles = [n.getText() for n in soup.select(".p-relatedNews__list li")]
for i, title in enumerate(related_news_titles):
    news_num = i + 1
    print(f"{news_num}. {title}")
print("\n")
    
# 見出し
print("【記事一覧】")
news_titles = [n.getText() for n in soup.select(".p-topNews__list .c-articleModule__link span")]
for i, title in enumerate(news_titles):
    news_num = i + 1
    print(f"{news_num}. {title}")
print("\n")