#Get the hold of all the events in the dictionary of this format
#{0:{'time':'2026-08-28','name':'PyCon JP 2020'},1:{'time':'2020-09-05','name':'PyCon TW 2020'}}

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)

# Pass options to the driver
driver = webdriver.Chrome(options=options)
driver.get("https://www.python.org/")

events = driver.find_elements(By.CSS_SELECTOR,".medium-widget.event-widget.last .shrubbery .menu a")
timings = driver.find_elements(By.CSS_SELECTOR,".medium-widget.event-widget.last .shrubbery .menu time")
# print(events)

upcoming_event = {}
upcoming_events = []
for time,event in zip(timings,events):
    upcoming_event['time'] = time.text.split('-',1)[1].strip()
    upcoming_event['name'] = event.text.strip()
    upcoming_events.append(upcoming_event.copy())

print(upcoming_events)
upcoming_events_dict = {i:upcoming_events[i] for i in range(len(upcoming_events))}
print(upcoming_events_dict)
driver.quit()