from bs4 import BeautifulSoup
import requests


def extract_jobs(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        jobs = soup.find_all('td',
                             class_="company position company_and_position")
        del jobs[0]
        for post in jobs:
            #<a>
            title = post.find('a')  #find_all를 하면 한개의멤버를 가진 리스트를 준다 [a] ->오류
            link = title['href']  #link
            position = title.find('h2')  #position
            #<span>
            spans = post.find('span', class_="companyLink")  #find_all 조심
            company = spans.find('h3')  #company

            #<div>list
            region = post.find('div', class_="location")  #region
            job_data = {
                'link': f"https://remoteok.com/{link}",
                'company': company.string,
                'position': position.string,
                'region': region.string
            }
            print(job_data)

    else:
        print("Can't get jobs.")


extract_jobs("rust")
