from django.core.management.base import BaseCommand
from listings.models import Listing

class Command(BaseCommand):
        help = "Seed the database with sample listings"

            def handle(self, *args, **kwargs):
                        sample_listings = [
                                            {"title": "Beachfront Villa", "description": "A beautiful villa by the sea.", "price": 250.00, "location": "Cape Town"},
                                                        {"title": "Mountain Cabin", "description": "Cozy cabin in the mountains.", "price": 150.00, "location": "Drakensberg"},
                                                                ]

                                for data in sample_listings:
                                                Listing.objects.create(**data)
                                                        self.stdout.write(self.style.SUCCESS("Successfully seeded the database!"))
                                                        
