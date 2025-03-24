import requests

# Define the API endpoint and parameters
url = "https://oeffentlichevergabe.de/api/notice-exports"
params = {
    "pubMonth": "2023-12",  # Example month (YYYY-MM)
    "format": "eforms.zip"  # Desired file format (eForms, OCDS, CSV)
}

# Send the GET request to download the file
response = requests.get(url, params=params)

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    # Write the ZIP file to the disk
    with open("notices.zip", "wb") as file:
        file.write(response.content)
    print("File downloaded successfully.")
else:
    print(f"Failed to download file. Status code: {response.status_code}")
