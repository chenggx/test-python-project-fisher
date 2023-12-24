from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import StringField
from wtforms.form import Form
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    q = StringField(validators=[DataRequired(message='查询关键词不能为空'), Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=1000)], default=1)
