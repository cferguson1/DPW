'''
Collin Ferguson
6/11/14
DPW Online
Lab 2 Simple Form
'''

import webapp2
from application import Page

class MainHandler(webapp2.RequestHandler):

    def get(self):

        home_page = Page()
        home_page.title = "Apply Now"

        review_page = Page()
        review_page.title = "Review The Application"

        home_page.body = '''
<div class="wrapper">
    <h1>{self.title}</h1>

    <div class="inner-wrap">
        <form type="GET">

            <div class="row">
                <label>Name: </label>
                <input class="inputbox" type="text" name="name" />
            </div>

            <div class="row">
                <label>Server: </label>
                <input class="inputbox" type="text" name="server" />
            </div>

            <div class="row">
                <label>Level: </label>
                <input class="inputbox" type="text" name="level" />
            </div>

            <div class="row">
                <label>Class: </label>
                <select name="class" class="select">
                    <option value="Warrior">Warrior</option>
                    <option value="Paladin">Paladin</option>
                    <option value="Hunter">Hunter</option>
                    <option value="Rogue">Rogue</option>
                    <option value="Priest">Priest</option>
                    <option value="Death Knight">Death Knight</option>
                    <option value="Shaman">Shaman</option>
                    <option value="Mage">Mage</option>
                    <option value="Warlock">Warlock</option>
                    <option value="Monk">Monk</option>
                    <option value="Druid">Druid</option>
                </select>
            </div>

            <div class="row">
                <span class="label">Role: </span>
                <div class="radio-wrap">
                    <input type="radio" name="role" value="DPS">
                    <span>DPS</span>
                </div>
                <div class="radio-wrap">
                    <input type="radio" name="role" value="Healer">
                    <span>Healer</span>
                </div>
                <div class="radio-wrap">
                    <input type="radio" name="role" value="Tank">
                    <span>Tank</span>
                </div>
            </div>

            <input class="button" type="submit" value="Apply"/>

        </form>
    </div>
</div>
'''
        review_page.body = '''
<div class="wrapper">
    <h1>{self.title}</h1>

    <div class="inner-wrap">
        <div class="row">
            <span class="label">Name: </span>
            <span class="inputbox">{self.name}</span>
        </div>

        <div class="row">
            <span class="label">Server: </span>
            <span class="inputbox">{self.server}</span>
        </div>

        <div class="row">
            <span class="label">Level: </span>
            <span class="inputbox">{self.level}</span>
        </div>

        <div class="row">
            <span class="label">Class: </span>
            <span class="inputbox">{self.char_class}</span>
        </div>

        <div class="row">
            <span class="label">Role: </span>
            <span class="inputbox">{self.role}</span>
        </div>
    </div>
</div>
'''

        if self.request.GET:
            review_page.name = self.request.GET['name']
            review_page.level = self.request.GET['level']
            review_page.server = self.request.GET['server']
            review_page.char_class = self.request.GET['class']
            review_page.role = self.request.GET['role']
            self.response.write(review_page.print_out())
        else:
            self.response.write(home_page.print_out())



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)