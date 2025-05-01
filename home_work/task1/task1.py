import pulp


def maximize_model():

    model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

    lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")
    fruit_juice = pulp.LpVariable("Fruit Juice", lowBound=0, cat="Integer")

    model += lemonade + fruit_juice, "Total Production"

    model += 2 * lemonade + 1 * fruit_juice <= 100, "Water"
    model += 1 * lemonade <= 50, "Sugar"
    model += 1 * lemonade <= 30, "Lemon Juice"
    model += 2 * fruit_juice <= 40, "Fruit Puree"

    model.solve()

    return model, lemonade, fruit_juice


if __name__ == "__main__":

    model, lemonade, fruit_juice = maximize_model()

    print("Status:", pulp.LpStatus[model.status])
    print("Optimal value of Lemonade:", lemonade.varValue)
    print("Optimal value of Fruit Juice:", fruit_juice.varValue)
    print("Total Production:", pulp.value(model.objective))
