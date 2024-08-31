# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 09:16:17 2023

@author: Juan
"""
# https://manganato.com/manga-un971622

# # The default installation path on Windows is often C:\Users\<YourUserName>\AppData\Local\Programs\Python\Python<Version>
# # WE also had to install somethiing else using, pip install requests beautifulsoup4
# # keep in mind this process wasnt so simple as the terminal was able to validate my command do to the
# # directory path so we had to do a little troubleshooting to be able to get it to work despite having
# #  python installed

# import requests
# from bs4 import BeautifulSoup

# # Define the URL of the webpage
# url = 'https://pythoninsider.blogspot.com/'

# # Send an HTTP GET request to the webpage
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the page content with BeautifulSoup
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Find and print the title and link of the blog post
#     post = soup.find('div', class_='post hentry')
#     title = post.find('h3', class_='post-title entry-title').text.strip()
#     link = post.find('h3', class_='post-title entry-title').a['href']

#     print("Title:", title)
#     print("Link:", link)

# else:
#     print('Failed to retrieve the webpage. Status code:', response.status_code)
# ///////////////////////////////////////////////////////////////////////////////////////////////

'''If you want to scrape more titles and links from the webpage, you can modify the code to loop 
through multiple blog posts and store the results in a list. Here's an example of how to do this:'''

import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage
url = 'https://pythoninsider.blogspot.com/'

# Send an HTTP GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and print the titles and links of all blog posts
    posts = soup.find_all('div', class_='post hentry')
    for post in posts:
        title = post.find('h3', class_='post-title entry-title').text.strip()
        link = post.find('h3', class_='post-title entry-title').a['href']

        print("Title:", title)
        print("Link:", link)
        print("----")

else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
