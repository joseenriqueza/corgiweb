from bs4 import BeautifulSoup as bs
import requests
from typing import List


class Sitemap:

    def __init__(self,
                 domain: str = None,  # Website domain address
                 sitemap_url: str = None,  # Sitemap Url
                 ):
        self.domain = domain
        self.sitemap_url = sitemap_url
        self.sitemap_list = None
        self.urls_list = None

        if not self.sitemap_url:
            raise Exception("It's required 1 URL to create an instance of Sitemap")

        self.__get_sitemap_list()

    def get_urls_from_sitemap_list(self, retrieve_only_from_index: List[str] = []):
        """
        Retrieves all the URLS from each sitemap
        """
        self.urls_list = set()

        i = -1
        while i < len(self.sitemap_list):
            i += 1
            if retrieve_only_from_index and i not in retrieve_only_from_index:
                continue
            soup = bs(requests.get(self.sitemap_list[i]).text, "html.parser")
            urls_tags = soup.findAll("url")

            for tag in urls_tags:
                for element in tag.findAll("loc"):
                    self.urls_list.add(element.text)
        return self.urls_list

    def __get_sitemap_list(self):
        """
        Retrieves all the sitemaps from the sitemap.xml document
        """
        headers = {'User-Agent': '*'}
        soup = bs(requests.get(self.sitemap_url, headers=headers).text, "html.parser")
        sitemap_tags = soup.findAll("sitemap")

        self.sitemap_list = []

        if sitemap_tags:
            for tag in sitemap_tags:
                for element in tag.findAll("loc"):
                    self.sitemap_list.append(element.text)
        else:
            self.sitemap_list.append(self.sitemap_url)