# Image Scraper Example

This repository contains a Python script that demonstrates how to use the `requests` and `BeautifulSoup4` modules to scrape and extract image URLs from a webpage.

## Overview

The `image_scraper.py` script retrieves HTML content from a specified URL and uses BeautifulSoup to parse the HTML. It is designed to find the first `<img>` tag in the document and extract the source URL of the image.

## Prerequisites

Before running this script, you will need Python installed on your system, along with the `requests` and `BeautifulSoup4` libraries. Python 3.6 or higher is recommended. You can install the necessary libraries using pip:

```bash
pip install requests beautifulsoup4
Installation
To run this script, first clone this repository or download the image_scraper.py file directly.
git clone https://github.com/your-username/your-repository.git
cd your-repository

Usage
To use the script, run it from the command line:

python image_scraper.py
The script will prompt you for the URL of the webpage you wish to scrape. Enter the URL, and the script will print out the image URL found.

Contributing
Contributions are welcome. To contribute, please fork the repository, make your changes, and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE.md file for details.
