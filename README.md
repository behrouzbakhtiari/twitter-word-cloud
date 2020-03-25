# Twitter Word Cloud

A tool to generate word cloud images from twitter user timeline.

# Demo Notebook :

- You can use this <a href="https://colab.research.google.com/drive/1uve4sned-qrmYm4aE7QsRS1a18twVhAz">Notebook</a> and run it online for yourself and get the output!

# Requirements :

- <a href="https://github.com/twintproject/twint">TWINT - Twitter Intelligence Tool</a>
- <a href="https://github.com/sobhe/hazm">Hazm</a>
- <a href="https://github.com/amueller/word_cloud">Word Cloud generator</a>
- <a href="https://github.com/pandas-dev/pandas">Pandas</a>

# how to run :

- `pip install -r requirements.txt` (Install dependencies)
- `python twc.py -u twitter_username` - Scrape all the Tweets from user's timeline and genarate word cloud images. You can find images in this path `output/twitter_username/`.
- `python twc.py -u twitter_username -c 100` - Scrape all the Tweets from user's timeline and genarate word cloud images with 100 words.
- `python twc.py -u twitter_username -f "XB Zar.ttf"` - Scrape all the Tweets from user's timeline and use "XB Zar.ttf" font on the image. Yon can find fonts in the `fonts` folder.

  # Ngram

  If you need a word cloud with a sequence of N adjacent word, you can use -n parameter.

  - `python twc.py -u Rouhani_ir -n 2`

  ![Bigram](Rouhani_ir_2.png?raw=true)

  - `python twc.py -u Rouhani_ir -n 3`

  ![Trigram](Rouhani_ir_3.png?raw=true)

# Sample Output:

![Sample Result](Rouhani_ir.png?raw=true)
