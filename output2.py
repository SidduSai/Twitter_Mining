from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey = '4hYGWHj7peoa0kBff9VfA1Vw6'
csecret = 'aSUl3A93jUAp0aQ6RdlfRiGynbnKGO6Ot9Eha9IVaFzNj8N0c9'
atoken = '786347486155649025-YnJqGH3RUq1NKQIlBhsuCmLPHmY1xAb' 
asecret = 'Lb3JvS4Ui2Vhlfh1A8PjM7PZKUA1xjRn2wr27JztG8tZO'

class listener(StreamListener):

        def on_data(self, data):
                try:
                        print(data)
                        tweet = data.split(',"text":"')[1].split('","source')[0]
                        print (data)
                        #saveThis = str(time.time())+'::'+tweet
                        saveFile = open('tweetDB.csv','a')
                        saveFile.write(data)
                        saveFile.write('\n')
                        saveFile.close()
                        return True
                except BaseException(e):
                        print ('failed ondata',str(e))
                        time.sleep(5)
                

        def on_error(self, status):
                print(status) 


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Donald Trump"])
