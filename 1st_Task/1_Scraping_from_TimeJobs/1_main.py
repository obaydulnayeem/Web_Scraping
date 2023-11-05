from bs4 import BeautifulSoup
import requests


# with open('home.html', 'r') as html_file:
#     content = html_file.read()
#     print(content)

#     # soup = BeautifulSoup(content, 'lxml')
#     # # # print(soup.prettify())

#     # course_cards = soup.find_all('div', class_='card')
#     # for course in course_cards:
#     #     course_name = course.h5.text
#     #     course_price = course.a.text.split()[-1]
#     # #     print(f'{course_name} costs {course_price}')

#     # tags = soup.find_all('h5')
#     # print(tags)


html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Java+%2C+Python&txtLocation=')
# print(html_text)
  
soup = BeautifulSoup(html_text, 'html5lib')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
print(jobs)