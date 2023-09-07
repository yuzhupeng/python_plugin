import os
import sys
import ctypes
import argparse
import win32com.client as client

MAX_DEPTH = 1

def run_as_admin():
    if args.depth < MAX_DEPTH:
        print('\n[!] 权限不足，重新以管理员身份运行')
        # 以管理员身份重新运行脚本
        ctypes.windll.shell32.ShellExecuteW(
            None,
            'runas',
            sys.executable,
            ' '.join(sys.argv + [f'--depth {args.depth + 1}']),
            None,
            1
        )
        print(' ~ Auto Maple 的设置完成')
    exit(0)

def create_desktop_shortcut():
    print('\n[~] 创建 Auto Maple 的桌面快捷方式:')
    cwd = os.getcwd()  # 获取当前工作目录的路径
    target = os.path.join(os.environ['WINDIR'], 'System32', 'cmd.exe')  # cmd.exe的路径

    flag = "/c"  # 默认关闭命令提示符窗口
    if args.stay:  # 如果指定了--stay参数，则保持命令提示符窗口打开
        flag = "/k"
        print(" - 程序运行结束后保持命令提示符窗口打开")

    shell = client.Dispatch('WScript.Shell')  # 创建Windows脚本shell对象
    shortcut_path = os.path.join(shell.SpecialFolders('Desktop'), 'Auto Maple.lnk')  # 快捷方式保存的路径和名称
    shortcut = shell.CreateShortCut(shortcut_path)  # 创建快捷方式对象
    shortcut.Targetpath = target  # 设置目标路径为cmd.exe
    shortcut.Arguments = flag + f' \"cd {cwd} & python main.py\"'  # 在命令行中执行切换到当前工作目录并运行main.py脚本
    shortcut.IconLocation = os.path.join(cwd, 'assets', 'icon.ico')  # 设置快捷方式的图标路径
    try:
        shortcut.save()  # 保存快捷方式
    except:
        run_as_admin()

    with open(shortcut_path, 'rb') as lnk:  # 打开快捷方式文件
        arr = bytearray(lnk.read())  # 将文件内容读取为字节数组
    arr[0x15] = arr[0x15] | 0x20  # 启用“以管理员身份运行”
    with open(shortcut_path, 'wb') as lnk:  # 以二进制写入模式打开快捷方式文件
        lnk.write(arr)  # 将修改后的字节数组写回快捷方式文件中
        print(' - 启用了“以管理员身份运行”选项')
    print(' ~ 成功创建 Auto Maple 快捷方式')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()  # 创建命令行参数解析器对象
    parser.add_argument('--depth', type=int, default=0)  # 添加一个整数类型的参数depth，默认值为0
    parser.add_argument('--stay', action='store_true')  # 添加一个布尔类型的参数stay，如果指定了该参数，则设置为True
    args = parser.parse_args()  # 解析命令行参数

    create_desktop_shortcut()  # 创建桌面快捷方式
