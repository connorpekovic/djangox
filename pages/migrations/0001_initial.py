# Generated by Django 3.1.13 on 2021-09-30 21:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Stregthen_social_safety_nets', models.TextField(choices=[('Yes', 'Yes. Enact UBI (Universal Basic Income).'), ('Same', 'No. Spending levels as is'), ('Reduce', 'Negatory. Slowly stop funding Social Security')])),
                ('Nationalize_healthcare', models.TextField(choices=[('Yes', 'Yes. Nationalize it like the NHS in England.'), ('No', 'No. Leave it as is.')])),
                ('Climate_responce', models.TextField(choices=[('Strong', 'Take extraordinary measures. Enact enforceable laws.'), ('Senseable', "Take oridnary meaures, don't tread on my consumption."), ('Capitalist', 'Take no meaures.')])),
                ('Should_we_limit_urban_sprall', models.TextField(choices=[('Yes', 'Yes. Promote city living.'), ('No', "No. Don't tread on me.")])),
                ('Do_you_support_or_oppose_globalization', models.TextField(choices=[('Yes', 'Yes. Globalization increases the quality of life and brings rich cultures together.'), ('No', 'No. We need to focus on issued at home. Things will work out better in the end.')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
