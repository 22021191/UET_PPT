import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    # Định nghĩa hàm f(t, y) = dy/dt
    return 1+(t-y)**2

def runge_kutta_4(f, t0, y0, t_end, h):
    """
    Giải phương trình vi phân sử dụng phương pháp Runge-Kutta bậc 4.
    
    :param f: Hàm f(t, y) = dy/dt
    :param t0: Thời điểm bắt đầu
    :param y0: Giá trị ban đầu của y tại t0
    :param t_end: Thời điểm kết thúc
    :param h: Bước nhảy
    :return: Các giá trị t và y
    """
    t_values = [t0]
    y_values = [y0]

    t = t0
    y = y0

    while t < t_end:
        k1 = h * f(t, y)
        k2 = h * f(t + h / 2, y + k1 / 2)
        k3 = h * f(t + h / 2, y + k2 / 2)
        k4 = h * f(t + h, y + k3)
        y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t = t + h

        t_values.append(t)
        y_values.append(y)

    return np.array(t_values), np.array(y_values)

def main():
    t0 = 2.0
    y0 = 1.0
    t_end = 3.0
    h = 0.1
    
    t_values, y_values = runge_kutta_4(f, t0, y0, t_end, h)

    plt.plot(t_values, y_values, 'o-', label='Runge-Kutta 4th Order')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('Solving ODE using Runge-Kutta 4th Order Method')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
