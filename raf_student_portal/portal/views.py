from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from .models import Subject, News
from django.contrib.auth.models import User
from .forms import SubjectForm, NewsForm, RegisterForm


def index(req):
    if not req.user.is_authenticated:
        return render(req, 'index.html', {'page_title': 'RAF Student Portal'})
    else:
        return redirect('portal:subjects')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, 'register.html', {
                    'form': form,
                    'error_message': 'Username already exists'
                })
            else:
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('portal:subjects')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def subjects(req):
    tmp = Subject.objects.all()
    return render(req, 'subjects.html', {'subjects': tmp})


@login_required
def subject(req, id):
    tmp = get_object_or_404(Subject, id=id)
    return render(req, 'subject.html', {'subject': tmp, 'page_title': tmp.name})


@permission_required('portal.change_subject')
def edit_subject(req, id):
    if req.method == 'POST':
        form = SubjectForm(req.POST)

        if form.is_valid():
            a = Subject.objects.get(id=id)
            a.name = form.cleaned_data['name']
            a.description = form.cleaned_data['description']
            a.save()
            return redirect('portal:subjects')
        else:
            return render(req, 'edit_subject.html', {'form': form, 'id': id})
    else:
        a = Subject.objects.get(id=id)
        form = SubjectForm(instance=a)
        return render(req, 'edit_subject.html', {'form': form, 'id': id})


@permission_required('portal.add_subject')
def new_subject(req):
    if req.method == 'POST':
        form = SubjectForm(req.POST)

        if form.is_valid():
            a = Subject(name=form.cleaned_data['name'], description=form.cleaned_data['description'], owner=req.user)
            a.save()
            return redirect('portal:subjects')
        else:
            return render(req, 'new_subject.html', {'form': form})
    else:
        form = SubjectForm()
        return render(req, 'new_subject.html', {'form': form})
