from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.http import HttpResponse
from . models import Major, Student, StudentModelForm, MajorModelForm
from . forms import MajorForm, StudentForm

# student_list = ListView.as_view(model=Student)
# major_list = ListView.as_view(model=Major)

class StudentListView(ListView):
    model = Student
    paginate_by = 6
    template_name = 'stdmj/student_list.html'

    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5  # Display only 5 page numbers
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        return context

class MajorListView(ListView):
    model = Major
    paginate_by = 6
    template_name = 'stdmj/major_list.html'

    def get_context_data(self, **kwargs):
        context = super(MajorListView, self).get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5  # Display only 5 page numbers
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        return context

student_list = StudentListView.as_view()
major_list = MajorListView.as_view()

student_detail = DetailView.as_view(model=Student)
major_detail = DetailView.as_view(model=Major)

student_delete = DeleteView.as_view(model=Student, success_url='/stdmj/')
major_delete = DeleteView.as_view(model=Major, success_url='/stdmj/mj')


def student_new(request):
    if request.method=='GET':
        form = StudentForm()
    else:
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            Student.objects.create(**form.cleaned_data)
            return redirect(reverse("stdmj:student_list"))
    return render(request, 'stdmj/student_form.html', {'form':form})

def major_new(request):
    if request.method=='GET':
        form = MajorForm()
    else:
        form = MajorForm(request.POST, request.FILES)
        if form.is_valid():
            Major.objects.create(**form.cleaned_data)
            return redirect(reverse("stdmj:major_list"))
    return render(request, 'stdmj/major_form.html', {'form':form})

def student_edit(request, pk):
    student = get_object_or_404(Student, studentID=pk)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            student.save()
            return redirect('/stdmj/')
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'stdmj/student_form.html', {'form':form}) 

def major_edit(request, pk):
    major = get_object_or_404(Major, major_id=pk)
    if request.method == 'POST':
        form = MajorModelForm(request.POST, request.FILES, instance=major)
        if form.is_valid():
            major.save()
            return redirect('/stdmj/mj')
    else:
        form = MajorModelForm(instance=major)
    return render(request, 'stdmj/major_form.html', {'form':form})