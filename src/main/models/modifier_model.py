from src.main.config.lib_instance import db
from src.main.models.base_model import BaseModel
from src.main.models.relation_model import ItemModifier


class Modifier(BaseModel):
    __tablename__ = "modifiers"

    description = db.Column(db.Text, nullable=False)

    items = db.relationship(
        "Item", secondary=ItemModifier.__table__, back_populates="modifiers"
    )
