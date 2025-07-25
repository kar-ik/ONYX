from deepface import DeepFace
import requests
import base64

def analyze_photo(img_path):
    print("[+] Performing DeepFace analysis...")
    try:
        result = DeepFace.analyze(img_path=img_path, actions=["age", "gender", "emotion", "race"])
    except Exception as e:
        result = {"error": str(e)}

    yandex_url = "https://yandex.com/images/search?rpt=imageview&url="
    with open(img_path, "rb") as f:
        img_data = base64.b64encode(f.read()).decode()
    reverse_img_url = yandex_url + img_data

    return {"deepface": result, "reverse_image": reverse_img_url}
