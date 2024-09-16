import socket

# 创建UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('192.168.10.10', 9002))  # 监听电脑的IP和端口

print("Listening for UDP packets on 192.168.10.10:9002...")

# 保存上一条接收到的报文的数据域
previous_data_field = None

# 定义每个字节的bit描述
bit_definitions = {
    11: {
        1: "Emergency Stop",
        2: "Horn",
        3: "Light",
        5: "Parking Brake",
        7: "Reel Forward"
    },
    12: {
        0: "Reel Reverse",
        1: "Drill",
        2: "Walk",
        3: "Oil Pump Start",
        4: "Oil Pump Stop",
        5: "Roof Raise",
        6: "Roof Lower",
        7: "Swing Right"
    },
    13: {
        0: "Swing Left",
        1: "Drill Impact",
        2: "Full Speed Impact",
        3: "Thrust High",
        4: "Thrust Low",
        5: "Rear Leg Raise",
        6: "Rear Leg Lower",
        7: "Water Steam Control"
    },
    14: {
        1: "Top Button",
        2: "Engine Start",
        3: "Engine Stop"
    }
}

def parse_bits(byte, bit_definitions):
    """解析一个字节的bit位并返回触发的状态"""
    bit_status = {}
    for bit_position, label in bit_definitions.items():
        if (byte >> bit_position) & 1:  # 只在bit位为1时触发
            bit_status[label] = "Triggered"
    return bit_status

def process_byte(byte_number, data):
    """处理指定的字节，解析并打印触发的状态"""
    if byte_number in bit_definitions:
        byte = data[byte_number - 1]  # 获取指定字节
        status = parse_bits(byte, bit_definitions[byte_number])
        if status:
            print(f"\nByte{byte_number} Status (Triggered):")
            print(status)

while True:
    try:
        # 接收UDP数据包
        data, addr = sock.recvfrom(1024)
        
        # 确保报文长度为53字节
        if len(data) == 53:
            # 提取中间部分数据（第11个字节到倒数第二个字节）
            current_data_field = data[10:-1]

            # 如果当前中间部分报文和上一个不一样，打印出来
            if current_data_field != previous_data_field:
                print(f"\nReceived packet from {addr}")

                # 将数据打印为十六进制格式
                hex_data = ' '.join(f'{byte:02X}' for byte in data)
                print(f"Data (hex): {hex_data}")

                # 处理字节11到14的触发状态
                for byte_number in range(11, 15):
                    process_byte(byte_number, data)

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
