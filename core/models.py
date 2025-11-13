from django.db import models
from django.utils.text import slugify

# ==========================================================
# 1. City  الاساسي
# ه# ==========================================================
class City(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, help_text="هذا هو الرابط، سيتم إنشاؤه تلقائياً. مثال: jeddah")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Cities" # لتصحيح الاسم في لوحة التحكم

    def __str__(self):
        return self.name

# ==========================================================
# 2.Destination 
# ==========================================================
class Destination(models.Model):
  
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="destinations")
    
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
   
    
    short_tagline = models.CharField(max_length=160, blank=True)
    season = models.CharField(max_length=80, blank=True)
    summary = models.TextField(blank=True)
    cover = models.ImageField(upload_to="destinations/covers/", blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
  
    price = models.IntegerField(default=0, help_text="السعر (مثال: 5000)")

    class Meta: 
        ordering = ["name"]
    
    def __str__(self): 
        return self.name

# ==========================================================
# 3. DestinationPhoto
# ==========================================================
class DestinationPhoto(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="photos")
    image = models.ImageField(upload_to="destinations/photos/")
    caption = models.CharField(max_length=150, blank=True)
    
    def __str__(self): 
        return f"{self.destination.name} photo"

# ==========================================================
# 4. Event
# ==========================================================
class Event(models.Model):

#كود ربط الفعاليات بالمدن 
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="events")
    
    name = models.CharField(max_length=200)
    location_text = models.CharField(max_length=100, help_text="مثال: 'DIRIYAH | SHOPPING'")
    price_text = models.CharField(max_length=50, blank=True, help_text="مثال: 'From $ 107'")
    event_date = models.DateField()
    image = models.ImageField(upload_to='events/')

    class Meta: 
        ordering = ["event_date"]

    def __str__(self):
        return self.name