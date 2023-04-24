import math
from scipy.integrate import quad

T = 100
CPA_T = 4.171 + 14.450 * (math.pow(10, -3)) * T + 0.267 * (math.pow(10, -6))*(T * T) - 1.722 * (math.pow(10, -9))*(T * T * T)
CPE_T = 5.152 + 15.224 * (math.pow(10, -3)) * T - 9.681 * (math.pow(10, -6))*(T * T) + 2.313 * (math.pow(10, -9))*(T * T * T)
CPF_T = 6.342 +  1.836 * (math.pow(10, -3)) * T - 0.2801* (math.pow(10, -6))*(T * T)
CPH_T = 6.947 - 0.2    * (math.pow(10, -3)) * T + 0.4808* (math.pow(10, -6))*(T * T)
CPW_T = 7.219 + 2.374  * (math.pow(10, -3)) * T + 0.267 * (math.pow(10, -6))*(T * T)
CPN2_T= 6.449 + 1.413  * (math.pow(10, -3)) * T - 0.0807* (math.pow(10, -6))*(T * T)

DELCP1_T = CPF_T + 3 * CPH_T - CPA_T - CPA_T - CPW_T
DELCP2_T = CPE_T + CPH_T - CPF_T - CPW_T

DELHR10 = 49270
DELHR20 = -9830
DELGR10 = 33980
DELGR20 = -6810
DELSR10 = 51.26
DELSR10 = -10.07

# calculate and plot the gibbs free energy chnage and equillibrium constants as a function of T
def integrand1(DELCP1_T):
    return DELCP1_T
ans,err = quad(integrand1,T,298.15)
DELHR1_T = DELHR10 + ans


def integrand2(DELCP2_T):
    return DELCP2_T
ans,err = quad(integrand2,T,298.15)
DELHR2_T = DELHR20 + ans
                              





#DELHR2_T = DELHR20