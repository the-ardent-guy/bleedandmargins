with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    s = f.read()

s = s.replace('href="work.html#boit"', 'href="boit-club.html"')
s = s.replace('href="work.html#vist"', 'href="vist-labs.html"')
s = s.replace('href="work.html#zeroed"', 'href="zeroed-out.html"')
s = s.replace('href="work.html#koodai"', 'href="koodai-kind.html"')
s = s.replace('href="work.html#oxy99"', 'href="oxy99.html"')

with open('index.html', 'w', encoding='utf-8', errors='ignore') as f:
    f.write(s)

print('done')
