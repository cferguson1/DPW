
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
        #setup a private place for the inputs
        self.__inputs = []
        self._figure_inputs = ''


    #get private var inputs
    @property
    def inputs(self):
        pass

    #set private var inputs
    @inputs.setter
    def inputs(self, arr):
        #set it to the array we passed in
        self.__inputs = arr
        for item in arr:
            self._figure_inputs += '''
<figure>
    <figcaption>
            '''
            self._figure_inputs += '<p><span class="label">Phylum: </span>' + item['phylum'] + '</p>'
            self._figure_inputs += '<p><span class="label">Class: </span>' + item['class'] + '</p>'
            self._figure_inputs += '<p><span class="label">Order: </span>' + item['order'] + '</p>'
            self._figure_inputs += '<p><span class="label">Family: </span>' + item['family'] + '</p>'
            self._figure_inputs += '<p><span class="label">Genus: </span>' + item['genus'] + '</p>'
            self._figure_inputs += '<p><span class="label">URL: </span>' + item['imgurl'] + '</p>'
            self._figure_inputs += '<p><span class="label">Average Lifespan: </span>' + item['lifespan'] + '</p>'
            self._figure_inputs += '<p><span class="label">Habitat: </span>' + item['habitat'] + '</p>'
            self._figure_inputs += '<p><span class="label">Geolocation: </span>' + item['geolocation'] + '</p>'
            self._figure_inputs += '''
    </figcatpion>
</figure>
            '''










app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
