import requests
from bs4 import BeautifulSoup

NPOINT_URL = "https://api.npoint.io/7c350afaa6af728cc142"

def get_matches():
    # الموقع الثاني بالقائمة
    url = "https://www.livesoccerhd.info/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=20)
        soup = BeautifulSoup(response.content, "html.parser")
        
        data = {"date": "مباريات اليوم - LiveSoccerHD", "leagues": []}
        matches_list = []
        
        # البحث عن المباريات في الموقع الثاني
        # ملاحظة: سنبحث عن العناصر الشائعة في مواقع يلا شوت
        match_boxes = soup.find_all('div', class_='match-event') or soup.find_all('a', class_='match-card')
        
        for box in match_boxes:
            try:
                # محاولة سحب الأسماء
                teams = box.find_all('div', class_='team-name')
                if len(teams) >= 2:
                    t1 = teams[0].text.strip()
                    t2 = teams[1].text.strip()
                    m_time = box.find('div', class_='match-time').text.strip()
                    
                    matches_list.append({
                        "time": m_time,
                        "team1": t1,
                        "team2": t2,
                        # اعتمدنا شعارات SofaScore الفخمة
                        "logo1": f"https://api.sofascore.app/api/v1/team/search/{t1}/image", 
                        "logo2": f"https://api.sofascore.app/api/v1/team/search/{t2}/image",
                        "link": "#"
                    })
            except: continue
            
        if matches_list:
            data["leagues"].append({"name": "أهم المباريات", "matches": matches_list})
        
        # إرسال البيانات
        res = requests.post(NPOINT_URL, json=data)
        if res.status_code == 200:
            print("تم التحديث من الموقع الثاني بنجاح! ✅")
        
    except Exception as e:
        print(f"خطأ في الموقع الثاني: {e}")

if __name__ == "__main__":
    get_matches()
