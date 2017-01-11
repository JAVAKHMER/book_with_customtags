from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from book_with_customtags.models import Books, Students
from book_with_customtags.forms import BookForm, StudentForm
class DisplayBookView(View):
    def get(self,request):
        books = Books.objects.all()
        form = BookForm()
        return render(request, 'books.html', {'books': books,'form': form})
    def post(self,request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        return render(request, 'books.html', {'form': form})
class updateBookView(View):
    def get(self,request,id_book):
        books = Books.objects.all()
        book = get_object_or_404(Books, id=id_book)
        form = BookForm(request.POST or None, instance=book)
        return render(request, "books.html", {'books': books,'form': form})
                
    def post(self,request,id_book):
        book = get_object_or_404(Books, id=id_book)
        form = BookForm(request.POST or None, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        return render(request, "books.html", {'form': form})
class deleteBookView(View):
    def get(self,request,id_book):
        book = Books.objects.get(id=id_book)
        book.delete()
        return redirect('book_list')


class DisplayStudents(View):
    def get(self,request):
        students = Students.objects.all()
        studentForm = StudentForm()
        lds = {'students':students,'studentForm':studentForm}
        return render(request,"student.html",lds)
    def post(self,request):
        studentForm = StudentForm(request.POST)
        if studentForm.is_valid():
            studentForm.save()
            return redirect('student_list')
        return render(request,"student.html",{'studentForm':studentForm})
            
class updateStudentView(View):
    def get(self,request,id_student):
        students = Students.objects.all()
        student = get_object_or_404(Students, id=id_student)
        studentForm = StudentForm(request.POST or None, instance=student)
        return render(request, "student.html", {'students': students,'studentForm': studentForm})
                
    def post(self,request,id_student):
        student = get_object_or_404(Students, id=id_student)
        studentForm = StudentForm(request.POST or None, instance=student)
        if studentForm.is_valid():
            studentForm.save()
            return redirect('student_list')
        return render(request, "student.html", {'studentForm': studentForm})
class deleteStudentView(View):
    def get(self,request,id_student):
        student = Students.objects.get(id=id_student)
        student.delete()
        return redirect('student_list')