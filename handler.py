from tornado.web import RequestHandler
from database import uuid, Applicant, Advice, db_session
import forms


class MainHandler(RequestHandler):
    def post(self):
        self.write('hello world')

    def check_status(self,
               name=None,
               contact=None):
        session = db_session()
        if name and contact:
            return session.query(Applicant).filter(Applicant.name==name, Applicant.contact==contact).all()
        else:
            return None

    def update(self, *uuid, **new_status):
        session = db_session()
        query = session.query(Applicant)
        for id in uuid:
            applicant = query.filter(Applicant.id == id).first()
            for key in new_status:
                applicant.__setattr__(key, new_status[key])
        session.commit()

    # def search(self)

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
        session = db_session()
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
        form = forms.AdviceForm(self.request.arguments,
                                locale_code=self.locale.code)
        if form.validate():
            self.insert_advice(form)
        else:
            self.write(form.errors)

    def insert_advice(self, form):
        session = db_session()
        new_advice = Advice(id=uuid.uuid4(),
                            name=form.name.data,
                            major=form.major.data,
                            email=form.email.data,
                            advice=form.advice.data)
        session.add(new_advice)
        session.commit()
        session.close()

if __name__ == "__main__":
    session = db_session()
    rows = session.query(Applicant).filter(Applicant.group=="ESD").first()
    rows.group = "PM"
    rows = session.query(Applicant).filter(Applicant.group=="Design").first()
    rows.group = 'lab'
    session.commit()
    print(rows)

