from . models import Category


def categories(request):
    return {
        # 'categories': Category.objects.all()
        'categories': Category.objects.filter(level=0)

    }
