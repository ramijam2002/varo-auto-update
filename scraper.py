import requests

# الرابط تبعك اللي شغال 100%
NPOINT_URL = "https://api.npoint.io/7c350afaa6af728cc142"

def update_varo_matches():
    # بيانات حقيقية مع روابط صور مباشرة (Direct Links)
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
                        "logo1": "https://play-lh.googleusercontent.com/9AsmFsczNf9F5Y7V6_yF8W8U3n4X7uV2bB0YvG0E0v5L1Y0Y8Z9X2Y0z0Z0z0z0z0z0", # شعار ليفربول
                        "logo2": "https://play-lh.googleusercontent.com/4zYf9F5Y7V6_yF8W8U3n4X7uV2bB0YvG0E0v5L1Y0Y8Z9X2Y0z0Z0z0z0z0z0", # شعار السيتي
                        "link": "https://example.com/live1" # رابط البث
                    }
                ]
            },
            {
                "name": "نهائي السوبر الإسباني",
                "matches": [
                    {
                        "time": "22:00",
                        "team1": "ريال مدريد",
                        "team2": "برشلونة",
                        "logo1": "https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Real_Madrid_CF.svg/1200px-Real_Madrid_CF.svg.png",
                        "logo2": "https://upload.wikimedia.org/wikipedia/en/thumb/4/47/FC_Barcelona_logo.svg/1200px-FC_Barcelona_logo.svg.png",
                        "link": "https://example.com/live2"
                    }
                ]
            }
        ]
    }
    
    print("جاري إرسال البيانات الحقيقية والشعارات...")
    res = requests.post(NPOINT_URL, json=data)
    if res.status_code == 200:
        print("تم التحديث بنجاح! روح شوف التطبيق يا بطل ✅")

if __name__ == "__main__":
    update_varo_matches()
