from form_launcher.scraper import WebScraper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from mock.utils import GetRandomChoice, GetRandomPersonalChoices

class GFormFiller(WebScraper):
    def perform_scraping(self):
        time.sleep(4) # let dom load
        next_button = self.driver.find_element(By.CSS_SELECTOR, "div.uArJ5e")
        next_button.click()

        time.sleep(4) # let dom load
        
        iterator = 0

        for _ in range(7): # 6 sections - the last one (personal info is seperate logic)
            # find form and loop through questions
            section_one_form = self.driver.find_elements(By.CSS_SELECTOR, "div.lrKTG div.o3Dpx div.Qr7Oae")
            for question in section_one_form:
                choice = GetRandomChoice(i=iterator) # getting question
                answers = question.find_elements(By.CSS_SELECTOR, "label.T5pZmf")
                
                for answer in answers:
                    try:
                        labelNo = answer.find_element(By.CSS_SELECTOR, "div.Zki2Ve")
                        if choice == int(labelNo.text):
                            answer.find_element(By.CSS_SELECTOR, "div.eRqjfd").click()
                            pass

                        pass
                    except Exception as e:
                        pass
                iterator += 1


            time.sleep(10)
            # go next section
            next_buttons = self.driver.find_elements(By.CSS_SELECTOR, "div.uArJ5e") 
            for button in next_buttons:
                try:
                    if button.text == "Berikutnya":
                        button.click()
                except:
                    pass
        
        # filling out personal info
        time.sleep(4)
        personal_info_form = self.driver.find_elements(By.CSS_SELECTOR, "div.lrKTG div.o3Dpx div.Qr7Oae")

        for idx, question in enumerate(personal_info_form):
            q = idx + 1
            answers = question.find_elements(By.CSS_SELECTOR, "div.d7L4fc")
            random_choice = GetRandomPersonalChoices(q)

            for idx, answer in enumerate(answers):
                q = idx + 1 
                try:
                    if random_choice == q:
                        answer.click()
                    pass
                except:
                    pass
            pass
        
        # go next section
        next_buttons = self.driver.find_elements(By.CSS_SELECTOR, "div.uArJ5e") 
        for button in next_buttons:
            try:
                if button.text == "Kirim":
                    button.click()
            except:
                pass
        
        time.sleep(3)
        
        