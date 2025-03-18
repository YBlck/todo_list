from django import forms

from manager.models import Task


class TaskCreateForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            attrs={
                "type": "datetime-local", "class": "form-control"
            }
        )
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
        widgets = {
            'tags': forms.CheckboxSelectMultiple(
                attrs={'class': 'form-check-inline'}
            ),
        }


class TaskUpdateForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            attrs={
                "type": "datetime-local", "class": "form-control"
            }
        )
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "is_done", "tags"]
        widgets = {
            'tags': forms.CheckboxSelectMultiple(
                attrs={'class': 'form-check-inline'}
            ),
        }
