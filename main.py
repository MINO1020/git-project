GradeSub = 0
GradeRead = 0
RatingPointSub = 0
RatingPointRead = 0
while True:
    print("작업을 입력하세요.\n")
    print("1. 입력\n")
    print("2. 계산\n")
    num = int(input())

    if num == 1:
        print("학점을 입력하세요. :\n")
        Grade = int(input())
        print("평점을 입력하세요. :\n")
        Rating = input()

        match Rating:
            case 'A+':
                GradeSub += Grade
                GradeRead += Grade
                RatingPointSub += (Grade * 4.5)
                RatingPointRead += (Grade * 4.5)
            case 'A':
                GradeSub += Grade
                GradeRead += Grade
                RatingPointSub += (Grade * 4.0)
                RatingPointRead += (Grade * 4.0)
            case 'B+':
                GradeSub += Grade
                GradeRead += Grade
                RatingPointSub += (Grade * 3.5)
                RatingPointRead += (Grade * 3.5)
            case 'B':
                GradeSub += Grade
                GradeRead += Grade
                RatingPointSub += (Grade * 3.0)
                RatingPointRead += (Grade * 3.0)
            case 'C+':
                GradeSub += Grade
                GradeRead += Grade
                RatingPointSub += (Grade * 2.5)
                RatingPointRead += (Grade * 2.5)
            case 'C1':
                GradeSub += Grade
                GradeRead += Grade
                RatingPointSub += (Grade * 2.0)
                RatingPointRead += (Grade * 2.0)
            case 'D+':
                GradeSub += Grade
                GradeRead += Grade
                RatingPointSub += (Grade * 1.5)
                RatingPointRead += (Grade * 1.5)
            case 'D':
                GradeSub += Grade
                GradeRead += Grade
                RatingPointSub += (Grade * 1.0)
                RatingPointRead += (Grade * 1.0)
            case 'F':
                GradeSub += 0
                GradeRead += Grade
                RatingPointSub += (Grade * 0)
                RatingPointRead += (Grade * 0)
    elif num == 2:
        GPASub = RatingPointSub/GradeSub
        GPARead = RatingPointRead/GradeRead
        print("제출용 : ", GradeSub, "학점", "(GPA: %.2f)" % GPASub)
        print("열람용 : ", GradeRead, "학점", "(GPA: %.2f)" % GPARead)
        print("\n")
        print("프로그램을 종료합니다.")
        break
