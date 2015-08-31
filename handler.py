from tornado.web import RequestHandler

from database import uuid, init_database,Applicant
import forms

USERNAME = 'root'
PASSWD = ''

class MainHandler(RequestHandler):
    # for test
    def get(self):
        print(self.request.arguments)
        # self.write(self.get_argument("name"))
        # self.write(self.request.arguments)

    def post(self):
        print(self.request.arguments)
        form = forms.ApplicantForm(self.request.arguments,
                                   locale_code=self.locale.code)
        print(form.name.data)
        print(form.validate())
        print(form.errors)
        if form.validate():
            self.insert_applicant(USERNAME, PASSWD,form)

    def insert_applicant(self, username, passwd, form):
        session = init_database(username, passwd)
        new_applicant = Applicant(id=uuid.uuid4(),
                                  name=form.name.data,
                                  gender=form.gender.data,
                                  campus=form.campus.data,
                                  major=form.major.data,
                                  contact=form.contact.data,
                                  backup_contact=form.backup_contact.data,
                                  group=form.group.data,
                                  intro=form.intro.data)
        session.add(new_applicant)
        session.commit()
        session.close()

    # def search(self):


    # def update(self)
