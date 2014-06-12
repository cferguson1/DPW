class Page(object):
    def __init__(self):
        self.title = "Application"
        self.css = "css/style.css"

        self.head = """
                    <!DOCTYPE HTML>
                    <html>
                        <head>
                            <title>{self.title}</title>
                            <link href="{self.css}" rel="Stylesheet" type="text/css" />
                            <link href='http://fonts.googleapis.com/css?family=Audiowide|Exo+2:400,500,700' rel='stylesheet' type='text/css'>
                        </head>
                        <body>
                    """

        self.body = " I'm in the body! "

        self.foot = """
                        </body>
                    </html>
                    """
    def print_out(self):
        html = self.head + self.body + self.foot
        html = html.format(**locals())
        return html