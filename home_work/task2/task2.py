import scipy.integrate as spi
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x ** 2 - x + 2


def view_spi_integral(f, a=0, b=2):
    return spi.quad(f, a, b)


def main(a, b):

    x = np.linspace(a-1, b+1, 400)
    y = f(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([-2, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = x^2 - x + 2 від ' +
                 str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()


def monte_carlo_integration(f, a, b, n=15000):
    x = np.random.uniform(a, b, n)
    y = f(x)
    return (b - a) * np.mean(y)


if __name__ == "__main__":

    a = -2
    b = 4
    n = 100000
    result_m_c = monte_carlo_integration(f, a, b, n)

    result = view_spi_integral(f, a, b)

    print("\n|---------------------|---------------------|")
    print("|      Метод          |      Результат      |")
    print("|---------------------|---------------------|")
    print(
        f"| Інтеграл за SPI     | {result[0]:<20}|")
    print("|---------------------|---------------------|")
    print(
        f"| Інтеграл за MC      | {result_m_c:<2}  |")
    print("|---------------------|---------------------|\n")

    main(a, b)
