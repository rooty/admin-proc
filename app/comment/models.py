from sqlalchemy import event

from app.extensions import db


class Comment(db.Model):
    __tablename__ = 'Comment'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(1000))
    entity_id = db.Column(db.ForeignKey('Entity'))


    def __str__(self):
        return self.comment




@event.listens_for(Comment, 'after_delete')
def event_after_delete(mapper, connection, target):
  # Здесь будет очень важная бизнес логика
  # Или нет. На самом деле, старайтесь использовать сигналы только
  # тогда, когда других, более правильных вариантов не осталось.
  pass

