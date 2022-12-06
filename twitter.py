import tweepy
import keys


def api():
    ''' Authorizes Twitter api keys '''
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_key_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)

    return tweepy.API(auth)


def tweet(api: tweepy.API, message: str, image_path=None):
    ''' Tweet function '''
    if image_path:
        api.update_status_with_media(message, image_path)
    else:
        api.update_status(message)

    print("Tweet was successful!")


#if __name__ == "__main__":
#api = api()
#tweet(api, " ")



