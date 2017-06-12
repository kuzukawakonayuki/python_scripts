#!/usr/bin/env python
# -*- coding: utf-8 -*-

#ライブラリインポート
import sys
import tweepy
import datetime
import webapp2

#キーセット
CONSUMER_KEY = "vNC4991tCDq9Z8l0UTIRnu3TN"
CONSUMER_SECRET = "wiYpSOlK64ZBA0AFgk3PTscl66KutRxxnjfKlyAFl6jk9NnrXZ"
ACCESS_TOKEN = "3240741168-zORyUwUXUT4tijvt7iz1NnAYhNlYCfrYoGy4auN"
ACCESS_SECRET = "U6LrcULlWzoFUoBRRmSLNqU8H7DKphdEPPCNjxH6J3WDR"
print(u"開始")

class HelloWorld(webapp2.RequestHandler):
    def get(self):
        #tweepyにキーセット
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        api = tweepy.API(auth)
        TIME = datetime.datetime.today()
        api.update_status(TIME)
        self.response.write(u"投稿しました")

applications = webapp2.WSGIApplication([
    ('/', HelloWorld),
    ], debug=True)


#以下ローカル用鯖建て
def main():
    from paste import httpserver
    httpserver.serve(applications, host='127.0.0.1', port='8080')

if __name__ == '__main__':
    main()