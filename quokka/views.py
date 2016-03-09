from django.http import HttpResponse
from django.shortcuts import render
from quokka.models import Question, Answer, Votes, Set
from quokka.forms import AnswerForm

def index(request):
    question_list = Question.objects.all()
    answer_list = Answer.objects.all()
    votes_list = Votes.objects.all()
    context_dict = {'questions': question_list, 'answers': answer_list, 'votes': votes_list}
    return render(request, 'quokka/index.html', context_dict)

def about(request):
    context_dict = {'boldmessage': "YAY QUOKKA"}
    return render(request, 'quokka/about.html', context_dict)

def add_answer(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = AnswerForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = AnswerForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'quokka/add_answer.html', {'form': form})