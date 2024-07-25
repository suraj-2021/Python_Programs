from PIL import Image
from django.core.files import File
import os

thumb = Image.open(new_file.photo.path)
thumb.thumbnail((100, 100))

thumb_path = os.path.join('path/to/thumbnails', f'thumb_{new_file.id}.jpg')
thumb.save(thumb_path, 'JPEG')

with open(thumb_path, 'rb') as thumb_file:
    new_file.thumb.save(f'thumb_{new_file.id}.jpg', File(thumb_file))

uploaded = request.FILES['photo']
file_content = ContentFile(uploaded.read())
new_file = YourModel()
new_file.img.save(f'{new_file.id}.jpg', file_content)
new_file.save()
