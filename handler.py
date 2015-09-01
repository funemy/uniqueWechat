from tornado.web import RequestHandler

from database import uuid, init_database,Applicant,Advice
import forms

USERNAME = 'root'
PASSWD = ''
URL = 'localhost:3307/uniqueWechat'

class MainHandler(RequestHandler):
    def post(self):
        self.write('hello world')

    # def search(self):

    # def update(self)


class ApplyHandler(RequestHandler):
    def post(self):
        form = forms.ApplicantForm(self.request.arguments,
                                   locale_code=self.locale.code)
        if form.validate():
            self.insert_applicant(form)
        else:
            self.set_status(400)
            self.write(form.errors)

    def insert_applicant(self, form):
        session = init_database(USERNAME, PASSWD, URL)
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

class AdviceHandler(RequestHandler):
    def post(self):
        form = forms.ApplicantForm(self.request.arguments,
                                   locale_code=self.locale.code)
        if form.validate():
            self.insert_advice(form)
        else:
            self.write(form.errors)

    def insert_advice(self, form):
        session = init_database(USERNAME, PASSWD, URL)
        new_advice = Advice(id=uuid.uuid4(),
                            name=form.name.data,
                            major=form.major.data,
                            email=form.email.data,
                            advice=form.advice.data)
        session.add(new_advice)
        session.commit()
        session.close()
