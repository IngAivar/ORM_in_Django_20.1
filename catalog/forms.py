from django import forms
from django.forms import ModelForm

from catalog.models import Product, Contact, Post


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('phone', 'email', 'site')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'preview', 'is_published')


class CreateProductForm(ModelForm):
    """
    Форма для создания товара
    """
    FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    def __init__(self, *args, **kwargs) -> None:
        """
        Инициализирует форму и добавляет CSS-классы и
        плейсхолдеры для полей формы.
        """
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name == 'image':
                field.widget.attrs['class'] = 'form-control-file'

        if 'product_name' in self.fields:
            self.fields['product_name'].widget.attrs['placeholder'] = 'Введите название товара'

    def clean_name(self) -> str:
        """
        Валидация названия продукта.
        Проверяет наличие запрещенных слов в названии.

        :return: Очищенное название продукта.
        :raises: forms.ValidationError, если название содержит запрещенное слово.
        """
        product_name = self.cleaned_data['product_name']
        for word in self.FORBIDDEN_WORDS:
            if word.lower() in product_name.lower():
                raise forms.ValidationError(f"Название содержит запрещенное слово: {word}")

        return product_name

    class Meta:
        model = Product
        fields = ('product_name', 'description', 'image', 'purchase_price', 'category')