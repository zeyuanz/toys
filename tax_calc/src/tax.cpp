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
#include <iostream>

double find_idx_from_tax_range(double num) {
	for (int i = 0; i < 6; i++) {
		if (num <= TAX_RANGE[i]) {
			return i;
		}
	}
	return 6;
}

double compute_tax_monthly(double income_month, int month, double prev_tax, double additional_tax_exempt, double reward_income) {
	double total_income = income_month * (1 - INSURANCE_FUNT_RATE) * month - HEALTH_INSURANCE_ADV + reward_income;
	double tax_amount = total_income - (EXEMPTION_PER_MONTH+additional_tax_exempt) * month;
	if (tax_amount <= 0) {
		return 0;
	}
	int idx = find_idx_from_tax_range(tax_amount);
	return tax_amount * TAX_RATE[idx] - TAX_NUMBER[idx] - prev_tax;
}

double compute_tax_reward(double prev_income, double reward, double prev_tax) {
	double total_income = prev_income + reward;	
	int idx = find_idx_from_tax_range(total_income);
	return total_income * TAX_RATE[idx] - TAX_NUMBER[idx] - prev_tax;
}
void print_usage() {
	printf("Usage: ./tax [month_income] [reward] [additional_tax_exempt]\n");
	printf("\tmonth_income\t\t--<DOUBLE>\tmonthly incomee\n");
	printf("\treward\t\t--<DOUBLE>\tone-time reward, it will be calcuated at the beginning the year\n");
	printf("\tadditional_tax_exempt\t--<DOUBLE>\t\tadditional tax exempt amount per month\n");
	printf("Options\n");
	printf("\t-h\t\t\t\tprint this message\n");
}
