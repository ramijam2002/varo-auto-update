import requests
from bs4 import BeautifulSoup

# الرابط تبعك
NPOINT_URL = "https://api.npoint.io/7c350afaa6af728cc142"

# الدوريات اللي إنت مهتم فيها (الفلتر)
TARGET_LEAGUES = [
    "الدوري الإنجليزي", "الدوري الإسباني", "الدوري الإيطالي", 
    "الدوري الألماني", "الدوري الفرنسي", "دوري أبطال أوروبا", 
    "الدوري السعودي", "كأس السوبر الإسباني"
]

def scrape_jdwel():
    url = "https://jdwel.com/today/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    
    data = {"date": "مباريات اليوم المختارة", "leagues": []}
    
    # البحث عن حاويات الدوريات في موقع جدول
    leagues_sections = soup.select(".league-block") # هذا تخمين للمسار، سنعدله حسب هيكلة الموقع
    
    for section in soup.find_all('div', class_='league-matches-container'):
        league_name = section.find('h2').text.strip()
        
        # تطبيق الفلتر تبعك
        if any(target in league_name for target in TARGET_LEAGUES):
            current_league = {"name": league_name, "matches": []}
            
            for match in section.find_all('div', class_='match-card'):
                try:
                    m = {
                        "time": match.find('div', class_='match-time').text.strip(),
                        "team1": match.find('div', class_='team-home').find('span').text.strip(),
                        "team2": match.find('div', class_='team-away').find('span').text.strip(),
                        "logo1": match.find('div', class_='team-home').find('img')['src'],
                        "logo2": match.find('div', class_='team-away').find('img')['src'],
                        "link": "https://jdwel.com" + match.find('a')['href']
                    }
                    current_league["matches"].append(m)
                except:
                    continue
            
            if current_league["matches"]:
                data["leagues"].append(current_league)
                
    # إرسال البيانات
    requests.post(NPOINT_URL, json=data)
    print("تم سحب أهم المباريات بنجاح! ✅")

if __name__ == "__main__":
    scrape_jdwel()
