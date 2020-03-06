# Twitter Word Cloud

A tool to generate word cloud images from twitter user timeline.

# Requirements :

- <a href="https://github.com/twintproject/twint">TWINT - Twitter Intelligence Tool</a>
- <a href="https://github.com/sobhe/hazm">Hazm</a>
- <a href="https://github.com/mehotkhan/persian-word-cloud">Persian Word Cloud Generator</a>
- <a href="https://github.com/pandas-dev/pandas">Pandas</a>

# how to run :

- `pip install -r requirements.txt` (Install dependencies)
- `python twc.py -u twitter_username` - Scrape all the Tweets from user's timeline and genarate word cloud images. You can find images in this path `output/twitter_username/`.
- `python twc.py -u twitter_username -c 100` - Scrape all the Tweets from user's timeline and genarate word cloud images with 100 words.
- `python twc.py -u twitter_username -f "XB Zar.ttf"` - Scrape all the Tweets from user's timeline and use "XB Zar.ttf" font on the image. Yon can find fonts in the `fonts` folder.

# Sample Output:

![Sample Result](BehrozBakhtiari.png?raw=true)
