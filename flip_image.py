from PIL import Image
import matplotlib.pyplot as plt

def flip_image_left_right(img):
    """
    输入：PIL图片对象
    输出：左右翻转后的图片对象
    """
    # 左右翻转图片
    flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    return flipped_img


if __name__ == "__main__":
    # 读取图片，把这里换成你的图片路径
    original_img = Image.open("test.jpg")
    # 调用函数翻转
    result_img = flip_image_left_right(original_img)

    # 同时展示原图 和 翻转后的图
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(original_img)
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.title("Flipped Image")
    plt.imshow(result_img)
    plt.axis("off")

    plt.show()