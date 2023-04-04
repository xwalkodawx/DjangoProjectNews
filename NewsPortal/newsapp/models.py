from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):  # Модель, содержащая объекты всех авторов.
	user_author = models.OneToOneField(User, on_delete=models.CASCADE)
	rating_author = models.SmallIntegerField(default=0)

	def update_rating(self):  # Обновляет рейтинг текущего автора
		post_rat = self.post_set.aggregate(post_rating=Sum('rating'))
		span_post_rating = 0
		span_post_rating += post_rat.get('post_rating')

		comment_rat = self.user_author.comment_set.aggregate(comment_rating=Sum('rating'))
		span_comm_rating = 0
		span_comm_rating += comment_rat.get('comment_rating')

		self.rating_author = span_post_rating * 3 + span_comm_rating
		self.save()


class Category(models.Model):  # Категории новостей/статей — темы, которые они отражают
	name = models.CharField(max_length=64, unique=True)


class Post(models.Model):  # Статьи и новости, которые создают пользователи
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	ARTICLE = 'AR'
	NEWS = 'NE'
	CATEGORY = ((NEWS, 'Новость'), (ARTICLE, 'Статья'),)
	choice_category = models.CharField(max_length=2, choices=CATEGORY, default=NEWS)
	date_creation = models.DateTimeField(auto_now_add=True)
	post_category = models.ManyToManyField(Category, through='PostCategory')
	title = models.CharField(max_length=255)
	text = models.TextField()
	rating = models.SmallIntegerField(default=0)

	def like(self):
		self.rating += 1
		self.save()

	def dislike(self):
		self.rating -= 1
		self.save()

	def preview(self):  # Возвращает начало статьи длиной 124 символа и добавляет многоточие в конце
		return self.text[0:123]+'...'


class PostCategory(models.Model):  # Промежуточная модель
	post_through = models.ForeignKey(Post, on_delete=models.CASCADE)
	category_through = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
	post_through = models.ForeignKey(Post, on_delete=models.CASCADE)
	user_through = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField()
	comment_datetime = models.DateTimeField(auto_now_add=True)
	rating = models.SmallIntegerField(default=0)

	def like(self):
		self.rating += 1
		self.save()

	def dislike(self):
		self.rating -= 1
		self.save()
