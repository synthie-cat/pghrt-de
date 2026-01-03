#source: @jonesetc.com ty king you're an icon
from bs4 import BeautifulSoup

# Parse the file into soup
with open('export/index.html', 'r', encoding='utf-8') as fin:
    soup = BeautifulSoup(fin, 'html.parser')

# Create menu button, header, and nest
menu = soup.new_tag(
    'button',
    id='menu',
    onclick='document.getElementById(\'sidebar\').classList.toggle(\'show\')',
    string='☰',
)
header = soup.new_tag('div', **{'class':'header'})
header.append(menu)

# Create toggle buttons, header, and nest
toggles = soup.new_tag('div', **{'class':'togglebuttons'})
menu = soup.new_tag(
    'button',
    id='theme-toggle',
    string='☀',
)
toggles.append(menu)
menu = soup.new_tag(
    'button',
    id='font-toggle',
    string='Aa',
)
toggles.append(menu)

# Extract nav
toc = soup.body.find('div', class_='ltx_page_main').nav.extract()

# need id to grab to make the menu button work
toc['id'] = 'sidebar'

# correcting a bug in latexml that drops em dash prefixes on toc in html output
toc_emdashes = toc.select('a[href*="SSx"] > span')
for line in toc_emdashes:
    line.string.insert_before('—')

# adding a toast
toast = soup.new_tag (
    "div",
    id="snackbar",
    string="Link Copied!"
)

# add return to ref button
ref = soup.new_tag (
    "div",
    id="return",
    title="Return to previous position"
)

# prepend bottom with all the silly stuff i add
soup.body.insert(0, toast, ref, toggles, header, toc)

# Add header info tags
# i don't know if there's a better way to do all of these in a batch but like eh w/e

head_meta = soup.new_tag(
    'meta',
    property='og:title',
    content='A Practical Guide To Feminizing HRT',
)
soup.head.append(head_meta)
soup.head.append("\n")

head_meta = soup.new_tag(
    'meta',
    property='og:type',
    content='website',
)
soup.head.append(head_meta)
soup.head.append("\n")

head_meta = soup.new_tag(
    'meta',
    property='og:url',
    content='https://www.pghrt.diy',
)
soup.head.append(head_meta)
soup.head.append("\n")

head_meta = soup.new_tag(
    'meta',
    property='og:image',
    content='/img/cover.png',
)
soup.head.append(head_meta)
soup.head.append("\n")

head_meta = soup.new_tag(
    'meta',
    property='og:description',
    content='The futile attempt at answering every possible question for someone looking to trans their sex.',
)
soup.head.append(head_meta)
soup.head.append("\n")

head_meta = soup.new_tag(
    'link',
    rel='icon',
    type='image/png',
    href='/img/favicon.png'
)
soup.head.append(head_meta)
soup.head.append("\n")

head_meta = soup.new_tag(
    'link',
    rel='stylesheet',
    type='text/css',
    href='pghrtcss.css'
)
soup.head.append(head_meta)
soup.head.append("\n")

head_meta = soup.new_tag(
    'script',
    type='text/javascript',
    src='pghrtjs.js',
    defer='true'
)
soup.head.append(head_meta)
soup.head.append("\n")

# find all the section and question headers then add a click to copy icon
for element in soup.find_all(["h2", "h3"]):
    #find the id of its section
    hash = element.parent['id']

    new_chain = soup.new_tag(
        'a',
        **{'class':'chain'},
        href="#" + hash,
        title="Click to copy a link here",
        onclick="copyURI(event)",
        string=' 🔗',
    )

    element.append(new_chain)

# replacing \DTMNow with the footer timestamp because there aren't latexml
# bindings for the datetime2 package and i want it to look prettier
# i also remove the double space because it REALLY annoys me. i already sent
# in an issue about it though. eventually i can remove that line lol
dtm = soup.body.find('span', class_='ltx_ERROR undefined')
dtm['class'] = 'undefined'
timestamp = soup.footer.div.contents[0]
postmarked = timestamp.text.replace("Generated  on ", "Generated on ")
timestamp.replace_with(postmarked)
dtm.string = postmarked.replace("Generated on ", "").replace(" by ", "")

# i'm at soup
print("soup")

# Write the updated soup back out to the file
with open('export/index.html', 'w', encoding='utf-8') as fout:
    fout.write(str(soup))