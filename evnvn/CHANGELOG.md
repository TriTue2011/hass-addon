Changelog

2025.7.18
Thêm tiền nợ khu vực NPC, Fix lấy hóa đơn kỳ mới NPC

2025.7.3
Fix tiền nợ CPC, HN,Fix lỗi hiển thị sai tiền nợ server HCMC. Fix lấy dữ liệu lỗi do cập nhập chậm server HN(server HN xóa evndata.db ở config/evnvn trước khi update để lấy lại dữ liệu chuẩn nhất).Chú ý đang thời kỳ sáp nhập nên đa số các server đang bảo trì khá nhiều nên trong ngày sẽ có thời điểm api không thể truy cập được.mọi người không cần lo lắng cứ kệ nó vì addon 2 tiếng lấy dữ liệu 1 lần

2025.7.2
Fix PDF Server SPC, thêm lấy tiền nợ server SPC

2025.7.1
Thêm cảm biến Tiền nợ hóa đơn.Hỗ trợ lấy file hóa đơn PDF gửi qua telegram khi có hóa đơn mới,vui lòng update cả EVN VN trên HACS lên cùng ver để dùng tính năng này, và đã config telegram trên HASS

2025.6.30
Hỗ trợ lấy file hóa đơn PDF gửi qua telegram khi có hóa đơn mới,vui lòng update cả EVN VN trên HACS lên cùng ver để dùng tính năng này, và đã config telegram trên HASS

2025.6.23
Hỗ trợ cấu hình tài khoản(thêm,xóa..) bên trong web-ui mà không cần cấu hình trên addon !

2025.6.22a
fix trình duyệt bị lỗi khi F5.mọi người xóa thư mục assets trong config/evnvn

2025.6.22
Fix lấy dữ liệu hóa đơn trên 1tr, thêm cấu hình ngày đầu kỳ vào web-ui để hiển thị cho chính xác theo khu vực, web-ui nhiều cải tiến, xóa index.html trước khi update nếu muốn dùng web-ui mới,ai dùng mod không có nhu cầu thì không cần xóa

2025.6.18a
Fix web-ui vs data khu vực HN, xóa evndata.db trước khi update

2025.6.18
Chuẩn hóa dữ liệu lưu trữ phục vụ cho lâu dài,buộc xóa file evndata.db trước khi update,bản update ổn định sau bao ngày beta, vui lòng update EVN VN trên HACS lên bản 2025.6.18

2025.6.17
Fix mất dữ liệu cho server SPC vì server SPC không ổn định, Ae SPC vui lòng xóa file evndata.db cũ đi rồi khởi động lại addon,SPC có thể không lấy được dữ liệu ngay vì server thi thoảng lag, cứ để addon chạy 

2025.6.16b
WEB-UI mới, tối ưu hóa bypass CAPCHA ngon hơn

2025.6.16
Fix dữ liệu cảm biến theo chuẩn mới, loại bỏ hoàn toàn sự phụ thuộc mqtt và ngaydauky ở config

2025.6.15d
Chuyển đổi phương thức lưu trữ từ Json lỏ sang SQLite để lưu trữ lâu dài tránh lag

2025.6.12d
Hỗ trợ lấy dữ liệu cho 1 tài khoản có nhiều mã khách hàng khu vực HN, CPC

2025.6.12b
Fix hiển thị sai số tiền trên web-ui cho HN. lấy thêm dữ liệu hóa đơn từ đầu năm cho e-thanglong

2025.6.12a
Hỗ trợ 3 pha cho khu vực HN

2025.6.12
Hỗ trợ đăng nhập bằng SĐT cho những username không phải là mã khách hàng, thêm server HCMC

2025.6.11a
Thêm ICON cho ingress web-ui, Fix kết nối spc

2025.6.11
Thêm lịch cắt điện cho CPC

2025.6.10
Tối ưu hóa cho cpu và ram lỏ. Update Sensor Lịch Cắt Điện chuẩn xác tới từng giây(NPC và SPC), Tối ưu tốc độ lấy dữ liệu cho NPC...

2025.6.8a
Trước khi Update bản này vui lòng xóa file index.html để cập nhập mới. Thêm ingress để hỗ trợ https. Tự động copy file html vào thư mục evnvn, Fix hiển thị web-ui khu vực HN

2025.6.7b
Fix đăng nhập CPC Miền Trung bằng mã khách hàng

2025.6.7a
FIX Cảm biến tiêu thụ ngày cho EVN HN

2025.6.7
Thêm E-thanglong,Thêm cấu hình ngaydauky cho từng tài khoản

2025.6.6
NPC Miền Bắc, SCP Miền Nam, CPC Miền Trung, EVN Hanoi

xaaa