2#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
#  Copyright 2017 Daniel Cruz <bwb0de@bwb0dePC>
#  Estatística Version 0.1
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#



import re
import numpy as np

from scipy.stats import t
from collections import OrderedDict

from .cli_tools import show_dict_data

model_type_nparray = type(np.array([]))
model_type_list = type([])
model_type_tuple = type(())

# Defining input check decorators
def is_input_nparray(function):
	def wrapper(*args):
		for arg in args:
			if (type(arg) == model_type_list) or (type(arg) == model_type_tuple):
				return function(np.array(arg))
			elif type(arg) == model_type_nparray:
				return function(*args)
			else:
				print("Column iterator must by list, tuple or np.array...")
				return
	return wrapper


def check_simetry(coefficient_of_pearson):
	if coefficient_of_pearson == 0:
		return "Simetric"
	elif coefficient_of_pearson > 0:
		return "Assimetric positive"
	elif coefficient_of_pearson < 0:
		return "Assimetric negative"


def check_distribuition_curve_style(coefficient_of_curtose):
	if coefficient_of_curtose == 0.263:
		return "Mesocúrtica"
	elif coefficient_of_curtose > 0.263:
		return "Platicúrtica"
	elif coefficient_of_curtose < 0.263:
		return "Leptocúrtica"


@is_input_nparray
def column_description(column_iterator):
	'''Show basic information about a numeric column...'''
	output = OrderedDict()
	output['num:e'] = column_iterator.size
	output['sigma:e'] = calc_sum(column_iterator)
	output['sigma:e²'] = (column_iterator ** 2).sum()
	output['mean'] = calc_mean(column_iterator)
	output['median'] = get_median(column_iterator)
	output['mode'] = get_mode(column_iterator)
	output['Q1'] = calc_Q1(column_iterator)
	output['Q3'] = calc_Q3(column_iterator)
	output['P10'] = calc_P10(column_iterator)
	output['P90'] = calc_P90(column_iterator)
	output['minimum'] = get_min(column_iterator)
	output['maximum'] = get_max(column_iterator)
	output['range'] = get_range(column_iterator)
	output['standard_deviation'] = calc_standard_deviation(column_iterator)
	output['mean_deviation'] = calc_mean_deviation(column_iterator)
	output['variance'] = calc_variance(column_iterator)
	output['dispersion'] = show_dispersion(column_iterator)
	output['1º_desvio %'] = (output['dispersion']['1º_desvio']/output['num:e'])*100
	output['2º_desvio %'] = (output['dispersion']['2º_desvio']/output['num:e'])*100
	output['coefficient_of_variation'] = output['standard_deviation'] / output['mean']
	output['coefficient_of_pearson'] = (output['mean'] - output['mode']) / output['standard_deviation']
	output['coefficient_of_curtose'] = (output['Q3'] - output['Q1']) / (2 * (output['P90'] - output['P10']))
	output['symmetry_status'] = check_simetry(output['coefficient_of_pearson'])
	output['distribuition_curve_style'] = check_distribuition_curve_style(output['coefficient_of_curtose'])
	return show_dict_data(output)


@is_input_nparray
def calc_sum(column_iterator):
	return column_iterator.sum()

@is_input_nparray
def calc_Q1(column_iterator):
	return np.percentile(column_iterator,25)

@is_input_nparray
def calc_Q3(column_iterator):
	return np.percentile(column_iterator,75)

@is_input_nparray
def calc_P10(column_iterator):
	return np.percentile(column_iterator,10)

@is_input_nparray
def calc_P90(column_iterator):
	return np.percentile(column_iterator,90)

@is_input_nparray
def calc_variance(column_iterator):
	n = column_iterator.size
	return ( 1 / n ) * ((column_iterator ** 2).sum() - ((column_iterator.sum() ** 2) / n))

@is_input_nparray
def calc_standard_deviation(column_iterator):
	return calc_variance(column_iterator) ** 0.5

@is_input_nparray
def calc_column_deviation(column_iterator):
	return (column_iterator - column_iterator.mean())

@is_input_nparray
def calc_reduced_scores(column_iterator):
	return (column_iterator - column_iterator.mean()) / column_iterator.std()

@is_input_nparray
def calc_mean_deviation(column_iterator):
	a = calc_column_deviation(column_iterator)
	n = column_iterator.size
	sigma_values = 0
	for value in a:
		if value > 0:
			sigma_values += value
		else:
			sigma_values += value * (-1)

	return sigma_values / n


