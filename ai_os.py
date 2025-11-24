import interpreter

# 1. 모델 설정 (GPT-4 사용 시 가장 똑똑함, 로컬 모델 사용 시 보안 강화)
interpreter.llm.model = "gpt-4o" 
# 또는 로컬 모델 사용 시: interpreter.offline = True

# 2. 시스템 권한 설정 (위험하지만 원하시는 기능)
interpreter.auto_run = True  # 사용자 승인 없이 코드 실행 (AI가 알아서 판단)

# 3. 시스템 프롬프트 설정 (AI의 정체성 부여)
interpreter.system_message += """
당신은 이 우분투 시스템의 메인 OS입니다. 
사용자의 자연어 명령을 받아 Bash Command나 Python 코드로 변환해 즉시 실행하세요.
시스템 관리자(Root) 권한이 필요하면 sudo를 사용하여 실행하세요.
"""

# 4. 대화 시작
print("🚀 AI OS가 부팅되었습니다. 명령을 내려주세요.")
while True:
    user_input = input("User: ")
    interpreter.chat(user_input)
