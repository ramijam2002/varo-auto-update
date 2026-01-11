import requests

# الرابط تبعك المعتمد
NPOINT_URL = "https://api.npoint.io/7c350afaa6af728cc142"

# قائمة الدوريات اللي بدنا نفلترها (أضفت لك الدوري الأردني يا غالي)
TARGET_LEAGUES = {
    "Jordan": "الدوري الأردني",
    "England": "الدوري الإنجليزي",
    "Spain": "الدوري الإسباني",
    "Germany": "الدوري الألماني",
    "Italy": "الدوري الإيطالي",
    "France": "الدوري الفرنسي",
    "Saudi Arabia": "الدوري السعودي",
    "Europe": "دوري أبطال أوروبا"
}

def get_matches():
    # رابط الـ API تبع مباريات اليوم من SofaScore
    url = "https://api.sofascore.com/api/v1/sport/football/scheduled-events/2026-01-11" # التاريخ بيتحدث تلقائياً بالكود المتقدم
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers)
        events = response.json().get('events', [])
        
        data = {"date": "مباريات اليوم - VARO LIVE", "leagues": []}
        temp_leagues = {}

        for event in events:
            league_name = event.get('tournament', {}).get('category', {}).get('name', '')
            
            if league_name in TARGET_LEAGUES:
                ar_league_name = TARGET_LEAGUES[league_name]
                
                if ar_league_name not in temp_leagues:
                    temp_leagues[ar_league_name] = []
                
                # سحب البيانات والشعارات الأصلية
                match_info = {
                    "time": "مباشر" if event.get('status', {}).get('type') == 'inprogress' else "قريباً",
                    "team1": event.get('homeTeam', {}).get('name', ''),
                    "team2": event.get('awayTeam', {}).get('name', ''),
                    "logo1": f"https://api.sofascore.app/api/v1/team/{event['homeTeam']['id']}/image",
                    "logo2": f"https://api.sofascore.app/api/v1/team/{event['awayTeam']['id']}/image",
                    "link": "#"
                }
                temp_leagues[ar_league_name].append(match_info)

        # تحويل البيانات للشكل اللي بيفهمه تطبيقك
        for name, matches in temp_leagues.items():
            data["leagues"].append({"name": name, "matches": matches})

        # إرسال البيانات لـ npoint
        requests.post(NPOINT_URL, json=data)
        print(f"تم سحب {len(data['leagues'])} دوريات بنجاح! ✅")

    except Exception as e:
        print(f"حدث خطأ: {e}")

if __name__ == "__main__":
    get_matches()
