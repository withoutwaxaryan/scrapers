from bs4 import BeautifulSoup
import requests

# html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=")
# print(html_text)

html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
# print(html_text)  # brings the whole html code

soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('li', class_= "clearfix job-bx wht-shd-bx")
# print(jobs)

# job = soup.find('li', class_= "clearfix job-bx wht-shd-bx")
# print(job)

for job in jobs:

    company_name = job.find('h3', class_ = 'joblist-comp-name').text
    # print(company_name.text)

    skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
    print(skills)

    published_date = job.find('span', class_= 'sim-posted').span.text

    more_info = job.header.h2.a['href']

    print(f'''
        Company Name : {company_name}, 
        Skills : {skills}
    ''')

    # for index, job in enumerate(jobs):
    