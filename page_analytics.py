# page_analytics.py
import json
import numpy as np
from collections import Counter

class PageAnalytics:
   
    def __init__(self, page_content):
        self.page_content = page_content
        self.analytics_data = {}

    def make_analytics(self):
        
        word_count = Counter(self.page_content.words)
        self.analytics_data['top_10_words'] = word_count.most_common(10)

        stopwords = set(['and', 'the', 'of', 'in', 'to', 'a', 'is', 'that', 'for', 'on'])
        filtered_words = [word for word in self.page_content.words if word.lower() not in stopwords]
        filtered_word_count = Counter(filtered_words)
        self.analytics_data['top_10_words_no_stopwords'] = filtered_word_count.most_common(10)

        word_lengths = [len(word) for word in self.page_content.words]
        self.analytics_data['average_word_length'] = np.mean(word_lengths)
        self.analytics_data['median_word_length'] = np.median(word_lengths)

        self.analytics_data['top_10_longest_words'] = sorted(self.page_content.words, key=len, reverse=True)[:10]

        sentence_lengths = [len(sentence) for sentence in self.page_content.sentences]
        self.analytics_data['average_sentence_length'] = np.mean(sentence_lengths)
        self.analytics_data['median_sentence_length'] = np.median(sentence_lengths)

        self.analytics_data['longest_sentence'] = max(self.page_content.sentences, key=len)

    def save_to_json(self, filename):
       
        data_to_save = {'url': self.page_content.url, 'analytics': self.analytics_data}
        with open(filename, 'w') as json_file:
            json.dump(data_to_save, json_file, indent=2)

    def __str__(self):
        
        return f"Analytics for {self.page_content.url}:\n{json.dumps(self.analytics_data, indent=2)}"
