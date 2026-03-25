#random garbage imports that actually make things function
import random
import time
import os
import pickle
import configparser
import datetime

#selenium imports
import undetected_chromedriver as UC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import selenium.webdriver.support.expected_conditions as EC

# ========= credit/s ========= #
# VV Come visit him, the retard that built this cathedral. VV
# &&&&&&&&&&&& https://www.twitch.tv/elbram_tsol &&&&&&&&&&&&

print("# ========= == ========= credit/s ========= == ========= #")
time.sleep(0.5)
print("# VV Come visit me, I built this slopthedral by hand. VV #")
time.sleep(0.5)
print("#  ~~~~~~~~~ https://www.twitch.tv/elbram_tsol ~~~~~~~~~ #")
time.sleep(0.5)
print("# ========= ====== ======= ==== ======= ====== ========= #")
time.sleep(0.5)
# ========= prep ========= #
Profile_DIR = os.path.abspath("./selenium_profile")

# setting session options
options = UC.ChromeOptions()

options.add_argument(f"--user-data-dir={Profile_DIR}")
options.add_argument("--no-first-run")
options.add_argument("--no-default-browser-check")

config = configparser.ConfigParser()
config.read("config.cfg")

twitch_video_producer_page = config.get("channels' info", "link_to_your_twitch_video_producer_page")

# setting export options
title_prefix = config.get("export options", "Date_prefix")
video_title  = config.get("export options", "Title")
title_suffix = config.get("export options", "Date_suffix")

add_VOD_note_Bool = config.get("export options", "VOD_denotion")

Description = config.get("export options", "Description")
Tags        = config.get("export options", "Tags")
Visibility  = config.get("export options", "Visibility")
Split       = config.get("export options", "Split")

print("\nExport Options for VOD as youtube video:\n")
print(title_prefix)
print(video_title)
print(title_suffix)
print(add_VOD_note_Bool)
print(Description)
print(Tags)
print(Visibility)
print(Split + "\n")

# function definitions
def save_tokens():
    cookies = driver.get_cookies()
    with open("session_tokens.pkl", "wb") as f:
        pickle.dump(cookies, f)
    
    local_storage = driver.execute_script("return JSON.stringify(localStorage)")
    with open("local_storage.json", "w") as f:
        f.write(local_storage)
    print("networking izzat saved")

def need_to_login_to_twitch(driver):
    try:
        WebDriverWait(driver=driver, timeout=5, poll_frequency=1).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-a-target="core-error-message"]')))
        return True
    except:
        return False
    
def need_to_login_to_google(driver):
    
    # try to click the button which may open the google sign in page
    try:
        time.sleep(random.uniform(1.7, 2.3))
        Video_export_button = driver.find_elements(By.CSS_SELECTOR, '[class="ScInteractableBase-sc-ofisyf-0 ScInteractableDefault-sc-ofisyf-1 CayVJ blixHj tw-interactable"]')
        Video_export_button[21].click()
        print("clicked")
    except:
        print("not clicked")
        time.sleep(2)
        print("I'm crashing out")
        driver.quit()

    # test if it did open or not
    if len(driver.window_handles) != 1:
        print("login fool")
        return True
    else:
        return False

driver = UC.Chrome(options=options, version_main=None)
driver.set_window_size(width=1000, height=720)

# real stuff happenning here

# wait for & allow twitch login if needed
driver.get(twitch_video_producer_page)

if need_to_login_to_twitch(driver) == True:
    print("waitin for nescessary Twitch sign in")
    WebDriverWait(driver=driver, timeout=300, poll_frequency=1).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="Layout-sc-1xcs6mc-0 kRsdRG"]')))
    print("done waitin loser")
else:
    print("no Twitch sign in found nescessary")
    try:
        WebDriverWait(driver=driver, timeout=5, poll_frequency=1).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="Layout-sc-1xcs6mc-0 kRsdRG"]')))
        print("I'm where I need to be")
    except:
        print("something has gone terribly wrong")

# save twitch networking izzat (cred (credentials)) locally if needed
save_tokens()

# navigate to & click twitch VOD's options menu
try:
    time.sleep(random.uniform(1.7, 2.3))
    video_options_button = driver.find_elements(By.CSS_SELECTOR, '[class="ScCoreButton-sc-ocjdkq-0 glPhvE ScButtonIcon-sc-9yap0r-0 dgVYJo"]')
    video_options_button[5].click()
    print("clicked")
except:
    print("not clicked")

# click export then wait for sign in if nescessary
if need_to_login_to_google(driver) == True:
    WebDriverWait(driver=driver, timeout=300, poll_frequency=1).until(len(driver.window_handles) == 1)
    print("all signed in")
