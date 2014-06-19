
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #create instance of Animal
        a = Animal()
        #pass some animals
        a.inputs = ['Name','Phylum','Class','Order','Family','Genus','Species','imgurl','lifespan','Habitat','Geolocation' ]
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
        print arr
        for item in arr:
            self._figure_inputs += '''
<figure>
    <figcaption>
            '''
            self._figure_inputs += '<p>' + item[0] + '</p>'
            self._figure_inputs += '<p><span class="label">Phylum: </span>' + item[1] + '</p>'
            self._figure_inputs += '<p><span class="label">Class: </span>' + item[2] + '</p>'
            self._figure_inputs += '<p><span class="label">Order: </span>' + item[3] + '</p>'
            self._figure_inputs += '<p><span class="label">Family: </span>' + item[4] + '</p>'
            self._figure_inputs += '<p><span class="label">Genus: </span>' + item[5] + '</p>'
            self._figure_inputs += '<p><span class="label">Species: </span>' + item[6] + '</p>'
            self._figure_inputs += '<p><span class="label">URL: </span>' + item[7] + '</p>'
            self._figure_inputs += '<p><span class="label">Average Lifespan: </span>' + item[8] + '</p>'
            self._figure_inputs += '<p><span class="label">Habitat: </span>' + item[9] + '</p>'
            self._figure_inputs += '<p><span class="label">Geolocation: </span>' + item[10] + '</p>'
            self._figure_inputs += '''
    </figcatpion>
</figure>
            '''

    #override superclass and print this
    def print_out(self):
        return self._open + self._figure_inputs + self._close








app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
