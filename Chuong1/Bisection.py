import math

def f(x):
    # Trả về giá trị của f(x) = x**3 - 2*x**2 - 2*x + 1
    return x**3 - 2*(x**2) - 2*x + 1

xa = 0  # Điểm bắt đầu của khoảng xét
xb = 1  # Điểm kết thúc của khoảng xét
saiso = 10  # Sai số ban đầu, lớn để bắt đầu vòng lặp
count = 0  # Đếm số lần lặp
nguongsaiso = 0.000000001 # Ngưỡng sai số 

while saiso > nguongsaiso:
    count += 1  # Tăng biến đếm mỗi lần lặp
    print('Buoc lap' , count)  

    # Tính nghiệm tại điểm chia đôi khoảng [xa, xb]
    x_interval = (xa + xb) / 2
    f_x_interval = f(x_interval)  # Tính giá trị của f tại x_interval

    # Tính f(x) tại xa và xb
    f_xa = f(xa)
    f_xb = f(xb)

    # Xác định nửa khoảng chứa nghiệm
    if f_x_interval * f_xa < 0:    
        xb = x_interval  #nghiệm nằm giữa xa và x_interval
    elif f_x_interval * f_xb < 0:
        xa = x_interval  #nghiệm nằm giữa x_interval và xb

    # Tính sai số dựa trên độ chênh lệch giữa xa và xb
    saiso = abs(xb - xa) / 2**count

    print('Sai so:', saiso)
    print('Nghiem xap xi:', x_interval)

# In ra nghiệm cuối cùng sau khi vòng lặp kết thúc
print('Nghiem cuoi cung:', x_interval)