class Poly:

    def __init__(self, **terms):
        self.terms_dict = {}
        for key, value in terms.items():
            exponent = int(key.replace('x', ''))
            self.terms_dict[exponent] = value
        self.degree = max(self.terms_dict.keys()) if self.terms_dict else 0

    def __str__(self):
        if not self.terms_dict:
            return "0"
        components = []
        for power in sorted(self.terms_dict.keys(), reverse=True):
            coeff = self.terms_dict[power]
            if coeff == 0:
                continue
            if power == 0:
                components.append(f"{coeff}")
            elif power == 1:
                components.append(f"{coeff}x")
            else:
                components.append(f"{coeff}x^{power}")
        return " + ".join(components) if components else "0"

    def __add__(self, another):
        result = {}
        powers = set(self.terms_dict.keys()).union(another.terms_dict.keys())
        for power in powers:
            result[f"x{power}"] = self.terms_dict.get(power, 0) + another.terms_dict.get(power, 0)
        return Poly(**result)


poly1 = Poly(x2=3, x1=2, x0=1)
poly2 = Poly(x1=5, x0=1)

print("First Polynomial:", poly1)
print("Second Polynomial:", poly2)

poly_sum = poly1 + poly2
print("Sum:", poly_sum)
