from wappalyzer import Wappalyzer, WebPage
url = 'https://example.com'
webpage = WebPage.new_from_url(url)
wappalyzer = Wappalyzer.latest()
# Analyze the webpage
technologies = wappalyzer.analyze(webpage)
for technology in technologies:
    print(f'Technology: {technology}')