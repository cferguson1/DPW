
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #create instance of Animal
        a = Animal()
        #pass animals to Animal object
        a.inputs = [ ['Cat','1','2','3','4','5','6','7','8','9','10','11'], ['Dog','1','2','3','4','5','6','7','8','9','10','11'], ['Mouse','1','2','3','4','5','6','7','8','9','10','11'] ]
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
        #create a form for user to choose animal
        self._body = "Hello World"
        self._close = '''
        <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
        <script type="text/javascript" src="js/script.js">
    </body>
</html>
        '''

    #print content
    def print_out(self, name):
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
        #for each animal, print out a figure
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
            self._figure_inputs += '<p><span>What does the ' + item[0] + ' say?<span></p>'
            self._figure_inputs += '<p>' + item[11] + '</p>'
            self._figure_inputs += '''
    </figcaption>'''
            self._figure_inputs += '<input type="button" value="' + item[0] + '" />'
            self._figure_inputs += '''
</figure>
            '''

    def print_out(self):
        return self._open + self._figure_inputs + self._close


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
