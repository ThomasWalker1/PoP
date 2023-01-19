from numbers import Number


class Polynomial:
    def __init__(self, coefs):

        self.coefficients = coefs

    def degree(self):

        return len(self.coefficients) - 1

    def __str__(self):

        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1]==1 else coefs[1]}x")

        terms += [f"{''if c==1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]
        return " + ".join(reversed(terms)) or "0"

    def __eq__(self, other):

        return self.coefficients == other.coefficients

    def __add__(self, other):
        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1

            coefs = tuple(a + b for a, b in zip(
                                            self.coefficients,
                                            other.coefficients
                                            ))
            coefs += self.coefficients[common:] + other.coefficients[common:]
            return Polynomial(coefs)
        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0]+other,)
                             + self.coefficients[1:]) # noqa E128
        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            neg_other = Polynomial(tuple(
                        -1*coef for coef in other.coefficients))
            return self + neg_other
        elif isinstance(other, Number):
            neg_other = -1*other
            return self + neg_other
        else:
            return NotImplemented

    def __rsub__(self, other):
        neg_Poly = Polynomial(tuple(-1*coef for coef in self.coefficients))
        return other + neg_Poly

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            end_poly = Polynomial((0,))
            for n, coef in enumerate(self.coefficients):
                end_poly += Polynomial(tuple(0 for i in range(n))
                         + tuple(coef*coef_2 for coef_2 in other.coefficients)) # noqa E128
            return end_poly
        elif isinstance(other, Number):
            return Polynomial(tuple(other*coef for coef in self.coefficients))
        else:
            return NotImplemented
