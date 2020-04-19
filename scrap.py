import requests, re
from bs4 import BeautifulSoup


languages = ["Java", "Python", "C++", "Ruby", "Javascript", "PHP", ".NET", "HTML", "React", "Angular", "Vue.js", "Django", "SQL", "Visual Basic", "C#"]

class Website():

    def __init__(self, name, base_url, tag, css_class, css_id):
        self.name = name
        self.base_url = base_url
        self.tag = tag
        self.css_class = css_class
        self.css_id = css_id

    def scrap(self, lang):
        r = requests.get(self.base_url[0] + lang + self.base_url[1])
        c = r.content
        return BeautifulSoup(c, "html.parser")


class pracuj_pl(Website):

    def __init__(self, name="pracuj.pl", base_url=["https://www.pracuj.pl/praca/", ";kw?rd=0"], 
                tag="span", css_class="results-header__offer-count-text-number", css_id=""):
        super().__init__(name, base_url, tag, css_class, css_id)

    def scrap(self, lang):
        soup = super().scrap(lang)
        return soup.find(self.tag, class_=self.css_class).text


class indeed(Website):

    def __init__(self, name="pl.indeed.com", base_url=["https://pl.indeed.com/jobs?q=", "&l="], 
                tag="div", css_class="", css_id="searchCountPages"):
        super().__init__(name, base_url, tag, css_class, css_id)

    def scrap(self, lang):
        soup = super().scrap(lang)
        num_word = soup.find(self.tag, id=self.css_id).text
        regex = re.compile(r'\d+ ofert')
        num = regex.search(soup.find(self.tag, id=self.css_id).text)[0].split()[0]
        return num


class bulldogjob_pl(Website):

    def __init__(self, name="bulldogjob.pl", base_url=["https://bulldogjob.pl/companies/jobs/s/skills,", ""], 
                tag="div", css_class="job-details", css_id=""):
        super().__init__(name, base_url, tag, css_class, css_id)

    def scrap(self, lang):
        soup = super().scrap(lang)
        all_offers = 0

        try:
            pages = soup.find("ul", {"class": "pagination"}).find_all("a")[-2].text

            for page in range(1, int(pages)+1):
                r = requests.get(self.base_url[0] + lang + "?page=" + str(page))
                c = r.content
                soup = BeautifulSoup(c, "html.parser")
                offers = soup.find_all(self.tag, class_=self.css_class)
                all_offers += int(len(offers))

            return all_offers

        except AttributeError:
            offers = soup.find_all(self.tag, class_=self.css_class)
            all_offers += int(len(offers))
            return all_offers


def scrap_all(lang):
    pracuj = pracuj_pl()
    indeed_com = indeed()

    results = {pracuj.name: pracuj.scrap(lang), indeed_com.name: indeed_com.scrap(lang)}
    return results
