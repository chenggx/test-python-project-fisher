from wtforms.fields.simple import StringField, PasswordField
from wtforms.form import Form
from wtforms.validators import DataRequired, Length, Email, ValidationError

from app.models.user import User


class AuthForm(Form):
    email = StringField(
        validators=[DataRequired(message='邮箱不能为空'), Length(8, 64), Email(message='电子邮箱不符合规则')])
    password = PasswordField(validators=[DataRequired('密码不能为空，请输入密码'), Length(6, 32)])


class LoginForm(AuthForm):
    pass


class RegisterForm(AuthForm):
    nickname = StringField(
        validators=[DataRequired(message='昵称不能为空'), Length(2, 10, message='昵称最少需要两个字符，最多10个字符')])

    @staticmethod
    def validate_email(field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经能被注册')
