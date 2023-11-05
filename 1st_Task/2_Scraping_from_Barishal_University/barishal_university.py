from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://bu.ac.bd/?ref=faculty_member')
html_content = html_text.text  # Access the .text attribute to get the HTML content

soup = BeautifulSoup(html_content, 'html.parser')
departments = soup.find_all('div', class_='academic')

with open('bu_departments.txt', 'w', encoding='utf-8') as file:
    for department in departments:
        department_name = department.find('ul')
        
        if department_name:
            file.write(department_name.text.strip() + '\n')
        else:
            file.write("Department name not found\n")
