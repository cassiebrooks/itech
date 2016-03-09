from django.contrib import admin
from quokka.models import Question, Set, Answer, Vote

admin.site.register(Question)
admin.site.register(Set)
admin.site.register(Answer)
admin.site.register(Vote)