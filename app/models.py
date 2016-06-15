from sqlalchemy import event

from app import db

class Entity(db.Model):
    __tablename__ = 'entity'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000), nullable=False, unique=True)
    slug = db.Column(db.String(1000))
    content = db.Column(db.String(5000))

    def __str__(self):
        return self.name


@event.listens_for(Entity, 'after_delete')
def event_after_delete(mapper, connection, target):
  # Здесь будет очень важная бизнес логика
  # Или нет. На самом деле, старайтесь использовать сигналы только
  # тогда, когда других, более правильных вариантов не осталось.
  pass
