import requests
from datetime import datetime

# رابط الـ npoint تبعك
NPOINT_URL = "https://api.npoint.io/6efc24dd557a89d1ee2d"

def fetch_live_matches():
    # سحب بيانات حقيقية ومحدثة من المصدر
    API_SOURCE = "https://raw.githubusercontent.com/saif-js/matches-api/main/data.json"
    
    try:
        response = requests.get(API_SOURCE)
        if response.status_code == 200:
            data = response.json()
            # تاريخ اليوم عشان يظهر بالتطبيق
            data["date"] = "مباريات " + datetime.now().strftime("%A - %d %B")
            return data
    except:
        return None

def update_varo_app():
    print("جاري سحب مباريات اليوم الحقيقية...")
    live_data = fetch_live_matches()
    
    if live_data:
        res = requests.post(NPOINT_URL, json=live_data)
        if res.status_code == 200:
            print("تم تحديث تطبيق VARO LIVE بنجاح! ✅")
        else:
            print("مشكلة في الإرسال لـ npoint")
    else:
        print("مشكلة في سحب البيانات من المصدر")

if __name__ == "__main__":
    update_varo_app()
