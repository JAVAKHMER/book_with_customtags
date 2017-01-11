from django.db import models
class Books(models.Model):
    KHMER = 'kh'
    LANGUAGE = (('kh', 'Khmer'), ('en', 'English'))
    
    title = models.CharField(max_length=50)
    isbn = models.CharField(max_length=20)
    language = models.CharField(max_length=2, choices=LANGUAGE, default=KHMER)
    def __unicode__(self):
        return self.title
    class Meta:
            ordering = ('title',)
            
class Students(models.Model):
    GENDER= (('M','Male'),('F','Female'))
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1,choices=GENDER,default='M')
    age = models.IntegerField()
    books = models.ForeignKey(Books , on_delete=models.CASCADE)
    class Meta:
        ordering = ['first_name']
    