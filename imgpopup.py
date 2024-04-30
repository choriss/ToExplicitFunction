import tkinter as tk
from PIL import Image, ImageTk

class ScrollableImageViewer:
    def __init__(self, master, image_path):
        self.master = master
        self.image_path = image_path
        self.scale_factor = 1.0
        self.start_x = None
        self.start_y = None

        # フレームを作成
        self.frame = tk.Frame(master)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # キャンバスを作成
        self.canvas = tk.Canvas(self.frame, bg="white")  # 背景色を白に設定
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 縦方向のスクロールバーを追加
        self.scrollbar_y = tk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.config(yscrollcommand=self.scrollbar_y.set)

        # 横方向のスクロールバーを追加
        self.scrollbar_x = tk.Scrollbar(master, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.config(xscrollcommand=self.scrollbar_x.set)

        # 画像の読み込みと表示
        self.load_image()

        # 画像のサイズにキャンバスを調整
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        # マウスホイールイベントを追加して拡大縮小
        self.canvas.bind("<MouseWheel>", self.on_mousewheel)

        # マウスのドラッグイベントを追加して画像の移動
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)

    def load_image(self):
        # 画像を読み込んで表示
        self.image = Image.open(self.image_path)
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas_image = self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

    def on_canvas_configure(self, event):
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def on_mousewheel(self, event):
        # マウスの位置を取得
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)

        now_x_bar_start,now_x_bar_end = self.scrollbar_x.get()
        now_y_bar_start,now_y_bar_end = self.scrollbar_y.get()

        # 拡大縮小率を設定
        if event.delta > 0:
            self.scale_factor *= 1.1
        else:
            self.scale_factor /= 1.1

        # 画像を拡大縮小
        new_width = int(self.image.width * self.scale_factor)
        new_height = int(self.image.height * self.scale_factor)
        resized_image = self.image.resize((new_width, new_height))

        # 更新された画像を表示
        self.photo = ImageTk.PhotoImage(resized_image)
        self.canvas.itemconfig(self.canvas_image, image=self.photo)

        # マウスの位置を中心にして画像を移動
        # self.canvas.scale(tk.ALL, x, y, self.scale_factor, self.scale_factor)

        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        self.canvas.xview_moveto(now_x_bar_start)
        self.canvas.yview_moveto(now_y_bar_start)
    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_move_press(self, event):
        if self.start_x and self.start_y:
            x_diff = event.x - self.start_x
            y_diff = event.y - self.start_y

            h = -self.scrollbar_x.delta(x_diff, y_diff)/(25*self.scale_factor)  # スクロール量調整
            v = -self.scrollbar_y.delta(x_diff, y_diff)/(25*self.scale_factor)
            # self.canvas.move(self.canvas_image, x_diff, y_diff)

            _start_x, end_x = self.scrollbar_x.get()
            self.after_x = max(min(_start_x + h, 1.0), 0.0) 
            self.canvas.xview_moveto(self.after_x)
            #マウス記憶
            self.start_x = event.x

            _start_y, end_y = self.scrollbar_y.get()
            self.after_y = max(min(_start_y + v, 1.0), 0.0)
            self.canvas.yview_moveto(self.after_y)
            # print(self.after_x)
            #マウス記憶
            self.start_y = event.y


            # self.canvas.xview_scroll(-x_diff//self.image.width,"unit")
            # self.canvas.yview_scroll(-y_diff//self.image.height,"unit")
            # print(self.scrollbar_x.delta(1,1))
            

def open_image_window(image_path):
    root = tk.Toplevel()
    root.title("Image Viewer")

    # 画像ビューアーのインスタンスを作成
    viewer = ScrollableImageViewer(root, image_path)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Window")

    button = tk.Button(root, text="Open Image", command=lambda: open_image_window("output.png"))
    button.pack()

    root.mainloop()
