from django import forms

class RobotFilterForm(forms.Form):
    min_price = forms.IntegerField(label="от", required=False)
    max_price = forms.IntegerField(label="до", required=False)
    ordering = forms.ChoiceField(label="сортировка", required=False, choices=[
        ["name", "по алфавиту"],
        ["price", "по возрастанию цены"],
        ["-price", "по уменьшению цены"]
    ])