# pizza_counting
## Bước 1: Clone repository về máy. Sau đó chuyển con trỏ chỉ mục vào thư mục vừa clone về
```cd pizza_counting``` \

## Bước 2: Tải các video cần xử lý về máy

## Bước 3: Khởi chạy môi trường ảo bằng các câu lệnh sau
```python -m venv venv-pizza-counting``` \
```.\venv-pizza-counting\Scripts\Activate.ps1``` \

## Bước 4: Tải và cài đặt các gói cần thiết
```pip install -r requirements.txt```

## Bước 5: Chạy mô hình
```python main.py``` \
Kết quả của mô hình nằm ở đường dẫn ./pizza_counting_output.avi. \
Trong đó pizza đếm được nằm ở góc trên bên phải của màn hình hiển thị.\
Nếu muốn xem kết quả chạy trên các video còn lại thì vào file main.py, kéo đến dòng cuối cùng, thay đổi biến \
index=0 \
, index chạy từ 0-5, đại diện cho 6 video cần xử lý. \
