import csv
import pickle

def read_csv(filename):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f'{filename} not found.')
        return []

def save_csv(filename, data, fieldnames):
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
    except Exception as e:
        print(f'Error saving {filename}: {e}')

def save_binary(filename, data):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(data, file)
    except Exception as e:
        print(f'Error saving {filename}: {e}')

def read_binary(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        print(f'{filename} not found.')
        return []

def print_inventory(data):
    for item in data:
        print(item)

if __name__ == '__main__':
    inventory = read_csv('Mars_Base_Inventory_List.csv')
    sorted_inventory = sorted(inventory, key=lambda x: float(x['Flammability']), reverse=True)

    high_flammability = [item for item in sorted_inventory if float(item['Flammability']) >= 0.7]
    print('Items with high flammability:')
    print_inventory(high_flammability)

    save_csv('Mars_Base_Inventory_danger.csv', high_flammability, fieldnames=sorted_inventory[0].keys())
    save_binary('Mars_Base_Inventory_List.bin', sorted_inventory)

    # 이진 파일 읽기 및 출력
    binary_inventory = read_binary('Mars_Base_Inventory_List.bin')
    print('Inventory from binary file:')
    print_inventory(binary_inventory)

    # 텍스트 파일과 이진 파일의 차이점 및 장단점 설명
    print("""
    텍스트 파일은 인간이 읽을 수 있는 텍스트로 저장되는 파일 형식입니다. 이진 파일은 데이터를 이진 형식(0과 1)으로 저장하는 파일 형식입니다.
    
    텍스트 파일의 장점:
    - 인간이 직접 읽고 이해할 수 있습니다.
    - 텍스트 편집기에서 쉽게 수정할 수 있습니다.
    
    텍스트 파일의 단점:
    - 일부 데이터 형식(예: 이미지, 오디오)을 비효율적으로 저장할 수 있습니다.
    
    이진 파일의 장점:
    - 모든 종류의 데이터를 저장할 수 있으며, 종종 더 효율적으로 저장할 수 있습니다.
    
    이진 파일의 단점:
    - 인간이 직접 읽을 수 없으며, 특정 프로그램이나 코드를 사용해야만 내용을 해석할 수 있습니다.
    """)
