import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from quokka.models import Set, Question, Answer, Vote
from django.contrib.auth.models import User
# import django.registration.redux


def populate():

    # Print out what we have added to the user.
    # for c in Category.objects.all():
    #     for p in Page.objects.filter(category=c):
    #         print "- {0} - {1}".format(str(c), str(p))

    my_set = add_set("My Set")
    set_1 = add_set("Set I")
    set_2 = add_set("Set II")
    set_3= add_set("Set III")
    add_question("Given the choice of anyone in the world, whom would you want as a dinner guest?", set=set_1)
    add_question("Would you like to be famous? In what way?", set=set_1)
    add_question("Before making a telephone call, do you ever rehearse what you are going to say? Why?", set=set_1)
    add_question("What would constitute a 'perfect' day for you?", set=set_1)
    add_question("What did you last sing to yourself? To someone else?", set=set_1)
    add_question("If you were able to live to the age of 90 and retain either the mind or body of a 30-year-old for"+
                 "the last 60 years of your life, which would you want?",set=set_1)
    add_question("Do you have a secret hunch about how you will die?",set=set_1)
    add_question("Name three things you and your partner appear to have in common.",set=set_1)
    add_question("For what in your life do you feel most grateful?",set=set_1)
    add_question("If you could change anything about the way you were raised, what would it be?",set=set_1)
    add_question("Take four minutes and tell your life story in as much detail as possible.",set=set_1)
    add_question("If you could wake up tomorrow having gained any one quality or ability, what would it be?", set=set_1)
    add_question("If a crystal ball could tell you the truth about yourself, your life, "+
                 "the future or anything else, what would you want to know?",set=set_2 )
    add_question("Is there something that you’ve dreamed of doing for a long time? Why haven’t you done it?", set=set_2)
    add_question("What is the greatest accomplishment of your life?",set=set_2)
    add_question("What do you value most in a friendship?",set=set_2)
    add_question("What is your most treasured memory?",set=set_2)
    add_question("What is your most terrible memory?",set=set_2)
    add_question("If you knew that in one year you would die suddenly, would you change anything about the way"+
                 " you are now living? Why?",set=set_2)
    add_question("What does friendship mean to you?",set=set_2)
    add_question("What roles do love and affection play in your life?",set=set_2)
    add_question("How close and warm is your family? Do you feel your childhood was happier than most other people's?",set=set_2)
    add_question("How do you feel about your relationship with your mother?",set=set_2)
    add_question("Share an embarrassing moment of your life",set=set_3)
    add_question("When did you last cry in front of another person?",set=set_3)
    add_question("What, if anything, is too serious to be joked about?",set=set_3)
    add_question("If you were to die this evening with no opportunity to communicate with anyone, "+
                 "what would you most regret not having told someone? Why haven’t you told them yet?",set=set_3)
    add_question("Your house, containing everything you own, catches fire. After saving your loved ones and pets, you"+
                 " have time to safely make a final dash to save any one item. What would it be? Why?",set=set_3)
    add_question("Of all the people in your family,w hose death would you find most disturbing? Why?",set=set_3)

    add_user("leifos", "leifos")
    add_user("laura", "laura")
    add_user("david", "david")

def add_user(name, pw):
    u = User.objects.create_user(name, email=None, password=pw)
    u.save()
    return u


def add_question(text, qset=None):
    q, created = Question.objects.get_or_create(text=text, set=qset)
    q.save()
    return q


def add_set(name):
    s = Set.objects.get_or_create(name=name)[0]
    s.save()
    return s


def add_answer(text):  # NOTE: assigns the answer to a random question
    a = Answer.objects.get_or_create(text=text, question=Question.objects.order_by('?').first())[0]
    return a

# Start execution here!
if __name__ == '__main__':
    print "Starting Quokka population script..."
    populate()
    print "Populated, no errors!\n"
