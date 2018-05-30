# Created by Aadit Trivedi
# Dependencies
# sudo pip install twython
# sudo pip install nltk

import nltk
nltk.download('vader_lexicon')

def bubbleSort(mylist):
    for num in range(len(mylist)-1,0,-1):
        for i in range(num):
            if mylist[i]>mylist[i+1]:
                temp = mylist[i]
                mylist[i] = mylist[i+1]
                mylist[i+1] = temp
    return mylist

def nltk_sentiment(sentence):
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    nltk_sentiment = SentimentIntensityAnalyzer()
    score = nltk_sentiment.polarity_scores(sentence)
    
    emotion_val = [score['neg'], score['neu'], score['pos'], score['compound']]
    emotion_val = bubbleSort(emotion_val)
    dominant_emotion = emotion_val[3]

    for key in score.keys():
        if score[key] == dominant_emotion:
            if (key == "pos"): print("positive")
            elif (key == "neg"): print("negative")
            elif (key == "neu"): print("neutral")
            elif (key == "compound"): print("compound")
