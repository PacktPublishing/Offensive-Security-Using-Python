# Parsing HTML with BeautifulSoup
from bs4 import BeautifulSoup

html = """
<html>
<head>
<title>Sample Page</title>
</head>
<body>
<p>This is a sample paragraph.</p>
</body>
</html>
"""

# Parse the HTML
soup = BeautifulSoup(html, "html.parser")
# Extract the text from the paragraph
paragraph = soup.find("p")
print(paragraph.text)