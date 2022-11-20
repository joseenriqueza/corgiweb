# TODO: read https://docs.pytest.org/en/6.2.x/fixture.html
# TODO: read https://stackoverflow.com/questions/37353960/pytest-exits-with-no-error-but-with-collected-0-items


import corgiweb as corgi

_Start = corgi.Crawler(domain="foxnews.com",  # Website domain address
                 user_agent= "*",  # User-Agent used to call the website
                 sitemap_url= "https://www.foxnews.com/sitemap.xml",  # Sitemap url
                 robots_url = "https://www.foxnews.com/robots.txt",  # Robots.txt url from the website
                 nodes_to_search= ["https://www.foxnews.com/politics"])  # JSON file with the URLS to search)
def test_name_should_be_tony():
    assert _Start.domain == "foxnews.com"