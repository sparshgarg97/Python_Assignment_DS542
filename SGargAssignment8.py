class University:
    def __init__(self, university_name, location, undergraduate_students, graduate_students):
        self.university_name = university_name
        self.location = location
        self.undergraduate_students = undergraduate_students
        self.graduate_students = graduate_students
        
    def print_university_size(self):
        total = self.undergraduate_students + self.graduate_students
        print('University Size: ', total)
    
    def is_undergraduate_greater(self):
        if self.undergraduate_students > self.graduate_students:
            print('There are more undergraduate students than graduate students')
        else:
            print('There are more graduate students than undergraduate students')

SPU = University('Saint Peters University', 'Jersey City', 5123, 3090)
SPU.print_university_size()
SPU.is_undergraduate_greater()
    
class College(University):
    
    def print_college_name(self):
        print("This is Child Method. This is the Data Science College")
        
DS = College('SPU', 'NJ', 2343, 434)
DS.print_college_name()
    
    