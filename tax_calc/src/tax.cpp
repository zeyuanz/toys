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

double compute_tax_monthly(double income_month, int month) {
	double total_income = income_month * month;
	double total_exemption = EXEMPTION_PER_MONTH * month;
	double tax;
	return tax;
}
