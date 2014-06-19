
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

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
        self.body = ""
        self._close = '''
    </body>
</html>
        '''

    #print content
    def print_out(self):
        pass


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
