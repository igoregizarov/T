from django import forms

from authapp.models import PollingUser
from pollapp.models import QuestionsCategory, Questions, Answer, ChoiseVoit, ChoisePoll


class QuestionsCreateForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ('name',)


class ChoisePollCreateForm(forms.ModelForm):
    class Meta:
        model = ChoisePoll
        fields = ('name',)
        # fields = '__all__'