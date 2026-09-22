import requests
class Post:
    def __init__(self):
        self.blog_url = "https://api.npoint.io/c790b4d5cab58020d391"


    def fetch_posts(self):

        response = requests.get(self.blog_url)

        print("URL:", self.blog_url)
        print("Status:", response.status_code)
        print("Content:", response.text[:500])

        all_posts = response.json()
        return all_posts