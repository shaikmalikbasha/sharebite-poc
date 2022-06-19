from src.main.config.lib_instance import db
from src.main.models.base_model import BaseModel


class ItemModifier(BaseModel):
    __tablename__ = "item_modifier"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))
    modifier_id = db.Column(db.Integer, db.ForeignKey("modifiers.id"))
