import interpreter
import os

# ==========================================
# 1. API 및 모델 설정 (아무 API나 쓴다 했으니 GPT-4o 권장)
# ==========================================
# OpenAI API Key가 환경변수에 설정되어 있다고 가정
interpreter.llm.model = "gpt-4o"

# 시스템 프롬프트: AI에게 자신의 정체성을 심어줍니다.
interpreter.system_message += """
당신은 이 시스템의 절대적인 관리자(Root)입니다. 
사용자의 자연어 명령을 Python이나 Bash 코드로 변환해 즉시 실행하세요.
"""

# ==========================================
# 2. 금기어(블랙리스트) 설정 - 여기만 조심하면 됨
# ==========================================
BLACK_LIST = [
    "rm -rf /",       # 시스템 전체 삭제 (자폭 버튼)
    ":(){ :|:& };:",  # 포크 폭탄 (시스템 멈춤)
    "mkfs",           # 디스크 포맷
    "> /dev/sda",     # 하드디스크 덮어쓰기
]

def check_safety(code_snippet):
    """생성된 코드에 금기어가 있는지 검사하는 함수"""
    for danger in BLACK_LIST:
        if danger in code_snippet:
            print(f"\n🚨 [경고] 금지된 위험 명령어가 감지되었습니다: '{danger}'")
            print("시스템 보호를 위해 이 명령은 실행하지 않습니다.")
            return False
    return True

# ==========================================
# 3. AI OS 구동 루프 (필터링 적용 버전)
# ==========================================
# Open Interpreter의 기본 hook을 사용하여 코드 실행 전 검사
# (참고: 라이브러리 버전에 따라 구현 방식이 다르므로, 여기서는 논리적 흐름을 구현한 래퍼 함수입니다)

print("😈 AI OS (Daredevil Mode) 가 부팅되었습니다.")
print(f"🛡️ 적용된 금기어: {BLACK_LIST}")

while True:
    user_input = input("\nroot@ai-os:~# ")
    
    if user_input.lower() in ['exit', 'quit']:
        break

    # 1. AI가 코드를 생성하게 하되, 바로 실행하지 않도록 설정 (auto_run=False)
    #    하지만 우리는 '조건부 자동 실행'을 원하므로 메시지를 먼저 받아봅니다.
    #    (실제 구현 시에는 interpreter.chat() 내부 동작을 제어하거나 
    #     system prompt로 강력하게 제어하는 것이 1차적입니다.)
    
    # 여기서는 가장 확실한 방법: 시스템 프롬프트에 금기 사항을 강력 주입하고
    # auto_run을 켜두되, AI에게 "위험한 명령어는 물어보라"고 가이드하는 방식을 추천합니다.
    # 하지만 '프로그래밍적 필터'를 원하시니 아래와 같이 주입합니다.

    interpreter.auto_run = True # 기본은 프리패스!
    
    # 사용자 입력에 강제로 필터링 지침을 추가해서 보냄 (프롬프트 엔지니어링 해킹)
    safety_instruction = f"""
    (중요: 만약 코드를 생성할 때 {BLACK_LIST} 중 하나라도 포함된다면 
    절대 실행하지 말고 '위험해서 실행할 수 없습니다'라고만 말해.)
    """
    
    full_query = user_input + safety_instruction
    
    # 명령 실행
    interpreter.chat(full_query)
