import requests  # Import the requests module to send HTTP requests easily.
from bs4 import BeautifulSoup  # Import BeautifulSoup from bs4 module for parsing HTML documents.

def find_image_url():
    # Define the URL of the webpage from which to scrape the image URL.
    url = "https://api.ecomcybercourse3.online/cybercourse7.html"
    
    # Send an HTTP GET request to the specified URL and store the response.
    response = requests.get(url)
    
    # Parse the HTML content of the page using BeautifulSoup. Specify 'html.parser' as the parser.
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the first <img> tag in the parsed HTML.
    image_tag = soup.find('img')
    
    # Check if an <img> tag was found and if it has a 'src' attribute. If so, print the URL.
    if image_tag and 'src' in image_tag.attrs:
        print("Image URL found:", image_tag['src'])
    else:
        # Print a message if no image URL is found.
        print("No image URL found.")

# Call the function to execute the image scraping.
find_image_url()
