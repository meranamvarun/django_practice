from django import forms
from models import Article, comment


class ArticleForm(forms.ModelForm):
   
    class Meta:
        model = Article
        fields = ('title','body','pub_date','thumbnail')



class commentForm(forms.ModelForm):


    class Meta:
        model = comment
        fields = ('name','body')
