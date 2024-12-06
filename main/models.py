from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

from django.utils.text import slugify

class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True, unique=True, max_length=255)
    image = models.ImageField(upload_to='articles/')
    reading_time = models.DurationField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    author = models.CharField(max_length=255, default="Anonymous")

    published = models.BooleanField(default=False)

    views = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            count = 1
            while Article.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"
                count += 1
            self.slug = slug
        super().save(*args, **kwargs)



class Content(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text[:40]


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:40]


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    subject = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


