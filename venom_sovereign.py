import flet as ft
import requests
import json

def main(page: ft.Page):
    page.title = "VENOM SOVEREIGN FACTORY"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.scroll = "adaptive"

    # النواة الذكية (مفتاحك الخاص)
    API_KEY = "AIzaSyArlWO5Vz317l9Z5CwgPMQ8cnvODY7Rycw"

    def solve_ai(e):
        if not task_input.value: return
        
        loader.visible = True
        page.update()
        
        prompt = f"حل هذه المهمة البرمجية كمصنع متكامل وباحترافية كاملة: {task_input.value}"
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"
        
        try:
            res = requests.post(url, json={"contents": [{"parts": [{"text": prompt}]}]})
            solution = res.json()['candidates'][0]['content']['parts'][0]['text']
            output_box.value = solution
            # حفظ السجل تلقائياً (قاعدة البيانات)
            with open("sovereign_db.txt", "a") as f:
                f.write(f"Task: {task_input.value}\nSolution: {solution[:100]}...\n---\n")
        except:
            output_box.value = "حدث خطأ في النظام السيادي. تحقق من الاتصال."
            
        loader.visible = False
        page.update()

    # تصميم الواجهة الاحترافية
    task_input = ft.TextField(label="وصف المهمة (قوة لا يمكن اختراقها)", multiline=True, border_color="purple")
    output_box = ft.Markdown(selectable=True)
    loader = ft.ProgressBar(width=400, color="purple", visible=False)
    
    page.add(
        ft.Row([ft.Icon(ft.icons.SETTINGS_SUGGEST, color="purple"), ft.Text("VENOM CORE V1", size=25, weight="bold")]),
        ft.Divider(color="purple"),
        task_input,
        ft.ElevatedButton("تفعيل المعالجة التلقائية", on_click=solve_ai, bgcolor="purple", color="white"),
        loader,
        ft.Container(output_box, padding=10, border=ft.border.all(1, "purple"), border_radius=10)
    )

ft.app(target=main)
