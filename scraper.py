import requests
from bs4 import BeautifulSoup
import cloudscraper

NPOINT_URL = "https://api.npoint.io/7c350afaa6af728cc142"

def get_matches():
    scraper = cloudscraper.create_scraper()
    # رح نجرب نسحب من كورة لايف أو يلا شوت دي زد
    url = "https://www.yalla-shootdz.com/"
    
    try:
        response = scraper.get(url, timeout=30)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # التنسيق اللي بيحبه تطبيقك (JSON)
        data = {
            "matches": [] 
        }
        
        # سحب المباريات الحقيقية
        items = soup.find_all('div', class_='match-box')
        for item in items:
            try:
                t1 = item.find('div', class_='team-home').text.strip()
                t2 = item.find('div', class_='team-away').text.strip()
                m_time = item.find('div', class_='match-time').text.strip()
                
                data["matches"].append({
                    "time": m_time,
                    "team1": t1,
                    "team2": t2,
                    # شعارات SofaScore الفخمة دايماً موجودة
                    "logo1": f"https://api.sofascore.app/api/v1/team/search/{t1}/image",
                    "logo2": f"https://api.sofascore.app/api/v1/team/search/{t2}/image",
                    "link": "https://www.yalla-shootdz.com/"
                })
            except: continue

        # إرسال البيانات
        requests.post(NPOINT_URL, json=data)
        print("تم سحب مباريات حقيقية وتحديث التطبيق! ✅")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_matches()
