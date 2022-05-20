#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2
	
	taux_taxes = (15/100)
	sous_total = 0

	for elem in data:
			sous_total += elem[INDEX_QUANTITY] * elem[INDEX_PRICE]

	taxes = (sous_total * (taux_taxes))
	montant_total = sous_total + taxes
	
	facture = [name, ("SOUS-TOTAL", "%.2f" % sous_total), ("TAXES", "%.2f" % taxes), ("TOTAL", "%.2f" % montant_total)]

	return facture


def format_number(number, num_decimal_digits):
	return ""

def get_triangle(num_rows):
	return ""


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
