import requests
from bs4 import BeautifulSoup

NPOINT_URL = "https://api.npoint.io/7c350afaa6af728cc142"

def get_matches():
    # الموقع الأول بالترتيب
    url = "https://www.kora-ksa.org/"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers, timeout=20)
        soup = BeautifulSoup(response.content, "html.parser")
        
        data = {"date": "مباريات اليوم - تحديث مباشر", "leagues": []}
        matches_list = []
        
        # البحث عن حاويات المباريات (تعديل بناءً على هيكلة الموقع)
        matches = soup.find_all('div', class_='match-container') # كود تجريبي للموقع الأول
        
        for match in matches:
            try:
                t1 = match.find('div', class_='left-team').text.strip()
                t2 = match.find('div', class_='right-team').text.strip()
                m_time = match.find('div', class_='match-time').text.strip()
                
                matches_list.append({
                    "time": m_time,
                    "team1": t1,
                    "team2": t2,
                    # لاحظ هون: استخدمنا روابط SofaScore اللي اتفقنا عليها
                    "logo1": f"https://api.sofascore.app/api/v1/team/search/{t1}/image", 
                    "logo2": f"https://api.sofascore.app/api/v1/team/search/{t2}/image",
                    "link": "#"
                })
            except: continue
            
        if matches_list:
            data["leagues"].append({"name": "أهم مباريات اليوم", "matches": matches_list})
        
        # إرسال البيانات
        requests.post(NPOINT_URL, json=data)
        print("تم التحديث من الموقع الأول ✅")
        
    except Exception as e:
        print(f"خطأ في الموقع الأول: {e}")

if __name__ == "__main__":
    get_matches()
