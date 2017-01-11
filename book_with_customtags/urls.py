
from django.conf.urls import url
from book_with_customtags.views import updateBookView, deleteBookView, DisplayBookView,DisplayStudents,\
    updateStudentView, deleteStudentView

urlpatterns = [
    url(r'^$', DisplayBookView.as_view(),name='book_list'),
    url(r'^updateBook/(\d+)/$', updateBookView.as_view(),name='update_book'),
    url(r'^deleteBook/(\d+)/$', deleteBookView.as_view(),name='delete_book'),
    
#     Display Students
    url(r'^students$', DisplayStudents.as_view(),name='student_list'),
    url(r'^updateStudent/(\d+)/$', updateStudentView.as_view(),name='update_student'),
    url(r'^deleteStudent/(\d+)/$', deleteStudentView.as_view(),name='delete_student'),
]
