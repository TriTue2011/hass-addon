# 🔌 EVN VN

- Công cụ EVN VN hỗ trợ toàn bộ khu vực lấy dữ liệu điện tiêu thụ & tiền điện.
- Vui Lòng Đọc Kỹ Hướng Dẫn Sử Dụng Trước Khi Dùng

- ✅ Không cần đăng nhập thủ công

---

## 🚀 Cách sử dụng

### 1. Tạo cấu hình

#### Cách 1 - Cấu hình bằng web-ui

- Sau khi cài addon thành công, chạy addon rồi vào giao diện web-ui cấu hình

<img title="EVN VN ADDON" src="https://raw.githubusercontent.com/smarthomeblack/hass-addon/refs/heads/main/evnvn/1.png" width="100%"></img>

<img title="EVNVN WEB-UI" src="https://raw.githubusercontent.com/smarthomeblack/hass-addon/refs/heads/main/evnvn/2.png" width="100%"></img>

<img title="EVNVN WEB-UI" src="https://raw.githubusercontent.com/smarthomeblack/hass-addon/refs/heads/main/evnvn/3.png" width="100%"></img>

#### Cách 2 - Cấu hình bằng tab cấu hình trên addon

- Sau khi cái addon thành công, sang tab cấu hình để thêm thông tin tài khoản, key api như hướng dẫn bên dưới
Chú ý tài khoản cuối cùng luôn không có ký tự , ở cuối
```ini
accounts_json: |
  [
    {"userevn": "xxxxxx", "passevn": "xxxxxx", "server": ""}
  ]
gemini_api_key: Key API
gemini_model: gemini-2.0-flash


```
NPC và SPC Cần điền đúng key api gemini để bypass Capcha. Còn lại EVN khác thì điền bừa key api cũng được
Nếu tên đăng nhập là mã khách hàng thì không cần điền server, nếu đăng nhập bằng số điện thoại thì điền server tương ứng với khu vực, ví dụ "server": "npc"
- npc : Điện lực Miền Bắc
- cpc : Điện lực Miền Trung
- spc : Điện lực Miền Nam
- hn : Điện lực Hà Nội
- tl : Điện lực Thăng Long
- hcmc : Điện lực TP Hồ Chí Minh

> Bạn cần có tài khoản [Google Gemini](https://makersuite.google.com/app/apikey) để lấy `gemini_api_key`.

---

### 2. Chạy Addon
- Sau khi config xong thì chạy addon, sang tab logs xem có lỗi gì không, đợi cho chạy xong lần đầu rồi làm bước tiếp theo
- Bấm vào đây để tải EVN VN trên HACS:
- [![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=smarthomeblack&repository=npc)
- Khởi động lại Home Assistant, Vào Thiết Bị --> Thêm Thiết bị --> Nhập Mã Khách Hàng(userevn là sdt thì chỗ này cũng nhập Mã Khách Hàng) để thêm các Sensor
- Hoặc tải thủ công custom_components/npc về rồi copy vào Home Assistant

---

## 📡 Kết quả

Sau khi khởi chạy lần đầu sẽ mất chút thời gian để lấy dữ liệu:

- `Chỉ số đầu kỳ`
- `Chỉ số cuối kỳ`
- `Chỉ số tạm chốt`
- `Tiêu thụ tháng này`
- `Tiêu thụ hôm nay`
- `Tiêu thụ hôm qua`
- `Tiêu thụ hôm kia`
- `Tiêu thụ tháng trước`
- `Tiền điện tháng trước`
- `Tiền điện tháng này`
- `Update Last`
- `Chi tiết tháng này`
- `Tiền điện sản lượng năm nay`
- `Lịch cắt điện`

- Và nhiều cảm biến khác

---

---
  
## Hiển Thị Cảm Biến Trên Home Assistant

- Chi Tiết Tiêu Thụ Các Ngày Trong Tháng
```yaml
type: markdown
title: Chi Tiết Tiêu Thụ Tháng Này
content: >
  **Trạng thái tháng**: `{{
  states('sensor.chi_tiet_dien_tieu_thu_thang_nay') }}`


  <details>
    <summary><strong>Chi tiết dữ liệu</strong></summary>
    
    Ngày         - Chỉ số (kWh)     - Điện tiêu thụ (kWh)
    -
    {% for d in state_attr('sensor.chi_tiet_dien_tieu_thu_thang_nay', 'data') %}
    {{ d['Ngày'] }} | {{ d['Chỉ số'] }} kWh | {{ d['Điện tiêu thụ (kWh)'] }} kWh
    {% endfor %}

    **Start date**: {{ state_attr('sensor.chi_tiet_dien_tieu_thu_thang_nay','start_date') }}  
    **End date**: {{ state_attr('sensor.chi_tiet_dien_tieu_thu_thang_nay','end_date') }}
  </details>``
```

- Chi Tiết Tiêu Thụ Và Tiền Điện Các Tháng Trong Năm
```yaml
type: markdown
title: Chi Tiết Năm
content: |
  <details>
    <summary><strong>Chi tiết dữ liệu</strong></summary>
    Tháng - Năm  | Tiêu Thụ (KWh) | Tiền Điện (VNĐ)
    {% for d in state_attr('sensor.tien_dien_san_luong_nam_nay', 'TienDien') %}
      {# Tìm entry SanLuong cùng Tháng/Năm #}
      {% set sl = state_attr('sensor.tien_dien_san_luong_nam_nay', 'SanLuong')
         | selectattr('Tháng', 'equalto', d['Tháng'])
         | selectattr('Năm', 'equalto', d['Năm'])
         | first %}
      {{ d['Tháng'] }} - {{ d['Năm'] }}  --> {{ sl['Điện tiêu thụ (KWh)'] }} KWh --> {{ "{:,}".format(d['Tiền Điện'] | int) | replace(',', '.') }} VNĐ
    {% endfor %}

  </details>

```

---

## 🖼️ Demo

<img title="EVNVN WEB-UI" src="https://raw.githubusercontent.com/smarthomeblack/hass-addon/refs/heads/main/evnvn/6.png" width="100%"></img>

<img title="EVNVN WEB-UI" src="https://raw.githubusercontent.com/smarthomeblack/hass-addon/refs/heads/main/evnvn/4.png" width="100%"></img>

<img title="EVNVN WEB-UI" src="https://raw.githubusercontent.com/smarthomeblack/hass-addon/refs/heads/main/evnvn/5.png" width="100%"></img>

---

## ❓ Câu hỏi thường gặp

#### Q: Dữ liệu có tự động cập nhập không?
> A: Có, dữ liệu sẽ tự động thu thập & gửi dữ liệu mỗi 120 phút.

#### Q: Có logs theo dõi không?
> A: Có. Bạn có thể xem tại tab logs trong addon.

---

## ❤️ Đóng góp

Nếu bạn có câu hỏi hoặc muốn cải tiến, hãy mở [Issue](https://github.com/smarthomeblack/hass-addon/evnvn/issues) hoặc gửi PR.



