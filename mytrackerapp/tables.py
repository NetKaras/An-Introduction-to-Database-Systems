import django_tables2 as tables
from django.utils.html import mark_safe
from .models import RecordModel

class MaterializeCssCheckboxColumn(tables.CheckBoxColumn):
    def render(self, value, bound_column, record):
        default = {"type": "checkbox", "name": bound_column.name, "value": value}
        if self.is_checked(value, record):
            default.update({"checked": "checked"})

        general = self.attrs.get("input")
        specific = self.attrs.get("td__input")
        attrs = tables.utils.AttributeDict(default, **(specific or general or {}))
        return mark_safe("<p><label><input %s/><span></span></label></p>" % attrs.as_html())

class RecordTable(tables.Table):
    check = MaterializeCssCheckboxColumn(accessor='date')
    date = tables.DateColumn(format='d/m/y')
    class Meta:
        model = RecordModel
        attrs = {'class': 'paleblue', "width":"100%"}