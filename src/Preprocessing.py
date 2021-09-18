import pandas as pd
import re
from nltk.corpus import stopwords
import preprocessor as p
import wordninja
from nltk.stem import WordNetLemmatizer


# Converting to lowercase
def to_lower(text):
    return text.lower()


# Removing punctuations
punctuation = '!"#$%&\'()*+,-/:;<=>?@[\\]^_`{|}~'
def remove_punctuations(text):
    # text = re.sub(".+","",text)
    return re.sub('[%s]' % re.escape(punctuation),'',text)


stop_words = set(stopwords.words('english'))
stop_words.add('http')
def remove_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in stop_words])


# Rephrasing url, mentions, and retweets
def rephrase_text(text):
    p.set_options(p.OPT.URL,p.OPT.MENTION)
    parsed_text = p.tokenize(text)
    clean_text = re.sub("RT\s\$MENTION\$:","retweet",parsed_text)
    clean_text = re.sub("\$MENTION\$:","mentions",clean_text)
    clean_text = re.sub("\$URL\$","link",clean_text)
    return clean_text


# Expanding hashtags
def handle_hashtag(text):
    p.set_options(p.OPT.HASHTAG) 
    parsed_text = p.parse(text)
    if(not parsed_text.hashtags):
        return text
    for hashtag in parsed_text.hashtags:
        match = hashtag.match
        text = re.sub(match, " ".join(wordninja.split(match)), text)
    return text


# Removing emojis
def remove_emoji(text):
    p.set_options(p.OPT.EMOJI,p.OPT.SMILEY)
    tokenized_text = p.tokenize(text)
    tokenized_text = re.sub(re.escape("$EMOJI$"),"",tokenized_text)
    return tokenized_text


# Lemmatizing words
lemmatizer = WordNetLemmatizer()
def lemmatize_word(text):
    return lemmatizer.lemmatize(text)


# Removing whitespace
def remove_whitespace(text):
    return re.sub(' +'," ",text)


def tweet_preprocessor(text):
    text = remove_stopwords(text)
    text = rephrase_text(text)
    text = handle_hashtag(text)
    text = remove_emoji(text)
    text = lemmatize_word(text)
    text = remove_whitespace(text)
    text = to_lower(text)
    text = remove_punctuations(text)
    return text






