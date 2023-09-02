import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import pyautogui
import cv2
import os
import pytesseract
from PIL import Image

import serial
import time
from serial import Serial

from tqdm import tqdm

arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)

# Hardcoded path to ChromeDriver executable
webdriver_service = Service('D:\.Papols\Ig lol bot\chromedriver.exe')

# Create ChromeOptions object
chrome_options = Options()

# Create a new ChromeDriver instance
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Follower value
Followers = 0

# Wait for the home page to load
time.sleep(5)

# login feature
username = 'imadrill'
password = 'Papolxd123'

#Serial Send
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

#login
def loginig():
    # Load the Instagram login page
    driver.get('https://www.instagram.com/accounts/login/')

    # Wait for the login page to load
    time.sleep(2)

    # Enter the username and password
    driver.find_element(By.NAME, 'username').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)

    # Click the login button
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Wait for the home page to load
    time.sleep(5)

    # Navigate to the user's profile page
    driver.get('https://www.instagram.com/imadrill/')

# Define the region of interest coordinates
x = 465
y = 225
w = 75
h = 17
# ...
# Continuously check for changes in the follower count

loginig()
while True:
    print("Next update:")
    for i in tqdm(range(100)):
        time.sleep(0.2)

    driver.refresh()

    # Wait for the page to fully load
    time.sleep(3)

    # Capture the region of interest (follower count section) using pyautogui
    follower_count_region = pyautogui.screenshot(region=(x, y, w, h))

    # Save the captured image
    follower_count_region.save('D:/.Papols/Ig lol bot/Img/followercount.png')
    time.sleep(3)

    # Read the image with text
    image_path = 'D:/.Papols/Ig lol bot/Img/followercount.png'
    image = cv2.imread(image_path)

    # Convert to grayscale image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Checking whether thresh or blur
    pre_processor = 'tresh'
    if pre_processor == "thresh":
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    elif pre_processor == "blur":
        gray = cv2.medianBlur(gray, 3)

    # Save grayscale image to disk
    filename = "{}.jpg".format(os.getpid())
    cv2.imwrite(filename, gray)

    # Use Tesseract to extract text from the image
    text = pytesseract.image_to_string(Image.open(filename))
    print("_________________________________")
    print("")
    print("Raw data:"+ text[:-1] + "s")

    # Print the extracted text
    textbool = "follower"
    textbool2 = "followes"
    textbool3 = "followe"
    if textbool in text:
        text = text[:-9]
        text_proc = int(text)
        print(text_proc)
    elif textbool2 in text:
        text = text[:-9]
        text_proc = int(text)
        print(text_proc)
    elif textbool3 in text:
        text = text[:-8]
        text_proc = int(text)
        print(text_proc)
    else:
        text_proc = "0"
        print("No Value! Follow not found!")

    # Main function trigger
    if int(text_proc) > Followers:
        
        # Convert to Integer
        Followers = text_proc

        # do
        print("DRILL!!")
        write_read('1')
        #if someone unfollowed
    elif int(text_proc) < Followers:
        Followers = text_proc
        print("someone unfollowed D';")