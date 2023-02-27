from django import forms
from . models import MyBlog
class OwnBlog(forms.ModelForm):
    class Meta:
        model=MyBlog
        fields=['title','category', 
        'body','slug','image']