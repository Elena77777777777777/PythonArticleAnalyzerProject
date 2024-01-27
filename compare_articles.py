# compare_articles.py

def compare_articles(articles):
    
    longest_sentence_article = max(articles, key=lambda article: len(article.page_content.sentences))
    longest_word_article = max(articles, key=lambda article: max(map(len, article.page_content.words)))
    most_sentences_article = max(articles, key=lambda article: len(article.page_content.sentences))
    most_words_article = max(articles, key=lambda article: len(article.page_content.words))

    return {
        'longest_sentence_article': longest_sentence_article.page_content.url,
        'longest_word_article': longest_word_article.page_content.url,
        'most_sentences_article': most_sentences_article.page_content.url,
        'most_words_article': most_words_article.page_content.url
    }
