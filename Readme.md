# README for Email Scraper Tool

## Overview
This Email Scraper Tool is a Python-based application designed to extract email addresses from a specified URL and its linked pages. It utilizes web scraping techniques to navigate through the website and gather email addresses efficiently.

## Features
- **URL Input**: Users can input any valid URL to start the scraping process.
- **Email Extraction**: The tool scans the webpage and its linked pages to find and collect email addresses.
- **Limit on Scraping**: The tool is designed to scrape a maximum of 10 pages to prevent excessive load on the server.
- **User-Friendly Output**: The extracted email addresses are displayed in a clear format for easy access.

## Requirements
To run this tool, you need to have the following Python packages installed:
- `requests`
- `beautifulsoup4`
- `lxml` (optional, for better parsing performance)

You can install the required packages using pip:
