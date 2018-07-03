from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import PlanoDeEstudo, Atividade, Disciplina, Assunto, Anotacao, User


admin.site.register(User, UserAdmin)
admin.site.register(PlanoDeEstudo)
admin.site.register(Atividade)
admin.site.register(Disciplina)
admin.site.register(Assunto)
admin.site.register(Anotacao)
