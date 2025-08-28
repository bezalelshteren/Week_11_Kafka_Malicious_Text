import nltk
from datetime import datetime
import os
from dotenv import load_dotenv
from comman_utils.processor import TextProcessor
# from nltk.data import find
NLTK_PATH = os.path.join(os.getcwd(), "..\comman_utils", "nltk_data")
nltk.data.path.append(NLTK_PATH)
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sentimentIntensityAnalyzer = SentimentIntensityAnalyzer()
load_dotenv()


class Enricher:
    path = os.getenv("PATH_TO_WEAPONS_LIST")
    with open(path) as file:
        weapons_list = (file.read().split("\n"))
    weapons_string = " ".join(weapons_list)
    prossor = TextProcessor(weapons_string)

    def __init__(self,message:dict):
        self.message = message
        self.clean_data = message["cleaned_text"]
        self.dirty_data = message["text"]




    def is_positive_or_negative(self):
        score = sentimentIntensityAnalyzer.polarity_scores(self.clean_data)["compound"]
        # print(score)
        if score >= 0.5:
            return "positive"
        if score < -0.5:
            return "negative"
        else:
            return "normal"


    def check_if_their_is_weapons(self):
        weapons_clean = self.prossor.process_all_and_get().split(" ")
        list_of_weapons = []
        for weapon in weapons_clean:
            if weapon in self.clean_data:
                list_of_weapons.append(weapon)
        return list_of_weapons


    def find_the_latest_date(self):
        list_of_dates = []
        for word in self.dirty_data.split(" "):
            try:
                date_obj = datetime.strptime(word, "%Y-%d-%m")
                list_of_dates.append(word)
            except ValueError:
                pass
        if len(list_of_dates) == 0:
            return "their not datas"
        return max(list_of_dates)


    def start_all_function_on_every_data(self):

        self.message["sentiment"] = self.is_positive_or_negative()
        self.message["detected_weapons"] = self.check_if_their_is_weapons()
        self.message["timestamp_relevant"] = self.find_the_latest_date()
        return self.message

# r = {'_id': '68ae981e5e29e58934bb268d', 'TweetID': 1.21e+18, 'CreateDate': '2020-01-08 12:42:48', 'Antisemitic': 0, 'text': "Iran, today. - Fired missiles at US base in Iraq - gun Threatened to strike locations in Israel and the UAE - Qassem Soleimani buried - Ukrainian Boeing 737 with 180 passengers crashes near Tehran - 4.9 magnitude earthquake in country's southwestern region", 'cleaned_text': 'iran today fire missil us base iraq gun threaten strike locat israel uae qassem soleimani buri ukrainian boe 737 180 passeng crash near tehran 49 magnitud earthquak countri southwestern region'}
#
# e = Enricher(r)