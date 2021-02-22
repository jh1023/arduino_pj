from django.db import models

# # SQLAlchemy
# from sqlalchemy import Sequence, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()
class BSensor(models.Model):
    s_no = models.AutoField(primary_key=True)
    s_data = models.FloatField(blank=True,max_length=255, null=True)
    s_date = models.DateTimeField(max_length=20, null=False, unique=True)

    class Meta:
        managed = False
        db_table = 'b_sensor'

# Create your models here.
class SensorData(models.Model):
    s_no = models.AutoField(primary_key=True)
    s_date = models.DateTimeField(blank=True, null=True)
    locate = models.CharField(max_length=50, blank=True, null=True)
    magnitude = models.FloatField(blank=True, null=True)
    degree = models.FloatField(blank=True, null=True)
    x = models.FloatField(blank=True, null=True,max_length=20)
    y = models.FloatField(blank=True, null=True,max_length=20)

    class Meta:
        managed = False
        db_table = 'sensor_data'
                

class Board(models.Model):
    b_no = models.AutoField(db_column='b_no', primary_key=True)
    b_title = models.CharField(db_column='b_title', max_length=255)
    b_note = models.TextField(db_column='b_note', )
    b_writer = models.CharField(db_column='b_writer', max_length=50)
    parent_no = models.IntegerField(db_column='parent_no', default=0)
    b_count = models.IntegerField(db_column='b_count', default=0)
    b_date = models.DateTimeField(db_column='b_date', )
    #usage_flag = models.CharField(db_column='usage_flag', max_length=10, default='1')

    class Meta:
        managed = False
        db_table = 'board'

    def __str__(self):
        return "제목 : " + self.b_title + ", 작성자 : " + self.b_writer

##
    