# OBS-Replay-Notifier
# OBSReplayNotifier

[中文](#中文介绍) | [English](#english-introduction)

---

## 中文介绍

轻量级的 OBS 回放保存通知脚本，自动识别系统语言，保存回放时在屏幕右上角弹出中英文通知，简洁美观，无操作干扰。

### 功能

- 监听 OBS 回放缓存保存事件  
- 支持中文和英文系统自动切换通知语言  
- 通知窗口无边框、半透明、置顶，3秒后自动消失  
- 使用跨平台 tkinter 实现，轻量无依赖  

### 安装与使用

1. 确保 OBS 启用了“回放缓存”功能  
2. 下载 `replay_notify.py` 脚本  
3. 打开 OBS → 工具 → 脚本，添加脚本  
4. 绑定“保存回放”快捷键（在回放缓冲区设置中）  
5. 每次保存时，右上角出现通知弹窗
## 效果展示

![通知效果示意图](replay_notify.png)

---

## English Introduction

A lightweight OBS replay save notification script that automatically detects system language and shows bilingual notifications at the top-right corner when a replay is saved. Simple, elegant, and non-intrusive.

### Features

- Listen to OBS replay buffer saved event  
- Automatically switch notification language for Chinese and English systems  
- Borderless, semi-transparent, topmost notification window that auto-closes after 3 seconds  
- Implemented with cross-platform tkinter, lightweight and dependency-free  

### Installation & Usage

1. Make sure OBS’s replay buffer feature is enabled  
2. Download the `replay_notify.py` script  
3. Open OBS → Tools → Scripts, and add the script  
4. Bind a hotkey for “Save Replay” (in Replay Buffer settings)  
5. Notification popup appears at the top-right corner on each replay save  
