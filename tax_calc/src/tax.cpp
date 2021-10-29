/*
 * =====================================================================================
 *
 *       Filename:  tax.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  10/28/2021 17:29:58
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */
#include "../include/tax.h"

double find_idx_from_tax_range(double num) {
	for (int i = 0; i < 6; i++) {
		if (num <= TAX_RANGE[i]) {
			return i;
		}
	}
	return 6;
}

double compute_tax_monthly(double income_month, int month, double prev_tax) {
	double total_income = income_month * (1 - INSURANCE_FUNT_RATE) * month;
	double tax_amount = total_income - TOTAL_EXEMPTION;
	if (tax_amount <= 0) {
		return 0;
	}
	int idx = find_idx_from_tax_range(tax_amount);
	return tax_amount * TAX_RATE[idx] - TAX_NUMBER[idx] - prev_tax;
}

double compute_tax_reward(double prev_income, double reward, double prev_tax) {
	double total_income = prev_income + reward;	
	int idx = find_idx_from_tax_range(total_income);
	return reward * TAX_RATE[idx];
}
