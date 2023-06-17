from django import forms
from django.forms import ModelForm, inlineformset_factory, BaseInlineFormSet

from catalog.models import Product, Contact, Post, Version


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


class VersionForm(forms.ModelForm):
    """
    Форма для создания версии
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        Инициализирует форму и добавляет CSS-классы и
        плейсхолдеры для полей формы.
        """
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name != 'is_current_version':
                field.widget.attrs['class'] = 'form-control'

        self.fields['version_number'].widget.attrs['placeholder'] = 'Введите номер версии'
        self.fields['version_name'].widget.attrs['placeholder'] = 'Введите название версии'

    class Meta:
        model = Version
        fields = ['version_number', 'version_name', 'is_current_version']


class VersionFormSet(BaseInlineFormSet):
    """
    Класс, описывающий формсет для версий продукта.
    Наследуется от BaseInlineFormSet Django.
    """

    def clean(self):
        """
        Проверяет, что выбрана только одна активная версия продукта.
        """
        super().clean()
        current_version_count = 0
        for form in self.forms:
            if not form.is_valid():
                return
            if form.cleaned_data and form.cleaned_data.get('is_current_version'):
                current_version_count += 1

        if current_version_count > 1:
            raise forms.ValidationError(
                'Может быть только одна активная версия продукта. Пожалуйста, выберите только одну активную версию.'
            )


ProductVersionFormSet = inlineformset_factory(
    parent_model=Product,
    model=Version,
    form=VersionForm,
    formset=VersionFormSet,
    extra=1
)