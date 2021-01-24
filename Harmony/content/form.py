from django.forms import ModelForm
from .models import Image,Tip
from django.utils.translation import gettext_lazy as _

# Create the form class.
class ImageForm(ModelForm):
        class Meta:
            model = Image
            fields = ['owner','title',
                      'description','url',
                      'department','category']
            help_texts = {
            'owner' : _(""),
            "title" : _(""),
            "department" : _(""),
            'description': _('Une courte description'),
            'url': _('Vous pouvez utiliser zupimages.net pour héberger vos images'),
            'category': _('Ctrl+Clic pour séléctionner plusieurs catégories'),
            }

class TipForm(ModelForm):
        class Meta:
            model = Tip
            fields = ['owner','title',
                      'description','content',
                      'category']
            help_texts = {
            'owner' : _(""),
            "title" : _(""),
            'content' : _(""),
            'description': _('Une courte description'),
            'category': _('Ctrl+Clic pour séléctionner plusieurs catégories'),
            }