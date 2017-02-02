import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= '46sLxqJGfVrMMQnncGzLnPuVu'
consumer_secret= 'jcCuVFmTl6AzP1m5KkRFgf3AJok0IAGDYneKEpTlo4ZsSNKL0i'

access_token='826513355187761152-OAaSxzPJJhFjSEMQNO3iNFos7YXGYOv'
access_token_secret='7E7MGqbP9VGMaTsH76CWKw6m7V74GwMWFRoBE24GpuRhU'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
Contact GitHub API Training Shop Blog About
