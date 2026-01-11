import requests

NPOINT_URL = "https://api.npoint.io/7c350afaa6af728cc142"

def update_varo_matches():
    data = {
        "date": "مباريات القمة - الأحد 11 يناير",
        "leagues": [
            {
                "name": "نهائي السوبر الإسباني",
                "matches": [
                    {
                        "time": "22:00",
                        "team1": "ريال مدريد", "team2": "برشلونة",
                        "logo1": "https://api.sofascore.app/api/v1/team/2829/image", # رابط مباشر لريال مدريد
                        "logo2": "https://api.sofascore.app/api/v1/team/2817/image", # رابط مباشر لبرشلونة
                        "link": "#"
                    }
                ]
            }
        ]
    }
    requests.post(NPOINT_URL, json=data)
    print("تم تحديث الشعارات من سيرفرات SofaScore ✅")

if __name__ == "__main__":
    update_varo_matches()
