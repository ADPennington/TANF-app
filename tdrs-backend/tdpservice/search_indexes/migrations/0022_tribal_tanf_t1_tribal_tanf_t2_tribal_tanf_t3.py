# Generated by Django 3.2.15 on 2023-10-31 16:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('data_files', '0012_datafile_s3_versioning_id'),
        ('search_indexes', '0021_ssp_m7'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tribal_TANF_T3',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('RecordType', models.CharField(max_length=156, null=True)),
                ('RPT_MONTH_YEAR', models.IntegerField(null=True)),
                ('CASE_NUMBER', models.CharField(max_length=11, null=True)),
                ('FAMILY_AFFILIATION', models.IntegerField(null=True)),
                ('DATE_OF_BIRTH', models.IntegerField(null=True)),
                ('SSN', models.CharField(max_length=9, null=True)),
                ('RACE_HISPANIC', models.IntegerField(null=True)),
                ('RACE_AMER_INDIAN', models.IntegerField(null=True)),
                ('RACE_ASIAN', models.IntegerField(null=True)),
                ('RACE_BLACK', models.IntegerField(null=True)),
                ('RACE_HAWAIIAN', models.IntegerField(null=True)),
                ('RACE_WHITE', models.IntegerField(null=True)),
                ('GENDER', models.IntegerField(null=True)),
                ('RECEIVE_NONSSA_BENEFITS', models.IntegerField(null=True)),
                ('RECEIVE_SSI', models.IntegerField(null=True)),
                ('RELATIONSHIP_HOH', models.CharField(max_length=2, null=True)),
                ('PARENT_MINOR_CHILD', models.IntegerField(null=True)),
                ('EDUCATION_LEVEL', models.CharField(max_length=2, null=True)),
                ('CITIZENSHIP_STATUS', models.IntegerField(null=True)),
                ('UNEARNED_SSI', models.CharField(max_length=4, null=True)),
                ('OTHER_UNEARNED_INCOME', models.CharField(max_length=4, null=True)),
                ('datafile', models.ForeignKey(blank=True, help_text='The parent file from which this record was created.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tribal_t3_parent', to='data_files.datafile')),
            ],
        ),
        migrations.CreateModel(
            name='Tribal_TANF_T2',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('RecordType', models.CharField(max_length=156, null=True)),
                ('RPT_MONTH_YEAR', models.IntegerField(null=True)),
                ('CASE_NUMBER', models.CharField(max_length=11, null=True)),
                ('FAMILY_AFFILIATION', models.IntegerField(null=True)),
                ('NONCUSTODIAL_PARENT', models.IntegerField(null=True)),
                ('DATE_OF_BIRTH', models.IntegerField(null=True)),
                ('SSN', models.CharField(max_length=9, null=True)),
                ('RACE_HISPANIC', models.IntegerField(null=True)),
                ('RACE_AMER_INDIAN', models.IntegerField(null=True)),
                ('RACE_ASIAN', models.IntegerField(null=True)),
                ('RACE_BLACK', models.IntegerField(null=True)),
                ('RACE_HAWAIIAN', models.IntegerField(null=True)),
                ('RACE_WHITE', models.IntegerField(null=True)),
                ('GENDER', models.IntegerField(null=True)),
                ('FED_OASDI_PROGRAM', models.IntegerField(null=True)),
                ('FED_DISABILITY_STATUS', models.IntegerField(null=True)),
                ('DISABLED_TITLE_XIVAPDT', models.IntegerField(null=True)),
                ('AID_AGED_BLIND', models.IntegerField(null=True)),
                ('RECEIVE_SSI', models.IntegerField(null=True)),
                ('MARITAL_STATUS', models.IntegerField(null=True)),
                ('RELATIONSHIP_HOH', models.CharField(max_length=2, null=True)),
                ('PARENT_MINOR_CHILD', models.IntegerField(null=True)),
                ('NEEDS_PREGNANT_WOMAN', models.IntegerField(null=True)),
                ('EDUCATION_LEVEL', models.CharField(max_length=2, null=True)),
                ('CITIZENSHIP_STATUS', models.IntegerField(null=True)),
                ('COOPERATION_CHILD_SUPPORT', models.IntegerField(null=True)),
                ('MONTHS_FED_TIME_LIMIT', models.CharField(max_length=3, null=True)),
                ('MONTHS_STATE_TIME_LIMIT', models.CharField(max_length=2, null=True)),
                ('CURRENT_MONTH_STATE_EXEMPT', models.IntegerField(null=True)),
                ('EMPLOYMENT_STATUS', models.IntegerField(null=True)),
                ('WORK_PART_STATUS', models.CharField(max_length=2, null=True)),
                ('UNSUB_EMPLOYMENT', models.CharField(max_length=2, null=True)),
                ('SUB_PRIVATE_EMPLOYMENT', models.CharField(max_length=2, null=True)),
                ('SUB_PUBLIC_EMPLOYMENT', models.CharField(max_length=2, null=True)),
                ('WORK_EXPERIENCE', models.CharField(max_length=2, null=True)),
                ('OJT', models.CharField(max_length=2, null=True)),
                ('JOB_SEARCH', models.CharField(max_length=2, null=True)),
                ('COMM_SERVICES', models.CharField(max_length=2, null=True)),
                ('VOCATIONAL_ED_TRAINING', models.CharField(max_length=2, null=True)),
                ('JOB_SKILLS_TRAINING', models.CharField(max_length=2, null=True)),
                ('ED_NO_HIGH_SCHOOL_DIPLOMA', models.CharField(max_length=2, null=True)),
                ('SCHOOL_ATTENDENCE', models.CharField(max_length=2, null=True)),
                ('PROVIDE_CC', models.CharField(max_length=2, null=True)),
                ('ADD_WORK_ACTIVITIES', models.CharField(max_length=2, null=True)),
                ('OTHER_WORK_ACTIVITIES', models.CharField(max_length=2, null=True)),
                ('REQ_HRS_WAIVER_DEMO', models.CharField(max_length=2, null=True)),
                ('EARNED_INCOME', models.CharField(max_length=4, null=True)),
                ('UNEARNED_INCOME_TAX_CREDIT', models.CharField(max_length=4, null=True)),
                ('UNEARNED_SOCIAL_SECURITY', models.CharField(max_length=4, null=True)),
                ('UNEARNED_SSI', models.CharField(max_length=4, null=True)),
                ('UNEARNED_WORKERS_COMP', models.CharField(max_length=4, null=True)),
                ('OTHER_UNEARNED_INCOME', models.CharField(max_length=4, null=True)),
                ('datafile', models.ForeignKey(blank=True, help_text='The parent file from which this record was created.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tribal_t2_parent', to='data_files.datafile')),
            ],
        ),
        migrations.CreateModel(
            name='Tribal_TANF_T1',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('RecordType', models.CharField(max_length=156, null=True)),
                ('RPT_MONTH_YEAR', models.IntegerField(null=True)),
                ('CASE_NUMBER', models.CharField(max_length=11, null=True)),
                ('COUNTY_FIPS_CODE', models.CharField(max_length=3, null=True)),
                ('STRATUM', models.CharField(max_length=2, null=True)),
                ('ZIP_CODE', models.CharField(max_length=5, null=True)),
                ('FUNDING_STREAM', models.IntegerField(null=True)),
                ('DISPOSITION', models.IntegerField(null=True)),
                ('NEW_APPLICANT', models.IntegerField(null=True)),
                ('NBR_FAMILY_MEMBERS', models.IntegerField(null=True)),
                ('FAMILY_TYPE', models.IntegerField(null=True)),
                ('RECEIVES_SUB_HOUSING', models.IntegerField(null=True)),
                ('RECEIVES_MED_ASSISTANCE', models.IntegerField(null=True)),
                ('RECEIVES_FOOD_STAMPS', models.IntegerField(null=True)),
                ('AMT_FOOD_STAMP_ASSISTANCE', models.IntegerField(null=True)),
                ('RECEIVES_SUB_CC', models.IntegerField(null=True)),
                ('AMT_SUB_CC', models.IntegerField(null=True)),
                ('CHILD_SUPPORT_AMT', models.IntegerField(null=True)),
                ('FAMILY_CASH_RESOURCES', models.IntegerField(null=True)),
                ('CASH_AMOUNT', models.IntegerField(null=True)),
                ('NBR_MONTHS', models.IntegerField(null=True)),
                ('CC_AMOUNT', models.IntegerField(null=True)),
                ('CHILDREN_COVERED', models.IntegerField(null=True)),
                ('CC_NBR_MONTHS', models.IntegerField(null=True)),
                ('TRANSP_AMOUNT', models.IntegerField(null=True)),
                ('TRANSP_NBR_MONTHS', models.IntegerField(null=True)),
                ('TRANSITION_SERVICES_AMOUNT', models.IntegerField(null=True)),
                ('TRANSITION_NBR_MONTHS', models.IntegerField(null=True)),
                ('OTHER_AMOUNT', models.IntegerField(null=True)),
                ('OTHER_NBR_MONTHS', models.IntegerField(null=True)),
                ('SANC_REDUCTION_AMT', models.IntegerField(null=True)),
                ('WORK_REQ_SANCTION', models.IntegerField(null=True)),
                ('FAMILY_SANC_ADULT', models.IntegerField(null=True)),
                ('SANC_TEEN_PARENT', models.IntegerField(null=True)),
                ('NON_COOPERATION_CSE', models.IntegerField(null=True)),
                ('FAILURE_TO_COMPLY', models.IntegerField(null=True)),
                ('OTHER_SANCTION', models.IntegerField(null=True)),
                ('RECOUPMENT_PRIOR_OVRPMT', models.IntegerField(null=True)),
                ('OTHER_TOTAL_REDUCTIONS', models.IntegerField(null=True)),
                ('FAMILY_CAP', models.IntegerField(null=True)),
                ('REDUCTIONS_ON_RECEIPTS', models.IntegerField(null=True)),
                ('OTHER_NON_SANCTION', models.IntegerField(null=True)),
                ('WAIVER_EVAL_CONTROL_GRPS', models.IntegerField(null=True)),
                ('FAMILY_EXEMPT_TIME_LIMITS', models.IntegerField(null=True)),
                ('FAMILY_NEW_CHILD', models.IntegerField(null=True)),
                ('datafile', models.ForeignKey(blank=True, help_text='The parent file from which this record was created.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tribal_t1_parent', to='data_files.datafile')),
            ],
        ),
    ]