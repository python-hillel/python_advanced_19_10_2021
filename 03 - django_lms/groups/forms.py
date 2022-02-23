from django.forms import ChoiceField
from django.forms import ModelForm

from .models import Group


class GroupBaseForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'


class GroupCreateForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        exclude = ['end_date', 'headman']


class GroupUpdateForm(GroupBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['headman_field'] = ChoiceField(
            choices=[(st.id, str(st)) for st in self.instance.students.all()],
            label='Headman',
            required=False
        )

    class Meta(GroupBaseForm.Meta):
        exclude = ['start_date', 'headman']
