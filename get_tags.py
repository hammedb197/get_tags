from bs4 import BeautifulSoup as  bs
from newspaper import Article


def get_tags(url):
    try:
        article = Article(url)
        article.download()
        html = article.html
        soup = bs(html, 'html.parser')
        find_h1 = soup.find_all('h1')
        h1_tags = [h1_tag.text for h1_tag in find_h1]
        find_h2 = soup.find_all('h2')
        h2_tags = [h2_tah.text for h2_tag in find_h2]
        find_h3 = soup.find_all('h3')
        h3_tags = [h3_tag.text for h3_tag in find_h3]
        tags = {'h1':h1_tags, 'h2': h2_tags, 'h3': h3_tags}
        return tags
    except Exception as e:
        print(e)
        print('tag not available')

print(get_tags('http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'))