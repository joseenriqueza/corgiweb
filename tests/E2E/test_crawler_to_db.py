import corgiweb as corgi

spiders = {}


spiders["foxnews_com"] = corgi.Crawler(domain="foxnews.com",  # Website domain address
                 user_agent= "*",  # User-Agent used to call the website
                 sitemap_url= "https://www.foxnews.com/sitemap.xml",  # Sitemap url
                 robots_url = "https://www.foxnews.com/robots.txt",  # Robots.txt url from the website
                 nodes_to_search= ["https://www.foxnews.com/politics"])  # JSON file with the URLS to search)

spiders["walmart_com"] = corgi.Crawler(domain="walmart.com",  # Website domain address
                 user_agent= "*",  # User-Agent used to call the website
                 robots_url = "https://www.walmart.com/robots.txt",  # Robots.txt url from the website
                 nodes_to_search= ["https://www.walmart.com/all-departments"])  # JSON file with the URLS to search)

# View results for first search
for k, v in spiders.items():
    v.start_bfs()

    print("---------")
    print("website", k)
    print("num_urls", len(v.new_urls))

# Use previous results, and take items from the queue to search 2 urls more
for k, v in spiders.items():
    v.nodes_to_search = list(v.new_urls)[:min(len(v.new_urls), 2)]
    v.start_bfs()

    print("---------")
    print("website", k)
    print("num_urls", len(v.new_urls))

# Save the data on the custom partition
data = corgi.DataAccess()
data.start_django()
for k, v in spiders.items():
    v.start_bfs()

    for url in v.new_urls:
        data.save_data_on_partitions(k, url)
