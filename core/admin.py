from django.contrib import admin
from .models import Pessoa
from .models import Cliente

# Register your models here.

admin.site.register(Pessoa)
admin.site.register(Cliente)