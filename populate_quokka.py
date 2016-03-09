import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from quokka.models import Set, Question, Answer, Vote


def populate():

    # Print out what we have added to the user.
    # for c in Category.objects.all():
    #     for p in Page.objects.filter(category=c):
    #         print "- {0} - {1}".format(str(c), str(p))

    my_set = add_set("My Set")

    add_question("What is your name?")
    add_question("What is your favourite colour?")
    add_question("What is the average airspeed velocity of an unladen swallow?")

    add_answer("My name is Quokka")
    add_answer("My name is Azzopardi")

def add_question(text):
    q, created = Question.objects.get_or_create(text=text)
    q.save()
    return q

def add_set(name):
    s = Set.objects.get_or_create(name=name)[0]
    s.save()
    return s

def add_answer(text): # NOTE: assigns the answer to a random question
    a = Answer.objects.get_or_create(text=text, question=Question.objects.order_by('?').first())[0]
    return a

# Start execution here!
if __name__ == '__main__':
    print "Starting Quokka population script..."
    populate()
    print "Populated, no errors!\n"