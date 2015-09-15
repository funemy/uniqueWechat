from tornado.web import RequestHandler
from database import uuid, Applicant, Advice, db_session
import forms


class MainHandler(RequestHandler):
    def get(self, ph):
        self.write("hello world")

    def post(self):
        self.write('hello world')

    def check_status(self,
               contact=None):
        session = db_session()
        if contact:
            return session.query(Applicant).filter(Applicant.contact==contact).all()
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

    def search(self, ):
        pass

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


class QueryHandler(RequestHandler):
    def get(self, phone_number=None):
        session = db_session()
        rows = session.query(Applicant).filter(Applicant.contact == phone_number).all()
        if not phone_number:
            self.render("query.html", result={})
        if rows:
            rows = rows[0]
            result = {
                "name": rows.name,
                "contact": rows.contact,
                "group": rows.group,
                "inter_place": rows.inter_place,
                "inter_round": rows.inter_round,
                "inter_time": rows.inter_time,
                "status": rows.status
            }
            self.render("query.html", result=result)
        else:
            self.render("query.html", result=False)


class InviteHandler(RequestHandler):
    def put(self, tid, status):
        session = db_session()
        row = session.query(Applicant).filter(Applicant.id == tid).first()
        status = int(status)
        if status:
            row.status = "进行中"
            row.inter_round += 1
        else:
            row.status = "未通过"
        session.commit()
        self.write("success")

    def get(self, group=None):
        session = db_session()
        counts = {
            'all': 0,
            'refuse': 0,
            'pass': 0
        }
        if group:
            rows = session.query(Applicant).filter(Applicant.group == group).all()
            counts['all'] = len(rows)
            counts['refuse'] = len(session.query(Applicant).filter(Applicant.status == '未通过')
                                   .filter(Applicant.group == group).all())
            counts['pass'] = counts['all'] - counts['refuse']
        else:
            rows = session.query(Applicant).all()
            counts['all'] = len(rows)
            counts['refuse'] = len(session.query(Applicant).filter(Applicant.status == '未通过').all())
            counts['pass'] = counts['all'] - counts['refuse']
        self.render("invite.html", data=rows, counts=counts)


class InfoHandler(RequestHandler):
    def put(self):
        tid = self.get_argument('id')
        inter_time = self.get_argument('inter_time')
        inter_place = self.get_argument('inter_place')
        session = db_session()
        row = session.query(Applicant).filter(Applicant.id == tid).first()
        row.inter_time = inter_time
        row.inter_place = inter_place
        session.commit()
        self.write("success")


if __name__ == "__main__":
    pass
    # session = db_session()
    # rows = session.query(Applicant).filter(Applicant.group=="web").first()
    # #rows.group = "PM"
    # rows = session.query(Applicant).filter(Applicant.group=="web").first()
    # #rows.group = 'web'
    # session.commit()
    # print(rows)

