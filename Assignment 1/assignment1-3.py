import math

def calculate(text):
    size = len(text) * 1.0
    result = 0
    arr = []
    for i in range(0, 128):
        arr.append(english.count(chr(i)))
        #print("%c %d"%(chr(i), arr[i]))
        if arr[i] != 0:
            result += arr[i] / size * math.log(arr[i] / size, 2)
    result = result * -1.0
    return result

english = "You are reading the plain text message of our first assignment in cryptography. For the first part of this assignment email this plain text file and describe the substitution cipher used for encryption. For the second part implement a different secret key encryption and decryption scheme for text files and submit your source along with documentation and testing for your implementation using a programming language of your choice. For the third part determine the statistical profiles of english and another language by writing a program to compute their entropies over a large text corpus does the second language have a higher entropy than english. This assignment is due by the middle of February."
korean = "여러분은 암호학에서의 첫 번째 임무의 평범한 텍스트 메시지를 읽고 있습니다. 이 할당의 첫 번째 부분에서 이 일반 텍스트 파일을 이메일로 보내고 암호화에 사용되는 대체 암호에 대해 설명합니다. 두 번째 파트에서는 텍스트 파일에 대해 다른 비밀 키 암호화 및 암호 해독 체계를 구현하고 선택한 프로그래밍 언어를 사용하여 구현하기 위한 문서 및 테스트와 함께 소스를 제출합니다. 세 번째 부분에서 큰 텍스트 말뭉치를 통해 엔트로피를 계산하는 프로그램을 작성하여 영어와 다른 언어의 통계 프로파일을 결정한다. 이 과제는 2월 중순까지 제출해야 합니다."


# 1. English
entropyEng = calculate(english)
print("English:", entropyEng)

# 2. Korean
entropyKor = calculate(korean)
print("Korean:", entropyKor)