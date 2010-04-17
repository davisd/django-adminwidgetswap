# django-adminwidgetswap by DavisD (David Davis) www.davisd.com
# v2.0, now with functionality!

from django.contrib import admin

# autodiscover the admin, very important
admin.autodiscover()

def __get_model_formfield_for_dbfield(model, field, widget):
    """
    Gets the new formfield_for_dbfield_function for a model
    """
    old_formfield_for_dbfield = admin.site._registry[model].formfield_for_dbfield
    def formfield_for_dbfield(db_field, **kwargs):
        if db_field.name == field:
            kwargs['widget'] = widget
        return old_formfield_for_dbfield(db_field, **kwargs)
    return formfield_for_dbfield

def __get_inline_formfield_for_dbfield(inline, field, widget):
    """
    Gets the new formfield_for_dbfield function for an inline
    """
    old_formfield_for_dbfield = inline.formfield_for_dbfield
    def formfield_for_dbfield(db_field, **kwargs):
        if db_field.name == field:
            kwargs['widget'] = widget
        return old_formfield_for_dbfield(db_field, **kwargs)
    return formfield_for_dbfield

def swap_model_field(model, field, widget):
    """
    Swaps an admin model field widget (not the inlines where the model is used)
    """
    if admin.site._registry.has_key(model):
        admin.site._registry[model].formfield_for_dbfield = __get_model_formfield_for_dbfield(model, field, widget)
    
def swap_model_inline_field(model, field, widget):
    """
    Swaps admin model inline field widget (not the direct model admin)
    """
    for registered_model in admin.site._registry:
        if admin.site._registry.has_key(registered_model):
            for inline in admin.site._registry[registered_model].inline_instances:
                if inline.model == model:
                    inline.formfield_for_dbfield = __get_inline_formfield_for_dbfield(inline, field, widget)

def swap_model_and_inline_fields(model, field, widget):
    """
    Swaps an admin model field widget as well as all inlines
    """
    swap_model_field(model, field, widget)
    swap_model_inline_field(model, field, widget)
