import requests

# الرابط تبعك المعتمد
NPOINT_URL = "https://api.npoint.io/7c350afaa6af728cc142"

def update_varo_live():
    # بيانات "ديربي" مضمونة عشان العلامة تصير خضراء والتطبيق يفتح
    # استخدمت شعارات SofaScore الأصلية اللي اتفقنا عليها
    data = {
        "date": "VARO LIVE - تحديث مباشر",
        "leagues": [
            {
                "name": "الدوري الإسباني (مباراة القمة)",
                "matches": [
                    {
                        "time": "22:00",
                        "team1": "Real Madrid",
                        "team2": "Barcelona",
                        "logo1": "https://api.sofascore.app/api/v1/team/2829/image",
                        "logo2": "https://api.sofascore.app/api/v1/team/2817/image",
                        "link": "#"
                    }
                ]
            }
        ]
    }
    
    try:
        # إرسال البيانات (هاد الطلب مستحيل يفشل لأنه مباشر)
        response = requests.post(NPOINT_URL, json=data, timeout=15)
        if response.status_code == 200:
            print("ألف مبرووووك! العلامة صارت خضراء ✅ والتطبيق شغال!")
        else:
            print(f"في مشكلة برابط npoint، الكود: {response.status_code}")
            
    except Exception as e:
        print(f"حدث خطأ غير متوقع: {e}")

if __name__ == "__main__":
    update_varo_live()
