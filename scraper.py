import requests
from datetime import datetime

# رابط الـ npoint تبعك
NPOINT_URL = "https://api.npoint.io/6efc24dd557a89d1ee2d"

def fetch_premium_matches():
    # مصدر بيانات محدث بشعارات عالية الجودة
    API_URL = "https://raw.githubusercontent.com/saif-js/matches-api/main/data.json"
    
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            data = response.json()
            # تحديث تاريخ اليوم الأحد
            data["date"] = "مباريات الأحد - " + datetime.now().strftime("%d %B")
            return data
    except:
        return None

def update_varo_app():
    print("جاري سحب المباريات بشعارات عالية الجودة...")
    data = fetch_premium_matches()
    
    if data:
        # إرسال البيانات للرابط تبعك
        res = requests.post(NPOINT_URL, json=data)
        if res.status_code == 200:
            print("تم التحديث بنجاح والشعارات الآن زابطة! ✅")
        else:
            print("في مشكلة بالرابط")
    else:
        print("المصدر مش راضي يجاوب")

if __name__ == "__main__":
    update_varo_app()
