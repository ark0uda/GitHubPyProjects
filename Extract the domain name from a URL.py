"""Write a function that when given a URL as a string, parses out just the domain name and returns it as a string."""

import re

def domain_name(url):
    res = re.search(r'[./]?(?:www.)?\w+\-?\w+[.]', url)
    return res[0].replace('www', '').replace('.', '').replace('/', '')
