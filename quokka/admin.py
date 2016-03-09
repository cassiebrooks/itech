from django.contrib import admin
from quokka.models import Question, Set, Answer, Votes

admin.site.register(Question)
admin.site.register(Set)
admin.site.register(Answer)
admin.site.register(Votes)