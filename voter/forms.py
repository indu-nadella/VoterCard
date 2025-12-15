from django import forms
from voter.models import Voter
from datetime import date

class voter_form(forms.ModelForm):
    class Meta:
        model=Voter
        fields=['name','father_name','dob','gender','address','photo']

    def clean_dob(self):
        dob = self.cleaned_data.get("dob")
        today = date.today()

        age = today.year - dob.year - (
            (today.month, today.day) < (dob.month, dob.day)
        )

        if age < 18:
            raise forms.ValidationError("Age must be 18 or above")
        return dob
