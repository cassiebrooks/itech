from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import datetime
from quokka.models import Question, Answer, Votes, Set
from quokka.forms import AnswerForm, UserForm, UserProfileForm

def index(request):
    question_list = Question.objects.all()
    answer_list = Answer.objects.all()
    votes_list = Votes.objects.all()
    context_dict = {'questions': question_list, 'answers': answer_list, 'votes': votes_list}
    response = render(request, 'quokka/index.html', context_dict)

    # Cookies
    visits = int(request.COOKIES.get('visits', '1'))
    reset_last_visit_time = False

    if 'last_visit' in request.COOKIES:
        last_visit = request.COOKIES['last_visit']
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
        if (datetime.now() - last_visit_time).days > 0:
            visits = visits + 1
            reset_last_visit_time = True
    else:
        reset_last_visit_time = True
        context_dict['visits'] = visits
        response = render(request, 'quokka/index.html', context_dict)

    if reset_last_visit_time:
        response.set_cookie('last_visit', datetime.now())
        response.set_cookie('visits', visits)

    return response


def about(request):
	if request.session.get('visits'):
	    count = request.session.get('visits')
	else:
	    count = 0
	return render(request, 'quokka/about.html', {'visits': count})

@login_required
def add_answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
        	form.save(commit=True)
        	return index(request)
        else:
            print form.errors
    else:
        form = AnswerForm()
    return render(request, 'quokka/add_answer.html', {'form': form})

# def register(request):
#     registered = False
#     if request.method == 'POST':
#         user_form = UserForm(data=request.POST)
#         profile_form = UserProfileForm(data=request.POST)

#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save()
#             user.set_password(user.password)
#             user.save()

#             profile = profile_form.save(commit=False)
#             profile.user = user

#             if 'picture' in request.FILES:
#                 profile.picture = request.FILES['picture']
#             profile.save()

#             registered = True

#         else:
#             print user_form.errors, profile_form.errors

#     else:
#         user_form = UserForm()
#         profile_form = UserProfileForm()

#     # Render the template depending on the context.
#     return render(request,
#             'quokka/register.html',
#             {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )



# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(username=username, password=password)
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect('/quokka/')
#             else:
#                 # An inactive account was used - no logging in!
#                 return HttpResponse("Your Quokka account is disabled.")
#         else:
#             # Bad login details were provided. So we can't log the user in.
#             print "Invalid login details: {0}, {1}".format(username, password)
#             return HttpResponse("Invalid login details supplied.")
#     else:
#         return render(request, 'quokka/login.html', {})

# @login_required
# def restricted(request):
# 	return HttpResponse("Since you're logged in, you can see this text")

# @login_required
# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect('/quokka/')