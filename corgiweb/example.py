
from crawler  import *

spiders = {}

spiders["foxnews.com"] = Crawler(domain="foxnews.com",  # Website domain address
                 user_agent= "*",  # User-Agent used to call the website
                 sitemap_url= "https://www.foxnews.com/sitemap.xml",  # sitemap url
                 robots_url = "https://www.foxnews.com/robots.txt",  # Robots.txt url from the website
                 nodes_to_search= ["https://www.foxnews.com/politics"])  # JSON file with the URLS to search)

spiders["walmart.com"] = Crawler(domain="walmart.com",  # Website domain address
                 user_agent= "*",  # User-Agent used to call the website
                 robots_url = "https://www.walmart.com/robots.txt",  # Robots.txt url from the website
                 nodes_to_search= ["https://www.walmart.com/all-departments"])  # JSON file with the URLS to search)

for k, v in spiders.items():
    v.start_bfs()

    print("website",k)



