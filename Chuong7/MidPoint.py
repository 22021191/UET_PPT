import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    # Định nghĩa hàm f(t, y) = dy/dt
    return 1+(t-y)**2

def midpoint_method(f, t0, y0, t_end, h):
    """
    Giải phương trình vi phân sử dụng phương pháp điểm giữa.
    
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
        # Tính giá trị trung gian
        k1 = f(t, y)
        y_mid = y + (h/2) * k1
        t_mid = t + h/2
        
        # Sử dụng giá trị trung gian để tính giá trị y tiếp theo
        k2 = f(t_mid, y_mid)
        y_next = y + h * k2

        t += h
        y = y_next

        t_values.append(t)
        y_values.append(y)
        print(f"x: {t:.2f}, y: {y:.4f}")

    return np.array(t_values), np.array(y_values)

def main():
    t0 = 2.0
    y0 = 1.0
    t_end = 3.0
    h = 0.5
    
    t_values, y_values = midpoint_method(f, t0, y0, t_end, h)

    plt.plot(t_values, y_values, 'o-', label='Midpoint Method')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('Solving ODE using Midpoint Method')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
