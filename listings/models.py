from django.db import models

class Listing(models.Model):
        title = models.CharField(max_length=255)
            description = models.TextField()
                price = models.DecimalField(max_digits=10, decimal_places=2)
                    location = models.CharField(max_length=255)
                        created_at = models.DateTimeField(auto_now_add=True)

                            def __str__(self):
                                        return self.title

                                    class Booking(models.Model):
                                            listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
                                                user = models.CharField(max_length=255)  # Replace with ForeignKey if using Django's User model
                                                    start_date = models.DateField()
                                                        end_date = models.DateField()
                                                            status = models.CharField(max_length=50, choices=[("pending", "Pending"), ("confirmed", "Confirmed"), ("cancelled", "Cancelled")])

                                                                def __str__(self):
                                                                            return f"Booking for {self.listing.title} by {self.user}"

                                                                        class Review(models.Model):
                                                                                listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
                                                                                    user = models.CharField(max_length=255)  # Replace with ForeignKey if using Django's User model
                                                                                        rating = models.IntegerField()
                                                                                            comment = models.TextField()
                                                                                                created_at = models.DateTimeField(auto_now_add=True)

                                                                                                    def __str__(self):
                                                                                                                return f"Review by {self.user} for {self.listing.title}"

# Create your models here.
