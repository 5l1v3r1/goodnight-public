import datetime
import tweepy
import config
import random
import schedule
import time
client = tweepy.Client(config.BEARER_TOKEN, config.API_KEY, config.API_KEY_SECRET, config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET, wait_on_rate_limit='true')
following = []
users = []
tweet = 'gn @akaTimmay'
blacklist = ['StimpyPvP', 'ezPimpy', 'chubsgrl']
priority = ['seakaori', 'mahvele', 'OddOW_', 'xyobun']

def find_following():
    global following
    temp = client.get_users_following(1197975170, max_results=1000)
    for person in temp.data:
        following.append(person.username)
    for blacklistUser in blacklist:
        following.remove(blacklistUser)
    for priorityUser in priority:
        following.append(priorityUser)
        following.append(priorityUser)
        following.append(priorityUser)


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


def post_tweet():
    global tweet
    client.create_tweet(text=tweet, user_auth=True)


def work():
    find_following()
    pick_users()
    create_tweet()
    post_tweet()
    print("A goodnight tweet has been posted:")
    print("\tUsers: " + str(len(users)))
    print("\tCharacter count: " + str(len(tweet)))
    print(tweet)


if __name__ == '__main__':
    schedule.every().day.at("23:00:00").do(work)
    while True:
        schedule.run_pending()
        time.sleep(10)

