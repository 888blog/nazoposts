from django import forms
from .models import Post
 
 
class PostForm(forms.ModelForm):
    question = forms.CharField(
        required=True,
        widget=forms.Textarea(),
        label='問題文',
    )
    explanation = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 20}),
        label='解説',
    )

    class Meta:
        model = Post
        fields = ('title','question', 'q_img1', 'q_img2', 'q_img3', 'q_img4', 'answer', 'explanation', 'e_img1', 'e_img2', 'e_img3', 'e_img4')
        widgets = {
            'description': forms.Textarea(attrs={'rows':80, 'cols':80}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            # htmlの表示を変更可能にする
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label