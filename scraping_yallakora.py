from datetime import datetime
import requests
from bs4 import BeautifulSoup
import csv 

while True:
    date = input("Enter the date (contain 8 numbers) as format mm/dd/yyyy : ")
    try:
        datetime.strptime(date, '%m/%d/%Y') # y_small --> 25  ,  Y_capital --> 2025
        break

    except ValueError:
        print("Invalid date, please Please enter again as mm/dd/yyyy ")

page = requests.get(f"https://www.yallakora.com/match-center?date={date}#days")

def main(page):

    src = page.content
    soup = BeautifulSoup(src , 'lxml')
    
    matches_details = []

    championships = soup.find_all("div",{"class":"matchCard"})

    def get_match_info(championships):
        championship_title = championships.contents[1].find("h2").text.strip()
        all_matches = championships.contents[3].find_all("div",{"class":"liItem"})
        number_of_matches = len(all_matches)

        for i in range(number_of_matches):

            team_A = all_matches[i].find('div',{'class':'teamA'}).text.strip()
            team_B = all_matches[i].find('div',{'class':'teamB'}).text.strip()

            result_match = all_matches[i].find('div',{'class':'MResult'}).find_all('span',{'class':'score'})
            score = f"{result_match[0].text.strip()} - {result_match[1].text.strip()}"

            time_match = all_matches[i].find('div',{'class':'MResult'}).find('span',{'class':'time'}).text.strip()

            matches_details.append({'championship':championship_title,
                                '1_Team':team_A,
                                '2_Team':team_B,
                                'Time':time_match,
                                'Score':score})
            
    for i in range(len(championships)):
        get_match_info(championships[i])

    keys = matches_details[0].keys()

    with open(r'D:\my python\scraping\details.csv', 'w', newline='', encoding='utf-8-sig') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(matches_details)

        print("file created")



main(page)