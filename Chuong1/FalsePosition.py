import math

def false_position(f, p0, p1, tol, max_iters):
    """
    Tìm một giải pháp xấp xỉ cho f(x) = 0 trên khoảng [p0, p1] sử dụng phương pháp vị trí sai.

    Đầu vào:
        f (hàm): Hàm liên tục mà chúng ta muốn tìm nghiệm.
        p0 (float): Một đầu mút của khoảng mà f(p0) và f(p1) có dấu đối nhau.
        p1 (float): Đầu mút kia của khoảng.
        tol (float): Sai số mong muốn cho nghiệm.
        max_iters (int): Số vòng lặp tối đa.

    Đầu ra:
        float: Nghiệm xấp xỉ nếu thành công, hoặc None nếu phương pháp thất bại.
    """
    i = 2
    q0 = f(p0)
    q1 = f(p1)

    for n in range(max_iters):
        p = p1 - q1 * (p1 - p0) / (q1 - q0)  # Tính p_i

        if abs(p - p1) < tol:
            return p  # Quá trình thành công

        i += 1
        q = f(p)

        if q * q1 < 0:
            p0 = p1
            q0 = q1
        p1 = p
        q1 = q

    print(f"Phương pháp thất bại sau {max_iters} vòng lặp.")
    return None  # Quá trình thất bại

def f(x):
    return x**3 - x**2 + 2

solution = false_position(f, 0, 2, 1e-6, 100)
if solution is not None:
    print(f"Nghiệm xấp xỉ: {solution}")
else:
    print("Phương pháp không hội tụ.")