import twint
from string import punctuation
import preprocessor as tp
import pandas as pd
from hazm import *
from persian_wordcloud.wordcloud import PersianWordCloud, add_stop_words
import re
import sys
from PIL import Image
import numpy as np
from os import path
import stopwords
from collections import Counter
import os
punctuation_list = list(punctuation)

username = ""
max_words = 200
tweets_file_path = ""
image_file_path = ""
output_dir = "output"

# get tweets from twiter with twint library
# twint repo: https://github.com/twintproject/twint


def export_tweets():
    if os.path.isfile(tweets_file_path):
        print(f"{tweets_file_path} is found and it will be processed.")
        print("If you want to get tweets from twitter, remove this file")
        return
    c = twint.Config()
    c.Username = username
    c.Store_csv = True
    c.Output = tweets_file_path
    twint.run.Search(c)

# remove enoji and some unicode chars from tweet text


def remove_emoji(tweet):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u'\U00010000-\U0010ffff'
                               u"\u200d"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\u3030"
                               u"\ufe0f"
                               u"\u2069"
                               u"\u2066"
                               u"\u2068"
                               u"\u2067"
                               "]+", flags=re.UNICODE)

    return emoji_pattern.sub(r'', tweet)

# preprocess tweet text (remove links, stopwords, images, mentions and numbers form tweets text )


def clean_tweet(tweet):
    tweet = str(tweet)
    tweet = tweet.lower()
    tweet = tweet.replace("#", "") # remove # so we preserve hashtags for the cloud
    tweet = tp.clean(tweet)
    tweet = remove_emoji(tweet)
    normalizer = Normalizer()
    tweet = normalizer.normalize(tweet)
    tweet = re.sub(r'ن?می[‌]\S+','',tweet) # removes verbs such as می‌شود or نمی‌گویند
    tokens = word_tokenize(tweet)
    tokens = [token for token in tokens if token not in stopwords.persian]
    tokens = [token for token in tokens if token not in stopwords.english]
    return " ".join(tokens).strip()

# draw word cloud from tweets with persian word cloud
# persian word cloud repo: https://github.com/mehotkhan/persian-word-cloud


def draw_cloud(cleantweets):
    text = " ".join(str(tweet) for tweet in cleantweets)
    tokens = word_tokenize(text)
    dic = Counter(tokens)
    print(dic.most_common(max_words))
    twitter_mask = np.array(Image.open("twitter-logo.jpg"))
    wordcloud = PersianWordCloud(
        only_persian=True,
        max_words=max_words,
        margin=0,
        width=800,
        height=800,
        min_font_size=1,
        max_font_size=500,
        background_color="white",
        mask=twitter_mask
    ).generate(text)

    image = wordcloud.to_image()
    wordcloud.to_file(image_file_path)
    image.show()


def generate_word_cloud():
    export_tweets()
    if not os.path.isfile(tweets_file_path):
        print("couldn't get tweets, please try again")
        return False
    data = pd.read_csv(tweets_file_path)
    if 'clean_tweet' not in data.columns:
        data.insert(11, 'clean_tweet', '')
        data['clean_tweet'] = data['tweet'].apply(lambda x: clean_tweet(x))
    draw_cloud(data.clean_tweet.values)


def main():
    if len(sys.argv) < 2:
        sys.stderr.write("Username is requried")
        exit(-1)

    global username
    global max_words
    global tweets_file_path
    global image_file_path
    username = sys.argv[1]

    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    tweets_file_path = "{}/{}.csv".format(output_dir, username)
    image_file_path = "{}/{}.png".format(output_dir, username)

    if len(sys.argv) > 2 and sys.argv[2].isnumeric():
        max_words = int(sys.argv[2])
    generate_word_cloud()


if __name__ == "__main__":
    main()
