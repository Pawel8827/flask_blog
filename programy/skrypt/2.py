def policz_wyplate(podstawa, policz_premie):
    return podstawa + policz_premie(podstawa)


def zwroc_zero(podstawa):
    return 0

def policz_premie_menagera(podstawa):
    return 0.5 * podstawa

print(policz_wyplate(1000, zwroc_zero))
print(policz_wyplate(2000, policz_premie_menagera))