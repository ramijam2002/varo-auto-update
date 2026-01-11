import requests
from bs4 import BeautifulSoup

NPOINT_URL = "https://api.npoint.io/7c350afaa6af728cc142"

def get_matches():
    # العودة للموقع الثالث في قائمتك
    url = "https://www.mop-kora-live.com/"
    
    # الـ Headers اللي طلبتها عشان نتخطى الحماية
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Referer": "https://www.google.com/"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=25)
        soup = BeautifulSoup(response.content, "html.parser")
        
        data = {"date": "مباريات اليوم - Mop Kora", "leagues": []}
        matches_list = []
        
        # البحث في هيكلة الموقع (عناصر المباريات)
        items = soup.select('.match-box') or soup.select('.event') or soup.find_all('div', class_='match')
        
        for item in items:
            try:
                # سحب الأسماء (توقع للكلاسات بناءً على المواقع المشابهة)
                t1 = item.find('div', class_='team-home').text.strip()
                t2 = item.find('div', class_='team-away').text.strip()
                m_time = item.find('div', class_='match-time').text.strip()
                
                matches_list.append({
                    "time": m_time,
                    "team1": t1, "team2": t2,
                    "logo1": f"https://api.sofascore.app/api/v1/team/search/{t1}/image",
                    "logo2": f"https://api.sofascore.app/api/v1/team/search/{t2}/image",
                    "link": "#"
                })
            except: continue
            
        if matches_list:
            data["leagues"].append({"name": "بث مباشر - أهم المباريات", "matches": matches_list})
        
        # إرسال البيانات
        res = requests.post(NPOINT_URL, json=data)
        if res.status_code == 200:
            print("الموقع الثالث اشتغل تمام! ✅")
        else:
            print("مشكلة في npoint")
            
    except Exception as e:
        print(f"خطأ في الموقع الثالث: {e}")

if __name__ == "__main__":
    get_matches()
