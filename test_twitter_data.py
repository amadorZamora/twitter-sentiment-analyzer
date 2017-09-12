#!/usr/bin/env python
import get_twitter_data

## PLACE YOUR CREDENTIALS in config.json file or run this file with appropriate arguments from command line
keyword = 'allende'
time = 'today'
language = 'es'
twitterData = get_twitter_data.TwitterData()
tweets = twitterData.getTwitterData(keyword, time,language)
print tweets
