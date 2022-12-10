import instaloader
from datetime import datetime
from itertools import dropwhile, takewhile
import csv

class GetInstagramProfile():
    def __init__(self) -> None:
        self.L = instaloader.Instaloader()


    def get_users_followers(self,user_name):
        print('.................FOLLOWERS COUNT OF ETIC.................................................')

        print('ETIC has', instaloader.Profile.from_username(self.L.context, user_name).followers, 'followers')
        print('.........................................................................................')
    


    def get_post_info_csv(self,username):
        with open(username+'.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            posts = instaloader.Profile.from_username(self.L.context, username).get_posts()
            
            print('This is ETIC\'s ', posts.count, 'post' )
            

            for post in posts:
                
                print("post date: "+str(post.date))
                print("post profile: "+post.profile)
                print("post caption: "+post.caption)
                print("post location: "+str(post.location))

                posturl = "https://www.instagram.com/p/"+post.shortcode
                print("post url: "+posturl)
                writer.writerow(["post",post.mediaid, post.profile, post.caption, post.date, post.location, posturl,  post.typename, post.mediacount, post.caption_hashtags, post.caption_mentions, post.tagged_users, post.likes,  post.url ])
                print("\n\n")
                break

                


if __name__=="__main__":
    cls = GetInstagramProfile()
    cls.get_users_followers("etic_club")
    cls.get_post_info_csv("etic_club")