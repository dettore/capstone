
Week 5
------
What progress have you made in obtaining your data, cleaning it up, and beginning your analysis? Did you decide to use a different data source than the one you had identified in Week 3? What challenges have you encountered so far?

I chose to use a different dataset than the one that I identified in Week 3 (the Yelp API).   It didn't quite have the data available for what I thought that I wanted to do with it, and the Yelp site already provides for a visualization tool with Google Maps.  

There was a dataset on kaggle.com that I found that looks to be interesting (https://www.kaggle.com/ryanxjhan/cbc-news-coronavirus-articles-march-26).   It is a COVID-19 News Articles Open Research Dataset, with links to nearly 7,000 news articles from CBC News about the coronavirus-related infectious diseases.

The data in the links file is just a list of URLs, so it is pretty clean already.   I was able to crawl the URLs on the CBC news site and use Beautiful Soup to extract the title for each article.   I then stored the URL, tag and title text in a database for later analysis.   I may end up using it to do some sort of word frequency visualization, or perhaps a simple sentiment analysis using NLTK. 

About this file
Contains more than 8,000 links for the news articles. 7,000 of them have been selected in the news dataset. The rest are discarded due to lack of text since they provide videos.

Purpose

In response to the COVID-19 pandemic, a free resource of over 7,000 news articles with full text, about COVID-19 and the coronavirus family of viruses for use by the global research community.

This dataset is intended to mobilize researchers to apply recent advances in natural language processing to generate new insights in support of the fight against this infectious disease and future pandemics. The news articles will be updated weekly and more news agencies covering more countries will be continuously added at a later date.

The dataset comes from CBC news's own search result regarding coronavirus. 
https://www.cbc.ca/search?q=coronavirus&section=news&sortOrder=relevance
https://www.cbc.ca/search?q=covid-19&section=news&sortOrder=relevance

A tailored news crawler was used to obtain the search results. Note that some news articles do not have text and provide videos and they are not crawled.
https://github.com/ryanxjhan/cbc-news-crawler-for-nlp

links.txt

About this file
Contains more than 8,000 links (url) for the news articles. 7,000 of them have been selected in the news dataset. The rest are discarded due to lack of text since they provide videos.

news.csv

About this file
It contains the authors, the title, the publish date, the description about the story, the main story, and the url.

index - unique sequential number starting with 0
authors - article authors
title - news title
publish_date - date published
description - short description of the story
text - main story
url - story url

Sentiment Analysis with NLTK
https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk
https://www.datacamp.com/community/tutorials/simplifying-sentiment-analysis-python









