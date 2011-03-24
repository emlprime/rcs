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

class VideoText(models.Model):
    """ the logic for the admin-editable video page text
    """
    date = models.DateField()
    text = models.TextField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return str(self.date)


class Video(models.Model):
    """ the logic for the admin-addable youtube videos on the video page
    """
    youtube_id = models.CharField(max_length=255)
    date = models.DateField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return str(self.date)



class LearnText(models.Model):
   #  the logic for the admin-editable learn page text
    
    date = models.DateField()
    top_text = models.TextField()
    bottom_text = models.TextField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return str(self.date)

class Instructor(models.Model):
    INSTRUMENT_CHOICES = (
        (u'V', u'Voice'),
        (u'G', u'Guitar'),
        (u'P', u'Piano'),
        (u'D', u'Drums'),
        (u'W', u'Woodwinds'),
        (u'M', u'Mandolin and Banjo')
        )

    name = models.CharField(max_length=255)
    instrument = models.CharField(max_length=2, choices=INSTRUMENT_CHOICES)
    bio = models.TextField()
    picture = models.ImageField(upload_to="images", blank=True, null=True)


    def __unicode__(self):
        return self.name


class RecordText(models.Model):
    # the logic for the admin-editable record page text
    
    date = models.DateField()
    text = models.TextField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return str(self.date)

class RecordEquipment(models.Model):
    equipment_type = models.ForeignKey('RecordEquipmentType')
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class RecordEquipmentType(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['order']

    def RecordEquipmentList(self):
        equipment_list=RecordEquipment.objects.filter(equipment_type=self)
        return equipment_list


    def __unicode__(self):
        return self.name


class RehearseText(models.Model):
    # the logic for the admin-editable rehearse page text
    
    date = models.DateField()
    text = models.TextField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return str(self.date)

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
