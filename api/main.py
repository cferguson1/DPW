
import webapp2
import urllib2 #so we can open URLs
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [ ['artist_name', 'text', 'Artist Name'],['song_name', 'text', 'Song Name'],['Submit', 'submit'] ]
        self.response.write(p.print_out())

        if self.request.GET:
            #get API info
            lm = LyricModel()
            lm.artist = self.request.GET['artist_name']
            lm.song = self.request.GET['song_name']
            lm.callApi()

class LyricModel(object):
    ''' Model handles processing api data '''
    def __init__(self):
        self.__url = "http://api.chartlyrics.com/apiv1.asmx/SearchLyricDirect?artist="
        self.__url2 = "&song="
        self.__artist = ''
        self.__song = ''
        self.__xmldoc = ''

    def callApi(self):
        request = urllib2.Request(self.__url + self.__artist + self.__url2 + self.__song)
        opener = urllib2.build_opener()
        #use url to get a result
        result = opener.open(request)

        #parse XML
        self.__xmldoc = minidom.parse(result)
        self._dos = []
        do = LyricData()
        do.artistName = xmldoc.getElementsByTagName('LyricArtist')[0].firstChild.nodeValue
        do.lyrics = xmldoc.getElementsByTagName('Lyric')[0].firstChild.nodeValue
        self._dos.append(do)


    @property
    def artist(self):
        pass

    @artist.setter
    def artist(self, a):
        self.__artist = a

    @property
    def song(self):
        pass

    @song.setter
    def song(self, s):
        self.__artist = s

class LyricData(object):
    ''' hold data fetched by model and shown by view '''
    def __init__(self):
        self.artistName = ''
        self.lyrics = ''

class Page(object): #borrowing stuff from the object class
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
    </head>
    <body>'''

        self._body = 'Lyrics App'
        self._close = '''
    </body>
</html>'''

    def print_out(self):
        return self._head + self._body + self._close

class FormPage(Page):
    def __init__(self):
        #constructor func for the super class
        super(FormPage, self).__init__() #Page.__init__()
        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
        self.__inputs = []
        self._form_inputs = ''

    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, arr):
        #change my private inputs variable
        self.__inputs = arr
        #sort through the array and create HTML inputs
        for item in arr:
            self._form_inputs += '<input type="' + item[1] + '" name="' + item[0]
            #if there is a third item, add it in
            try:
                self._form_inputs += '" placeholder="' + item[2] + '" />'
            #otherwise end the tag
            except:
                self._form_inputs += '" />'

    def print_out(self):
        return self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
