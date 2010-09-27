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
    instrument = models.ForeignKey('Instrument')
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Instrument(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['order']

    def InstructorList(self):
        instructor_list=Instructor.objects.filter(instrument=self)
        return instructor_list


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
