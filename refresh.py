from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import json

# Path to the ChromeDriver executable
chromedriver_path = '/usr/bin/chromedriver'  # Replace this with your actual path to ChromeDriver

def refresh_cookie(url):
    options = Options()
    options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

    # options.add_argument('--no-sandbox')  # Necessary for some environments
    # options.add_argument('--disable-dev-shm-usage')  # Prevent resource issues in some environments
    # options.add_argument('--disable-extensions')  # Disable extensions to avoid conflicts
    options.add_argument('--headless')  # Optional: Run browser in headless mode (no UI)
    options.add_argument('--incognito')
    # options.add_argument('--disable-gpu')  # Disable GPU for headless mode (Linux fix)
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Disable logging

    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)

    time.sleep(5)

    perf = driver.get_log('performance')
    with open("essentials.json", "w") as f:
        f.write("{\}")
        f.close()
    with open("essentials.json", "r+") as g:
        data = json.load(g)

        for entry in perf:
            log = json.loads(entry['message'])
            message = log['message']
            if message['method'] == 'Network.requestWillBeSent':
                request = message['params']['request']
                if request['url']=="https://in.puma.com/api/graphql" and request['headers']['x-operation-name']=='PDP':

                    data['headers'] = request['headers']

                    cookies = driver.get_cookies()
                    cook = {}
                    cook = {cookie['name']: cookie['value'] for cookie in cookies}
                    data['cookies'] = cook
                    break
        g.seek(0)
        g.write(json.dumps(data))
        g.truncate()

    driver.quit()

    print("New Cookie and Header Provided")
