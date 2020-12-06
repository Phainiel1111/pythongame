import pygame,sys

screen = pygame.display.set_mode((1280, 720))
# Độ phân giải hiện tại để cho thuận tiện
# Nếu ai làm được thì tìm cách để cho game maximize/restore down được mà vẫn
# giữ được asprect ratio cho màn hình game (16:9)

background = pygame.image.load('pieces.png').convert()
# Map chọn để đua



class racer1:
    img=pygame.image.load('racer1.png').convert() # gán ảnh
    spd=50                                        # tốc độ
    xy=img.get_rect()
    xy=xy.move(1220,100)                          # tọa độ ban đầu của xe
    step=0                                        # số bước xe đã đi
    choose=0                                      # xe có phải là xe đặt cược?
    
class racer2:
    img=pygame.image.load('racer1.png').convert()
    spd=50
    xy=img.get_rect()
    xy=xy.move(1125,150)
    step=0
    choose=0

    
class racer3:
    img=pygame.image.load('racer1.png').convert()
    spd=50
    xy=img.get_rect()
    xy=xy.move(1000,250)
    step=0
    choose=0

    
class racer4:
    img=pygame.image.load('racer1.png').convert()
    spd=50
    xy=img.get_rect()
    xy=xy.move(850,350)
    step=0
    choose=0

    
class racer5:
    img=pygame.image.load('racer1.png').convert()
    spd=50
    xy=img.get_rect()
    xy=xy.move(720,450)
    step=0
    choose=1



# vị trí camera ban đầu
class bg:
    x=0
    y=0

# dịch camera theo xe đã đặt cược theo tốc độ của xe
def dich_camera_x(huong,self):
    if huong=='phai':
        bg.x-=self.spd
        racer1.xy[0]-=self.spd
        racer2.xy[0]-=self.spd
        racer3.xy[0]-=self.spd
        racer4.xy[0]-=self.spd
        racer5.xy[0]-=self.spd
    if huong=='trai':
        bg.x+=self.spd
        racer1.xy[0]+=self.spd
        racer2.xy[0]+=self.spd
        racer3.xy[0]+=self.spd
        racer4.xy[0]+=self.spd
        racer5.xy[0]+=self.spd
def dich_camera_y(huong,self):
    if huong=='len':
        bg.y+=self.spd
        racer1.xy[1]+=self.spd
        racer2.xy[1]+=self.spd
        racer3.xy[1]+=self.spd
        racer4.xy[1]+=self.spd
        racer5.xy[1]+=self.spd
    if huong=='xuong':
        bg.y-=self.spd
        racer1.xy[1]-=self.spd
        racer2.xy[1]-=self.spd
        racer3.xy[1]-=self.spd
        racer4.xy[1]-=self.spd
        racer5.xy[1]-=self.spd



# cac ham di chuyen xe theo toc do
def ngang_phai(self):
    self.step+=self.spd # cộng vào quãng đường mỗi vận tốc trên giây đi được
    self.xy=self.xy.move(self.spd,0) # dịch xe theo tốc độ của xe
    if self.choose==1:
        dich_camera_x('phai',self)
def ngang_trai(self):
    self.step+=self.spd
    self.xy=self.xy.move(-self.spd,0)
    if self.choose==1:
        dich_camera_x('trai',self)
def doc_xuong(self):
    self.step+=self.spd
    self.xy=self.xy.move(0,self.spd)
    if self.choose==1:
        dich_camera_y('xuong',self)
def doc_len(self):
    self.step+=self.spd
    self.xy=self.xy.move(0,-self.spd)
    if self.choose==1:
        dich_camera_y('len',self)

def chay_xe(self):
    if self.step<=1150:
        ngang_phai(self)
    if self.step>=1150 and self.step<=1150+450:
        doc_xuong(self)
    if self.step>=1150+450 and self.step<=1150+450+1150:
        ngang_trai(self)
    if self.step>=(1150+450+1150) and self.step<=(1150+450+1150+400):
        doc_len(self)
        
    pass
    # Khúc này là để lập trình cho xe chạy theo tọa độ,
    # Chạy theo khoảng cách từ x đến y theo chiều:
    # ngang_phai(self) - sang phải
    # ngang_trai(self) - sang trái
    # doc_len(self) - đi lên
    # doc_xuong(self) - đi xuống

    # Ví dụ trên phân khúc cho chạy theo 4 khúc:
    # 0->1150
    # 1150->1150+450
    # 1150+450->1150+450+1150
    # 1150+450+1150->1150+450+1150+400

    # Nếu muốn chạy xe theo hướng chéo thì cho hai hàm ngang và dọc vào cùng
    # một nhóm lệnh trong if




    
def hien_xe(self):
    screen.blit(self.img, self.xy)

def nam_chiec_xe():
    hien_xe(racer1)
    hien_xe(racer2)
    hien_xe(racer3)
    hien_xe(racer4)
    hien_xe(racer5)
    
    chay_xe(racer1)
    chay_xe(racer2)
    chay_xe(racer3)
    chay_xe(racer4)
    chay_xe(racer5)


# NO NEED TO CARE #
while 1:
    for event in pygame.event.get():
        if (event.type==pygame.QUIT or
            (event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
            sys.exit()
# NO NEED TO CARE #

    screen.blit(background,(bg.x,bg.y))
    nam_chiec_xe() # hien hinh anh xe va cho chay xe    
    pygame.time.delay(100) # tu dieu chinh theo y muon
    pygame.display.update()
