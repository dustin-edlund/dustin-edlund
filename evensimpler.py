import tweepy
import csv
import numpy as np
from textblob import TextBlob
from keras.models import Sequential
from keras.layers import Dense



consumer_key= 'A0Rt6Vgis1Z1Z19BofuseESCK'
consumer_secret= 'Gf0bGcGxvkrR5KCsS6rKk0SwmRA4ry4kau8rbJifzusxNFQXXc'
access_token='826513355187761152-OAaSxzPJJhFjSEMQNO3iNFos7YXGYOv'
access_token_secret='7E7MGqbP9VGMaTsH76CWKw6m7V74GwMWFRoBE24GpuRhU'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


public_tweets = api.search('amd')



for tweet in public_tweets:    
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    


dates = []
prices = []
def get_data(amd):
	with open(amd, 'r') as csvfile:
		csvFileReader = csv.reader(csvfile)
		next(csvFileReader)
		for row in csvFileReader:
			dates.append(int(row[0].split('-')[0]))
			prices.append(float(row[1]))
	return


get_data('amd')

def predict_prices(dates, prices, x):

	predicted_price = predict_price(dates, prices, 29)
print(predicted_price)