from django.db import models
from datetime import datetime
from django.conf import settings
from django.template.defaultfilters import slugify

class Categories(models.TextChoices):
    WORLD = 'world'
    ATTRACTION = 'attraction'
    CULTURE = 'culture'
    NATURAL_PARKS_AND_RESERVES = 'natural parks and reserves'
    ANIMALS = 'animals'
    PLANTS = 'plants'
    SPORT = 'sport'
    HEALTH = 'health'
    EXTREME = 'extreme'


class CategoriesTours(models.TextChoices):
    OTHER = 'other'
    CARAVANNING = 'caravanning'
    BANANA = 'banana'
    FOPE_PARK = 'rope_park'
    BIKE_RIDE = 'bike_ride'
    HORSE_RIDE = 'horse_ride'
    CAMPING = 'camping'
    LINER = 'liner'
    SKIS = 'skis'
    HUNTING = 'hunting'
    PARA = 'para'
    FISHING = 'fishing'
    SNOW_SCOOTER = 'snow_scooter'
    ALLOY = 'alloy'
    PHOTO_TOURISM = 'photo_tourism'
    ECOTOURISM = 'ecotourism'


class BlogPost(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    category = models.CharField(max_length=50, choices=Categories.choices, default=Categories.WORLD)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    content = models.TextField()
    featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = BlogPost.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = BlogPost.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug

        if self.featured:
            try:
                temp = BlogPost.objects.get(featured=True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except BlogPost.DoesNotExist:
                pass
        
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class PostTour(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    category = models.CharField(max_length=50, choices=CategoriesTours.choices, default=CategoriesTours.OTHER)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    content = models.TextField()
    featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = PostTour.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = PostTour.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug

        if self.featured:
            try:
                temp = PostTour.objects.get(featured=True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except PostTour.DoesNotExist:
                pass
        
        super(PostTour, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
