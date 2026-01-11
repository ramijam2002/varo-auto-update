import requests
from bs4 import BeautifulSoup

NPOINT_URL = "https://api.npoint.io/7c350afaa6af728cc142"

def get_matches():
    # الموقع الخامس: يلا شوت دي زد
    url = "https://www.yalla-shootdz.com/"
    
    # Headers احترافية لتمويه الطلب
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://www.google.com/"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=20)
        soup = BeautifulSoup(response.content, "html.parser")
        
        data = {"date": "مباريات اليوم - Yalla Shoot DZ", "leagues": []}
        matches_list = []
        
        # المواقع اللي من نوع يلا شوت بتستخدم كلاسات واضحة مثل 'match-box' أو 'match-details'
        items = soup.find_all('div', class_='match-box') or soup.select('.match-details')
        
        for item in items:
            try:
                # سحب أسماء الفرق وتوقيت المباراة
                t1 = item.find('div', class_='team-home').text.strip()
                t2 = item.find('div', class_='team-away').text.strip()
                m_time = item.find('div', class_='match-time').text.strip()
                
                matches_list.append({
                    "time": m_time,
                    "team1": t1, 
                    "team2": t2,
                    # بنركب شعارات SofaScore الفخمة على الأسماء
                    "logo1": f"https://api.sofascore.app/api/v1/team/search/{t1}/image",
                    "logo2": f"https://api.sofascore.app/api/v1/team/search/{t2}/image",
                    "link": "#"
                })
            except: continue
            
        if matches_list:
            data["leagues"].append({"name": "أهم مباريات اليوم", "matches": matches_list})
        
        # تحديث الرابط تبعك
        res = requests.post(NPOINT_URL, json=data)
        if res.status_code == 200:
            print("أخيراً! الموقع الخامس اشتغل بنجاح ✅")
            
    except Exception as e:
        print(f"خطأ في الموقع الخامس: {e}")

if __name__ == "__main__":
    get_matches()
