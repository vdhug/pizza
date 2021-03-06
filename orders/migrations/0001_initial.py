# Generated by Django 2.0.3 on 2018-12-22 21:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dinner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='ItemOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='')),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date_submitted', models.DateField(auto_now_add=True)),
                ('date_delivered', models.DateField(blank=True, null=True)),
                ('status_order', models.CharField(choices=[('SUBMITTED', 'Submitted'), ('PRODUCTION', 'In Production'), ('DELIVERING', 'Left to Deliver'), ('DELIVERED', 'Delivered'), ('CANCELLED', 'Cancelled')], default='SUBMITTED', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(default='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(default='')),
                ('custom', models.BooleanField(default=False)),
                ('numberOfToppings', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PriceOfDinner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('dinner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices_of_dinner', to='orders.Dinner')),
            ],
        ),
        migrations.CreateModel(
            name='PriceOfPizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices_of_pizza', to='orders.Pizza')),
            ],
        ),
        migrations.CreateModel(
            name='PriceOfSub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Salad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(default='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='SizeOfPizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=128)),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sizeOfPizzas', to='orders.Size')),
            ],
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('prices', models.ManyToManyField(through='orders.PriceOfSub', to='orders.Size')),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfPizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='sizeofpizza',
            name='typeOfPizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.TypeOfPizza'),
        ),
        migrations.AddField(
            model_name='priceofsub',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Size'),
        ),
        migrations.AddField(
            model_name='priceofsub',
            name='sub',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices_of_sub', to='orders.Sub'),
        ),
        migrations.AddField(
            model_name='priceofpizza',
            name='sizeOfPizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.SizeOfPizza'),
        ),
        migrations.AddField(
            model_name='priceofdinner',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Size'),
        ),
        migrations.AddField(
            model_name='pizza',
            name='prices',
            field=models.ManyToManyField(through='orders.PriceOfPizza', to='orders.SizeOfPizza'),
        ),
        migrations.AddField(
            model_name='itemorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.Order'),
        ),
        migrations.AddField(
            model_name='dinner',
            name='prices',
            field=models.ManyToManyField(through='orders.PriceOfDinner', to='orders.Size'),
        ),
    ]
