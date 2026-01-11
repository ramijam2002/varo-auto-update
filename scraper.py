import requests
from datetime import datetime

NPOINT_URL = "https://api.npoint.io/7c350afaa6af728cc142"

# فلتر الدوريات (أضفت لك معرفات الأرقام عشان نضمن السحب)
TARGET_LEAGUES = ["الأردن", "إنجلترا", "إسبانيا", "السعودية", "ألمانيا", "إيطاليا", "فرنسا", "أبطال"]

def get_matches():
    # التاريخ الحالي بشكل تلقائي
    today = datetime.now().strftime('%Y-%m-%d')
    url = f"https://api.sofascore.com/api/v1/sport/football/scheduled-events/{today}"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print("سيرفر SofaScore ما رد علينا")
            return

        events = response.json().get('events', [])
        data = {"date": f"مباريات اليوم - {today}", "leagues": []}
        temp_leagues = {}

        for event in events:
            # سحب اسم الدوري واسم الدولة
            league_name = event.get('tournament', {}).get('name', '')
            country_name = event.get('tournament', {}).get('category', {}).get('name', '')
            
            # إذا الدوري أو الدولة ضمن قائمتنا
            if any(target in league_name or target in country_name for target in TARGET_LEAGUES):
                full_name = f"{country_name} - {league_name}"
                if full_name not in temp_leagues:
                    temp_leagues[full_name] = []
                
                match_info = {
                    "time": datetime.fromtimestamp(event['startTimestamp']).strftime('%H:%M'),
                    "team1": event.get('homeTeam', {}).get('nameAr', event['homeTeam']['name']),
                    "team2": event.get('awayTeam', {}).get('nameAr', event['awayTeam']['name']),
                    "logo1": f"https://api.sofascore.app/api/v1/team/{event['homeTeam']['id']}/image",
                    "logo2": f"https://api.sofascore.app/api/v1/team/{event['awayTeam']['id']}/image",
                    "link": "#"
                }
                temp_leagues[full_name].append(match_info)

        for name, matches in temp_leagues.items():
            data["leagues"].append({"name": name, "matches": matches})

        # إرسال البيانات (حتى لو فاضية رح نحدث التاريخ عشان نعرف إنه شغال)
        requests.post(NPOINT_URL, json=data)
        print(f"تم تحديث {len(data['leagues'])} دوريات ✅")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_matches()
