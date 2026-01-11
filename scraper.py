import requests

NPOINT_URL = "https://api.npoint.io/7c350afaa6af728cc142"

def update_varo_matches():
    # البيانات مستخرجة بدقة من صورة "رادار كورة" بتاريخ 11 يناير
    data = {
        "date": "مباريات اليوم - الأحد 11 يناير 2026",
        "leagues": [
            {
                "name": "الدوري الإسباني - الجولة 19",
                "matches": [
                    {
                        "time": "22:00",
                        "team1": "Real Madrid", "team2": "Barcelona",
                        "logo1": "https://api.sofascore.app/api/v1/team/2829/image",
                        "logo2": "https://api.sofascore.app/api/v1/team/2817/image"
                    },
                    {
                        "time": "04:00",
                        "team1": "Rayo Vallecano", "team2": "Mallorca",
                        "logo1": "https://api.sofascore.app/api/v1/team/2818/image",
                        "logo2": "https://api.sofascore.app/api/v1/team/2825/image"
                    }
                ]
            },
            {
                "name": "الدوري الإيطالي - الجولة 20",
                "matches": [
                    {
                        "time": "10:45",
                        "team1": "Napoli", "team2": "Inter",
                        "logo1": "https://api.sofascore.app/api/v1/team/2714/image",
                        "logo2": "https://api.sofascore.app/api/v1/team/2697/image"
                    },
                    {
                        "time": "05:00",
                        "team1": "Milan", "team2": "Fiorentina",
                        "logo1": "https://api.sofascore.app/api/v1/team/2692/image",
                        "logo2": "https://api.sofascore.app/api/v1/team/2693/image"
                    }
                ]
            },
            {
                "name": "الدوري الألماني - الجولة 16",
                "matches": [
                    {
                        "time": "07:30",
                        "team1": "Bayern Munich", "team2": "Wolfsburg",
                        "logo1": "https://api.sofascore.app/api/v1/team/2672/image",
                        "logo2": "https://api.sofascore.app/api/v1/team/2685/image"
                    }
                ]
            },
            {
                "name": "كأس الاتحاد الإنجليزي - الدور الثالث",
                "matches": [
                    {
                        "time": "07:30",
                        "team1": "Manchester United", "team2": "Brighton",
                        "logo1": "https://api.sofascore.app/api/v1/team/35/image",
                        "logo2": "https://api.sofascore.app/api/v1/team/30/image"
                    },
                    {
                        "time": "05:00",
                        "team1": "Arsenal", "team2": "Portsmouth",
                        "logo1": "https://api.sofascore.app/api/v1/team/42/image",
                        "logo2": "https://api.sofascore.app/api/v1/team/41/image"
                    }
                ]
            }
        ]
    }
    
    try:
        response = requests.post(NPOINT_URL, json=data, timeout=15)
        if response.status_code == 200:
            print("تم تحديث جدول المباريات من الصورة بنجاح! ✅")
        else:
            print(f"فشل التحديث، كود الخطأ: {response.status_code}")
    except Exception as e:
        print(f"خطأ: {e}")

if __name__ == "__main__":
    update_varo_matches()
