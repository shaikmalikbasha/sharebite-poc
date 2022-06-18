from src.main.models.base_model import BaseModel
from src.main.config.lib_instance import db


class Section(BaseModel):
    __tablename__ = "sections"

    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Textm, nullable=False)

    items = db.relationship("Item", backref="sections", lazy=True)
