# Generated by Django 3.0.8 on 2020-07-16 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0029_auto_20200716_0525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='bandleader_fee',
        ),
        migrations.RemoveField(
            model_name='event',
            name='bandleader_fee_all_incl',
        ),
        migrations.RemoveField(
            model_name='event',
            name='bandleader_feedback_status',
        ),
        migrations.RemoveField(
            model_name='event',
            name='bandleader_gst_amnt',
        ),
        migrations.RemoveField(
            model_name='event',
            name='bandleader_invoice_status',
        ),
        migrations.RemoveField(
            model_name='event',
            name='bandleader_payment_status',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_2_fee',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_2_fee_all_incl',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_2_gst_amnt',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_2_invoice_status',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_2_payment_status',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_3_fee',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_3_fee_all_incl',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_3_gst_amnt',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_3_invoice_status',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_3_payment_status',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_4_fee',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_4_fee_all_incl',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_4_gst_amnt',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_4_invoice_status',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_4_payment_status',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_5_fee',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_5_fee_all_incl',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_5_gst_amnt',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_5_invoice_status',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_5_payment_status',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_6_fee',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_6_fee_all_incl',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_6_gst_amnt',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_6_invoice_status',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_6_payment_status',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_7_fee',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_7_fee_all_incl',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_7_gst_amnt',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_7_invoice_status',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_7_payment_status',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_8_fee',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_8_fee_all_incl',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_8_gst_amnt',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_8_invoice_status',
        ),
        migrations.RemoveField(
            model_name='event',
            name='musician_8_payment_status',
        ),
        migrations.AddField(
            model_name='eventmusicians',
            name='fee_all_incl',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='eventmusicians',
            name='feedback_status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='eventmusicians',
            name='gst_amnt',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='eventmusicians',
            name='invoice_status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='eventmusicians',
            name='is_bandleader',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='eventmusicians',
            name='payment_status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]