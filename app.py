from fastapi import FastAPI, Query
from collections import defaultdict
from typing import List

from utils import index_tweets, read_tweets

app = FastAPI()

tweets = read_tweets("10k_tweets.txt")
index = defaultdict(list)
index = index_tweets(tweets)

@app.get("/search/")
async def search(terms: List[str] = Query(...)):
    scores = defaultdict(int)
    print(terms)
    for term in terms:
        for tweet_index in index[term]:
            scores[tweet_index] += 1
    sorted_tweets = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_tweets = [{"tweet": tweets[tweet_index], "score": score} for tweet_index, score in sorted_tweets[:10]]
    return top_tweets
