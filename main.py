import flet as ft
import requests

def main(page: ft.Page):
    page.title = "VENOM SOVEREIGN FACTORY"
    page.theme_mode = ft.ThemeMode.DARK
    
    api_key = "AIzaSyArlWO5Vz317l9Z5CwgPMQ8cnvODY7Rycw"
    
    def solve_ai(e):
        if not task_input.value: return
        loader.visible = True
        page.update()
        
        prompt = f"حل هذه المهمة البرمجية كمصنع متكامل وباحترافية كاملة: {task_input.value}"
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
        
        try:
            res = requests.post(url, json={"contents": [{"parts": [{"text": prompt}]}]})
            solution = res.json()['candidates'][0]['content']['parts'][0]['text']
            output_box.value = solution
        except:
            output_box.value = "حدث خطأ في الاتصال بالنواة السيادية."
            
        loader.visible = False
        page.update()

    task_input = ft.TextField(label="وصف المهمة", multiline=True, border_color="purple")
    output_box = ft.Markdown(selectable=True)
    loader = ft.ProgressBar(width=400, color="purple", visible=False)
    
    page.add(
        ft.Text("VENOM FACTORY CORE", size=25, weight="bold", color="purple"),
        task_input,
        ft.ElevatedButton("توليد الحل التلقائي", on_click=solve_ai, bgcolor="purple", color="white"),
        loader,
        ft.Container(output_box, padding=10, border=ft.border.all(1, "purple"), border_radius=10)
    )

ft.app(target=main)
