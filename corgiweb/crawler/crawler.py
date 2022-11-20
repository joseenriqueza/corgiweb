from typing import List
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from corgiweb.crawler.sitemap import * 
from corgiweb.crawler.robotstxt import *

class Crawler:

    def __init__(self,
                 domain: str,  # Website domain address
                 user_agent: str = "corgiweb",  # User-Agent used to call the website
                 retrieve_sitemap: bool = False,  # Get the sitemap from the domain address
                 sitemap_url: str = None,  # sitemap url
                 retrieve_robots: bool = False,  # Get the robots.txt from the domain address
                 robots_url: str = "",  # Robots.txt url from the website
                 nodes_to_search: List[str] = [],  # JSON file with the URLS to search
                 retrieve_visited_nodes: bool = False,  # Get the visited nodes from the database
                 visited_nodes: set = ()):  # Send the already visited nodes
        self.domain = domain
        self.user_agent = user_agent
        self.retrieve_sitemap = retrieve_sitemap
        self.sitemap_url = sitemap_url
        self.retrieve_robots = retrieve_robots
        self.robots_url = robots_url
        self.nodes_to_search = nodes_to_search
        self.retrieve_visited_nodes = retrieve_visited_nodes
        self.visited_nodes = visited_nodes

        # Requests
        self.user_fake_agent = UserAgent()

        # Results
        self.new_urls = set() # TODO: Create own class for new_urls

        # start_robots
        self.robots_i = Robots(robots_url= robots_url, user_agent= user_agent)

        # start_sitemap
        if sitemap_url:
            self.sitemap_i = Sitemap(sitemap_url=sitemap_url)
            self.start_sitemap()

    def start_sitemap(self):
        """
        Get all sitemaps (For demo purposes we are only retrieving from the URL 1
        """
        self.sitemap_i.get_urls_from_sitemap_list(retrieve_only_from_index=[0])

        for url in self.sitemap_i.sitemap_list:
            if url not in self.new_urls and self.robots_i.can_fetch(url=url):
                self.new_urls.add(url)

    def start_bfs(self):
        # TODO: enable customization of BFS level search
        """
        Start the BFS search on each item on the queue(It's really just searching for now childs for each node)
        """
        for url in self.nodes_to_search:
            # TODO: Create a request Class to handle all the connections with websites & Headers
            headers = {
                'User-Agent': self.user_fake_agent.google,
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "es-US,es;q=0.9",
                "cache-control": "max-age=0",
                'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"'
            }
            r = requests.get(url, headers=headers).text
            soup = BeautifulSoup(r, 'html.parser')

            for link in soup.find_all('a'):
                url = link.get('href')
                # TODO: handle find new urls outside of the domain
                try:
                    if url and self.domain in url and url not in self.new_urls and self.robots_i.can_fetch(url=url):
                        self.new_urls.add(url)
                except Exception as e:
                    Exception(e)
