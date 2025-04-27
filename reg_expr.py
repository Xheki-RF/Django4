import re

# text = "eda, b-Edu, pobeda"

# match = re.findall(r".", text)
# # match = re.findall(r"[\S\w]", text)
# print(match)


# Quantificators
# text = "Google, Gooogle, Gooooogle"
# match = re.findall(r"o{2,5}", text)
# match = re.findall(r"Go{,4}gle", text)
# ? makes the algo - minor. Finds the shortest sequences
# match = re.findall(r"o{2,5}?", text)

# text = "стеклянный, стекляный"
# match = re.findall(r"стеклянн?ый", text)

# text = "author=Pushkin A.C.; title=Onegin; price =200; year= 2001"
# match = re.findall(r"(\w*)\s*=\s*([^;]*)", text)

# text = "<p>Picture <img src='bg.jpg'> in text</p>"
# match = re.findall(r"<img\s+src\s*=\s*[^>]*>", text)
# print(match)


# Grouping and saving
# text = "lat = 5, lon=7"
# match = re.findall(r"(lat|lon)\s*=\s*(\d+)", text)

# text = """<point lon="40.4882" lat="52.665" /> <point lon="30.82" lat="57.575" />"""
# match = re.findall(r"<point\s+[^>]*?lon=([\"'])([\d.,]+)\1\s+[^>]*lat=\1([\d.,]+)\1", text)
# match = re.findall(r"<point\s+[^>]*?lon=([\"'])(?P<lon>[\d.,]+)\1\s+[^>]*lat=\1(?P<lat>[\d.,]+)\1", text)
# print(match)


# Flags anc checks
# text = "подоходный налог доход"
# match = re.findall(r"\b(?:прибыль|обретение|доход)\b", text)
# text = """
# <html>
# <head>
# <meta http-equiv="Content-Type " content="text/html; charset=windows-1251">
# <meta name="viewport" content="width=device-width, initial-scale=1.0">
# <html>
# <head>
# <body>
# <p align=center>Hello world!</p>
# console.log()
# </script>
# </body>
# </html>"""

# # match = re.findall(r"^<script.*?>([\w\W]*)(?=</script>)", text, re.MULTILINE)
# match = re.findall(r"[-\w]*[\s]*=[\s]*[\"'][^\"']*(?<![\s])", text, re.MULTILINE)
# match = re.findall(r"([-\w]+)[ \t]*=[ \t]*(?P<q>[\"'])?(?(q)([^\"']+(?<![ \t]))|([^ \t>]+))", text, re.MULTILINE)

# text = "pythonPython pythob"
# match = re.findall(r"(?i)python", text)
# print(match)


# Re.match, re.search
# text = "<font colour=#CC0000"
# match = re.search(r"([\w]+)[\s]*=(#[\d\w]{6})", text)
# print(match.group(1), match.group(2))
# print(match.groups())
# print(match.span())
# print(match.span(1))

# match = re.search(r"(?P<key>[\w]+)[\s]*=[\s]*(?P<value>#[\d\w]{6})", text)
# print(match.groupdict())
# print(match.expand(r"\g<key> - \g<value>"))

# text = "<font colour=#CC0000 gg=#AAFF05"
# print(re.search(r"([\w]+)[\s]*=[\s]*(#[\d\w]{6})\b", text))
# [print(match.groupdict()) for match in re.finditer(r"(?P<key>[\w]+)[\s]*=[\s]*(?P<value>#[\d\w]{6})\b", text)]


# re.match, re.split, re.sub
text = "+7(915)391-43-41"
m = re.match(r"\+7\(\d{3}\)\d{3}-\d{2}-\d{2}", text)
m = re.findall(r"\+7\(\d{3}\)\d{3}-\d{2}-\d{2}", text)
print(m)

t = """<point lon="40.8482" lat="52.6274" />
<point lon="40.8559" lat="52.6361" />; <point lon="40.8614" lat="52.651" />
<point lon="40.8676" lat="52.6585" />, <point lon="40.8672" lat="52.6626" />"""

m = re.split(r"[\n,;]+", t)
print(m)

f = """
Moscow
Kazan
Tver
Samara
Ufa"""

m = re.sub(r"\s*([\w]{2,})\s*", r"<option>\1<option>\n", f)
print(m)