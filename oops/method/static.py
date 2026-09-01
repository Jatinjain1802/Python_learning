class student:
    def __init__(self,name,rollnumber):
        self.name=name
        self.rollnumber=rollnumber
    @staticmethod
    def percentage(marks,total_marks):
        percentage=(((marks/total_marks)*100))
        return percentage
print(student.percentage(500,700))