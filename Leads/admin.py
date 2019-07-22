from django.contrib import admin

from .models import NewApplicants,Lead_Category,Leads,Send_To



class AddressAdmin(admin.ModelAdmin):

    list_display=['leads','lead_Category','Send_to']
    fields = ['lead_Category','leads','Send_to']
    readonly_fields = ['lead_Category']

    # custom attributes (used in "add" view)
    initial_fields = ['lead_Category']
    initial_readonly_fields = []
    lead_Category = None

    def get_fields(self, request, obj=None):
        """ show initial fields in add view, show all fields in change view """
        fields = super().get_fields(request, obj)
        if obj is None:
            fields = self.initial_fields
        return fields

    def get_readonly_fields(self, request, obj=None):
        """ set the initial field readonly in the change view """
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj is None:
            readonly_fields = self.initial_readonly_fields
        return readonly_fields

    def add_view(self, request, form_url='', extra_context=None):
        """ remove the save button from the "add" view """
        extra_context = dict(show_save=False)
        return super().add_view(request, form_url, extra_context)
   
        return super().changeform_view(request, object_id, extra_context=extra_context)
    def save_model(self, request, obj, form, change):
        """ store the select country for use in get_field_queryset """
        self.lead_Category = obj.lead_Category


      
        return super().save_model(request, obj, form, change)

    def get_field_queryset(self, db, db_field, request):
        queryset = super().get_field_queryset(db, db_field, request)
        querysets = super().get_field_queryset(db, db_field, request)


        if db_field.name == 'leads':
            if queryset is None:
             
                queryset = Leads.objects.all()
            # Filter by country
            queryset = queryset.filter(lead_Category=self.lead_Category)


        
        if db_field.name == 'Send_to':
            if querysets is None:
                querysets = Send_To.objects.all()


            querysets = querysets.filter(lead_Category=self.lead_Category)

            return querysets

        return queryset           


        


  
admin.site.register(NewApplicants, AddressAdmin)

