import requests
from datetime import datetime

NPOINT_URL = "https://api.npoint.io/7c350afaa6af728cc142"

# فلتر الدوريات (كلمات مفتاحية)
TARGET_KEYWORDS = ["الأردن", "إسبانيا", "إنجلترا", "السعودية", "إيطاليا", "ألمانيا", "فرنسا", "أبطال"]

def get_matches():
    # تاريخ اليوم 2026-01-11
    today = datetime.now().strftime('%Y-%m-%d')
    url = f"https://api.sofascore.com/api/v1/sport/football/scheduled-events/{today}"
    
    # رأسية الطلب (Headers) لمحاكاة متصفح حقيقي عشان نتخطى الحماية
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Origin": "https://www.sofascore.com",
        "Referer": "https://www.sofascore.com/"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code != 200:
            print(f"فشل الطلب، الكود: {response.status_code}")
            return

        events = response.json().get('events', [])
        data = {"date": f"مباريات اليوم - {today}", "leagues": []}
        temp_leagues = {}

        for event in events:
            # التحقق من اسم الدولة أو الدوري
            category = event.get('tournament', {}).get('category', {}).get('name', '')
            tournament = event.get('tournament', {}).get('name', '')
            
            # إذا كان الدوري من اللي بدنا إياهم
            if any(k in category or k in tournament for k in TARGET_KEYWORDS):
                league_key = f"{category} - {tournament}"
                if league_key not in temp_leagues:
                    temp_leagues[league_key] = []
                
                # توقيت المباراة
                match_time = datetime.fromtimestamp(event['startTimestamp']).strftime('%H:%M')
                
                temp_leagues[league_key].append({
                    "time": match_time,
                    "team1": event['homeTeam'].get('nameAr', event['homeTeam']['name']),
                    "team2": event['awayTeam'].get('nameAr', event['awayTeam']['name']),
                    "logo1": f"https://api.sofascore.app/api/v1/team/{event['homeTeam']['id']}/image",
                    "logo2": f"https://api.sofascore.app/api/v1/team/{event['awayTeam']['id']}/image",
                    "link": "#"
                })

        for name, matches in temp_leagues.items():
            data["leagues"].append({"name": name, "matches": matches})

        # إرسال البيانات النهائية
        res = requests.post(NPOINT_URL, json=data)
        if res.status_code == 200:
            print(f"مبروك! تم سحب {len(data['leagues'])} دوري بنجاح ✅")
        else:
            print("فشل إرسال البيانات لـ npoint")

    except Exception as e:
        print(f"حدث خطأ: {e}")

if __name__ == "__main__":
    get_matches()
