import string

tweet = "I am tired! I like fruit...and milk"
translator = tweet.maketrans(string.punctuation, ' ' * len(string.punctuation))
cleaned_tweet = tweet.translate(translator)

print(cleaned_tweet)
