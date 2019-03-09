from flipboard import ma
from flipboard.models import News, User


class UserSchema(ma.ModelSchema):

    class Meta:
        model = User


class NewsSchema(ma.ModelSchema):
    class Meta:
        model = News
