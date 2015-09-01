from form import Form
from wtforms.fields import (Field,
                            IntegerField,
                            StringField,
                            SelectField)
from wtforms.validators import (ValidationError,
                                StopValidation,
                                InputRequired,
                                NumberRange,
                                Email,
                                Length)


class ApplicantForm(Form):
    name = StringField('name', [
        InputRequired(),
        Length(max=8)
    ])

    gender = SelectField('gemder',
                         default='male',
                         choices=[('male', 'male'),
                                 ('female', 'female')]
                         )

    campus = SelectField('campus',
                         default='yy',
                         choices=[('yy', 'yy'),
                                  ('zs', 'zs'),
                                  ('qy', 'qy')]
                         )

    major = StringField('major', [
        InputRequired(),
        Length(max=32)
    ])

    contact = IntegerField('contact', [
        InputRequired(),
        NumberRange(min=10000000000,
                    max=19999999999)
    ])

    backup_contact = IntegerField('backup contact', [
    ])

    group = SelectField('group',
                        default='Android',
                        choices=[('Android', 'Android'),
                                 ('Web', 'Web'),
                                 ('iOS', 'iOS'),
                                 ('Design', 'Design'),
                                 ('lab', 'lab'),
                                 ('PM', 'PM')]
                        )

    intro = StringField('introduction', [
        Length(max=2000)
    ])

    def validate_backup_contact(form, field):
        if field.data is None:
            return
        else:
            if field.data < 10000000000 or field.data > 19999999999:
                raise ValidationError('invalid phone number')

class AdviceForm(Form):
    name = name = StringField('name', [
        InputRequired(),
        Length(max=8)
    ])

    major = StringField('major', [
        InputRequired(),
        Length(max=32)
    ])

    email = StringField('email', [
        InputRequired(),
        Email()
    ])

    advice = StringField('advice', [
        InputRequired()
        Length(max=2000)
    ])