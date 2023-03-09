# A row is called a page !!!

import requests
from datetime import datetime, timezone

notion_tocken = 'secret_cIGknvyxjpd1ucDAHSFSuJWLKgAkfsKPZ8IgyQCHOoY'
db_id ='8c5db08cf6bb4113b5a64277dfb00623'

headers = {
    "Authorization": "Bearer " + notion_tocken,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

def get_pages(num_pages=None):
    url = f"https://api.notion.com/v1/databases/{db_id}/query"
    get_all = num_pages is None
    page_size = 100 if get_all else num_pages
    payload = {"page_size": page_size}
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    results = data["results"]
    while data["has_more"] and get_all:
        payload = {"page_size": page_size, "start_cursor": data["next_cursor"]}
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
    return results

def create_page(data: dict):
    create_url = "https://api.notion.com/v1/pages"

    payload = {"parent": {"database_id": db_id}, "properties": data}

    res = requests.post(create_url, headers=headers, json=payload)
    # print(res.status_code)
    return res

def printAll():
    print("\nSTUDY TRACKER")
    for page in pages:
        props = page["properties"]
        sl_no = props['SlNo']['title'][0]['text']['content']
        date = props["Date"]["date"]["start"]
        ai_hr = props["AI"]["number"]
        math_hr = props["Mathematics"]["number"]
        college_hr = props["College"]["number"]
        tot_hr = props["College"]["number"]
        print(f"{sl_no}:{date}  AI:{ai_hr} Mathematics:{math_hr} College:{college_hr}  TOTAL:{tot_hr}")

# MAIN
pages = get_pages()
for page in pages:
    props = page["properties"]
    sl_no = props['SlNo']['title'][0]['text']['content']
    date = props["Date"]["date"]["start"]
    ai_hr = props["AI"]["number"]
    math_hr = props["Mathematics"]["number"]
    college_hr = props["College"]["number"]
    # props["College"]["number"] = ai_hr + math_hr + college_hr
    tot_hr = props["College"]["number"]
    

title = "Test Title"
description = "Test Description"
published_date = datetime.now().astimezone(timezone.utc).isoformat()
data = {
    "URL": {"title": [{"text": {"content": description}}]},
    "Title": {"rich_text": [{"text": {"content": title}}]},
    "Published": {"date": {"start": published_date, "end": None}}
}

# create_page(data)
printAll()