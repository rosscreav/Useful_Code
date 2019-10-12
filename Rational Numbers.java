
//Note: This solution was written on an old version of Exercism. The tests below might not correspond to the solution code, and the exercise may have changed since this code was written.
import java.util.stream.IntStream;

class Rational {

	private static final Double DOUBLE_PRECISION = 0.000001;

	private int numerator;
	private int denominator;

	Rational(final int numerator, final int denominator) {
		this.numerator = numerator;
		this.denominator = denominator;

		clean();
	}

	int getNumerator() {
		return this.numerator;
	}

	int getDenominator() {
		return this.denominator;
	}

	public Rational add(final Rational r) {
		final Rational sum = new Rational((this.numerator * r.denominator) + (r.numerator * this.denominator),
				this.denominator * r.denominator);
		sum.clean();

		return sum;
	}

	public Rational subtract(final Rational r) {
		final Rational diff = new Rational((this.numerator * r.denominator) - (r.numerator * this.denominator),
				this.denominator * r.denominator);
		diff.clean();

		return diff;
	}

	public Rational multiply(final Rational r) {
		final Rational product = new Rational(this.numerator * r.numerator, this.denominator * r.denominator);
		product.clean();

		return product;
	}

	public Rational divide(final Rational r) {
		final Rational quotient = new Rational(this.numerator * r.denominator, this.denominator * r.numerator);
		quotient.clean();

		return quotient;
	}

	public Rational abs() {
		return new Rational(Math.abs(this.numerator), Math.abs(this.denominator));
	}

	public Rational pow(final int exponent) {
		final Rational result = (exponent >= 0) ? withPositiveExponent(exponent) : withNegativeExponent(exponent);
		result.clean();

		return result;
	}

	private Rational withPositiveExponent(final int exponent) {
		return new Rational(pow(this.numerator, exponent), pow(this.denominator, exponent));
	}

	private Rational withNegativeExponent(final int exponent) {
		return new Rational(pow(this.numerator, Math.abs(exponent)), pow(this.denominator, Math.abs(exponent)));
	}

	private int pow(final int number, final int exponent) {
		return Double.valueOf(Math.pow(number, exponent)).intValue();
	}

	public double exp(final double exponent) {
		final double root = Math.pow(exponent, this.numerator);
		double exp = Math.pow(root, 1. / this.denominator);
		exp = (Math.abs((Math.round(exp) - exp)) < DOUBLE_PRECISION) ? Math.round(exp) : exp;

		return exp;
	}

	private void clean() {
		final int greatestCommonDivider = getGreatestCommonDivider(this.numerator, this.denominator);
		this.numerator = this.numerator / greatestCommonDivider;
		this.denominator = this.denominator / greatestCommonDivider;

		if (this.denominator < 0) {
			this.numerator *= -1;
			this.denominator *= -1;
		}
	}

	private int getGreatestCommonDivider(final int a, final int b) {
		if (b > a) {
			return getGreatestCommonDivider(b, a);
		}

		return IntStream.rangeClosed(1, a).filter(n -> (a % n) == 0).filter(n -> (b % n) == 0).max().orElse(1);
	}

	@Override
	public String toString() {
		return String.format("%d/%d", this.getNumerator(), this.getDenominator());
	}

	@Override
	public boolean equals(final Object obj) {
		if (obj == null || !this.getClass().isAssignableFrom(obj.getClass())) {
			return false;
		}

		final Rational other = (Rational) obj;
		return this.getNumerator() == other.getNumerator() && this.getDenominator() == other.getDenominator();
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + this.getNumerator();
		result = prime * result + this.getDenominator();

		return result;
	}

}
