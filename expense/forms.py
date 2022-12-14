from django.forms import ModelForm
from .models import *


class CollectionForm(ModelForm):

    def clean(self):
        cleaned_data = super(CollectionForm, self).clean()
        if cleaned_data['building'] != 'OTHERS' and self.instance.id is None:
            already_paid = MoneyCollection.objects.filter(building=cleaned_data['building'],
                                                          flat_no=cleaned_data['flat_no']).count()
            if already_paid:
                self.add_error('building', 'Money is already collected for this flat!')

    class Meta:
        model = MoneyCollection
        fields = ('id', 'building', 'flat_no', 'name', 'amount', 'note', 'attachment', 'status')

