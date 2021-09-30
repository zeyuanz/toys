/*
 * =====================================================================================
 *
 *       Filename:  rate.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  09/27/2021 14:08:19
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */
#include <iostream>
#include <cmath>
#include <string>

double compute_money(double, double, int, int);
void print_usage();
using namespace std;

int main(int argc, char** argv) {
	if (argc != 5 || string(argv[1]) == "-h") {
		print_usage();
		return 0;
	}
	double money = atof(argv[1]);
	double rate = atof(argv[2]);
	int accu_year = atoi(argv[3]);
	int total_year = atoi(argv[4]);
	if (accu_year > total_year) {
		cout << "accu_year should be greater than the total_year\n";
		exit(1);
	}
	double reward = compute_money(money, rate, accu_year, total_year);
	printf("Money: %.2f\n", money);
	printf("Rate: %.4f\n", rate);
	printf("Accu year: %d\n", accu_year);
	printf("Total year: %d\n", total_year);
	cout << "Reward is: " << reward << endl;
	return 0;
}

void print_usage() {
	printf("Usage: ./rate [money] [rate] [accu_year] [total_year]\n");
	printf("\tmoney\t\t--<DOUBLE>\tamount of money accumulated each year\n");
	printf("\trate\t\t--<DOUBLE>\trate of interest for your money\n");
	printf("\taccu_year\t--<INT>\t\tthe number of years you need to save your money\n");
	printf("\ttotal_year\t--<INT>\t\tthe total number of years you want to compute\n");
	printf("Options\n");
	printf("\t-h\t\t\t\tprint this message\n");
}
double compute_money(double money, double rate, int accu_year, int total_year) {
	double reward = 0.0;
	for (int i = 0; i < accu_year; i++) {
		reward += money * pow(1.0+rate, double(i));
	}
	return reward * pow(1.0+rate, double(total_year-accu_year));
}
