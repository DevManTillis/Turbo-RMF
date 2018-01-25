from django.contrib import admin

# Register your models here.
from upload.models import Document
#from polls.models import 

class DocumentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['document_name']}),
        ('Date information', {'fields': ['uploaded_at']}),
    ]

admin.site.register(Document, DocumentAdmin)
