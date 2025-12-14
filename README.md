# tim kiem doi khang trong tro choi tic tac toe

## gioi thieu

du an nay trinh bay bai toan tim kiem doi khang (adversarial search) thong qua viec mo hinh hoa va giai tro choi hai nguoi tic tac toe. muc tieu cua bai toan la xay dung thuat toan ra quyet dinh nuoc di toi uu, dam bao loi ich lon nhat cho nguoi choi toi uu (max) trong dieu kien doi thu choi toi uu (min).

hai giai thuat chinh duoc ap dung trong du an gom:

* minimax
* minimax ket hop cat tia alpha beta

---

## mo ta bai toan tim kiem doi khang

-Tìm kiếm đối kháng là mô hình hóa trò chơi 2 người dưới dạng bài toán tìm kiếm, giải thuật quyết định nước đi tối ưu trong trò chơi, nhằm tìm được đường đi đảm bảo chiến thắng cho người chơi

trong bai toan tic tac toe:

* so nguoi choi: 2
* nguoi choi x: max (toi da hoa loi ich)
* nguoi choi o: min (toi thieu hoa loi ich cua x)

---

## mo hinh hoa tro choi tic tac toe

### 1. trang thai ban dau

* initial_state(): ban co kich thuoc n x n
* tat ca cac o ban dau deu rong va duoc gan gia tri empty

vi du:

empty empty empty
empty empty empty
empty empty empty

---

### 2. xac dinh nguoi choi tiep theo

* ham player(board) xac dinh nguoi se di nuoc tiep theo
* cach xac dinh:

  * dem so o x va o
  * neu so x bang so o thi den luot x
  * neu so x lon hon so o thi den luot o

quy uoc:

* x la max
* o la min

---

### 3. trang thai ket thuc

* ham winner(board): kiem tra nguoi thang

  * kiem tra cac hang, cot va duong cheo
  * neu co 3 o lien tiep cung gia tri x hoac o thi nguoi do thang

* ham terminal(board):

  * tra ve true neu:

    * co nguoi thang
    * hoac ban co day va khong ai thang (hoa)
  * nguoc lai tra ve false

---

### 4. ham chuyen trang thai (actions va result)

* actions(board):

  * liet ke tat ca cac nuoc di hop le
  * moi nuoc di duoc bieu dien boi toa do (i, j)
  * dieu kien: o tai (i, j) dang empty

* result(board, action):

  * sao chep ban co hien tai
  * xac dinh nguoi choi hien tai bang player(board)
  * gan quan co vao vi tri duoc chon
  * tra ve trang thai moi cua ban co

---

### 5. ham loi ich (utility function)

* utility(board): gan gia tri so cho trang thai ket thuc

quy uoc:

* x thang: utility = 1

* o thang: utility = -1

* hoa: utility = 0

* trong qua trinh tim kiem:

  * neu terminal(state) la true thi tra ve utility(state)
  * neu chua ket thuc thi tiep tuc sinh cac trang thai con

---

### 6. ham luong gia (heuristic)

trong truong hop khong the duyet het cay tro choi, su dung ham luong gia:

e(n) = x(n) - o(n)

trong do:

* x(n): so dong thang tiem nang cua x
* o(n): so dong thang tiem nang cua o

ham nay giup danh gia muc do tot xau cua mot trang thai trung gian.

---

## giai thuat minimax

### y tuong

* tro choi gom cac luot di luan phien giua max va min
* max co muc tieu toi da hoa gia tri utility
* min co muc tieu toi thieu hoa gia tri utility cua max

---

### hien thuc

* maxvalue(state):

  * neu state la trang thai ket thuc thi tra ve utility(state)
  * nguoc lai:

    * khoi tao v = -vo cuc
    * duyet tat ca cac action
    * goi minvalue(result(state, action))
    * cap nhat v = max(v, gia tri tra ve)

* minvalue(state):

  * neu state la trang thai ket thuc thi tra ve utility(state)
  * nguoc lai:

    * khoi tao v = +vo cuc
    * duyet tat ca cac action
    * goi maxvalue(result(state, action))
    * cap nhat v = min(v, gia tri tra ve)

* minimax(board):

  * xac dinh nguoi choi hien tai
  * duyet cac nuoc di hop le
  * chon nuoc di co gia tri tot nhat doi voi nguoi choi do

---

## giai thuat alpha beta pruning

### y tuong

* minimax duyet toan bo cay tro choi nen ton thoi gian
* alpha beta pruning giup loai bo cac nhanh khong can thiet

khai niem:

* alpha: gia tri tot nhat hien tai cua max
* beta: gia tri tot nhat hien tai cua min

nguyen tac cat tia:

* neu alpha >= beta thi dung duyet nhanh hien tai

---

### cac buoc chinh

* buoc 1: kiem tra dieu kien dung

  * trang thai ket thuc hoac dat gioi han do sau

* buoc 2: luot cua max

  * khoi tao best = -vo cuc
  * thu tung nuoc di
  * cap nhat best va alpha
  * cat tia neu beta <= alpha

* buoc 3: luot cua min

  * khoi tao best = +vo cuc
  * thu tung nuoc di
  * cap nhat best va beta
  * cat tia neu beta <= alpha

* buoc 4: ham ra quyet dinh

  * findbestmove(): thu tung nuoc di
  * goi minimax voi alpha beta
  * chon nuoc di co diem cao nhat

---

## muc dich hoc tap

* hieu ro ban chat tim kiem doi khang
* phan biet minimax va alpha beta
* ap dung ly thuyet tri tue nhan tao vao tro choi hai nguoi

