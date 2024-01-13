from collections import defaultdict
import re


def read_tweets(file_name):
    input_array = []
    # Open the file in read mode
    with open(file_name, "r") as file:
        # Read the contents of the file
        for line in file:
            # Print the current line
            input_array.append(line.strip())
        return input_array


tweets = read_tweets("10k_tweets.txt")
print(len(tweets))


"""
Optimized Approach
"""




def search_index(terms, index):
    tweet_scores = defaultdict(int)
    for term in terms:
        for tweet_index in index[term]:
            tweet_scores[tweet_index] += 1
    return tweet_scores


def index_tweets(tweets):
    index = defaultdict(list)
    for i, t in enumerate(tweets):
        t = t.split()
        for word in t:
            index[word].append(i)
    return index


index = index_tweets(tweets)
terms = ["here's", "sounds"]
scores = search_index(terms, index)
print(scores)

# sort on score
sorted_tweets = sorted(scores.items(), key=lambda x: x[1], reverse=True)

for tweet_index, score in sorted_tweets[:10]:
    print(f"Score: {score}, Tweet: {tweets[tweet_index]}")


"""
OLD Approach
"""


def find_score(tweet, search):
    total_score = 0
    for s in search:
        score = re.findall(s.lower(), tweet.lower())
        total_score += len(score)
    return (total_score, tweet)


scores = []


def find_scores_for_all(tweets, search):
    for t in tweets:
        score = find_score(t, search)
        scores.append(score)


find_scores_for_all(tweets, ["sounds", "missed"])
scores.sort(reverse=True)
