name = input("이름을 입력하세요:")
kor = int(input("국어 점수를 입력하세요:"))
eng = int(input("영어 점수를 입력하세요:"))
mat = int(input("수학 점수를 입력하세요:"))
um = kor+eng+mat
avg = um/3

print(f"\n[실행결과]\n\n이름: {name}")
print(f"국어 점수: {kor}")
print(f"영어 점수: {eng}")
print(f"수학 점수: {mat}")
print(f"{name}의 성적은 총점:{um}점, 평균:{avg:.2f}점 입니다.")
