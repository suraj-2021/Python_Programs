import re

url_regex = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
url_pattern = re.compile(url_regex)
