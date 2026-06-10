with open('work.html', 'r', encoding='utf-8', errors='ignore') as f:
    s = f.read()

# Fix Kutty Jetty - has a page
s = s.replace('href="https://www.kuttyjetty.com" target="_blank" class="proj-link">View Site', 'href="kutty-jetty.html" class="proj-link">View Case Study')

with open('work.html', 'w', encoding='utf-8', errors='ignore') as f:
    f.write(s)

print('done')
