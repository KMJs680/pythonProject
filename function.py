#함수는 별도의 이름을 가졌고, 특정 작업만 하도록 설계된 코드 블록이다. 함수를 호출 하면 함수에 정의 된
#작업이 수행된다. 모듈(module)이라는 별도의 파일에 함수를 저장해 메인 프로그램을 간결하게 정리하는 방법도 있다.

#함수 정의하기
def greet_user():
    """단순한 인사말을 표시 합니다. """
    print("hello!")
greet_user()

#함수에 정보 전달하기
def greet_user(username):
    """단순한 인사말을 표현 합니다."""
    print(f"반가워! 귀여운, {username.title()}!")
greet_user('jangu!')