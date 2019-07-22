from django.db import models
from smart_selects.db_fields import ChainedForeignKey
User_choice = (
    ('Institute', 'Institute'),
    ('All Institute', 'All Institute'),
   
    ('Company', 'Company'),
    ('All Company', 'All Company')
)

class Lead_Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Leads(models.Model):
    lead_Category = models.ForeignKey(Lead_Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
class Send_To(models.Model):
    lead_Category = models.ForeignKey(Lead_Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=450,choices=User_choice)

    def __str__(self):
        return self.name
        

class NewApplicants(models.Model):
    lead_Category = models.ForeignKey(Lead_Category,on_delete=models.CASCADE)
    leads = models.ForeignKey(
        Leads, on_delete=models.CASCADE,null=True, blank=True
    )
    Send_to=models.ForeignKey(Send_To,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.lead_Category,self.leads,self.Send_to)


   
                                        

