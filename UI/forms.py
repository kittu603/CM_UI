from django.forms import ModelForm
from .models import UserSqlData, UserApiData, UserSshData

class UserSqlDataForm(ModelForm):
    class Meta:
        fields = "__all__"
        model = UserSqlData


class UserApiDataForm(ModelForm):
    class Meta:
        fields = "__all__"
        model = UserApiData


class UserSshDataForm(ModelForm):
    class Meta:
        fields = "__all__"
        model = UserSshData





