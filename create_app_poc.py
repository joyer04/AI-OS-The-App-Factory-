import interpreter
import os
import subprocess
import time

# 1. 설정: Gemini 모델 (미래의 Gemini 3라고 가정하고 현재 최신 모델 연결)
interpreter.llm.model = "gpt-4o"  # 혹은 "gemini-pro-1.5"

# 2. 시스템 프롬프트: 앱 개발자 페르소나 추가
interpreter.system_message = """
당신은 'Gemini OS'의 코어입니다.
두 가지 역할을 수행합니다:
1. 시스템 제어: 사용자의 명령을 리눅스 쉘로 실행.
2. 앱 생성(App Factory): 사용자가 '앱 만들어줘'라고 하면, 
   Python의 'Streamlit' 라이브러리를 사용해 즉시 실행 가능한 GUI 앱 코드를 작성하고 저장하세요.
   파일명은 'generated_app.py'로 저장하고, 백그라운드에서 실행 명령을 내리세요.
"""

# 3. 안전장치 (그대로 유지)
FORBIDDEN = ["rm -rf", "mkfs"]
interpreter.auto_run = True

print("✨ Gemini OS with App Factory Online.")
print("   Tip: '환율 계산기 앱 만들어줘'라고 말해보세요.\n")

while True:
    user_input = input("User: ")
    
    if user_input.lower() in ['exit', 'quit']:
        break
        
    # 앱 생성 요청인지 판단하기 위한 프롬프트 엔지니어링
    # (실제 Gemini 3라면 의도를 완벽히 파악하겠지만, 지금은 프롬프트로 유도)
    prompt = f"""
    사용자 입력: "{user_input}"
    
    [지침]
    1. 만약 사용자가 '앱'이나 '프로그램', '계산기', '도구' 등을 만들어 달라고 하면:
       - Python Streamlit 코드를 작성하세요.
       - 코드는 완벽하게 작동해야 하며 'app_gen.py' 파일로 저장하세요.
       - 그리고 `streamlit run app_gen.py` 명령어를 실행하여 앱을 띄우세요.
       
    2. 일반 시스템 명령이면:
       - 그냥 기존처럼 bash/python으로 처리하세요.
       
    3. 금기어 {FORBIDDEN}는 절대 실행 금지.
    """
    
    interpreter.chat(prompt)