else:
    time.sleep(random.uniform(1.7, 2.3))
    print("all signed in")

# save google networking izzat (cred (credentials)) locally if needed.
save_tokens()

# ========= filling the export form ========= #
time.sleep(random.uniform(1.5, 2.5))

title_box = driver.find_element(By.ID, "ye-title")
title_box_default = title_box.get_attribute("value")

desc_box = driver.find_element(By.ID, "ye-description")
desc_box_default  = desc_box.get_attribute("value")

tags_box = driver.find_element(By.ID, "ye-tags")
tags_box_default  = tags_box.get_attribute("value")

new_title = """"""
new_description = """"""
new_tags = """"""

date_time_today = datetime.datetime.now()
DD_MM_YYYY = date_time_today.strftime("%d/%m/%Y")

# title selections
if video_title != "False" and video_title != "default":
    new_title = new_title + video_title
    print(f"\nTitle to be changed from: {title_box_default} to: {new_title}")
else:
    new_title = new_title + title_box_default

if title_prefix == "True":
    new_title = DD_MM_YYYY + new_title

if title_suffix == "True" and add_VOD_note_Bool == "True":
    new_title = new_title + " VOD, from: "
    new_title = new_title + DD_MM_YYYY
    print(f"Finalized Title will be: {new_title}")
elif title_suffix == "True" and add_VOD_note_Bool == "False":
    new_title = new_title + " "
    new_title = new_title + DD_MM_YYYY
    print(f"Finalized Title will be: {new_title}")
elif title_suffix == "False" and add_VOD_note_Bool == "True":
    new_title = new_title + " VOD"
    print(f"Finalized Title will be: {new_title}")
else:
    print(f"Finalized Title will be: {new_title}")

# description selections
if Description != "default":
    new_description = Description
    print(f"\nDescription will be changed from: {desc_box_default} to: {Description}")
else:
    new_description = desc_box_default
    print(f"\nDescription will be left as is, which is: {desc_box_default}")

# tags selections
if Tags != "default":
    new_tags = Tags
    print(f"\nTags will be changed from: {tags_box_default} to: {Tags}")
else:
    new_tags = tags_box_default
    print(f"\nTags will be left as is, which is: {tags_box_default}")

# clear & re-fill text boxes
title_box.clear()
time.sleep(random.uniform(1.7, 2.3))
title_box.send_keys(new_title)
time.sleep(random.uniform(1.7, 2.3))

desc_box.clear()
time.sleep(random.uniform(1.7, 2.3))
desc_box.send_keys(new_description)
time.sleep(random.uniform(1.7, 2.3))

tags_box.clear()
time.sleep(random.uniform(1.7, 2.3))
tags_box.send_keys(new_tags)
time.sleep(random.uniform(1.7, 2.3))

# select visibility
radio_buttons = driver.find_elements(By.CSS_SELECTOR, '[type="radio"]')

if Visibility == "default":
    print("\nvisibility set to: default")
elif Visibility == "Public":
    radio_buttons[0].click()
    print("\nvisibility set to: Public")
elif Visibility == "Private":
    radio_buttons[1].click()
    print("\nvisibility set to: Private")
elif Visibility == "Unlisted":
    radio_buttons[2].click()
    print("\nvisibility set to: Unlisted")
else:
    print("\nYou suck at spelling. You had all the time in the world, no rush at all & still couldn't type what you wanted. As such; visibility set to: default")

time.sleep(random.uniform(1.7, 2.3))

# select whether or not to split into 15 minute segments
split_box = driver.find_element(By.ID, "ye-split")

if Split == "True":
    split_box.click()
    print("\nVOD will be split into 15 minute segments.")
else:
    print("\nVOD will NOT be split into 15 minute segments.")

time.sleep(random.uniform(1.7, 2.3))

# shenanigans & export
print("\nThe export is ready.")

time.sleep(2)

print("\n\033[31mIntervene now, or forever be immortalized on the internet.\033[0m")

countdown = 10

time.sleep(1)

while countdown != 0:
    print(f"\n\033[31m{countdown}\033[0m")
    countdown = countdown - 1
    time.sleep(1)

time.sleep(1)

for l in "TIME IS UP.":
    print(f"\033[31m{l}\033[0m")
    time.sleep(0.1)

export_button = driver.find_elements(By.CSS_SELECTOR, '[class="ScCoreButton-sc-ocjdkq-0 cikFpu"]')[1]
export_button.click()

# ========= closing time ========= #

time.sleep(2)

driver.quit()