from django.shortcuts import render, get_object_or_404, redirect
from .models import EmploymentHistory, Skill, Profile,Qualification,EducationHistory
from django.contrib.auth import login, authenticate
from .forms import EducationHistoryForm, RegistrationForm, SkillForm, QualificationForm, EmploymentHistoryForm
from django.http import HttpResponse, FileResponse
from docxtpl import DocxTemplate

# Create your views here.
def index(request):

    if request.user.is_authenticated:
        resume_cta = "Create your CV, " + request.user.username
        details_cta = "View your account details " + request.user.username
    else:
        resume_cta = None
        details_cta = None

    context = {
        "resume_cta": resume_cta,
        "pk": request.user.id,
        "details_cta":details_cta,
    }

    return render(request, "cvgen/index.html", context)


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


def create_skill(request, pk):
    profile = Profile.objects.get(id=pk)
    skills = Skill.objects.filter(profile=profile)
    

    if request.method == "POST":
        qualification_form = QualificationForm(request.POST)
        emp_form = EmploymentHistoryForm(request.POST)
        edu_form = EducationHistoryForm(request.POST)
        skill_form = SkillForm(request.POST)

        if qualification_form.is_valid():
            qualification = qualification_form.save(commit=False)
            qualification.profile = profile
            qualification.save()
            return HttpResponse("qualification successfully added")

        if skill_form.is_valid():
            skill = skill_form.save(commit=False)
            skill.profile = profile
            skill.save()
            return HttpResponse("skill successfully added")

        if edu_form.is_valid():
            education = edu_form.save(commit=False)
            education.profile = profile
            education.save()
            return HttpResponse("education history added with success")

        if emp_form.is_valid():
            employment = emp_form.save(commit=False)
            employment.profile = profile
            employment.save()
            return HttpResponse("employment  history added with success")

        else:
            return HttpResponse(str(emp_form.errors))
    else:
        skill_form = SkillForm()    
        emp_form = EmploymentHistoryForm(request.POST)
        edu_form = EducationHistoryForm(request.POST)
        qualification_form = QualificationForm()
        context = {
            "skill_form":skill_form,
            "qualification_form": qualification_form,
            "edu_form":edu_form,
            "emp_form":emp_form,
            "profile": profile,
            "skills": skills,
            }
    return render(request, "cvgen/resume.html", context)

def create_skill_form(request):

    form = SkillForm()
    context = {
        "form": form,
    }
    return render(request, "cvgen/skill_form.html",context)


def create_qualification_form(request):
    form = QualificationForm()
    context = {
        "form": form,
    }
    return render(request, "cvgen/qualification_form.html",context)

def create_education_history_form(request):
    form = EducationHistoryForm()
    context = {
        "form" : form,
    }
    return render(request, "cvgen/edu_form.html", context)

def create_employment_history_form(request):
    form = EmploymentHistoryForm()
    context = {
        "form":form,
    }
    return render(request, "cvgen/emp_form.html",context)

def user_info(request,pk):
    profile = Profile.objects.get(id=pk)
    skills = Skill.objects.filter(profile=profile)
    emp_history = EmploymentHistory.objects.filter(profile=profile)
    edu_history = EducationHistory.objects.filter(profile=profile)
    qualifications = Qualification.objects.filter(profile=profile)

    context =  {
        "profile":profile,
        "skills":skills,
        "emp_history":emp_history,
        "edu_history":edu_history,
        "qualifications":qualifications,
    }
    return render(request,"cvgen/details.html",context)

def resumedetails(request,pk):
    profile = Profile.objects.get(id=pk)
    skills = Skill.objects.filter(profile=profile)
    emp_history = EmploymentHistory.objects.filter(profile=profile)
    edu_history = EducationHistory.objects.filter(profile=profile)
    qualifications = Qualification.objects.filter(profile=profile)

    
    resume = DocxTemplate('cvgen/templates/cvgen/Resume_Sample_Functional.docx')
    docContext = {
    "name": profile.user,
    "address": profile.address,
    "phoneNumber": profile.phoneNumber,
    "email": profile.email,
    "high_qualifications": qualifications,
    "skills_and_experiences":skills,
    "employments":emp_history,
    "education_history":edu_history,
    }
    file_path = "cvgen/media/files/resume"+ str(request.user.id) +".docx"
    resume.render(docContext)
    resume.save(file_path)
    with open(file_path, 'rb') as f:
        response = FileResponse(f)

        response['Content-Type'] = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        response['Content-Disposition'] = 'attachment; filename="downloaded_file.docx"'

        return response



