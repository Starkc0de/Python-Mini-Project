import mechanize
from bs4 import BeautifulSoup

url = "https://www.findandtrace.com/trace-mobile-number-location"

brow = mechanize.browser()
brow.set_handle_robots(False)

brow.open(url)
brow.select_form(name="trace")
brow['mobilenumber'] = str(input("Enter The Mobile Number"))

result = brow.submit()

soup = BeautifulSoup(result.read(),'html.parser')
table_extr = soup.find_all('table', class_='shop_table')

data_extracted = table_extr(0).find('tfoot')
count = 0

for tr in data_extracted:
    count += 1
    th= tr.find('th')
    td= tr.find('td')
    print