import os
import sys
import tweepy
import requests
import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from textblob import TextBlob


consumer_key = 'A0Rt6Vgis1Z1Z19BofuseESCK'
consumer_secret = 'Gf0bGcGxvkrR5KCsS6rKk0SwmRA4ry4kau8rbJifzusxNFQXXc'
access_token = '826513355187761152-OAaSxzPJJhFjSEMQNO3iNFos7YXGYOv'
access_token_secret = '7E7MGqbP9VGMaTsH76CWKw6m7V74GwMWFRoBE24GpuRhU'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
user = tweepy.API(auth)

FILE_NAME = 'amd.csv'


def stock_sentiment(quote, num_tweets):
    list_of_tweets = user.search(quote, count=num_tweets)
    positive, null = 0, 0

    for tweet in list_of_tweets:
        blob = TextBlob(tweet.text).sentiment
        if blob.subjectivity == 0:
            null += 1
            next
        if blob.polarity > 0:
            positive += 1

    if positive > ((num_tweets - null)/2):
        return True


def get_historical(quote):
    # Download our file from google finance
    url = 'http://www.google.com/finance/historical?q=NASDAQ%3A'+quote+'&output=csv'
    r = requests.get(url, stream=True)

    if r.status_code != 400:
        with open(FILE_NAME, 'wb') as f:
            for chunk in r:
                f.write(chunk)

        return True


def stock_prediction():

    dataset = []

    with open(FILE_NAME) as f:
        for n, line in enumerate(f):
            if n != 0:
                dataset.append(float(line.split(',')[1]))

    dataset = np.array(dataset)

    def create_dataset(dataset):
        dataX = [dataset[n+1] for n in range(len(dataset)-2)]
        return np.array(dataX), dataset[2:]
        
    trainX, trainY = create_dataset(dataset)

    model = Sequential()
    model.add(Dense(8, input_dim=1, activation='relu'))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(trainX, trainY, nb_epoch=200, batch_size=2, verbose=2)

    prediction = model.predict(np.array([dataset[0]]))
    result = 'The price will move from %s to %s' % (dataset[0], prediction[0][0])

    return result

    
stock_quote = raw_input('amd').upper()

if not stock_sentiment(stock_quote, num_tweets=100):
    print ('This stock has bad sentiment, please re-run the script')
    sys.exit()

if not get_historical(stock_quote):
    print ('Google returned a 404, please re-run the script and')
    print ('enter a valid stock quote from NASDAQ')
    sys.exit()

print (stock_prediction)

os.remove(csv)
