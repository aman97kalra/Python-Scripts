from textblob import TextBlob
import requests
import re
import tweepy
import matplotlib.pyplot as plt
import pandas as pd

# function to authenticate the user using twitter API , i.e. tweepy 
def authentication():

    # keys and tokens from the developer console
    consumer_key = 'YOUR CONSUMER KEY'
    consumer_secret = 'YOUR CONSUMER SECRET KEY'
    access_token = 'YOUR ACCESS TOKEN'
    access_token_secret = 'YOUR SECRET ACCESS TOKEN'

    #Tweepy supports OAuth authentication. Authentication is handled by the tweepy.OAuthHandler class.
    #An OAuthHandler instance must be created by passing a consumer token and secret.

    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        api = tweepy.API(auth)        
    except:
        print("Authentication failed")
            
    topic = input('Enter the topic you want to search  ') 
    count = input('Enter the number of tweets you want to fetch  ') 
    public_tweets = api.search(topic, count=count )
    analyse_tweet( public_tweets )

# Function to clean the tweet and perform sentiment analysis on it.
def analyse_tweet( public_tweets ):
    print(len(public_tweets))
    data=[]
    pos=[]
    neg=[]
    for tweet in public_tweets:
        if tweet.lang == "en":
            tweet= tweet.text
            cleanedTweet=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
            # print(cleanedTweet+'\n')
            analysis= TextBlob(cleanedTweet)
            # print(analysis.sentiment)
            if(analysis.sentiment.polarity>0):
                # print("Positive Tweet")
                dictionary = {}
                dictionary['Sentiment']=analysis.sentiment.polarity
                dictionary['Tweet']=cleanedTweet
                data.append(dictionary)
                pos.append(cleanedTweet)
            else:
                # print("Negative Tweet")
                dictionary = {}
                dictionary['Sentiment']=analysis.sentiment.polarity
                dictionary['Tweet']=cleanedTweet
                data.append(dictionary)
                neg.append(cleanedTweet)

    plot_on_pie_chart(data,pos,neg)

# Function to plot the positive and negative tweets on pie chart
def plot_on_pie_chart(data, pos, neg):

    print(len(pos),len(neg))
    slices = [len(pos),len(neg)]

    plt.pie(slices,colors=['g','r'], labels=['Positive','Negative'])
    plt.xlabel('Sentiment Polarity')
    plt.ylabel('Number of Tweets')
    plt.title("Sentiment Analysis from Tweets")
    plt.show()

# Function to plot tweets and their polarity on histogram and generate a csv file also.
def plot_on_histogram( data, pos, neg ):

    #columns is optional arguement , see documentation
    sentiment_df= pd.DataFrame(data,columns=["Sentiment","Tweet"])

    # convert dataframe to csv
    sentiment_df.to_csv('analysis.csv')

    fig = plt.figure()
    ax = fig.add_subplot(111) 
    # Concise form of these two lines is given below, though it is not necessary
    fig, ax = plt.subplots(figsize=(8, 6))
    # Plot histogram with break at zero
    sentiment_df.hist(bins=[-1, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1],
                 color="red")
    plt.xlabel('Sentiment Polarity')
    plt.ylabel('Number of Tweets')
    plt.title("Sentiment Analysis from Tweets")
    plt.show()


if __name__ == '__main__':
    authentication()


