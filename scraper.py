import requests
from bs4 import BeautifulSoup

NPOINT_URL = "https://api.npoint.io/7c350afaa6af728cc142"

def get_matches():
    # موقع في الجول - ملك البيانات البسيطة
    url = "https://www.filgoal.com/matches/"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "ar,en;q=0.9"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=20)
        soup = BeautifulSoup(response.content, "html.parser")
        
        data = {"date": "مباريات اليوم - VARO LIVE", "leagues": []}
        
        # سحب كل ماتش في الصفحة
        for match_card in soup.select('.mc-block'):
            try:
                t1 = match_card.select_one('.f').text.strip()
                t2 = match_card.select_one('.s').text.strip()
                m_time = match_card.select_one('.match-aux span').text.strip()
                
                # هون السر: بنركب شعارات SofaScore اللي حفظناها
                match_data = {
                    "time": m_time,
                    "team1": t1, "team2": t2,
                    "logo1": f"https://api.sofascore.app/api/v1/team/search/{t1}/image",
                    "logo2": f"https://api.sofascore.app/api/v1/team/search/{t2}/image",
                    "link": "#"
                }
                
                # تصنيف بسيط
                if not data["leagues"]:
                    data["leagues"].append({"name": "أهم مباريات اليوم", "matches": []})
                data["leagues"][0]["matches"].append(match_data)
            except: continue

        requests.post(NPOINT_URL, json=data)
        print("تمت العملية بنجاح ساحق! ✅")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_matches()
