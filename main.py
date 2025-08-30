import json
from datetime import datetime

# Example JSON inputs (two different formats)
json_device1 = '{"device_id": "A123", "time": "2023-08-15 12:30:45", "temperature": 35.6}'
json_device2 = '{"id": "B456", "timestamp": 1692097845, "temp": 33.2}'

def convert_device1(data):
    """Convert device1 format to unified format"""
    parsed = json.loads(data)
    return {
        "device_id": parsed["device_id"],
        "timestamp": datetime.strptime(parsed["time"], "%Y-%m-%d %H:%M:%S").isoformat(),
        "temperature": parsed["temperature"]
    }

def convert_device2(data):
    """Convert device2 format to unified format"""
    parsed = json.loads(data)
    return {
        "device_id": parsed["id"],
        "timestamp": datetime.fromtimestamp(parsed["timestamp"]).isoformat(),
        "temperature": parsed["temp"]
    }

if __name__ == "__main__":
    unified1 = convert_device1(json_device1)
    unified2 = convert_device2(json_device2)

    print("Unified Device 1:", unified1)
    print("Unified Device 2:", unified2)
