from django.forms import ModelForm
from .models import Collection, Item


class NewCollectionForm(ModelForm):
    class Meta:
        model = Collection
        fields = ['name', 'photo', 'category']
        labels = {
            'name': 'Nome',
            'photo': 'Imagem',
            'category': 'Categoria',
        }


class NewItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'photo', 'description', 'quantity', 'collection']
        labels = {
            'name': 'Nome',
            'photo': 'Imagem',
            'description': 'Descrição',
            'quantity': 'Quantidade',
            'collection': 'Coleção'
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(NewItemForm, self).__init__(*args, **kwargs)
        self.fields['collection'].queryset = self.user.collection_set.all()
