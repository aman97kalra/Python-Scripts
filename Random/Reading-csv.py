import numpy as np   
import re
import pandas as pd  
from textblob import TextBlob
  
# Import dataset 
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t') 

for i in range(0,10):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])  
    print(review)
    analysis = TextBlob(review)
    print(analysis.sentiment.polarity)
