import socket

# 创建UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('192.168.10.10', 9002))  # 监听电脑的IP和端口

print("Listening for UDP packets on 192.168.10.10:9002...")

# 保存上一条接收到的报文的数据域
previous_data_field = None

while True:
    try:
        # 接收UDP数据包
        '''
        recvfrom既可以接收数据,又能获取发送方的地址信息
        @1024 指定接收的最大字节数,超出部分会被截断
        @data 接收到的数据,数据类型是bytes
        @addr 发送方的IP和port
        '''
        data, addr = sock.recvfrom(1024)
        
        # 确保报文长度为53字节
        if len(data) == 53:
            # 提取中间部分数据（第11个字节到倒数第二个字节）
            current_data_field = data[10:-1]

            # 如果当前中间部分报文和上一个不一样，打印出来
            if current_data_field != previous_data_field:
                print(f"\nReceived packet from {addr}")

                # 将数据打印为十六进制格式#将byte转换为大写十六进制并且连接成字符串
                hex_data = ' '.join(f'{byte:02X}' for byte in data) 
                print(f"Data (hex): {hex_data}")

                # 解析第11个字节
                byte11 = data[10]

                # 解析各个功能位并输出状态
                emergency_stop = (byte11 >> 1) & 1  # bit1: 急停
                horn = (byte11 >> 2) & 1            # bit2: 喇叭
                light = (byte11 >> 3) & 1           # bit3: 灯光
                parking_brake = (byte11 >> 5) & 1   # bit5: 驻车刹车
                reel_forward = (byte11 >> 7) & 1    # bit7: 卷盘正转

                # 打印各功能状态
                print(f"Emergency Stop (bit1): {'Triggered' if emergency_stop else 'Not Triggered'}")
                print(f"Horn (bit2): {'On' if horn else 'Off'}")
                print(f"Light (bit3): {'On' if light else 'Off'}")
                print(f"Parking Brake (bit5): {'Engaged' if parking_brake else 'Disengaged'}")
                print(f"Reel Forward (bit7): {'Active' if reel_forward else 'Inactive'}")

                # 更新保存的中间部分报文
                previous_data_field = current_data_field
        else:
            print("Received packet too short to process.")

    except KeyboardInterrupt:
        print("\nStopped by user")
        break
    except Exception as e:
        print(f"Error receiving packet: {e}")

# 关闭Socket
sock.close()