@is_input_nparray
def calc_mean(column_iterator):
	return column_iterator.mean()


@is_input_nparray
def get_mode(column_iterator):
	unique, counts = np.unique(column_iterator, return_counts=True)
	column_iterator_counts = dict(zip(unique, counts))
	mode_count = 0
	mode_list = []
	for key in column_iterator_counts:
		if column_iterator_counts[key] > mode_count:
			mode_count = column_iterator_counts[key]
			mode_list = [key]
		elif column_iterator_counts[key] == mode_count:
			mode_list.append(key)
	if len(mode_list) > 1:
		return mode_list
	else:
		return mode_list[0]


@is_input_nparray
def get_median(column_iterator):
	return np.median(column_iterator)

@is_input_nparray
def get_max(column_iterator):
	return column_iterator.max()

@is_input_nparray
def get_min(column_iterator):
	return column_iterator.min()

@is_input_nparray
def get_range(column_iterator):
	return get_max(column_iterator) - get_min(column_iterator)

@is_input_nparray
def show_dispersion(column_iterator):
	mean = column_iterator.mean()
	std = column_iterator.std()

	output = OrderedDict()
	output['1º_desvio'] = 0
	output['2º_desvio'] = 0
	output['3º_desvio'] = 0
	output['4º_desvio'] = 0
	for value in column_iterator:
		if (value <= mean + std) and (value >= mean - std):
			output['1º_desvio'] += 1
		elif ((value <= mean + (2*std)) and ( value > mean + (1*std))) or ((value < mean - (1*std)) and (value >= mean - (2*std))):
			output['2º_desvio'] += 1
		elif ((value <= mean + (3*std)) and ( value > mean + (2*std))) or ((value < mean - (2*std)) and (value >= mean - (3*std))):
			output['3º_desvio'] += 1
		elif ((value <= mean + (4*std)) and ( value > mean + (3*std))) or ((value < mean - (3*std)) and (value >= mean - (4*std))):
			output['4º_desvio'] += 1

	return output


def calc_combined_variance(set_A, set_B):
	a_A = np.array(set_A)
	a_B = np.array(set_B)
	n_A = a_A.size
	n_B = a_B.size
	return (((n_A*a_A.var() + n_B*a_B.var())/(n_A + n_B - 2))*((n_A + n_B)/(n_A * n_B)))**0.5
	

def calc_t(set_A, set_B, significance=0.05):
	combined_variance = calc_combined_variance(set_A, set_B)
	a_A = np.array(set_A)
	a_B = np.array(set_B)
	degree_of_freedom = a_A.size + a_B.size - 2
	critical_t = get_critical_t(degree_of_freedom, sig=significance)
	t = (a_A.mean() - a_B.mean()) / combined_variance

	if (t <= (critical_t*(-1))) or (t >= critical_t):
		significativo = True
	else:
		significativo = False

	if significativo:
		return "A diferença entre os grupos A e B é estatisticamente significativa (t={t}, t_crit={critical_t}, sig={significance})".format(t=t, critical_t=critical_t, significance=significance)

	return "Não há diferença significativa entre os grupos A e B (t={t}, t_crit={critical_t}, sig={significance})".format(t=t, critical_t=critical_t, significance=significance)


def get_critical_t(degree_of_freedom, sig=0.05):
	return t.ppf(1-(sig/2), df=degree_of_freedom)


def calc_covariance(column_A, column_B):
	a_A = np.array(column_A)
	a_B = np.array(column_B)
	n = len(a_A)
	if n != len(a_B):
		print('Size of columns are different... Must be equal...')
		exit()
	return (1/n) * ((a_A * a_B).sum() - ((a_A.sum() * a_B.sum()) / n))


def calc_pearsons_correlation(column_A, column_B):
	return (calc_covariance(column_A, column_B) / (column_description(column_A)['std'] * column_description(column_B)['std']))


def calc_coefficient_b_of_curve(column_A, column_B):
	return calc_pearsons_correlation(column_A, column_B) * ((column_description(column_B)['std'] / column_description(column_A)['std']) ** 0.5)


def show_linear_correlation_curve(column_A_mean, column_B_mean, coeficient_b_of_curve):
	c = column_B_mean - (coeficient_b_of_curve * column_A_mean)
	b = coeficient_b_of_curve
	output_str = "Y = {c} + {b}X".format(c=c,b=b)
	return output_str

