import requests

# رابط الـ npoint تبعك
NPOINT_URL = "https://api.npoint.io/6efc24dd557a89d1ee2d"

def fetch_and_update():
    # كود تجريبي للتأكد من الاتصال، رح نحدثه ليسحب من موقع حقيقي بالخطوة الجاية
    data = {
        "date": "مباريات محدثة تلقائياً",
        "leagues": [
            {
                "name": "الدوري الإسباني",
                "matches": [
                    {
                        "h_name": "ريال مدريد",
                        "h_logo": "https://ssl.gstatic.com/onebox/media/sports/logos/Th4fM9Z9yMreHlsE6q_atA_96x96.png",
                        "a_name": "برشلونة",
                        "a_logo": "https://ssl.gstatic.com/onebox/media/sports/logos/96x96/fcb.png",
                        "time": "22:00",
                        "status": "قريباً",
                        "is_live": False,
                        "link": "player.html"
                    }
                ]
            }
        ]
    }
    
    response = requests.post(NPOINT_URL, json=data)
    if response.status_code == 200:
        print("تم التحديث التلقائي بنجاح!")
    else:
        print("فشل التحديث، تأكد من الرابط")

if __name__ == "__main__":
    fetch_and_update()
