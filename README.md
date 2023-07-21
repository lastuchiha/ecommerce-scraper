# Product Details Scraper with Beautiful Soup
## Overview
This repository contains a Python script that utilizes Beautiful Soup, a popular web scraping library, to extract product details from an e-commerce website. The script is designed to fetch product names, prices, and ratings, but can easily be extended to gather more information.

## Features
* Simple and modular Python script to scrape product details from a website.
* Utilizes Beautiful Soup for efficient HTML parsing and data extraction.
* Flexible and customizable for scraping various e-commerce websites.
* Lightweight and easy to use, making it accessible for developers of all levels.

## Requirements
* Python 3.7 or higher.
* Beautiful Soup 4 library (install using `pip install beautifulsoup4`).
* Requests library (install using `pip install requests`).

## Usage
1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/lastuchiha/ecommerce-scraper.git
    cd ecommerce-scraper
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Script:

    ### Single Product
    ```bash
    python main.py -url <product-url>
    ```
    replace the `<product-url>` with the url of the product

    ### Multiple Products
    ```bash
    python main.py -f <filename>
    ```
    if you have multiple products to scrape then keep the links inside a `.txt` file with urls of products in separate lines and replace the `<filename>` with the name of that file.

## Disclaimer
This project and the provided script are intended for educational purposes only. The primary goal is to demonstrate web scraping techniques using Beautiful Soup and provide a learning resource for developers interested in this topic.

## Contributions and Issues
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.