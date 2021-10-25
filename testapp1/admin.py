from django.contrib import admin

from testapp1.models import Question, Choice
admin.site.register(Question)
admin.site.register(Choice)