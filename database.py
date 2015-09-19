from sqlalchemy import create_engine
from sqlalchemy import Column, Unicode, BigInteger, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import TypeDecorator, CHAR
from sqlalchemy.dialects.postgresql import UUID

import uuid

USERNAME = 'root'
PASSWD = 'aliyunmysqlP@ssw0rd'
URL = 'localhost:3306/uniqueWechat'

Base = declarative_base()
engine = create_engine(
    'mysql+mysqlconnector://%(username)s:%(passwd)s@%(url)s' % {'username': USERNAME,
                                                                'passwd': PASSWD,
                                                                'url': URL}, pool_recycle=3600)
db_session = sessionmaker(bind=engine)


class GUID(TypeDecorator):
    """Platform-independent GUID type.
    Uses Postgresql's UUID type, otherwise uses
    CHAR(32), storing as stringified hex values.
    """
    impl = CHAR

    def load_dialect_impl(self, dialect):
        if dialect.name == 'postgresql':
            return dialect.type_descriptor(UUID())
        else:
            return dialect.type_descriptor(CHAR(32))

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        elif dialect.name == 'postgresql':
            return str(value)
        else:
            if not isinstance(value, uuid.UUID):
                return "%.32x" % uuid.UUID(value)
            else:
                # hexstring
                return "%.32x" % value

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        else:
            return uuid.UUID(value)


class Applicant(Base):
    __tablename__ = 'applicant'

    # unique ID
    id = Column(GUID(),
                default=uuid.uuid4,
                primary_key=True)

    # name of the applicant
    name = Column(Unicode(8),
                  nullable=False)

    # gender
    gender = Column(Unicode(8),
                    nullable=False)

    # the campus the applicant lives in
    # zs/yy/qy
    campus = Column(Unicode(2),
                    nullable=False)

    major = Column(Unicode(32),
                   nullable=False)

    # phone number
    contact = Column(BigInteger,
                     nullable=False)

    # phone number of the applicant‘s roommate
    backup_contact = Column(BigInteger,
                            nullable=True)

    # the group applicant apply for
    group = Column(Unicode(16),
                   nullable=False)

    # self introduction
    intro = Column(Unicode(2000),
                   nullable=True)

    inter_time = Column(Unicode(32),
                        nullable=False)

    inter_place = Column(Unicode(128),
                         nullable=False)

    inter_round = Column(BigInteger,
                         nullable=False)

    sms_status = Column(Unicode(32),
                        nullable=False)
    # 通过/拒绝/进行中
    status = Column(Unicode(8),
                    nullable=False)

    def __init__(self, id,
                 name,
                 gender,
                 campus,
                 major,
                 contact,
                 group,
                 intro,
                 inter_round=0,
                 backup_contact=None,
                 inter_time='待定',
                 inter_place='待定',
                 sms_status='未发送',
                 status='未通过'):
        self.id = id
        self.name = name
        self.gender = gender
        self.campus = campus
        self.major = major
        self.contact = contact
        self.group = group
        self.intro = intro
        self.backup_contact = backup_contact
        self.inter_time = inter_time
        self.inter_place = inter_place
        self.status = status
        self.inter_round = inter_round
        self.sms_status = sms_status


class Advice(Base):
    __tablename__ = 'advice'

    id = Column(GUID(),
                default=uuid.uuid4,
                primary_key=True)

    name = Column(Unicode(8),
                  nullable=False)

    major = Column(Unicode(32),
                   nullable=False)

    email = Column(Unicode(64),
                   nullable=False)

    advice = Column(Unicode(2000),
                    nullable=False)

    def __init__(self, id,
                 name,
                 major,
                 email,
                 advice):
        self.id = id
        self.name = name
        self.major = major
        self.email = email
        self.advice = advice

def init_database():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    # test case
    session = db_session()
    new_applicant = Applicant(id=uuid.uuid4(),
                              name="简小奇",
                              gender="男",
                              campus="yy",
                              major="软件工程",
                              contact=13685795128,
                              backup_contact=13685795128,
                              group="web",
                              intro="我的梦想是当校长",
                              inter_round=0)
    session.add(new_applicant)
    session.commit()
    session.close()
