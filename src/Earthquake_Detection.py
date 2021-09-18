from Twitter import get_tweets
from Preprocessing import tweet_preprocessor
import tensorflow as tf
import tensorflow_text

tweets = get_tweets()
model = tf.keras.models.load_model("../Saved Models/lstm_model")

for tweet in tweets:
    preprocessed_tweet = tweet_preprocessor(tweet)
    prediction = model.predict([preprocessed_tweet])
    print(prediction)
    print(f"The tweet is {preprocessed_tweet}")
    break
    
