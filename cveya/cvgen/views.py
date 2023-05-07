from django.shortcuts import render, get_object_or_404, redirect
from .models import Skill, Profile
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm

# Create your views here.
def index(request):
    skills_list = Skill.objects.order_by("id")[:5]

    if request.user.is_authenticated:
        resume_cta = "Create your CV, " + request.user.username
    else:
        resume_cta = None

    context = {
        "skills_list": skills_list,
        "resume_cta": resume_cta
    }

    return render(request, "cvgen/index.html", context)

def details(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)
    return render(request, "cvgen/detail.html", {"skill": skill})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            profile = Profile.objects.create(user=user,
                                             address=request.POST.get('address'),
                                             email=request.POST.get('email'),
                                                                    phoneNumber=request.POST.get('phoneNumber'))
            return redirect("cvgen:index")
    else:
        form = RegistrationForm()
    return render(request, 'cvgen/register.html', {'form': form})

def createResume(request):
    return render(request, 'cvgen:index')
