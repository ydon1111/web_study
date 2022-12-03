# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class SongdamData1H(models.Model):
    dt = models.DateTimeField(db_column='DT')  # Field name made lowercase.
    whumi = models.FloatField(db_column='Whumi', blank=True, null=True)  # Field name made lowercase.
    wwind = models.FloatField(db_column='Wwind', blank=True, null=True)  # Field name made lowercase.
    s0a = models.FloatField(db_column='S0a', blank=True, null=True)  # Field name made lowercase.
    s0b = models.FloatField(db_column='S0b', blank=True, null=True)  # Field name made lowercase.
    s0c = models.FloatField(db_column='S0c', blank=True, null=True)  # Field name made lowercase.
    s1a = models.FloatField(db_column='S1a', blank=True, null=True)  # Field name made lowercase.
    s1b = models.FloatField(db_column='S1b', blank=True, null=True)  # Field name made lowercase.
    s1c = models.FloatField(db_column='S1c', blank=True, null=True)  # Field name made lowercase.
    s2a = models.FloatField(db_column='S2a', blank=True, null=True)  # Field name made lowercase.
    s2b = models.FloatField(db_column='S2b', blank=True, null=True)  # Field name made lowercase.
    s2c = models.FloatField(db_column='S2c', blank=True, null=True)  # Field name made lowercase.
    s3a = models.FloatField(db_column='S3a', blank=True, null=True)  # Field name made lowercase.
    s3b = models.FloatField(db_column='S3b', blank=True, null=True)  # Field name made lowercase.
    s3c = models.FloatField(db_column='S3c', blank=True, null=True)  # Field name made lowercase.
    avg = models.FloatField(db_column='Avg', blank=True, null=True)  # Field name made lowercase.
    temp = models.FloatField(db_column='Temp', blank=True, null=True)  # Field name made lowercase.
    humi = models.FloatField(db_column='Humi', blank=True, null=True)  # Field name made lowercase.
    result = models.CharField(db_column='Result', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'songdam_data_1h'


class TestResult(models.Model):
    result_date = models.DateTimeField(blank=True, null=True)
    s0a = models.FloatField(db_column='S0a', blank=True, null=True)  # Field name made lowercase.
    s0b = models.FloatField(db_column='S0b', blank=True, null=True)  # Field name made lowercase.
    s0c = models.FloatField(db_column='S0c', blank=True, null=True)  # Field name made lowercase.
    s1a = models.FloatField(db_column='S1a', blank=True, null=True)  # Field name made lowercase.
    s1b = models.FloatField(db_column='S1b', blank=True, null=True)  # Field name made lowercase.
    s1c = models.FloatField(db_column='S1c', blank=True, null=True)  # Field name made lowercase.
    s2a = models.FloatField(db_column='S2a', blank=True, null=True)  # Field name made lowercase.
    s2b = models.FloatField(db_column='S2b', blank=True, null=True)  # Field name made lowercase.
    s2c = models.FloatField(db_column='S2c', blank=True, null=True)  # Field name made lowercase.
    s3a = models.FloatField(db_column='S3a', blank=True, null=True)  # Field name made lowercase.
    s3b = models.FloatField(db_column='S3b', blank=True, null=True)  # Field name made lowercase.
    s3c = models.FloatField(db_column='S3c', blank=True, null=True)  # Field name made lowercase.
    avg = models.FloatField(blank=True, null=True)
    label = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_result'


class TestResult1H(models.Model):
    result_date = models.DateTimeField(unique=True, blank=True, null=True)
    s0a = models.FloatField(db_column='S0a', blank=True, null=True)  # Field name made lowercase.
    s0b = models.FloatField(db_column='S0b', blank=True, null=True)  # Field name made lowercase.
    s0c = models.FloatField(db_column='S0c', blank=True, null=True)  # Field name made lowercase.
    s1a = models.FloatField(db_column='S1a', blank=True, null=True)  # Field name made lowercase.
    s1b = models.FloatField(db_column='S1b', blank=True, null=True)  # Field name made lowercase.
    s1c = models.FloatField(db_column='S1c', blank=True, null=True)  # Field name made lowercase.
    s2a = models.FloatField(db_column='S2a', blank=True, null=True)  # Field name made lowercase.
    s2b = models.FloatField(db_column='S2b', blank=True, null=True)  # Field name made lowercase.
    s2c = models.FloatField(db_column='S2c', blank=True, null=True)  # Field name made lowercase.
    s3a = models.FloatField(db_column='S3a', blank=True, null=True)  # Field name made lowercase.
    s3b = models.FloatField(db_column='S3b', blank=True, null=True)  # Field name made lowercase.
    s3c = models.FloatField(db_column='S3c', blank=True, null=True)  # Field name made lowercase.
    avg = models.FloatField(blank=True, null=True)
    label = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_result_1h'


class TestResult1HHumi(models.Model):
    result_date = models.DateTimeField(primary_key=True,unique=True, blank=True)
    s0a = models.FloatField(db_column='S0a', blank=True, null=True)  # Field name made lowercase.
    s0b = models.FloatField(db_column='S0b', blank=True, null=True)  # Field name made lowercase.
    s0c = models.FloatField(db_column='S0c', blank=True, null=True)  # Field name made lowercase.
    s1a = models.FloatField(db_column='S1a', blank=True, null=True)  # Field name made lowercase.
    s1b = models.FloatField(db_column='S1b', blank=True, null=True)  # Field name made lowercase.
    s1c = models.FloatField(db_column='S1c', blank=True, null=True)  # Field name made lowercase.
    s2a = models.FloatField(db_column='S2a', blank=True, null=True)  # Field name made lowercase.
    s2b = models.FloatField(db_column='S2b', blank=True, null=True)  # Field name made lowercase.
    s2c = models.FloatField(db_column='S2c', blank=True, null=True)  # Field name made lowercase.
    s3a = models.FloatField(db_column='S3a', blank=True, null=True)  # Field name made lowercase.
    s3b = models.FloatField(db_column='S3b', blank=True, null=True)  # Field name made lowercase.
    s3c = models.FloatField(db_column='S3c', blank=True, null=True)  # Field name made lowercase.
    avg = models.FloatField(blank=True, null=True)
    humi = models.FloatField(blank=True, null=True)
    label = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_result_1h_humi'
