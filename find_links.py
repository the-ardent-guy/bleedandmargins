with open('work.html', 'r', encoding='utf-8', errors='ignore') as f:
    s = f.read()

import re

# Find all proj-title values and their nearby links
titles = [(m.start(), m.group(1)) for m in re.finditer(r'class="proj-title">([^<]+)', s)]
print('All project titles found:')
for pos, title in titles:
    # find nearest proj-link href after this title
    chunk = s[pos:pos+600]
    hrefs = re.findall(r'href="([^"]+)".*?proj-link', chunk, re.DOTALL)
    print(f'  {title!r} -> {hrefs}')
