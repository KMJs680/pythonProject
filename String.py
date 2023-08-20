name = "ada Lovelace"
#title()메서드는 파이썬이 데이터에서 수행할 수 있는 동작, title() 메서드는 문자열의 각 단어 첫글자를 대문자로 변환해줌
#upper() 메서드는 문자열 전체를 대문자로 변환 / lower() 메서드는 문자열 전체를 소문자로 변환
print(name.title())
print(name.upper())
print(name.lower())

#문자열 안에서 변수 사용
first_name = "jang"
last_name = "gu"
full_name = f"{first_name} {last_name}"
print("우리집 강아지 : " + full_name)
print(f"Hello, {full_name.title()}!")

#공백 제거
favorite_language = '    python   '
#모든 공백 제거
print(favorite_language.strip())
#오른쪽 공백 제거
print(favorite_language.rstrip())
#왼쪽 공백 제거
print(favorite_language.lstrip())


#접두사 제거
nostarch_url = 'https://www.naver.com/'
print('https 제거 전 : ' , nostarch_url)
print('https 제거 후 : ' ,nostarch_url.removeprefix('https://'))

#문자열의 문법 에러 피하기
message = "One of Python's strengths is its diverse community!"
#작은 따옴표로 표기하면 에러가 난다.
#message2 = 'One of Python's strengths is its diverse community!'
print(message)

#문제 1: 변수에 사람의 이름을 저장하고 그 사람에게 보내는 메시지를 출력하세요.
tongs = 'tongtong'
print("메세지 : " + f"Hello, {tongs.title()} 오늘 파이썬을 배워보는게 어떨가요?")
print("=====================================================================")

#문제 2: 위인의 이름과 명언을 출력하세요. (핵심 단어에 따옴표를 출력하세요)
famousPerson = "프리다칼로"
famousSaying = ("절대적인 것은 없다. "
                "\n 모든 것은 '바뀌고', "
                "\n 모든 것은 '움직이고', "
                "\n 모든 것은 '회전하고', "
                "\n 모든 것은 '떠오르고' '사라진다'.")
print(f"\n{famousSaying}\n \t{famousPerson}")

