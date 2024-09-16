import socket

# 创建一个函数来解析单个字节的各个bit位
def parse_bits(byte, bit_definitions):
    """解析一个字节的bit位并返回对应状态"""
    bit_status = {}
    #@bit_position key  @label value
    for bit_position, label in bit_definitions.items():
        bit_status[label] = (byte >> bit_position) & 1
    return bit_status

# 打印解析结果
def print_bit_status(bit_status):
    """打印bit位的状态"""
    for label, status in bit_status.items():
        print(f"{label}: {'Active' if status else 'Inactive'}")

# 解析并打印第11个和第12个字节的状态
def process_packet(data):
    """处理数据报文,解析并打印特定字节的bit位状态"""
    byte11 = data[10]
    byte12 = data[11]

    # 第11个字节的bit定义
    byte11_bits = {
        1: "Emergency Stop (bit1)",
        2: "Horn (bit2)",
        3: "Light (bit3)",
        5: "Parking Brake (bit5)",
        7: "Reel Forward (bit7)"
    }
 
    # 第12个字节的bit定义
    byte12_bits = {
        0: "Reel Reverse (bit0)",
        1: "Drilling (bit1)",
        2: "Walking (bit2)",
        3: "Pump Start (bit3)",
        4: "Pump Stop (bit4)",
        5: "Roof Up (bit5)",
        6: "Roof Down (bit6)",
        7: "Rotate Right (bit7)"
    }

    # 解析并打印第11个字节
    print("\nByte 11 (Control Commands):")
    byte11_status = parse_bits(byte11, byte11_bits)
    print_bit_status(byte11_status)

    # 解析并打印第12个字节
    print("\nByte 12 (Control Commands):")
    byte12_status = parse_bits(byte12, byte12_bits)
    print_bit_status(byte12_status)

# 主函数处理UDP数据包接收和处理
def main():
    # 创建UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('192.168.10.10', 9002))  # 监听电脑的IP和端口

    print("Listening for UDP packets on 192.168.10.10:9002...")

    previous_data_field = None

    while True:
        try:
            # 接收UDP数据包
            data, addr = sock.recvfrom(1024)  # 最大接收1024字节

            # 确保报文长度为53字节
            if len(data) == 53:
                current_data_field = data[10:-1]

                # 如果当前报文与之前不同，则处理
                if current_data_field != previous_data_field:
                    print(f"\nReceived packet from {addr}")

                    # 将数据打印为十六进制格式
                    hex_data = ' '.join(f'{byte:02X}' for byte in data)
                    print(f"Data (hex): {hex_data}")

                    # 处理和解析报文
                    process_packet(data)

                    # 更新上一个报文记录
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

if __name__ == "__main__":
    main()
