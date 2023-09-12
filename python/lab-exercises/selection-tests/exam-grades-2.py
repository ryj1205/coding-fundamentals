exam_mark = int(input("Please input the exam mark: "))
student_level = int(input("Please input the student level: "))

if (student_level == 1):
    if (exam_mark < 1 or exam_mark > 100):
        print("ERROR: marks must be between 1 and 100")
    else:
        if (exam_mark < 50):
            print("The exam result is: FAIL")
        elif (exam_mark >= 50 and exam_mark <= 60):
            print("The exam result is: PASS")
        elif (exam_mark > 60 and exam_mark <= 70):
            print("The exam result is: MERIT")
        elif (exam_mark > 70):
            print("The exam result is: DISTINCTION")
elif (student_level == 2):
    if (exam_mark < 1 or exam_mark > 100):
        print("ERROR: marks must be between 1 and 100")
    else:
        if (exam_mark < 40):
            print("The exam result is: FAIL")
        elif (exam_mark >= 40 and exam_mark <= 50):
            print("The exam result is: PASS")
        elif (exam_mark > 50 and exam_mark <= 65):
            print("The exam result is: MERIT")
        elif (exam_mark > 65):
            print("The exam result is: DISTINCTION")