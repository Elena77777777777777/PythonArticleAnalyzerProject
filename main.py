# main.py
from url_error import UrlError
from raw_page import RawPage
from page_content import PageContent
from extractor import Extractor
from page_analytics import PageAnalytics
if __name__ == "__main__":
    
    article_urls = [
        "https://en.wikipedia.org/wiki/Python_(programming_language)",
        "https://en.wikipedia.org/wiki/Machine_learning",
        "https://en.wikipedia.org/wiki/Data_science"
"https://en.wikipedia.org/wiki/Data_science"
from url_error import UrlError
from raw_page import RawPage
from page_content import PageContent 
from extractor import Extractor
from page_analytics import PageAnalytics

if __name__ == "__main__":
  
    article_urls = [
        "https://en.wikipedia.org/wiki/Python_(programming_language)",
        "https://en.wikipedia.org/wiki/Machine_learning",
        "https://en.wikipedia.org/wiki/Data_science"
    ]

    articles = []
    for url in article_urls:
        try:
            raw_page = RawPage(url)
            page_content = PageContent()
            extractor = Extractor()
            extractor.extract_sentences(raw_page, page_content)
            extractor.extract_words(raw_page, page_content)
            articles.append(PageAnalytics(page_content))
        except UrlError as e:
            print(f"Error processing URL {e.url}: {e}")

    
    for article in articles:
        article.make_analytics()
        print(article)

    
    comparison_result = compare_articles(articles)
    print("\nComparison Result:")
    for key, value in comparison_result.items():
        print(f"{key}: {value}")
"https://en.wikipedia.org/wiki/Data_science"
"https://en.wikipedia.org/wiki/Data_science"

    ]

    articles = []
    for url in article_urls:
        try:
            raw_page = RawPage(url)
            page_content = PageContent()
            extractor = Extractor()
            extractor.extract_sentences(raw_page, page_content)
            extractor.extract_words(raw_page, page_content)from page_content import PageContent
from raw_page import RawPage
# main.py
from url_error import UrlError
from raw_page import RawPage
from page_content import PageContent  # Import PageContent here


from url_error import UrlError
from raw_page import RawPage
from page_content import PageContent 

if __name__ == "__main__":
    
from url_error import UrlError
from raw_page import RawPage
from page_content import PageContent 
from extractor import Extractor

if __name__ == "__main__":
  
from url_error import UrlError
from raw_page import RawPage
from page_content import PageContent
from extractor import Extractor

if __name__ == "__main__":
   

            articles.append(PageAnalytics(page_content))
        except UrlError as e:
            print(f"Error processing URL {e.url}: {e}")

   
    for article in articles:
        article.make_analytics()
        print(article)

   
    comparison_result = compare_articles(articles)
    print("\nComparison Result:")
    for key, value in comparison_result.items():
        print(f"{key}: {value}")
