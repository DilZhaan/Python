import requests
from bs4 import BeautifulSoup

# Replace these with the actual URLs
target_url = 'https://eservices.elections.gov.lk/pages/myVoterRegistration.aspx'

# Your NIC value
nic_value = '200377600418'

# Create a session to persist the session
session = requests.Session()

# Access the target page with the form
target_response = session.get(target_url)

# Parse the HTML of the target page using BeautifulSoup
soup = BeautifulSoup(target_response.text, 'html.parser')

# Find the form on the target page
form = soup.find('form')

# Extract other form data (if needed)
# For example, you might need to find the names or IDs of other form elements
# and include them in the payload dictionary.

# Prepare the form data
form_data = {
    'ContentMain_txtNIC': nic_value,
    'recaptcha_response': 'your_recaptcha_response'  # Replace with actual response
}

# Submit the form
response = session.post(target_url, data=form_data)

# Parse the result page (adjust based on the structure of the result page)
result_soup = BeautifulSoup(response.text, 'html.parser')

# Extract the information you need from the result page
# This depends on the structure of the result page
your_name = result_soup.find('div', {'class': 'your-name-class'}).text

print(f"Your Name: {your_name}")
