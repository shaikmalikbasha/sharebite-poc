from src.main.models.base_model import BaseModel
from src.main.config.lib_instance import db


class ItemModifier(BaseModel):
    __tablename__ = "item_modifier"

    item_id = db.Column(db.Integer, db.ForeignKey("items.id"), primary_key=True)
    modifier_id = db.Column(db.Integer, db.ForeignKey("modifiers.id"), primary_key=True)
