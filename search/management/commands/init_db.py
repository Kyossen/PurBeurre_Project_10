#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This import is obligatory for the good of the system
Lib imports, they are important to help Django a have all tools for a good use
Imports of files, they are important for
this view file because it gives access to forms and templates
Imports of Django lib, is a base for well functioning"""

# Import lib
import requests

# Import file & Django
from search.models import Categories, Product
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """This class use a one method only for the imports in the database.
    This imports are the imports of the products and categories
    such category name or product name"""
    help = "Command to initialize the database"

    def handle(self, *args, **options):
        a = 0
        new_categories_1 = Categories(name="Petit déjeuné",
                                      url="https://world.openfoodfacts.org/"
                                          "category/fr:petit-dejeune")
        new_categories_2 = Categories(name='Pâtes à tartiner',
                                      url="https://world.openfoodfacts.org/"
                                          "category/"
                                          "fr:P%C3%A2tes%20%C3%A0%20tartiner")
        new_categories_3 = Categories(name='Produits origine Végetal',
                                      url="https://world.openfoodfacts.org/"
                                          "category/fr:origine-vegetal")
        new_categories_1.save()
        new_categories_2.save()
        new_categories_3.save()

        while a < 1:
            all_Categories = Categories.objects.all()
            for save_products in all_Categories:
                id_s = requests.get(
                    "https://world.openfoodfacts.org/api/v0/product/"
                    + '3017620422003' + ".json")
                id_r = id_s.json()
                if 'product' in id_r:
                    save = id_r['product']
                    if 'product_name' not in save:
                        save['product_name'] = ''
                    if 'nutrition_grades' not in save:
                        save['nutrition_grades'] = ''
                    if 'image_url' not in save:
                        save['image_url'] = ''
                    if 'ingredients_text_fr' in save:
                        save['ingredients_text_fr'] = \
                            save['ingredients_text_fr']
                    if 'ingredients_text_fr' not in save:
                        save['ingredients_text_fr'] = ''

                    if save['id'] not in all_Categories:
                        Categories_id = \
                            Categories.objects.get(pk=save_products.pk)

                        url = "https://fr.openfoodfacts.org/" \
                              "product/" + save['id'] + "/" + \
                              save['product_name']

                        a += 1
                        new_products = Product(
                            name=save['product_name'],
                            image_url=save['image_url'],
                            code=save['id'],
                            nutrition_grade=save['nutrition_grades'],
                            ingredients=save['ingredients_text_fr'],
                            url=url,
                            categories=Categories_id)
                        new_products.save()
