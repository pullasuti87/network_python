# psutil -> cross-platform lib for process and system monitoring
import psutil
import time
import os


def byte_size(bytes):
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024


def clear_screen():
    # hide cursor
    print("\033[?25l", end="")
    if os.name == "posix":
        os.system("clear")
    # windows
    elif os.name == "nt":
        os.system("cls")


def main():
    clear_screen()
    download_speed = 0
    upload_speed = 0
    delay = 1
    try:
        while True:
            time.sleep(delay)
            stats = psutil.net_io_counters()
            upload_speed = (stats.bytes_sent - upload_speed) / delay
            download_speed = (stats.bytes_recv - download_speed) / delay
            print(
                f"Upload: {byte_size(stats.bytes_sent)}  "
                f"Download: {byte_size(stats.bytes_recv)}  "
                f"Upload Speed: {byte_size(upload_speed/delay)}/s  "
                f"Download Speed: {byte_size(download_speed/delay)}/s     ",
                end="\r",
            )
            download_speed = stats.bytes_recv
            upload_speed = stats.bytes_sent
    except KeyboardInterrupt:
        # cursor is back
        print("\033[?25h", end="")
        print("\nexit")


if __name__ == "__main__":
    main()
