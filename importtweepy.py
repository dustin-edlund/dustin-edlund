import tweepy
from textblob import TextBlob


consumer_key= 'A0Rt6Vgis1Z1Z19BofuseESCK'
consumer_secret= 'Gf0bGcGxvkrR5KCsS6rKk0SwmRA4ry4kau8rbJifzusxNFQXXc'

access_token='826513355187761152-OAaSxzPJJhFjSEMQNO3iNFos7YXGYOv'
access_token_secret='7E7MGqbP9VGMaTsH76CWKw6m7V74GwMWFRoBE24GpuRhU'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


public_tweets = api.search('Trump')






for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")

