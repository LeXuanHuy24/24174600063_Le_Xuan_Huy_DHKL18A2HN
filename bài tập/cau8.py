# 8. Viết chương trình phân loại sinh viên dựa vào kết quả điểm học tập. 
# Nếu điểm A thì phân loại là sinh viên xuất sắc, 
# điểm B là sinh viên loại giỏi, 
# điểm C là sinh viên loại khá, 
# điểm D là sinh viên loại trung bình, 
# điểm E là sinh viên loại yếu, 
# điểm F là sinh viên xếp loại kém.
diem_chuyen_can = float(input("Nhập điểm chuyên cần: "))
diem_giua_ky = float(input("Nhập điểm giữa kỳ: "))
diem_cuoi_ky = float(input("Nhập điểm cuối kỳ: "))
    

diem_trung_binh = (diem_chuyen_can + diem_giua_ky + diem_cuoi_ky) / 3
    

if diem_trung_binh >= 9:
       loai= "A"
elif diem_trung_binh >= 7:
        loai = "B"
elif diem_trung_binh >= 5:
        loai = "C"
elif diem_trung_binh <5:
        loai = "D"
    
print(f"Điểm trung bình: {diem_trung_binh:.2f} - Loại: {loai}")