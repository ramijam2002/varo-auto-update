import requests
from bs4 import BeautifulSoup

NPOINT_URL = "https://api.npoint.io/7c350afaa6af728cc142"

def get_matches():
    # الموقع الرابع بالقائمة
    url = "https://www.koorayou.com/"
    
    # هاد هو الـ Header اللي رح يحل المشكلة
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "ar,en-US;q=0.7,en;q=0.3",
        "Referer": "https://www.google.com/"
    }
    
    try:
        # بنضيف الـ headers هون عشان الطلب ينجح
        response = requests.get(url, headers=headers, timeout=20)
        soup = BeautifulSoup(response.content, "html.parser")
        
        data = {"date": "مباريات اليوم - Koorayou", "leagues": []}
        matches_list = []
        
        # البحث عن الكلاسات في Koorayou
        match_divs = soup.find_all('div', class_='match-container') or soup.find_all('div', class_='match-card')
        
        for div in match_divs:
            try:
                # سحب أسماء الفرق
                t1 = div.find('div', class_='team-home').text.strip()
                t2 = div.find('div', class_='team-away').text.strip()
                m_time = div.find('div', class_='match-time').text.strip()
                
                matches_list.append({
                    "time": m_time,
                    "team1": t1, "team2": t2,
                    # بنسحب الشعارات من SofaScore زي ما اتفقنا
                    "logo1": f"https://api.sofascore.app/api/v1/team/search/{t1}/image",
                    "logo2": f"https://api.sofascore.app/api/v1/team/search/{t2}/image",
                    "link": "#"
                })
            except: continue
            
        if matches_list:
            data["leagues"].append({"name": "أهم المباريات الآن", "matches": matches_list})
        
        # إرسال البيانات لـ npoint
        res = requests.post(NPOINT_URL, json=data)
        if res.status_code == 200:
            print("تم التحديث بالـ Headers بنجاح! ✅")
            
    except Exception as e:
        print(f"حدث خطأ: {e}")

if __name__ == "__main__":
    get_matches()
