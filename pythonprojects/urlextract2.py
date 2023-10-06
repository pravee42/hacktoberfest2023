from urllib.request import urlopen
page=urlopen("https://hacktoberfest.com")

sourcecode=page.read()
print(sourcecode)