from mouse.mouse import draw_rect
import matplotlib.pyplot as plt
import cv2

def test_draw_rect():
    img = cv2.imread("./img/0.png")
    res = img.copy()
    plt.imshow(res)
    plt.show()
    params = [ res, (0, 0, 0, 0) ]
    cv2.setMouseCallback('Figure 1', draw_rect, params)
    while 1:
        plt.imshow('image', res)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    print params[1]

if __name__ == '__main__':
    test_draw_rect()
