import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p1 = Person()
        p1.name = "Joe"
        p1.weight = 190
        p1.waist = 30.5
        p1.calc_fat()

        p2 = Person()
        p2.name = "John"
        p2.weight = 160
        p2.waist = 27
        p2.calc_fat()

        p3 = Person()
        p3.name = "Jack"
        p3.weight = 145
        p3.waist = 24
        p3.calc_fat()

        p4 = Person()
        p4.name = "Jake"
        p4.weight = 166
        p4.waist = 28
        p4.calc_fat()

        p5 = Person()
        p5.name = "Jerry"
        p5.weight = 220
        p5.waist = 39
        p5.calc_fat()

        p6 = Person()
        p6.name = "Jorge"
        p6.weight = 200
        p6.waist = 35
        p6.calc_fat()

        self.response.write("""
<!doctype html>
    <head>
        <title>Document</title>
        <link rel='stylesheet' href='css/style.css'>
    </head>
    <body>
    <div class="wrapper">
        <h1>Bodyfat Percentage Calculator for Men</h1>
""")

        self.response.write("""
        <div class="table">
            
                <div class="header">""")
        self.response.write(p1.name)
        self.response.write("""
                </div>
            
            
                <div class="label">Body Weight: </div>
                <div>""")
        self.response.write(p1.weight)
        self.response.write("""
                </div>
            
            
                <div class="label">Waist Circum. : </div>
                <div>""")
        self.response.write(p1.waist)
        self.response.write("""
                </div>
            
        </div>
        """)

        self.response.write("""
        <div class="table">
            
                <div class="header">""")
        self.response.write(p2.name)
        self.response.write("""
                </div>
            
            
                <div class="label">Body Weight: </div>
                <div>""")
        self.response.write(p2.weight)
        self.response.write("""
                </div>
            
            
                <div class="label">Waist Circum. : </div>
                <div>""")
        self.response.write(p2.waist)
        self.response.write("""
                </div>
            
        </div>
        """)

        self.response.write("""
        <div class="table">
            
                <div class="header">""")
        self.response.write(p3.name)
        self.response.write("""
                </div>
            
            
                <div class="label">Body Weight: </div>
                <div>""")
        self.response.write(p3.weight)
        self.response.write("""
                </div>
            
            
                <div class="label">Waist Circum. : </div>
                <div>""")
        self.response.write(p3.waist)
        self.response.write("""
                </div>
            
        </div>
        """)

        self.response.write("""
        <div class="table">
            
                <div class="header">""")
        self.response.write(p4.name)
        self.response.write("""
                </div>
            
            
                <div class="label">Body Weight: </div>
                <div>""")
        self.response.write(p4.weight)
        self.response.write("""
                </div>
            
            
                <div class="label">Waist Circum. : </div>
                <div>""")
        self.response.write(p4.waist)
        self.response.write("""
                </div>
            
        </div>
        """)

        self.response.write("""
        <div class="table">
            
                <div class="header">""")
        self.response.write(p5.name)
        self.response.write("""
                </div>
            
            
                <div class="label">Body Weight: </div>
                <div>""")
        self.response.write(p5.weight)
        self.response.write("""
                </div>
            
            
                <div class="label">Waist Circum. : </div>
                <div>""")
        self.response.write(p5.waist)
        self.response.write("""
                </div>
            
        </div>
        """)

        self.response.write("""
        <div class="table">

                <div class="header">""")
        self.response.write(p6.name)
        self.response.write("""
                </div>


                <div class="label">Body Weight: </div>
                <div>""")
        self.response.write(p6.weight)
        self.response.write("""
                </div>


                <div class="label">Waist Circum. : </div>
                <div>""")
        self.response.write(p6.waist)
        self.response.write("""
                </div>

        </div>
        """)



        self.response.write("""
    </div>
    </body>
</html>""")


class Person(object):
    def __init__(self):
        self.name = "Name"
        self.weight = 0
        self.waist = 0
        self.__body_fat = 0

    @property
    def body_fat(self):
        return self.__body_fat

    @body_fat.setter
    def body_fat(self, new_body_fat):
        self.__body_fat = new_body_fat

    def calc_fat(self):
        self.__body_fat = ((self.weight - (((self.weight * 1.082) + 94.42) - (self.waist * 4.15))) * 100) / self.weight

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
