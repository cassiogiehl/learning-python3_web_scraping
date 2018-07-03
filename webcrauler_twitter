import tweepy
import csv
import time

consumer_key = "W6TzJ9TGTS8Ptkbv1AXYksqcx"
consumer_secret = "NLcu37UAncU24IBDeMBwXLjbi2MnOgV5xaSYONsAMVZYmLKk30"
acess_token = "228233387-trdWazlwulSVXtjk5yNCN7gQoetTxgI7wqx5ZpDG"
acess_token_secret = "xSF0qD70kLTryqyNljfceHcyN4WjxR4Lgyv8EEKr7fdxA"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(acess_token, acess_token_secret)

api = tweepy.API(auth)

arq = csv.writer(open("base_teste.csv", "w"))
arq2 = open("base_teste.json", "w")

row = []

statuses = tweepy.Cursor(api.search, q="#orlando", since="2018-06-25", until="2018-06-27", lang="en").items()

while True:
    try:
        status = statuses.next()
        row = str(status.user.screen_name),str(status.created_at),str(status.text),status.geo
        arq.writerow(row)

        arq2.write(str(status))
        arq2.write('\n')

        exit()

    except tweepy.TweepError:
        print("wait 15 minutes...")
        time.sleep(60*15)
        continue
    except StopIteration:
        print("Acabou")
        break
