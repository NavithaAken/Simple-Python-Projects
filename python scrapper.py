import requests
from bs4 import BeautifulSoup

def scrape_hotels(location, budget):
    url = f'https://www.examplehotelsite.com/{location}'  # Replace 'examplehotelsite.com' with the actual hotel website URL
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        hotels = soup.find_all('div', class_='hotel')[:5]  # Extracting data for 5 hotels

        for hotel in hotels:
            name = hotel.find('h2', class_='hotel-name').text.strip()
            price = hotel.find('span', class_='price').text.strip()
            if float(price[1:]) <= budget:  # Assuming price is in format $xxx.xx
                print(f'Hotel: {name}, Price: {price}')
    else:
        print('Failed to retrieve data. Please try again later.')

def main():
    location = input('Enter the location you want to search for hotels: ')
    budget = float(input('Enter your budget (in dollars): '))

    scrape_hotels(location, budget)

if __name__ == "__main__":
    main()
