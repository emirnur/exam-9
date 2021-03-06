from django.db import models

COUNT = 0


class Photo(models.Model):
    photo = models.ImageField(upload_to='product_images', verbose_name='Фото')
    sign = models.CharField(max_length=200, verbose_name='Подпись')
    like_count = models.IntegerField(default=COUNT, verbose_name='Количество лайков')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Автор',
                             related_name='photo_author')

    def __str__(self):
        return self.sign


class LikePhoto(models.Model):
    author = models.ForeignKey('auth.User', related_name='like_user', on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, related_name='like_photo', on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField(max_length=3000, verbose_name='Текст')
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, verbose_name='Фото', related_name='comment_photo')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Автор',
                               related_name='comment_author')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.text


# class PhotoLike(models.Model):
#     photo = models.ForeignKey(Photo, on_delete=models.CASCADE, verbose_name='Фото', related_name='photo_likes')
#     like = models.ForeignKey(Like, on_delete=models.CASCADE, verbose_name='Лайк', related_name='photo_likes')
#
#     def __str__(self):
#         return "{} - {}".format(self.photo, self.like)

