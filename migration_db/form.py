from django import forms


class CustomSearchForm(forms.Form):
	from_date =forms.DateField(label = 'From',required=False,widget=forms.SelectDateWidget(years = YEAR_CHOICES,
		months=MONTH_CHOICES))
	to_date = forms.DateField(label = 'To',required=False,widget=forms.SelectDateWidget(years = YEAR_CHOICES,
		months=MONTH_CHOICES))
	choices = forms.MultipleChoiceField(choices = SEARCH_CHOICES,widget=forms.CheckboxSelectMultiple)