from django.db import models

class HomeText(models.Model):
    """ the logic for the admin-editable home page text
    """
    date = models.DateField()
    text = models.TextField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return str(self.date)

class ContactText(models.Model):
    """ the logic for the admin-editable contact page text
    """
    date = models.DateField()
    text = models.TextField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return str(self.date)


"""
class LearnText(models.Model):
     the logic for the admin-editable learn page text
    
    date = models.DateField()
    text = models.TextField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return self.date
"""

"""
class RecordText(models.Model):
    # the logic for the admin-editable record page text
    
    date = models.DateField()
    text = models.TextField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return self.date
"""

"""
class RehearseText(models.Model):
    # the logic for the admin-editable rehearse page text
    
    date = models.DateField()
    text = models.TextField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return self.date
"""

class PerformText(models.Model):
    """ the logic for the admin-editable perform page text
    """
    date = models.DateField()
    text = models.TextField()
    header = models.CharField(max_length=255)

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return self.header
