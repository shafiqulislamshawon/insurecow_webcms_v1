from django.db import models

# Create your models here.

class Logo(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="logos/")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class Slider(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='sliders/')

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    parent = models.ForeignKey('self', null=True, blank=True, related_name='sub_menu', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact from {self.name}"


class Gallery(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Gallery/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

class Testimonial(models.Model):
    name = models.CharField(max_length=120, null=True)
    designation = models.CharField(max_length=120, null=True)
    quotes = models.TextField()
    image = models.ImageField(upload_to='testimonials/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name