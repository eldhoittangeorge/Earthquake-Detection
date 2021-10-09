from Twitter import get_tweets
from Preprocessing import tweet_preprocessor
import tensorflow as tf
import tensorflow_text
from Location import get_location

tweets = get_tweets()
model = tf.keras.models.load_model("../Saved Models/lstm_model")

def create_output(tweet,score,location=""):
    print(f"The tweet is:\n{tweet}")
    if(score > .5):
        print(f"The tweet is valid with score-> {score}")
        if(location):
            print(f"The location is:\t {location}")
    else:
        print(f"The tweet is invlaid with score -> {score}")


for tweet in tweets:
    location = get_location(tweet)
    preprocessed_tweet = tweet_preprocessor(tweet)
    prediction = model.predict([preprocessed_tweet])
    create_output(tweet, prediction[0][0], location)
    break
    