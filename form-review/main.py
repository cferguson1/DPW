'''
Collin Ferguson
6/11/14
DPW
Form Review
'''

import webapp2

class MainHandler(webapp2.RequestHandler):

    def get(self):
        page_head = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Form Review</title>
    </head>
    <body>'''

        page_body = '''
<a href="?email=mickey@disney.com&user=Mickey">Mickey</a><br/>
<a href="?email=donald@disney.com&user=Donald">Donald</a><br/>
<a href="?email=minnie@disney.com&user=Minnie">Minnie</a><br/>
<a href="?email=goofy@disney.com&user=Goofy">Goofy</a><br/>
        '''

        page_close = '''</form>
    </body>
</html>'''


        if self.request.GET:
            #Store form info
            user = self.request.GET['user']
            email = self.request.GET['email']
            self.response.write(page_head + user + ' ' + email + ' ' + page_body + page_close)
        else:
            self.response.write(page_head + page_body + page_close)

        #self.response.write(page) #PRINT

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
