import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise RuntimeError("GOOGLE_API_KEY が見つかりません。.env を確認してください。")

genai.configure(api_key=api_key)

# 速さ重視なら 2.5-flash、精度重視なら 2.5-pro に差し替え可
model = genai.GenerativeModel("gemini-2.5-flash")

resp = model.generate_content("こんにちは。1行で自己紹介して。")
print(resp.text)
