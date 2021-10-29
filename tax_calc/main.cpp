/*
 * =====================================================================================
 *
 *       Filename:  main.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  10/28/2021 17:25:31
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */
#include "include/tax.h"
#include <iostream>
#include <string>
using namespace std;

int main(int argc, char** argv) {
	double monthly_income = stod(argv[1]);	
	double reward = stod(argv[2]);	
	double prev_tax = 0.0;
	double total_income = 0.0;

	for (int month = 1; month < 13; month++) {
		double tax = compute_tax_monthly(monthly_income, month, prev_tax);
		prev_tax += tax;
		total_income += monthly_income-tax-monthly_income * INSURANCE_FUNT_RATE;
		printf("[Month %d]: tax: %2.f\tincome: %.2f\n", month, tax, monthly_income-tax-monthly_income * INSURANCE_FUNT_RATE);
	}

	double reward_tax = compute_tax_reward(total_income, reward, prev_tax);
	printf("[Reward]: tax: %2.f\tincome: %.2f\n",  reward_tax, reward-reward_tax);
	printf("[Total income]: %.2f\t[Total tax]: %.2f\n", total_income+reward-reward_tax, prev_tax+reward_tax);
	return 0;
}
