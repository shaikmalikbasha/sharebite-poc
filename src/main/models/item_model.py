from src.main.config.lib_instance import db
from src.main.models.base_model import BaseModel
from src.main.models.output_mixin import OutputMixin
from src.main.models.relation_model import ItemModifier


class Item(OutputMixin, BaseModel):
    __tablename__ = "items"
    RELATIONSHIPS_TO_DICT = True

    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    section_id = db.Column(db.Integer, db.ForeignKey("sections.id"), nullable=False)

    modifiers = db.relationship(
        "Modifier", secondary=ItemModifier.__table__, back_populates="items"
    )
