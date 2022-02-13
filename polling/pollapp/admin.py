from django.contrib import admin
# Register your models here.
from pollapp.models import QuestionsCategory, Questions, Answer, ChoiseVoit, ChoisePoll

admin.site.register(QuestionsCategory)
admin.site.register(Questions)
admin.site.register(Answer)
admin.site.register(ChoiseVoit)
admin.site.register(ChoisePoll)