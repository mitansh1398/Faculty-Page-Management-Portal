# Generated by Django 2.0 on 2017-12-18 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssl_main', '0059_auto_20171129_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(choices=[('Chemistry', 'Chemistry'), ('Civil Engineering', 'Civil Engineering'), ('Mathematics', 'Mathematics'), ('Bio-Tech', 'Bio-Tech'), ('Chemical Engineering', 'Chemical Engineering'), ('Design', 'Design'), ('Electronics and Electrical Engineering', 'Electronics and Electrical Engineering'), ('Physics', 'Physics'), ('Humanities', 'Humanities'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Computer Science and Engineering', 'Computer Science and Engineering')], max_length=200),
        ),
        migrations.AlterField(
            model_name='students',
            name='course',
            field=models.CharField(choices=[('Ph.D.', 'Ph.D.'), ('M.Tech', 'M.Tech'), ('B.Tech', 'B.Tech')], max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.CharField(choices=[('Chemistry', 'Chemistry'), ('Civil Engineering', 'Civil Engineering'), ('Mathematics', 'Mathematics'), ('Bio-Tech', 'Bio-Tech'), ('Chemical Engineering', 'Chemical Engineering'), ('Design', 'Design'), ('Electronics and Electrical Engineering', 'Electronics and Electrical Engineering'), ('Physics', 'Physics'), ('Humanities', 'Humanities'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Computer Science and Engineering', 'Computer Science and Engineering')], default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='designation',
            field=models.CharField(choices=[('Associate Professor', 'Associate Professor'), ('Assistant Professor', 'Assistant Professor'), ('Head of Department', 'Head of Department'), ('Professor', 'Professor')], default='', max_length=50),
        ),
    ]