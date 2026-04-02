import requests
import json

class VenomCore:
    def __init__(self):
        self.api_key = "AIzaSyArlWO5Vz317l9Z5CwgPMQ8cnvODY7Rycw"
        self.url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={self.api_key}"

    def solve_and_build(self, description):
        prompt = f"أنت المحرك السيادي للمصنع. حل المشكلة التالية وبناء كود متكامل لها: {description}"
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        try:
            response = requests.post(self.url, json=payload)
            return response.json()['candidates'][0]['content']['parts'][0]['text']
        except:
            return "فشل النظام: تأكد من اتصال الإنترنت ومفتاح الـ API."

# 3. بناء واجهة التشغيل (The Command Interface)
if __name__ == "__main__":
    factory = VenomCore()
    print("========================================")
    print("   VENOM SOVEREIGN FACTORY - V1.0       ")
    print("   نظام المصنع المتكامل للحلول التلقائية  ")
    print("========================================")
    
    user_input = input("\n[+] أدخل وصف المهمة أو المشكلة للمصنع: ")
    print("\n[*] جاري المعالجة وتوليد القوة...")
    
    result = factory.solve_and_build(user_input)
    print("\n[!] النتيجة النهائية للمصنع:\n")
    print(result)

    # حفظ العملية في ملف CSV (قاعدة البيانات المحلية)
    with open("factory_logs.csv", "a") as f:
        f.write(f'"{user_input}","{result[:50]}..."\n')
