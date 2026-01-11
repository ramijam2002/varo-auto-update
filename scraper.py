import requests
from bs4 import BeautifulSoup

NPOINT_URL = "https://api.npoint.io/7c350afaa6af728cc142"

# الدوريات اللي بدنا إياها
TARGET_LEAGUES = ["الدوري الإنجليزي", "الدوري الإسباني", "الدوري الإيطالي", "الدوري الألماني", "الدوري الفرنسي", "الدوري السعودي", "أبطال"]

def scrape_jdwel():
    url = "https://jdwel.com/today/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    
    try:
        response = requests.get(url, headers=headers, timeout=20)
        soup = BeautifulSoup(response.content, "html.parser")
        
        data = {"date": "مباريات اليوم المختارة", "leagues": []}
        
        # البحث عن كل قسم دوري
        sections = soup.find_all('div', class_='league-matches-container')
        
        for section in sections:
            league_title = section.find('h2').text.strip() if section.find('h2') else "دوري غير معروف"
            
            # فلترة الدوريات
            if any(target in league_title for target in TARGET_LEAGUES):
                league_data = {"name": league_title, "matches": []}
                
                matches = section.find_all('div', class_='match-card')
                for match in matches:
                    try:
                        time = match.find('div', class_='match-time').text.strip() if match.find('div', class_='match-time') else "--:--"
                        t1 = match.find('div', class_='team-home').text.strip()
                        t2 = match.find('div', class_='team-away').text.strip()
                        # سحب الشعارات
                        img1 = match.find('div', class_='team-home').find('img')['src'] if match.find('div', class_='team-home').find('img') else ""
                        img2 = match.find('div', class_='team-away').find('img')['src'] if match.find('div', class_='team-away').find('img') else ""
                        
                        league_data["matches"].append({
                            "time": time, "team1": t1, "team2": t2,
                            "logo1": img1, "logo2": img2, "link": "#"
                        })
                    except: continue
                
                if league_data["matches"]:
                    data["leagues"].append(league_data)
        
        # إرسال البيانات حتى لو كانت فاضية عشان نتأكد إن السيرفر شغال
        requests.post(NPOINT_URL, json=data)
        print("تم التحديث بنجاح ✅")
        
    except Exception as e:
        print(f"حدث خطأ: {e}")

if __name__ == "__main__":
    scrape_jdwel()
