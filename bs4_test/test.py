from bs4 import BeautifulSoup

with open("bs4_test/bs4test.html") as fin:
    html_doc = fin.read()


soup = BeautifulSoup(html_doc, "html.parser")

div_node = soup.find("div", id="content")

links = div_node.find_all("a")

for link in links:
    print(link.name, link["href"], link.get_text())
