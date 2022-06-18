from src.main.config.lib_instance import db
from src.main.models.base_model import BaseModel
from src.main.models.relation_model import ItemModifier


class Item(BaseModel):
    __tablename__ = "items"

    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Textm, nullable=False)
    price = db.Column(db.Float, nullable=False)
    section_id = db.Column(db.Integer, db.ForeignKey("sections.id"), nullable=False)

    modifiers = db.relationship(
        "Modifier", secondary=ItemModifier.__table__, backpopulates="items"
    )
