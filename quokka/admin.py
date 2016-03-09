from django.contrib import admin
from quokka.models import Question, Set, Answer, Votes, UserProfile

admin.site.register(Question)
admin.site.register(Set)
admin.site.register(Answer)
admin.site.register(Votes)
admin.site.register(UserProfile)
