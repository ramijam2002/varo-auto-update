import requests

# الرابط اللي بالصورة تبعتك بالظبط
NPOINT_URL = "https://api.npoint.io/7c350afaa6af728cc142"

def force_update():
    # بيانات تجريبية سريعة عشان نتأكد إنه اشتغل
    data = {
        "date": "تم التحديث بنجاح ✅",
        "leagues": [
            {
                "name": "الدوري الإنجليزي",
                "matches": [
                    {
                        "time": "18:00",
                        "team1": "ليفربول",
                        "team2": "مانشستر سيتي",
                        "logo1": "https://ssl.gstatic.com/onebox/media/sports/logos/0iTh9rq34dW9pzzS87D9oQ_48x48.png",
                        "logo2": "https://ssl.gstatic.com/onebox/media/sports/logos/z44lWGywnAsclwi9Wqz97A_48x48.png",
                        "link": "#"
                    }
                ]
            }
        ]
    }
    
    print("جاري الإرسال للرابط...")
    res = requests.post(NPOINT_URL, json=data)
    if res.status_code == 200:
        print("مبروك! البيانات وصلت الرابط ✅")
    else:
        print(f"خطأ في الإرسال: {res.status_code}")

if __name__ == "__main__":
    force_update()
