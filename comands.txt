1 - python manage.py makemigrations
	python manage.py migrate
	python manage.py shell
	from news.models import *

	u1 = User.objects.create_user(username = 'user1') 
	u2 = User.objects.create_user(username = 'user2') 

2 - Author.objects.create(user = u1)
	Author.objects.create(user = u2)


3 - Category.objects.create(category_name = 'category_1')
	Category.objects.create(category_name = 'category_2')
	Category.objects.create(category_name = 'category_3')
	Category.objects.create(category_name = 'category_4')

4 - Author.objects.get(id=1)
	Post.objects.create(author = author, choice_field = 'NW', article_header = 'First news', article_text = 'Text in first news')
	Post.objects.create(author = Author.objects.get(id=2), choice_field = 'AR', article_header = 'article1', article_text = 'article text') 
	Post.objects.create(author = Author.objects.get(id=1), choice_field = 'AR', article_header = 'article2', article_text = 'article text') 
	
5 - Post.objects.get(id = 1).category.add(Category.objects.get(id=1))
	Post.objects.get(id = 1).category.add(Category.objects.get(id=2))
	Post.objects.get(id = 2).category.add(Category.objects.get(id=3))
	Post.objects.get(id = 2).category.add(Category.objects.get(id=4))
	Post.objects.get(id = 3).category.add(Category.objects.get(id=3))
	Post.objects.get(id = 3).category.add(Category.objects.get(id=4))



6 - Comment.objects.create(post=Post.objects.get(id=1), user=User.objects.get(id=1), comment_text='This news is very good!')
	Comment.objects.create(post=Post.objects.get(id=1), user=User.objects.get(id=2), comment_text='Nice one!')
	Comment.objects.create(post=Post.objects.get(id=2), user=User.objects.get(id=1), comment_text=':(')
	Comment.objects.create(post=Post.objects.get(id=3), user=User.objects.get(id=1), comment_text='XD')

7 - Comment.objects.get(id=1).like() 
	Comment.objects.get(id=1).like()
	Comment.objects.get(id=1).dislike()

	Post.objects.get(id=1).like() 
	Post.objects.get(id=2).like() 
	Post.objects.get(id=3).like() 
	Post.objects.get(id=1).dislike()


8 - Author.objects.get(id=1).update_rating()
	Author.objects.get(id=2).update_rating()


9 - Author.objects.order_by('-user_rating')[:1]

>>> a = Author.objects.order_by('-user_rating')    
>>> for i in a:   ingme                         
...     i.user_rating                               
...     i.user.username    

10 -  a = Post.objects.order_by('-article_rating')[:1]    
>>> for i in a:                                         
...     i.creation_date
...     i.author
...     i.article_rating
...     i.article_header
...     i.preview()

11 -  for i in Comment.objects.all():
...     i.comment_date
...     i.user.username
...     i.comment_rating
... 



