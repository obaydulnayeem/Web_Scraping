from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Java+%2C+Python&txtLocation=')
html_content = html_text.text  # Access the .text attribute to get the HTML content

soup = BeautifulSoup(html_content, 'html.parser')  # Change 'html5lib' to 'html.parser'
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    company_name = job.find('h3', class_='joblist-comp-name')
    if company_name:
        print(company_name.text)
    else:
        print("Company name not found")
