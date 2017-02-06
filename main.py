
import json
from urllib.request import urlopen

def get_random_page():
    response = urlopen('https://en.wikipedia.org/w/api.php?action=query&format=json&generator=random&grnnamespace=0&prop=info|links|linkshere&inprop=url')
    json_string = response.read().decode('utf-8')
    data = json.loads(json_string)
    pages = data['query']['pages']
    page = pages[list(pages)[0]]
    return page

def get_start_page():
    return get_random_page()

def get_end_page():
    return get_random_page()

start_page = get_start_page()
end_page = get_end_page()

print('Navigate from start page to end page before your opponent!' )
print('Start: ' + start_page['title'] + ': ' + start_page['canonicalurl'])
print('End: ' + end_page['title'] + ': ' + end_page['canonicalurl'])
