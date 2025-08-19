from django.db import models

# Create your models here.

class Report(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pendente"),
        ("in_progress", "Em andamento"),
        ("resolved", "Resolvido"),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    localizacao = models.CharField(max_length=255)  # Ex: "-23.55,-46.63" (lat,lon)
    foto = models.ImageField(upload_to="reports_photos/", null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"{self.titulo} - {self.status}"