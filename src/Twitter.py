from datetime import timezone, datetime, timedelta
import requests
from env_variable import bearer_token    

search_url = "https://api.twitter.com/2/tweets/search/recent"


def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def create_tweets(response):
    tweets = []
    if (response['meta']['result_count'] == 0):
        print("Now tweets found")
        return 
    for tweet in response['data']:
        tweets.append(tweet['text'])
    # print(tweets)
    return tweets


def get_tweets():
    time = datetime.now(timezone.utc).astimezone() - timedelta(minutes = 1) 
    query_params = {'query': 'earthquake','start_time':str(time.isoformat())}
    json_response = connect_to_endpoint(search_url, query_params)
    return create_tweets(json_response)





