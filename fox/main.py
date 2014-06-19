
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #create instance of Animal
        a = Animal()
        self.response.write(a.print_out())

class AbstractAnimal(object):
    #initialize Object
    def __init__(self):
        self._open = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>What does the fox say?</title>
        <link rel="stylesheet" type="text/css" href="css/styles.css"/>
    </head>
    <body>
        '''
        self._body = "Hello World!"
        self._close = '''
    </body>
</html>
        '''

    #print content
    def print_out(self):
        return self._open + self._body + self._close


class Animal(AbstractAnimal):
    def __init__(self):
        #call Superclass::__init__
        super(Animal, self).__init__()
        self.__inputs = []





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
