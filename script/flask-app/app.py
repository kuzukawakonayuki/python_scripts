#coding: UTF-8
import tweepy
from tweepy import OAuthHandler, API
import os
import sys
import logging
from flask import Flask, render_template, request, redirect, session

C_K = "vNC4991tCDq9Z8l0UTIRnu3TN"
C_S = "wiYpSOlK64ZBA0AFgk3PTscl66KutRxxnjfKlyAFl6jk9NnrXZ"
C_URL = "http://127.0.0.1:5000/callback"

logging.warn("app start!")
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = "0530"

def set_R_T(key):
    return session.get(key)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/auth",methods=["GET"])
def auth():
    auth = tweepy.OAuthHandler(C_K, C_S, C_URL)

    try:
        api = tweepy.API(auth)
        R_URL = auth.get_authorization_url()
        session["R_T"] = auth.request_token
    except tweepy.TweepError, e:
        logging.error(str(e))
        return{}


    return session.get("R_T", "not set")



@app.route("/callback")
def callback():
    token = session.pop("R_T")
    verifier = request.args.get("oauth_verifier")

    #if token is None or verifier is None:
     #return False

    auth = tweepy.OAuthHandler(C_K, C_S, C_URL)
    #auth.access_token = token

    #try:
        #auth.get_access_token(verifier)
    #except tweepy.TweepError, e:
        #logging.error(str(e))
        #return{}

    api = tweepy.API(auth)
    return "callback"


if __name__ == "__main__":
    app.run()