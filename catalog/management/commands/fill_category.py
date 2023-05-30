from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'id': 1, 'category': 'Бытовая техника', 'description': 'это техника, используемая в быту, предназначенная для'
                                                           ' облегчения ручного и монотонного труда, а'
                                                           ' так же повышению комфорта. Она может быть'
                                                           ' как электрической, так и механической.'},
            {'id': 2, 'category': 'Встраиваемая бытовая техника', 'description': 'это техника, используемая в быту,'},
            {'id': 3, 'category': 'ТВ и приставки', 'description': 'Небольшое устройство для приема волн с последующей'
                                                          ' передачей информации на телевизоры любого типа. '},
            {'id': 4, 'category': 'Климатическое оборудование', 'description': 'Оборудование, основанное на работе холодильных'
                                                                      ' машин, предназначенное для автоматического'
                                                                      ' поддержания температуры и иных параметров'
                                                                      ' воздуха в закрытых помещениях или'
                                                                      ' термоизолированных камерах.'},
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(category_for_create)

