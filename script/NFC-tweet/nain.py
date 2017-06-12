#! -*- coding: utf-8 -*-
from google.appengine.ext import db

import webapp2, tweepy

#Twitterコンシュマーキー
CONSUMER_KEY = 'vNC4991tCDq9Z8l0UTIRnu3TN'
CONSUMER_SECRET = 'wiYpSOlK64ZBA0AFgk3PTscl66KutRxxnjfKlyAFl6jk9NnrXZ'

class modelUser(db.Model): #Twitterアカウント情報格納用のモデル定義
    twitter_name = db.StringProperty()
    access_key = db.StringProperty()
    access_secret = db.StringProperty()
    date = db.DateTimeProperty(auto_now_add=True)

class mainHandler(webapp2.RequestHandler):
    def get(self):
        #認証開始ボタンを出力
        self.response.out.write('<form method="POST" action="./"><button type="submit">認証</button></form>')
    def post(self):
        #Tweepyにコンシュマーキーをセット
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        try:
            redirect_url = auth.get_authorization_url() #OAuth認証用URLを取得
            self.redirect(redirect_url) #OAuth認証用URLにリダイレクト
        except Exception as e:
            self.response.out.write('エラ')

class callbackHandler(webapp2.RequestHandler):
    def get(self):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        try:
            #なんか受け取ったパラメタをTweepyに色々と認証させる
            auth.set_request_token(self.request.get('oauth_token'), self.request.get('oauth_verifier'))
            auth.get_access_token(self.request.get('oauth_verifier'))
            access_key = auth.access_token.key
            access_secret = auth.access_token.secret
            auth.set_access_token(access_key, access_secret)
            api = tweepy.API(auth) #以降、このオブジェクトから色々情報を取得できる

            modeluser = modelUser().get_or_insert(str(api.me().id)) #モデルキーをTwitter内部IDに設定
            modeluser.twitter_name = api.me().screen_name #Twitter Id
            modeluser.access_key = access_key #アクセストークンキー
            modeluser.access_secret = access_secret #アクセスシークレットトークンキー
            modeluser.put() #データベースに反映

            self.response.out.write('登録完了')
        except Exception as e:
            self.response.out.write('エラ')

app = webapp2.WSGIApplication([ ('/', mainHandler), ('/callback', callbackHandler) ])