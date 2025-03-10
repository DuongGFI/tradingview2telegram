## 📋 Yêu cầu hệ thống
- Tài khoản TradingView
- Tài khoản Telegram -> Tạo chatbot
- Tài khoản Render.com

## 🚀 Triển khai trên Render.com
1. **Kết nối repository GitHub**
- Tạo Web Service mới trên Render
- Chọn repo chứa mã nguồn FastAPI
- Cấu hình branch cần deploy (khuyến nghị `main`)

2. **Thiết lập cấu hình**
```bash
Build Command: pip install -r requirements.txt
Start Command: uvicorn main:app --host 0.0.0.0 --port 10000
```

3. **Thêm biến môi trường**
```env
TOKEN = "API_TOKEN_BOT_TELEGRAM"
chat_id = "ID_CHAT_TELEGRAM"
```

## 🔧 Cấu hình TradingView Alert
1. **Tạo Alert chính cho tín hiệu giao dịch**
- Trên biểu đồ TradingView: Nhấn nút **Tạo cảnh báo**
- Thiết lập điều kiện kích hoạt
- Trong mục **Thông báo**:
  ```
  Webhook URL: https://[tên-dịch-vụ].onrender.com/telegram
  Message: {"mes": "{{ticker}} - {{close}} - Tín hiệu mua"}
  ```

2. **Tạo Alert ping định kỳ**
- Tạo alert mới với điều kiện luôn đúng:
  ```pine
  security("m5", close) // Điều kiện luôn true
  ```
- Cấu hình thông báo:
  ```
  Webhook URL: https://[tên-dịch-vụ].onrender.com/telegram
  Message: {"mes": "PING - {{ticker}} - {{time}}"}
  ```
- Thiết lập tần suất: `Cứ sau 1 phút` 

## ⚙️ Kiểm tra hoạt động
**Test endpoint bằng lệnh curl:**
```bash
curl -X POST "https://[tên-dịch-vụ].onrender.com/telegram" \
-H "Content-Type: application/json" \
-d '{"mes": "Test signal"}'
```

## 📌 Lưu ý quan trọng
1. **Bảo mật thông tin**:
- Luôn bật 2FA trên TradingView[5][6]
- Không chia sẻ webhook URL công khai

2. **Tối ưu hoá Alert**:
```json
{"mes": "{{strategy.order.action}} {{ticker}} @ {{close}}"}
```
3. **Xử lý lỗi**:
- Kiểm tra logs trực tiếp trên Render Dashboard
- Đảm bảo message luôn đúng định dạng JSON

Phương pháp này sử dụng chính cơ chế alert của TradingView để gửi request định kỳ, giúp duy trì trạng thái active cho dịch vụ trên Render mà không cần dùng đến các công cụ bên ngoài[5][9].
