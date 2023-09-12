exam_mark = int(input("Please input the exam mark: "))

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