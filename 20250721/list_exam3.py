
# list 활용 문제

StudentScorelist = [["Kor"],["Eng"],["Math"]]

# 한 학생의 국어, 영어, 수학 점수를 키보드로 입력 처리
# 결과 예) [["Kor",90],["Eng",80],["Math",70]]
# 국어, 영어, 수학의 총점 출력
# 평균 계산해서 출력

totalscore = 0
for item in StudentScorelist:
    item.append(int(input(item[0] + " 점수 입력 : ")))  # == int(input("{} 점수 입력 : ".format(grade[0])))
    totalscore += item[1]

print(StudentScorelist)
print("총 점수 : " , totalscore)
print("평균 점수 : {:.3f}".format(totalscore/len(StudentScorelist)))