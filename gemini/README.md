## ❓ Nhóm Support:
- Zalo: https://zalo.me/g/alvkgn274
- Telegram: https://t.me/smarthomeblack

---

# 🤖 Gemini Web API

LLM FREE TOKEN.


# Gemini Web API Addon Home Assistant

- Gemini Web API là một Addon cho phép bạn sử dụng gemini web làm API cho bộ tích hợp LLM để dùng vô hạn token.

## 🧰 Tính năng

- Chat, fun call...

---

## 📡 Cấu hình Gemini Web API

- Chú ý làm đủ các bước trước khi chạy container
- Tạo file my_cookie.txt ở thư mục /config/gemini-web-api/my_cookie.txt (các bạn lưu file ở đâu thì mount ở đó).
- Mở trình duyệt ẩn danh đăng nhập vào gemini.google.com (Các bạn nên dùng tài khoản phụ và hạn chế đăng nhập, tốt nhất là mở ẩn danh, sẽ không bao giờ bị hết hạn và mất cookie).
- Bật develop(F12). Sau đó chat 1 cuộc hội thoại bất kỳ với gemini.
- Tại Develop bấn sang tab Network, và làm theo như ảnh.
- Copy toàn bộ cookie ở Request Headers.
- Tải file cookie.html xuống và mở bằng chrome, copy toàn bộ cookie vừa lấy được vào ô đầu tiên,sau đó bấm trich xuất rồi copy toàn bộ text trích xuất được vào file my_cookie.txt đã tạo ở bước 2.
- Docker compose:

```yaml

services:
  gemini-web-api:
    image: ghcr.io/smarthomeblack/gemini-web-api
    container_name: gemini-web-api
    ports:
      - "5002:5002"
    restart: unless-stopped
    volumes:
      - /config/gemini-web-api/my_cookie.txt:/app/my_cookie.txt

```

<img title="Gemini Web API" src="https://raw.githubusercontent.com/smarthomeblack/hass-addon/refs/heads/main/gemini/1.png" width="100%"></img>

<img title="Gemini Web API" src="https://raw.githubusercontent.com/smarthomeblack/hass-addon/refs/heads/main/gemini/2.png" width="100%"></img>

<img title="Gemini Web API" src="https://raw.githubusercontent.com/smarthomeblack/hass-addon/refs/heads/main/gemini/3.png" width="100%"></img>

---

## 📡 Cài Bộ tích hợp Gemini Web API
- Dùng cho Home Assistant:
Xem chi tiết hướng dẫn cài ở đây: https://github.com/smarthomeblack/gemini-web-api

- Dùng cho các dự án ngoài Home Assistant
Sử dung endpoint /v1 . Dự án sử dụng chuẩn format của OpenAi, nên mọi người tự kham khảo OpenAI, mình không hỗ trợ
---

## 📞 Hỗ trợ

Nếu bạn có câu hỏi hoặc muốn cải tiến, hãy mở [Issue](https://github.com/smarthomeblack/hass-addon/gemini-web-api/issues) hoặc gửi PR.

---

## 🧾 License

MIT License

## Cảm ơn
- Cảm ơn tới HanaokaYuzu đã tạo ra 1 thư viện miễn phí và giúp cộng đồng tiết kiệm được vài lít máu
- Khảm khảo: https://github.com/HanaokaYuzu/Gemini-API

