from django.contrib import admin
from .models import Person
from.models import Documento


# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados_pessoais', {'fields': ('first_name', 'last_name', 'doc')}),
        ('Dados_complementares', {
            'classes': ('collapse',),
            'fields': ('age', 'salary', 'photo')}),
        ('Biografia', {
            'classes': ('collapse',),
            'fields': ['bio']})
    )
    # fields = ['first_name', 'last_name', 'doc', ('salary', 'age'),
    #           'photo', 'bio']
    # exclude = ['bio']
    list_display = ('first_name', 'last_name', 'age', 'salary', 'bio',
              'tem_foto', 'doc')
    list_filter = ('age', 'salary')
    autocomplete_fields = ('doc', )
    search_fields = ('id', 'first_name')

    def tem_foto(self, obj):
        if obj.photo:
            return 'Sim'
        else:
            return 'Nao'

    tem_foto.short_description = 'Possui foto'


# class ProdutoAdmin(admin.ModelAdmin):
#     list_display = ('id', 'descricao', 'preco')
#     search_fields = ('id', 'descricao')


class DocumentoAdmin(admin.ModelAdmin):
    search_fields = ['num_doc']


admin.site.register(Person, PersonAdmin)
admin.site.register(Documento, DocumentoAdmin)
# admin.site.register(Produto, ProdutoAdmin)
