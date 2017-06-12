#!/usr/bin/env python
#coding: UTF-8

#ライブラリインポート
import sys
import tweepy
import webapp2

#キーセット
CONSUMER_KEY = "xY1GztQlN1QRnxojvCfygsGTd"
CONSUMER_SECRET = "8cr9f76uHXQYfefuGIQgLdjTiHRsvAi6j3QnyffzOcMYtlUCgn"
ACCESS_TOKEN = "3240741168-zORyUwUXUT4tijvt7iz1NnAYhNlYCfrYoGy4auN"
ACCESS_SECRET = "U6LrcULlWzoFUoBRRmSLNqU8H7DKphdEPPCNjxH6J3WDR"
print(u"開始")

class HelloWorld(webapp2.RequestHandler):
    def get(self):
        #tweepyにキーセット
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        api = tweepy.API(auth)
        tweet = u"ぬっ"
        tweet.encode("UTF-8")
        api.update_status(tweet)
        self.response.write(u"投稿しました")


applications = webapp2.WSGIApplication([
    ('/', HelloWorld),
    ], debug=True)


#以下ローカル用鯖建て
def main():
    from paste import httpserver
    httpserver.serve(applications, host='127.0.0.1', port='8081')

if __name__ == '__main__':
    main()
