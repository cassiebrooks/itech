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


@register.simple_tag
def user_has_answered (question, user, answers):
# if user has already answered the question:
	for answer in answers:
		if answer.question.id == question.id:
			if answer.author.id == user.id:
				return 1
	return 0


# @register.simple_tag
# def display_answer_form(answer_id, votes):
# 	# returns html of answer form ?
# 	return "<div class='card'>[form]</div>"

# @register.simple_tag
# def highlight_answer(answer_id):
# 	# somehow highlights the user's answer within the answer list
# 	return -1




# # within 'for answer in answers'
# if answer.author.id == user.id:
#     user_replied = True
#     highlight_answer(answer.id) # highlight user's own answer

# # after for loop:
# if !user_replied:
#     insert question answer form at top of list