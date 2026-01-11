import requests

# الرابط تبعك المعتمد
NPOINT_URL = "https://api.npoint.io/7c350afaa6af728cc142"

def update_varo_matches():
    data = {
        "date": "مباريات اليوم - الأحد 11 يناير",
        "leagues": [
            {
                "name": "الدوري الإنجليزي",
                "matches": [
                    {
                        "time": "19:30",
                        "team1": "ليفربول",
                        "team2": "مانشستر سيتي",
                        "logo1": "https://upload.wikimedia.org/wikipedia/en/thumb/0/0c/Liverpool_FC.svg/800px-Liverpool_FC.svg.png",
                        "logo2": "https://upload.wikimedia.org/wikipedia/en/thumb/e/eb/Manchester_City_FC_badge.svg/800px-Manchester_City_FC_badge.svg.png",
                        "link": "https://example.com/live1"
                    }
                ]
            },
            {
                "name": "نهائي السوبر الإسباني",
                "matches": [
                    {
                        "time": "22:00",
                        "team1": "ريال مدريد",
                        "team2": "Varo",
                        "logo1": "https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Real_Madrid_CF.svg/800px-Real_Madrid_CF.svg.png",
                        "logo2": "https://upload.wikimedia.org/wikipedia/en/thumb/4/47/FC_Barcelona_logo.svg/800px-FC_Barcelona_logo.svg.png",
                        "link": "https://example.com/live2"
                    }
                ]
            }
        ]
    }
    
    print("جاري تحديث الشعارات الأصلية...")
    res = requests.post(NPOINT_URL, json=data)
    if res.status_code == 200:
        print("تم التحديث! الشعارات هسا رح تنور بالتطبيق ✅")

if __name__ == "__main__":
    update_varo_matches()
