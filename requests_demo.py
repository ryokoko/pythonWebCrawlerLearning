import requests

url = "https://twitter.com/Google?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor"

# get url info
r = requests.get(url)

r_statusCode = r.status_code
print("status:", r_statusCode, "\n")

r_headers = r.headers
print("headers: ", r_headers, "\n")

r_encoding = r.encoding
print("encoding: ", r_encoding, "\n")

r_text = r.text
print("text: ", r_text, "\n")

r_cookies = r.cookies
print("cookies: ", r_cookies, "\n")
