import requests
from bs4 import BeautifulSoup
import cloudscraper

NPOINT_URL = "https://api.npoint.io/7c350afaa6af728cc142"

def scrape_yalla_shoot():
    scraper = cloudscraper.create_scraper()
    # نستخدم موقع مستقر وجدوله سهل السحب
    url = "https://www.yalla-shoot.com/live/index.php"
    
    try:
        response = scraper.get(url, timeout=20)
        soup = BeautifulSoup(response.content, "html.parser")
        
        matches_data = {"date": "مباريات اليوم - تحديث تلقائي", "leagues": []}
        
        # سحب كل "بلوك" مباراة
        match_blocks = soup.find_all('div', class_='match-container')
        
        current_matches = []
        for block in match_blocks:
            try:
                t1 = block.find('div', class_='team-1').text.strip()
                t2 = block.find('div', class_='team-2').text.strip()
                m_time = block.find('div', class_='match-time').text.strip()
                # رابط صفحة المشاهدة
                live_link = block.find('a')['href']
                
                current_matches.append({
                    "time": m_time,
                    "team1": t1,
                    "team2": t2,
                    "logo1": f"https://api.sofascore.app/api/v1/team/search/{t1}/image",
                    "logo2": f"https://api.sofascore.app/api/v1/team/search/{t2}/image",
                    "stream": live_link # الرابط اللي رح يفتحه التطبيق
                })
            except: continue
        
        # تنظيمها في قسم واحد (أو تقسيمها حسب الدوري إذا حبيت لاحقاً)
        matches_data["leagues"].append({"name": "جميع مباريات اليوم", "matches": current_matches})
        
        requests.post(NPOINT_URL, json=matches_data)
        print("تم تحديث الجدول والروابط تلقائياً! ✅")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    scrape_yalla_shoot()
