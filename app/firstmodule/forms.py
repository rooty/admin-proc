from flask_wtf import Form
from wtforms import (
    StringField,
    TextAreaField,
)
from wtforms.validators import DataRequired

class EntityCreateForm(Form):
    name = StringField(
        'Название',
        [
            DataRequired(message="Поле обязательно для заполнения")
        ],
        description="Название"
    )
    content = TextAreaField(
        'Содержимое',
        [],
        description="Содержимое записи",
    )

