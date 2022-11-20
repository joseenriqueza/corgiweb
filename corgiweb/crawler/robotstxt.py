import urllib.robotparser

from corgiweb.crawler.ignore_path_list import *


class Robots:

    def __init__(self,
                 domain: str = None,  # Website domain address
                 robots_url: str = None,  # Robots Url
                 user_agent: str = "*"  # Default user agent
                 ):
        self.domain = domain
        self.robots_url = robots_url
        self.user_agent = user_agent
        self.robot_parser = None
        self.rate = None
        self.ignore_path_list = self.__read_ignore_path_list_file()  # TODO: read from Database the ignore path list

        if not self.robots_url:
            raise Exception("It's required 1 URL to create an instance of Robots")

        self.__get_robot_parser()

    def can_fetch(self, url: str) -> bool:
        """
        Check if URL is valid based on website and custom rules
        """
        if self.__can_fetch_domain_urlib(url) and self.__can_fetch_custom(url):
            return True
        else:
            return False

    def __can_fetch_domain_urlib(self, url: str) -> bool:
        """
        Check if URL is valid based on website rules
        """
        return self.robot_parser.can_fetch(self.user_agent, url)

    def __can_fetch_custom(self, url: str) -> bool:
        """
        Check if URL is valid based on custom rules
        """
        # TODO: Implement a better way to verify URLs
        for ignore_path in self.ignore_path_list:
            if ignore_path in url:
                return False
        return True

    def __get_robot_parser(self):
        """
        This private method obtains the robot_parser from the website and saves it to self.robot_parser
        """
        self.robot_parser = urllib.robotparser.RobotFileParser()
        self.robot_parser.set_url(self.robots_url)
        self.robot_parser.read()
        self.rate = self.robot_parser.request_rate(self.user_agent)
        # self.robot_parser.crawl_delay(self.user_agent)

        # TODO: research more about robot_parser
        # https://docs.python.org/3/library/urllib.robotparser.html

        self.robot_parser.disallow_all = False

    @staticmethod
    def __read_ignore_path_list_file():
        """
        Read file ignore_path_list.py, and retrieve the list of custom paths to ignore
        """
        return get_ignore_list()
