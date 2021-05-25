from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

# envio de emails
from django.core.mail import send_mail, mail_admins, send_mass_mail
from django.template.loader import render_to_string

# Create your models here.
# one to one impede que outro cadastro use o mesmo previamente cadastrado
# one to many (foreignkey) permite que uma tabela seja instanciada em varias outras
# many to many permite varias instancias de um elemento para varios elementos


class Documento(models.Model):
    num_doc = models.CharField(max_length=30)

    def __str__(self):
        return self.num_doc


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)  # campo opcional
    doc = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        permissions = (
            ('deletar_clientes', 'Deletar clientes'),
        )

    @property
    def nome_completo(self):
        return self.first_name+' '+self.last_name

    # def save(self, *args, **kwargs):  # envia email apos novo cliente cadastrado (necessario server SMTP para usar)
    #     super(Person, self).save(*args, **kwargs)
    #     data = {'cliente': self.first_name}
    #     plain_text = render_to_string('clientes/emails/novo_cliente.txt', data)
    #     html_email = render_to_string('clientes/emails/novo_cliente.html', data)
    #     send_mail(
    #         'Novo cliente cadastrado',
    #         # 'O cliente %s foi cadastrado' % self.first_name,
    #         plain_text,
    #         'from@example.com',
    #         ['to@example.com'],
    #         fail_silently=False,
    #         html_message=html_email,
    #     )
    #     mail_admins(  #envia email para os admins
    #         # 'O cliente %s foi cadastrado' % self.first_name,
    #         'Novo cliente cadastrado',
    #         plain_text,
    #         fail_silently=False,
    #         html_message=html_email,)
    #     message1 = (
    #     'Subject here', 'Here is the message', 'from@example.com', ['first@example.com', 'other@example.com'])
    #     message2 = ('Another Subject', 'Here is another message', 'from@example.com', ['second@test.com'])
    #     send_mass_mail((message1, message2), fail_silently=False)  # envia emails em massa

    def __str__(self):
        return self.first_name+' '+self.last_name

