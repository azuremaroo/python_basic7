# Student 클래스 설계
class Student():
    def __init__(self, name, *arg):
        self.name = name
        self.scoredata = arg

    def show_score(self):
        print(self.name,  sum(self.scoredata),  sum(self.scoredata)/len(self.scoredata))

Students_Scorelist = [
Student("홍길동", 88, 77, 95, 65), # 이름, korean, english, math, science
Student("대조영", 92, 83, 77, 85),
Student("손흥민", 100, 95, 90, 98),
Student("박찬호", 99, 78, 96, 73),
Student("피카츄", 76, 87, 92, 68)
]


# 이름 총점 평균 으로 출력
print("이름 \t 총점 \t 평균")
for student in Students_Scorelist:
    student.show_score()
