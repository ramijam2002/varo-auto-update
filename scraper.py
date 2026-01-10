import requests
from datetime import datetime

# رابط الـ npoint تبعك
NPOINT_URL = "https://api.npoint.io/6efc24dd557a89d1ee2d"

def fetch_all_matches():
    # مصدر بيانات عالمي ومحدث لحظة بلحظة
    API_SOURCE = "https://raw.githubusercontent.com/saif-js/matches-api/main/data.json"
    
    try:
        response = requests.get(API_SOURCE)
        if response.status_code == 200:
            data = response.json()
            # تحديث التاريخ ليظهر في تطبيقك الفخم
            data["date"] = "مباريات اليوم - " + datetime.now().strftime("%d %B")
            return data
    except:
        return None

def update_varo_live():
    print("جاري سحب كل مباريات اليوم من المصدر...")
    full_data = fetch_all_matches()
    
    if full_data:
        res = requests.post(NPOINT_URL, json=full_data)
        if res.status_code == 200:
            print("مبروك! تم تحديث الجدول بالكامل بنجاح ✅")
        else:
            print("مشكلة في الإرسال")
    else:
        print("مشكلة في جلب البيانات من المصدر")

if __name__ == "__main__":
    update_varo_live()
