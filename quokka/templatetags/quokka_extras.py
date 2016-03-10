from django import template
from quokka.models import Question, Answer, Vote
import django.template.defaultfilters

register = template.Library()

@register.simple_tag
def get_vote_count(answer_id, votes):
	count = 0
	for vote in votes:
		if vote.answer.id == answer_id:
			if vote.score == 1:
				count += 1
			elif vote.score == -1:
				count -= 1
	return count