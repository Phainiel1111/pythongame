Nhóm cài pygame, pygame-menu. 

>Đọc và tìm hiểu cách dùng qua https://pygame-menu.readthedocs.io/en/latest/ để làm menu và giao diện các thành phần cho game. 
>Cố gắng tìm hiểu sâu vào cách tạo giao diện qua pygame-menu.
>
>Nhóm code bổ sung các thành phần đã có ghi đỏ tên hàm vào code file main.py trên github. Trước tiên cứ tham khảo cách tạo menu trên file main.py đó.
>Cách đặt tên hàm, gói code vào hàm nào thì xem mấy chữ bôi đỏ ở các trang 4-6. Tiện thể việt hóa mấy cái nút luôn.
>
>Riêng nhóm design tìm hiểu tập trung vào hai trang https://pygame-menu.readthedocs.io/en/latest/_source/add_sounds.html, https://pygame-menu.readthedocs.io/en/latest/_source/themes.html, https://pygame-menu.readthedocs.io/en/latest/_source/add_widgets.html để chỉnh sửa giao diện và âm thanh ở màn hình giao diện menu.



#Cài và sử dụng pygame-menu
>Đặt biến môi trường để có thể sử dụng được pip của python, cách để làm sao có thể google
>(hoặc mở cmd, dùng lệnh set PATH=<tên thư mục để pip, ví dụ ở đây là D:\Python38\Scripts>
>
>cài pygame thông qua lệnh cmd: 
>  pip install pygame
>  
>cài pygame-menu thông qua lệnh:
>  pip install pygame-menu
>(nếu chưa được thì xem báo lỗi xem nó yêu cầu cài thêm cái gì, ví dụ như sphinx thì phải dùng lệnh pip install sphinx)


Task 06/12/2020
Cả nhóm chạy thử file race.py rồi tìm hiểu để làm việc. Ví dụ minh họa là để cảnh báo nhóm đừng thiết kế map theo kiểu đó.

- Nhóm design:
  + Thiết kế ít nhất 5 set nhân vật để đưa vào trong game như đã nói. Nên để các file gốc có kích thước lớn để về sau tiện chỉnh sửa. 
  Nhớ để cho các khoảng trắng transparent để khi đưa vào không bị lẫn màu. 
  Thiết kế mỗi nhân vật tầm bao nhiêu img để khi load tuần tự các img nhìn sẽ giống như đang động đậy (có thể test bằng cách tạo gif xem thử). 
  Hiện tại ít nhất cố gắng thiết kế set cơ bản nhất là 5 chiếc xe 5 màu.
  + Thiết kế ít nhất 5 map theo dạng background như yêu cầu (xem file biên bản). Đánh dấu điểm bắt đầu của 5 chiếc xe và làn đường của mỗi chiếc. 
  Lưu ý là đừng để 5 chiếc đứng thành một hàng dọc hoặc ngang nếu như map đó không phải là map chỉ đi thẳng một chiều. 
  Đồng thời đừng thiết kế map theo hình vòng cung, hoặc trừ phi tính thiết kế map có đường này luồn dưới đường kia thì đừng thiết kế map đi quá 2 chiều.
  Lý do là code chỉ để cho xe chạy song song cùng một lúc chứ không điểu khiển rời từng xe.
  Lưu ý 2 là đảm bảo cho quãng đường cả 5 xe chạy từ đầu đến đích đều bằng nhau. 
  Hoàn thành được map nào thì đưa map đó cho team code xử lý.

- Nhóm code:   
  + Chỉnh sửa code để đọc dữ liệu map từ file khác, mỗi map sẽ có một file dữ liệu để điều chỉnh: 
     /vị trí ban đầu
     /tọa độ ban đầu của mỗi xe 
     /tốc độ xe (nếu muốn)
     /đường đi của xe
  + Nhận map từ team design rồi viết code để xe chạy theo quỹ đạo đi hết từ đầu cho tới đích. Xác định vị trí camera ban đầu phù hợp rồi xác định vị trí từng xe.
    Code vào một file làm sao để file race.py đọc được dữ liệu từ file đó, đảm bảo điều khiển được xe từ hàm chay_xe(self)
    Nếu không được thì ta có thể chữa cháy bằng cách tạo ra 5 file race.py và nhập thông số dữ liệu của mỗi map vào mỗi file, nhưng nếu được thì cố làm như trên.
  + Viết hàm ngẫu nhiên hóa tốc độ mỗi xe khi bắt đầu game. Bám vào tốc độ n, tốc độ ngẫu nhiên thì chênh lệch n+epsilon hoặc n-epsilon (epsilon nhỏ) thôi.
  + Viết luôn code để đọc dữ liệu xuất ra từ phần menu như là:
    /xe đặt cược
    /v.v.
  + Coi biến step là vị trí x của xe trên quãng đường dài MAXSTEP, ngẫu nhiên hóa với xác xuất nhỏ để mỗi n step thì ngẫu nhiên một lần tại điểm x thứ n step đó 
  với xác suất k% xuất hiện bùa. Nếu bùa xuất hiện thì thỏa mãn điều kiện để code hiện ảnh bùa trên đường đó thực hiện cũng như là code hiệu ứng.
  + Viết code để lưu thứ tự các xe đạt mốc MAXSTEP (tức là về đích) để khi xe cược về đích thì hiện thông báo thắng thua cũng như là bảng xếp hạng. 
  (có thể để các xe còn lại về đến đích thì mới xuất bảng hoặc về đích rồi thì báo thắng thua, nhảy thẳng sang bảng xếp hạng rồi ngẫu nhiên hóa thứ hạng các xe sau
  nói chung là tùy ý tìm cách giải quyết)
  
  + (Làm được luôn thì tốt, không thì thôi):
      /Tìm hiểu và viết code để load ảnh động cho từng xe: tham khảo https://stackoverflow.com/questions/14044147/animated-sprite-from-few-images
      /Tìm cách để cho game maximize/restore down được mà vẫn giữ được aspect ratio cho màn hình game (16:9)
      /Nếu được thì cải thiện chất lượng code nếu có thể
      /Viết hàm để tạo object 'bùa' theo xác suất ngẫu nhiên. 
