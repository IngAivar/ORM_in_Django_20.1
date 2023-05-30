from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'id': 1, 'category': 'Бытовая техника',
             'description': 'это техника, используемая в быту, предназначенная для'
                            ' облегчения ручного и монотонного труда, а'
                            ' так же повышению комфорта. Она может быть'
                            ' как электрической, так и механической.'},
            {'id': 2, 'category': 'Встраиваемая бытовая техника', 'description': 'это техника, используемая в быту,'},
            {'id': 3, 'category': 'ТВ и приставки', 'description': 'Небольшое устройство для приема волн с последующей'
                                                                   ' передачей информации на телевизоры любого типа. '},
            {'id': 4, 'category': 'Климатическое оборудование',
             'description': 'Оборудование, основанное на работе холодильных'
                            ' машин, предназначенное для автоматического'
                            ' поддержания температуры и иных параметров'
                            ' воздуха в закрытых помещениях или'
                            ' термоизолированных камерах.'},
        ]
        product_list = [
            {'product_name': 'Игровая приставка Microsoft Xbox Series X 1TB',
             'description': 'Приставка',
             'image': 'product/9023.970_I3kMiaY.jpg',
             'purchase_price': '24000',
             'creation_date': '2023-05-03',
             'last_modified_date': '2023-05-07',
             'category': 3},
            {'product_name': 'Беспроводной пылесос Tefal Dual Force TY6737WH, белый',
             'description': 'Аккумуляторный вертикальный пылесос Tefal TY6737WH позволяет '
                            'работать независимо от источника электроэнергии при сохранении '
                            'всех функций хозяйственного пылесоса. Мощный литий-ионный аккумулятор 18 В.',
             'image': 'product/2.970.jpg',
             'purchase_price': '8390',
             'creation_date': '2023-05-06',
             'last_modified_date': '2023-05-18',
             'category': 1},
            {'product_name': 'Двухкамерный холодильник Beko RCNK 335E20VW',
             'description': 'Технология Harvest Fresh Инновационная технология 3-х цветов от Beko внутри отделения '
                            'для фруктов и овощей воссоздает природный световой цикл, сохраняя витамины дольше.',
             'image': 'product/20358.970_8gJVQmI.jpg',
             'purchase_price': '32990',
             'creation_date': '2023-04-06',
             'last_modified_date': '2023-05-14',
             'category': 1},
            {'product_name': 'Газовая плита GEFEST 3200-08',
             'description': 'Газовая плита с эмалированным фасадом и защитным щитком от брызг. '
                            'Исполнена в классическом дизайне, четыре конфорки рабочего стола различного '
                            'диаметра и мощности, мощность нагрева варьируется поворотными переключателями.',
             'image': 'product/29.970.jpg',
             'purchase_price': '15170',
             'creation_date': '2023-05-13',
             'last_modified_date': '2023-05-23',
             'category': 2}
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(category_for_create)

        product_for_create = []
        for product_item in product_list:
            product_for_create.append(
                Product(product_name=product_item['product_name'],
                        description=product_item['description'],
                        image=product_item['image'],
                        purchase_price=product_item['purchase_price'],
                        creation_date=product_item['creation_date'],
                        last_modified_date=product_item['last_modified_date'],
                        category=Category.objects.get(id=product_item['category']),
                        )
            )

        Product.objects.bulk_create(product_for_create)
