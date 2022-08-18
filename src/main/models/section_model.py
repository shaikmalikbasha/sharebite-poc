from sqlalchemy import inspect
from src.main.config.lib_instance import db, ma
from src.main.models.base_model import BaseModel
from src.main.models.item_model import Item
from src.main.models.modifier_model import Modifier


class Section(BaseModel):
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


class ModifierSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Modifier

    # items = fields.Nested("ItemSchema", exclude=("modifiers",), many=True) # Working
    items = ma.Nested("ItemSchema", exclude=("modifiers",), many=True)


class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Item

    # modifiers = fields.Nested("ModifierSchema", exclude=("items",), many=True) #Working
    modifiers = ma.Nested("ModifierSchema", exclude=("items",), many=True)
    section = ma.Nested("SectionSchema", exclude=("items",))


class SectionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Section

    # items = fields.Nested("ItemSchema", many=True) # Working
    items = ma.Nested("ItemSchema", exclude=("section",), many=True)
