'''Class method'''
class student:
    school="Adarsh vidyalya"
    principal="Gundegowda"
    fees=200000
    @classmethod
    def change(cls):
        cls.fees=cls.fees+50000      #modification logic
        # if cls.fees>=200000:
        #   new_fees=cls.fees+50000  
        # cls.fees=new_fees
        # cls.school=cls.school.upper()
        print(cls.fees)
    @classmethod
    def display_school(cls):
        print(cls.school)
        
        
student.change()
student.change()
student.change()
student.change()

student.display_school()
# print(student.__dict__)