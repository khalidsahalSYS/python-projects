from django import forms


class PageCheckForm(forms.Form):
    url = forms.URLField(
        label="Website URL",
        widget=forms.URLInput(
            attrs={
                "placeholder": "https://example.com",
                "class": "form-control",
            }
        ),
        required=True,
    )
