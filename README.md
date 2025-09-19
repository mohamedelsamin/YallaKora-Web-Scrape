# Yallakora Football Matches Scraper

This project is a Python script that scrapes football match details (teams, scores, match time, and championship name) from **[Yallakora](https://www.yallakora.com/)** for a specific date entered by the user.

The extracted data is saved into a **CSV file** for further analysis or usage.

---

## Features
- Takes a date input from the user (`mm/dd/yyyy` format).
- Scrapes all matches from Yallakora's Match Center for that date.
- Extracts:
  - Championship name
  - Team A & Team B
  - Match time
  - Final score
- Saves all results in a CSV file (`details.csv`).

## Technologies Used
- Python
- Requests
 – for fetching the webpage

- BeautifulSoup4
 – for HTML parsing

- lxml
 – as the parser

- CSV – for saving data
