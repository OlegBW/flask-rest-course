from db import db


class ItemTagsModel(db.Model):
    __tablename__ = "items_tags"

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"))

    # items = db.relationship('ItemModel', back_populates="item_tags", cascade="all, delete")
    # tags = db.relationship('TagModel', back_populates="tag_items", cascade="all, delete")
