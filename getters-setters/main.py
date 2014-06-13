import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        t = Transcript()
        t.grade1 = 90
        t.grade2 = 100
        t.quiz1 = 75
        t.quiz2 = 99
        self.response.write("Tommy's final grade is " + str(t.final_grade)) #pulling property, not private variable

        s = Transcript()
        s.grade1 = 45
        s.grade2 = 80
        s.quiz1 = 66
        s.quiz2 = 76
        self.response.write("<br/>Sally's final grade is " + str(s.final_grade)) #pulling property, not private variable


class Transcript(object):
    def __init__(self):
        self.grade1 = 0
        self.grade2 = 0
        self.quiz1 = 0
        self.quiz2 = 0
        self.final_exam = 0
        self.__final_grade = 0 #__private

    @property
    def final_grade(self):
        #calculate final grade
        self.__final_grade = (self.grade1 + self.grade2 + self.quiz1 + self.quiz2 + self.final_exam)/5
        return self.__final_grade

    @final_grade.setter
    def final_grade(selfnew):

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
