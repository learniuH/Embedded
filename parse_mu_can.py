import ctypes
from ctypes import *

# 加载 ControlCAN DLL
can_dll = ctypes.windll.LoadLibrary("./ControlCAN.dll")

# 定义必要的结构体
class VCI_CAN_OBJ(Structure):
    _fields_ = [("ID", c_uint),
                ("TimeStamp", c_uint),
                ("TimeFlag", c_byte),
                ("SendType", c_byte),
                ("RemoteFlag", c_byte),
                ("ExternFlag", c_byte),
                ("DataLen", c_byte),
                ("Data", c_ubyte * 8),
                ("Reserved", c_byte * 3)]

class VCI_INIT_CONFIG(Structure):
    _fields_ = [("AccCode", c_uint),
                ("AccMask", c_uint),
                ("Reserved", c_uint),
                ("Filter", c_byte),
                ("Timing0", c_byte),
                ("Timing1", c_byte),
                ("Mode", c_byte)]

# CAN 协议定义
CAN_PROTOCOLS = {
    '0x9c4': {
        'byte1': {
            'Bit0': '引擎启动',
            'Bit1': '引擎熄火',
            'Bit2': '前进档',
            'Bit3': '空档',
            'Bit4': '后退档',
            'Bit5': '加档',
            'Bit6': '减档',
            'Bit7': '拖车',
        },
        'byte2': {
            'Bit0': '驻车刹车',
            'Bit1': '急停开关',
            'Bit2': '前灯',
            'Bit3': '后灯',
            'Bit4': '喇叭',
        },
        'byte8': {
            'heartbeat': '心跳信号'
        }
    },
    '0x9c5': {
        'byte1': '油门',
        'byte2': '左转',
        'byte3': '右转',
        'byte4': '升臂',
        'byte5': '降臂',
        'byte6': '装料',
        'byte7': '卸料',
        'byte8': '辅助刹车'
    }
}

# 解析 CAN 报文
def parse_can_message(frame_id, frame_data):
    frame_id_hex = hex(frame_id)
    # print(frame_id_hex)
    protocol = CAN_PROTOCOLS.get(frame_id_hex)
    
    if not protocol:
        return f"未定义协议的帧ID: {frame_id_hex}, 数据: {[hex(x) for x in frame_data]}"
    
    parsed_data = {}
    for byte_index, byte_value in enumerate(frame_data):
        byte_key = f"byte{byte_index + 1}"
        if byte_key in protocol:
            if isinstance(protocol[byte_key], dict):
                byte_protocol = protocol[byte_key]
                for bit_position in range(8):
                    bit_value = (byte_value >> bit_position) & 1
                    bit_key = f"Bit{bit_position}"
                    if bit_key in byte_protocol:
                        parsed_data[f"{byte_key} - {byte_protocol[bit_key]}"] = bit_value
            else:
                parsed_data[byte_key] = byte_value
    return parsed_data

# 打印解析结果
def print_can_message(parsed_data):
    if isinstance(parsed_data, str):
        print(parsed_data)  # 对于未定义协议的帧，直接输出
    else:
        for key, value in parsed_data.items():
            if value:
                print(f"{key}: {value}")

# 接收 CAN 数据
def receive_can_data(device_type, device_index, can_index, max_frames=1000):
    can_obj = VCI_CAN_OBJ * max_frames  # 创建存储接收到数据的数组
    receive_buffer = can_obj()
    result = can_dll.VCI_Receive(device_type, device_index, can_index, byref(receive_buffer), max_frames, 100)
    return receive_buffer, result

# 启动 CAN 通道
def start_can(device_type, device_index, can_index):
    result = can_dll.VCI_StartCAN(device_type, device_index, can_index)
    if result == 1:
        print(f"CAN 通道 {can_index + 1} 启动成功!")
    else:
        print(f"CAN 通道 {can_index + 1} 启动失败!")
    return result

# 初始化 CAN 通道
def init_can(device_type, device_index, can_index, baud_rate=250):
    init_config = VCI_INIT_CONFIG()
    init_config.AccCode = 0x80000000
    init_config.AccMask = 0xFFFFFFFF
    init_config.Filter = 0  # 接收所有类型的报文
    # 根据波特率设置 Timing0 和 Timing1
    if baud_rate == 250:  # 250kbps
        init_config.Timing0 = 0x01
        init_config.Timing1 = 0x1C
    elif baud_rate == 500:  # 500kbps
        init_config.Timing0 = 0x00
        init_config.Timing1 = 0x1C
    else:
        print("未支持的波特率")
        return 0
    init_config.Mode = 0  # 正常模式

    result = can_dll.VCI_InitCAN(device_type, device_index, can_index, byref(init_config))
    if result == 1:
        # 启动 CAN 通道
        start_can(device_type, device_index, can_index)
    else:
        print(f"CAN 通道 {can_index} 初始化失败")
    return result

# 打开设备
def open_device(device_type, device_index, can_index):
    result = can_dll.VCI_OpenDevice(device_type, device_index, 0)
    if result == 1:
        # 初始化 CAN 通道
        init_can(device_type, device_index, can_index, baud_rate=250)
    else:
        print(f"设备 {device_index} 打开失败")
    return result

# 主函数
if __name__ == "__main__":
    device_type = 4  # 设备类型为 USBCAN-2A 或 CANalyst-II
    device_index = 0  # 设备索引

    # 创建一个字典，存储上一次的报文（以CAN ID为键，报文数据为值）
    previous_messages = {}

    # 打开 Canalyst 并初始化 ch1 和 ch2
    for can_index in [0, 1]:
        open_device(device_type, device_index, can_index)

    # 接收 两条通道上的 CAN 报文
    while True:
        for can_index in [0]:  # 轮询通道 0 和 1
            receive_buffer, result = receive_can_data(device_type, device_index, can_index)
            if result > 0:
                for i in range(result):
                    frame = receive_buffer[i]
                    frame_id = frame.ID
                    if frame_id == 0x9c4:
                        frame_data = frame.Data[:frame.DataLen - 1] # 心跳信号不做处理
                    else:
                        frame_data = frame.Data[:frame.DataLen]  # 获取当前帧的数据

                    # 将数据转换为元组便于比较
                    frame_data_tuple = tuple(frame_data)

                    # 检查此CAN ID是否已经有记录
                    if frame_id not in previous_messages or frame_id != 0x9c4 and previous_messages[frame_id] != frame_data_tuple or frame_id == 0x9c4 and previous_messages[frame_id][:7] != frame_data_tuple:
                        # 打印 CAN 数据
                        print(f"\nCAN_ID: {hex(frame_id)}, 数据: {[hex(x) for x in frame_data]}")
                        # 解析 CAN 报文
                        parsed_data = parse_can_message(frame_id, frame_data)
                        # 打印解析后的数据
                        print_can_message(parsed_data)
                        
                        # 记录当前帧数据
                        previous_messages[frame_id] = frame_data_tuple
