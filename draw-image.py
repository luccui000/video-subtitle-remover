import cv2

x1, y1, x2, y2 = 0, 0, 0, 0
drawing = False

def get_key(event, x, y, flags, param):
    global key

    if event == cv2.EVENT_KEYDOWN:
        key = cv2.waitKey(1) & 0xFF


def draw_rectangle(image, x1, y1, x2, y2):
    if x1 < 0 or y1 < 0 or x2 > image.shape[1] or y2 > image.shape[0]:
        print("Tọa độ không hợp lệ!")
        return

    print((x1, y1), (x2, y2))
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)


def get_coordinates(event, x, y, flags, param):
    global x1, y1, x2, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        x1, y1 = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            x2, y2 = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        x2, y2 = x, y

def main():
    try:
        video_path = "3231473987169980134.mp4"
        video = cv2.VideoCapture(video_path)
        ret, image = video.read()
        video.release()

        cv2.namedWindow("Vẽ khung hình chữ nhật")
        cv2.setMouseCallback("Vẽ khung hình chữ nhật", get_coordinates)

        # Lặp lại hiển thị ảnh và chờ thao tác chuột
        while True:
            draw_rectangle(image, x1, y1, x2, y2)
            # Hiển thị ảnh
            cv2.imshow("Vẽ khung hình chữ nhật", image)

            # Thoát khi nhấn phím 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # In ra 4 điểm
        print(f"x1: {x1}")
        print(f"y1: {y1}")
        print(f"x2: {x2}")
        print(f"y2: {y2}")

        # Hủy cửa sổ
        cv2.destroyAllWindows()
    except:
        pass


main()
