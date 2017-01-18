# django-file-md5
Django File Md5

## Installation
```shell
pip install django-file-md5
```

## Usage
```python
from filemd5 import calculate_md5

def xxx(request):
    photo = request.FILES.get('photo', '')
    if photo:
        md5 = calculate_md5(photo)
```
