import obspython as obs
import tkinter as tk
import threading

def show_notification(title="通知", message="回放已保存成功", duration=3):
    def notification():
        root = tk.Tk()
        root.overrideredirect(True)  # 去除窗口边框
        root.attributes("-topmost", True)  # 窗口置顶
        root.attributes("-alpha", 0.9)  # 设置透明度

        # 设置窗口大小和位置
        width, height = 300, 100
        screen_width = root.winfo_screenwidth()
        x = screen_width - width - 10  # 右上角，距离右边10像素
        y = 10  # 距离顶部10像素
        root.geometry(f"{width}x{height}+{x}+{y}")

        # 创建标签显示标题和消息
        frame = tk.Frame(root, bg="#333333")
        frame.pack(fill="both", expand=True)
        title_label = tk.Label(frame, text=title, font=("Arial", 14, "bold"), fg="white", bg="#333333")
        title_label.pack(pady=(10, 0))
        message_label = tk.Label(frame, text=message, font=("Arial", 12), fg="white", bg="#333333")
        message_label.pack(pady=(5, 10))

        # 自动关闭窗口
        root.after(int(duration * 1000), root.destroy)
        root.mainloop()

    threading.Thread(target=notification).start()

def on_event(event):
    if event == obs.OBS_FRONTEND_EVENT_REPLAY_BUFFER_SAVED:
        show_notification("OBS 通知", "回放已保存成功", duration=3)

def script_load(settings):
    obs.obs_frontend_add_event_callback(on_event)
