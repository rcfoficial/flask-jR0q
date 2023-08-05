# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from bs4 import BeautifulSoup

number = "995571776826"
url_wc = f"https://anonymsms.com/number/{number}"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url_wc, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    table_rows = soup.select('.table-panel tbody tr')

    for row in table_rows:
        columns = row.find_all('td')

        if len(columns) >= 2:
            from_de = columns[0].get_text(strip=True)
            content_message = columns[1].get_text(strip=True)

            print("From:", from_de)
            print("Content:", content_message)
            print("---")
else:
    print("Error fetching the page. Status Code:", response.status_code)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
