# django-adminwidgetswap by DavisD (David Davis) www.davisd.com

from django.contrib import admin

# autodiscover the admin, very important
admin.autodiscover()

def swap_model_field(model, field, widget):
    """
    Swaps an admin model field widget (not the inlines where the model is used)
    """
    if admin.site._registry.has_key(model):
        old_formfield_for_dbfield = admin.site._registry[model].formfield_for_dbfield
        def formfield_for_dbfield(db_field, **kwargs):
            if db_field.name == field:
                kwargs['widget'] = widget
            return old_formfield_for_dbfield(db_field, **kwargs)

        admin.site._registry[model].formfield_for_dbfield = formfield_for_dbfield
    
def swap_model_inline_field(model, field, widget):
    """
    Swaps admin model inline field widget (not the direct model admin)
    """
    for registered_model in admin.site._registry:
        for inline in admin.site._registry[registered_model].inlines:
            if inline.model == model:
                old_formfield_for_dbfield=inline.formfield_for_dbfield
                def formfield_for_dbfield(instance, db_field, *args, **kwargs):
                    if db_field.name == field:
                        kwargs['widget'] = widget
                    return old_formfield_for_dbfield(instance, db_field, *args, **kwargs)
                inline.formfield_for_dbfield = formfield_for_dbfield

def swap_model_and_inline_fields(model, field, widget):
    """
    Swaps an admin model field widget as well as all inlines
    """
    swap_model_field(model, field, widget)
    swap_model_inline_field(model, field, widget)

