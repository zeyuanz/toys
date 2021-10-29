/*
 * =====================================================================================
 *
 *       Filename:  tax.h
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  10/29/2021 11:20:53
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */
const double EXEMPTION_PER_MONTH = 5000.0;
const double INSURANCE_FUNT_RATE = 0.225;
const double TAX_RANGE[6] = {36000,144000,300000,420000,660000,960000};
const double TAX_RATE[7] = {0.03,0.1,0.2,0.25,0.3,0.35,0.45};
const double TAX_NUMBER[7] = {0,2520,16920,31920,52920,85920,181920};


double compute_tax_monthly(double, int);
