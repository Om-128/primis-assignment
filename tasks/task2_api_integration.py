import os
import sys
from custom_exception import CustomException

import requests
import time
from datetime import datetime, timedelta

URL = "https://jsonplaceholder.typicode.com/posts"

class APIClient:

    def __init__(self):
        self.URL = URL
        self.cache_data = None
        self.cache_time = None
        self.cache_duration = timedelta(minutes=5)


    # Fetch All Posts
    def fetch_all_posts(self):
        try:
            # First check cache
            if self.cache_data and self.cache_time:
                if datetime.now() - self.cache_time < self.cache_duration:
                    print("Using cached data")
                    return self.cache_data

            # Simple Retry Mechanism
            max_attempts = 3

            for attempt in range(1, max_attempts + 1): 
                try:
                    response = requests.get(self.URL, timeout=5)
                    response.raise_for_status()
                    
                    data = response.json()

                    # Save data to cache
                    self.cache_data = data
                    self.cache_time = datetime.now()

                    return data

                except Exception as e:
                    print(f"Attempt {attempt} failed.")

                    if attempt == max_attempts:
                        raise CustomException(e, sys)
                    
                    time.sleep(1)
        except Exception as e:
            raise CustomException(e, sys)

    # Get All Posts
    def get_all_posts(self, posts):
        try:
            return len(posts)
        except Exception as e:
            raise CustomException(e, sys)

    # Get Post by User_ID
    def post_by_id(self, posts, user_id=1):
        try:
            return [post for post in posts if post["userId"] == user_id]
        except Exception as e:
            raise CustomException(e, sys)

    # Get Post by longest title
    def longest_post_title(self, posts):
        try:
            longest_title_post = max(posts, key=lambda x : len(x["title"]))
            return longest_title_post["title"]
        except Exception as e:
            raise CustomException(e, sys)

    # Create New Post
    def create_new_post(self, userId, title, body):
        try:
            post_data = {
                "userId": userId,
                "title": title,
                "body": body
            }

            response = requests.post(self.URL, json=post_data, timeout=3)
            response.raise_for_status()

            return response.json()

        except Exception as e:
            raise CustomException(e, sys)
        

if __name__=="__main__":

    client = APIClient()
    
    print("\n-------------------------------------------------------------\n")

    print("FIRST CALL - API Call Successfull...")
    posts1 = client.fetch_all_posts()

    print("\n-------------------------------------------------------------\n")

    print("\nSECOND CALL")
    posts2 = client.fetch_all_posts()
    
    print("\n-------------------------------------------------------------\n")

    if posts1 or posts2:
        print("All Posts Fetched Successfully...")
    else:
        print("Failed to fetch Posts")

    print("\n-------------------------------------------------------------\n")

    print("Total Posts:", client.get_all_posts(posts1))

    print("\n-------------------------------------------------------------\n")

    print("Posts by user ID:", client.post_by_id(posts1, user_id=1))

    print("\n-------------------------------------------------------------\n")

    print("Longest Post Title:", client.longest_post_title(posts1))

    print("\n-------------------------------------------------------------\n")

    print("New Post By User:", client.create_new_post(userId=28, title="Test Post Title", body="This is a test post"))

    print("\n-------------------------------------------------------------\n")