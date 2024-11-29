import random

def main():
    print("숫자 맞추기 게임에 오신 것을 환영합니다!")
    
    # 1부터 100 사이의 랜덤 숫자 생성
    target_number = random.randint(1, 100)
    attempts = 0
    
    print("1부터 100 사이의 숫자를 맞춰보세요!")
    
    while True:
        # 사용자 입력 받기
        try:
            guess = int(input("추측한 숫자를 입력하세요: "))
            attempts += 1
            
            # 입력값 검증
            if guess < 1 or guess > 100:
                print("1부터 100 사이의 숫자를 입력해주세요!")
                continue
                
            # 숫자 비교
            if guess < target_number:
                print("더 큰 숫자입니다!")
            elif guess > target_number:
                print("더 작은 숫자입니다!")
            else:
                print(f"축하합니다! {attempts}번 만에 숫자를 맞추셨습니다!")
                break
                
        except ValueError:
            print("올바른 숫자를 입력해주세요!")

if __name__ == "__main__":
    main()