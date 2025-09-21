from django.core.management.base import BaseCommand
from references.models import Category

class Command(BaseCommand):
    help = 'Create sample categories for the reference manager'

    def handle(self, *args, **options):
        categories = [
            {'name': 'Court Case', 'description': 'Legal documents and court-related files'},
            {'name': 'Payment Receipt', 'description': 'Financial documents and payment records'},
            {'name': 'Site Picture', 'description': 'Photographs of physical locations or sites'},
            {'name': 'Contract', 'description': 'Legal agreements and contracts'},
            {'name': 'Invoice', 'description': 'Billing documents and invoices'},
            {'name': 'Correspondence', 'description': 'Letters, emails, and other communications'},
            {'name': 'Technical Drawing', 'description': 'Engineering drawings and technical specifications'},
            {'name': 'Certificate', 'description': 'Certificates and official documents'},
        ]

        created_count = 0
        for category_data in categories:
            category, created = Category.objects.get_or_create(
                name=category_data['name'],
                defaults={'description': category_data['description']}
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created category: {category.name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Category already exists: {category.name}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} new categories')
        )
