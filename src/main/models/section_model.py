from sqlalchemy import inspect
from src.main.config.lib_instance import db
from src.main.models.base_model import BaseModel
from src.main.models.output_mixin import OutputMixin


class Section(OutputMixin, BaseModel):
    __tablename__ = "sections"
    # RELATIONSHIPS_TO_DICT = True

    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)

    items = db.relationship("Item", backref="sections", lazy=True)

    # def __iter__(self):
    #     return self.to_dict().iteritems()

    def to_json_old(self) -> dict:
        return {
            c.key: str(getattr(self, c.key)) for c in inspect(self).mapper.column_attrs
        }
