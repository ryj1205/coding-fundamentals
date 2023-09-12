average_exam_mark = (40 + 70 + 85) / 3
if average_exam_mark >= 65.00:
    print("PASS!")
else:
    print("FAIL")

##############################################################

min_value = 0
max_value = 100

exam_mark_maths = int(input("Please enter the exam mark for Maths: "))
while exam_mark_maths < min_value or exam_mark_maths > max_value:
    print("Error - that exam mark must be between 0 and 100")
    exam_mark_maths = int(input("Please enter the exam mark for Maths: "))

exam_mark_english = int(input("Please enter the exam mark for English: "))
while exam_mark_english < min_value or exam_mark_english > max_value:
    print("Error - that exam mark must be between 0 and 100")
    exam_mark_english = int(input("Please enter the exam mark for Maths: "))

exam_mark_ict = int(input("Please enter the exam mark for English: "))
while exam_mark_ict < min_value or exam_mark_ict > max_value:
    print("Error - that exam mark must be between 0 and 100")
    exam_mark_ict = int(input("Please enter the exam mark for Maths: "))

# ^ I would use a function for the while loop to avoid duplication of code ^

average_exam_mark = (exam_mark_maths + exam_mark_english + exam_mark_ict) / 3

print("Average Exam Mark - ", average_exam_mark)
print("Exam Mark - Maths", exam_mark_maths)
print("Exam Mark - English", exam_mark_english)
print("Exam Mark - ICT", exam_mark_ict)