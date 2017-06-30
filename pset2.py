# Problem 1


def credit_card_balance(balance, annualInterestRate, monthlyPaymentRate):
    """Write a program to calculate the credit card balance after one year if a
    person only pays the minimum monthly payment required by the credit card
    company each month.
    """

    year = 12
    previous_balance = balance

    for month in range(1, year + 1):

        minimum_monthly_payment = monthlyPaymentRate * previous_balance
        monthly_unpaid_balance = previous_balance - minimum_monthly_payment
        monthly_interest_rate = ((annualInterestRate/12.0) * monthly_unpaid_balance)
        previous_balance = monthly_unpaid_balance + monthly_interest_rate

    return (" Remaining balance: " + str(round(previous_balance, 2)))

print (credit_card_balance(balance, annualInterestRate, monthlyPaymentRate))

# Problem 2


def fixed_payment(balance, annualInterestRate):
    """Now write a program that calculates the minimum fixed monthly payment
    needed in order pay off a credit card balance within 12 months. By a fixed
    monthly payment, we mean a single number which does not change each month,
    but instead is a constant amount that will be paid each month.

    In this problem, we will not be dealing with a minimum monthly payment rate.
    """

    monthlyInterestRate = (annualInterestRate/12)
    updatedBalance = balance
    monthlyPayment = 0

    while updatedBalance > 0:

        updatedBalance = balance
        monthlyPayment += 10

        for month in range(12):

            updatedBalance -= monthlyPayment
            updatedBalance += (monthlyInterestRate * updatedBalance)
            month += 1

    return ("Lowest Payment: " + str(monthlyPayment))

print (fixed_payment(balance, annualInterestRate))

# Problem 3


def bisection_fixed_payment(balance, annualInterestRate):
    """You'll notice that in Problem 2, your monthly payment had to be a multiple
    of $10. Why did we make it that way? You can try running your code locally so
    that the payment can be any dollar and cent amount (in other words, the
    monthly payment is a multiple of $0.01). Does your code still work? It should,
    but you may notice that your code runs more slowly, especially in cases with
    very large balances and interest rates. (Note: when your code is running on
    our servers, there are limits on the amount of computing time each submission
    is allowed, so your observations from running this experiment on the grading
    system might be limited to an error message complaining about too much time
    taken.)

    Well then, how can we calculate a more accurate fixed monthly payment than we
    did in Problem 2 without running into the problem of slow code? We can make
    this program run faster using a technique introduced in lecture - bisection
    search!
    """

    monthlyInterestRate = annualInterestRate / 12.0
    startbalance = balance
    step = 0.01
    lowbound = startbalance / 12.0
    highbound = (startbalance * (1 + monthlyInterestRate)**12) / 12.0
    monthlyPayment = (lowbound + highbound) / 2.0

    while (abs(startbalance)) >= step:
        startbalance = balance
        for month in range(0, 12):
            startbalance -= monthlyPayment
            startbalance = startbalance + ((monthlyInterestRate) * startbalance)

        if startbalance < 0:
            highbound = monthlyPayment
        if startbalance > 0:
            lowbound = monthlyPayment
        monthlyPayment = (lowbound + highbound) / 2.0

    return ('Lowest Payment: ', round(monthlyPayment, 2))

print (bisection_fixed_payment(balance, annualInterestRate))
