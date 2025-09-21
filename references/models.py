from django.db import models
from django.core.validators import FileExtensionValidator

class Category(models.Model):
    """Categories for media files (e.g., court case, payment receipt, site picture)"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Reference(models.Model):
    """Main reference number with basic details"""
    reference_number = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=200)
    tariff = models.CharField(max_length=100, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.reference_number} - {self.title}"

class MediaFile(models.Model):
    """Media files (images and PDFs) associated with references"""
    MEDIA_TYPE_CHOICES = [
        ('image', 'Image'),
        ('pdf', 'PDF'),
    ]
    
    reference = models.ForeignKey(Reference, on_delete=models.CASCADE, related_name='media_files')
    file = models.FileField(
        upload_to='media_files/%Y/%m/%d/',
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'pdf'])
        ]
    )
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)
    categories = models.ManyToManyField(Category, related_name='media_files', blank=True)
    remarks = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return f"{self.reference.reference_number} - {self.get_filename()}"
    
    def get_filename(self):
        return self.file.name.split('/')[-1]
