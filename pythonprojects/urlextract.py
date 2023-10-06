from urllib.request import urlopen

page=urlopen("https://hacktoberfest.com")
print(page.headers)