from django.forms import ModelForm
from book_with_customtags.models import Books, Students
class BookForm(ModelForm):
    class Meta:
        model = Books
        fields = '__all__'

class StudentForm(ModelForm):
    class Meta:
        model = Students
        fields = '__all__'