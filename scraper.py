import requests
from datetime import datetime

# رابط الـ npoint تبعك
NPOINT_URL = "https://api.npoint.io/6efc24dd557a89d1ee2d"

def update_varo():
    # سحب بيانات من مصدر رياضي ضخم فيه كل مباريات اليوم
    SOURCE = "https://raw.githubusercontent.com/saif-js/matches-api/main/data.json"
    try:
        data = requests.get(SOURCE).json()
        data["date"] = "مباريات اليوم - " + datetime.now().strftime("%d %B")
        requests.post(NPOINT_URL, json=data)
        print("تم سحب كل مباريات اليوم بنجاح! ✅")
    except:
        print("فشل السحب")

if __name__ == "__main__":
    update_varo()
