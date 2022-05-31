import tweepy
import config
import random
import time
client = tweepy.Client(config.BEARER_TOKEN, config.API_KEY, config.API_KEY_SECRET, config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET, wait_on_rate_limit='true')
following = []
users = []
tweet = 'Goodnight @akaTimmay'


def find_following():
    global following
    temp = client.get_users_following(1197975170, max_results=1000)
    for person in temp.data:
        following.append(person.username)

def pick_users():
    charCount = 0
    while True:
        random.seed()
        randomIndex = random.randint(0, len(following) - 1 - len(users))
        randomUser = following[randomIndex]
        following.remove(randomUser)
        charCount += len(randomUser) + 2
        if charCount <= config.TWEET_LENGTH:
            users.append(' @' + randomUser)
            continue
        else:
            break

def create_tweet():
    global tweet
    for user in users:
        tweet += user
    client.create_tweet(text=tweet, user_auth=True)


if __name__ == '__main__':
    find_following()
    pick_users()
    create_tweet()
    print("A goodnight tweet has been posted:")
    print("\tUsers: " + str(len(users)))
    print("\tCharacter count: " + str(len(tweet)))
    print(tweet)
