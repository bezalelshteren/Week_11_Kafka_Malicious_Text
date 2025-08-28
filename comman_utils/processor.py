import nltk
import os
# nltk.data.path.append("./nltk_data")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import re
NLTK_DIR = os.path.join(os.path.dirname(__file__), "comman_utils")


class TextProcessor:
    def __init__(self,text_processor):
        self.text_processor=text_processor
        self.clean_text=None


    def removing_punctuation_marks(self):
        self.clean_text = re.sub(r'[^\w\s]', '', self.text_processor)

        return self.clean_text

    def removing_whitespace_and_tab_characters(self):
        self.clean_text = re.sub(r'\s+', ' ',  self.clean_text).strip()

    def removing_stopwords(self):
        stop_words = set(stopwords.words("english"))
        tokens = word_tokenize(self.clean_text)
        filtered_words = [w for w in tokens if w.lower() not in stop_words]
        self.clean_text = ' '.join(filtered_words)


    def chang_word_to_root(self):
        stemmer = PorterStemmer()
        stemmed_words = [stemmer.stem(word) for word in self.clean_text.split()]
        self.clean_text = ' '.join(stemmed_words)



    def to_lowercase(self):
        self.clean_text = self.clean_text.lower()




    def get_clean_text(self):
        return self.clean_text

    def process_all_and_get(self):
        self.removing_punctuation_marks()
        self.removing_whitespace_and_tab_characters()
        self.removing_stopwords()
        self.chang_word_to_root()
        self.to_lowercase()
        return self.get_clean_text()





#
# text = """Hello!!!  Did you see   the  are   this? → AI & humans—working together.Email me at: test@example.com, or visit https://example.org.
# Price: $19.99 (limited-time offer ).
# Café Münsterstraße – déjà vu? ¡Sí, señor! gun guns run running
# Symbols: © ® ™ ± ÷ × ≠ ≤ ≥ ∑ ∞ ♥ ♦ ♣ ♠ ★ ☆"""
# a = TextProcessor(text)
# a.removing_punctuation_marks()
# a.removing_whitespace_and_tab_characters()
# a.removing_stopwords()
# a.chang_word_to_root()
# a.to_lowercase()
# print(a.get_clean_text())





