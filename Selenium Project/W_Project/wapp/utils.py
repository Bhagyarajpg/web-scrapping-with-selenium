from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def extract_entities(url):
    
    #service = Service(executable_path='C:/Users/R/Downloads/chromedriver-win64/chromedriver-win64/chromedriver')
    
    options = webdriver.ChromeOptions()
    options.headless = True
    service = Service(r"C:\Users\R\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    #driver = webdriver.Chrome("C:/Users/R/Downloads/chromedriver-win64/chromedriver-win64/chromedriver")
    
    driver.get(url)
    #time.sleep(5)  # Wait for the page to load completely

    # Replace the following lines with actual logic to extract data
    artist_name = driver.find_element(By.CSS_SELECTOR, '#buy > div > div > div:nth-child(1) > div:nth-child(2) > p.subhead4.margin-bottom-0 > a').text
    program_name = driver.find_element(By.CSS_SELECTOR, '#buy > div > div > div:nth-child(2) > div:nth-child(1) > div > div > div:nth-child(2)').text
    artist_role = driver.find_element(By.CSS_SELECTOR, '#buy > div > div > div:nth-child(1) > div:nth-child(2) > p.subhead6.margin-bottom-0').text
    date = driver.find_element(By.CSS_SELECTOR, '#buytix > div.performance-card.margin-bottom-2 > div.content > p.body-text3').text
    time = driver.find_element(By.CSS_SELECTOR, '#buytix > div.performance-card.margin-bottom-2 > div.content > p.body-text3').text
    auditorium = driver.find_element(By.CSS_SELECTOR, '#buytix > div.performance-card.margin-bottom-2 > div.content > p.location.subhead6 > strong').text

    driver.quit()

    return {
        'artist_name': artist_name,
        'program_name': program_name,
        'artist_role': artist_role,
        'date': date,
        'time': time,
        'auditorium': auditorium,
    }


# myapp/utils.py
import openai
from django.conf import settings

# Set up OpenAI API key
openai.api_key = settings.OPENAI_API_KEY

def clean_data(raw_data):
    def process_text(text):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the latest recommended model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": text}
            ],
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].message['content'].strip()

    cleaned_data = {
        'artist_name': process_text(raw_data.get('artist_name', '')),
        'program_name': process_text(raw_data.get('program_name', '')),
        'artist_role': process_text(raw_data.get('artist_role', '')),
        'date': process_text(raw_data.get('date', '')),
        'time': process_text(raw_data.get('time', '')),
        'auditorium': process_text(raw_data.get('auditorium', ''))
    }
    return cleaned_data