# Generated by Django 5.1.1 on 2024-11-02 16:24

import datetime
import django.core.validators
import django.db.models.deletion
import uuid
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('produtos', '0002_servico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orcamento',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('validade', models.DateField(default=datetime.date(2024, 11, 18), verbose_name='Validade')),
                ('status', models.CharField(choices=[('NAO ENVIADO', 'NÃO ENVIADO'), ('EM ANALISE', 'EM ANALISE'), ('APROVADO', 'APROVADO'), ('CANCELADO', 'CANCELADO'), ('NAO APROVADO', 'NÃO APROVADO')], default='NAO ENVIADO', max_length=50, verbose_name='Situação')),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Total')),
                ('total_equipamentos', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Total Equipamentos')),
                ('total_servicos', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Total Mão de Obra')),
                ('total_lucro', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Total Lucro')),
                ('total_compra', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Total Compra')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orcamento_cliente', to='clientes.cliente', verbose_name='Cliente')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ItemServico',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('valor', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=16, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Preço')),
                ('quantidade', models.PositiveIntegerField(default=1, verbose_name='Quantidade')),
                ('total', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=16, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Total')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_servico', to='produtos.servico', verbose_name='Serviço')),
                ('orcamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mao_obra_orcamento', to='orcamentos.orcamento', verbose_name='Orçamento')),
            ],
            options={
                'verbose_name': 'Item Serviço',
                'verbose_name_plural': 'Itens Serviços',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='ItemProduto',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('acrescimo', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=16, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Acréscimo em Porcentagem')),
                ('preco', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=16, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Preço de Compra')),
                ('total', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=16, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Total')),
                ('quantidade', models.PositiveIntegerField(default=1, verbose_name='Quantidade')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_produto', to='produtos.produto', verbose_name='Produto')),
                ('orcamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produto_orcamento', to='orcamentos.orcamento', verbose_name='Orcamento')),
            ],
            options={
                'verbose_name': 'Item Produto',
                'verbose_name_plural': 'itens Produtos',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='InformacoesOrcamento',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('titulo', models.CharField(max_length=200, verbose_name='Descrição')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('orcamento', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='orcamentos.orcamento', verbose_name='Descricao')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]