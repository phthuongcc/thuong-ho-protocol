*/
Mô phỏng tiết kiệm năng lượng (Energy Simulation)
So sánh lượng dữ liệu và điện năng tiêu thụ giữa Blockchain truyền thống (Merkle) và Thương Hồ (Verkle) qua 1 triệu giao dịch.
/*

import math

def simulate_energy_impact():
    print("--- THUONG HO PROTOCOL: GREEN TECH SIMULATION ---")
    print("Goal: Visualizing CO2 reduction in decentralized verification\n")
    
    # Giả định: 1 GB dữ liệu truyền tải tiêu thụ khoảng 0.06 kWh (số liệu ước tính trung bình)
    # 1 kWh phát thải khoảng 0.4 kg CO2
    KWH_PER_GB = 0.06
    CO2_PER_KWH = 0.4
    
    transactions = [10**3, 10**4, 10**6, 10**9] # Từ 1 nghìn đến 1 tỷ giao dịch
    
    for tx in transactions:
        # Merkle: Mỗi proof cần log2(N) hashes, mỗi hash 32 bytes (0.03125 KB)
        merkle_proof_kb = math.log2(tx) * 0.03125
        
        # Verkle: Cố định ~2KB cho mọi quy mô
        verkle_proof_kb = 2.0
        
        # Tính toán cho 1 triệu node xác thực cùng lúc (mô phỏng mạng lưới lớn)
        network_nodes = 1_000_000
        total_data_gb_merkle = (merkle_proof_kb * network_nodes) / (1024 * 1024)
        total_data_gb_verkle = (verkle_proof_kb * network_nodes) / (1024 * 1024)
        
        co2_merkle = total_data_gb_merkle * KWH_PER_GB * CO2_PER_KWH
        co2_verkle = total_data_gb_verkle * KWH_PER_GB * CO2_PER_KWH
        
        print(f"Scale: {tx:,} Transactions")
        print(f"  [Merkle] Proof: {merkle_proof_kb:.2f} KB | Network CO2: {co2_merkle:.4f} kg")
        print(f"  [Verkle] Proof: {verkle_proof_kb:.2f} KB | Network CO2: {co2_verkle:.4f} kg")
        
        if co2_merkle > co2_verkle:
            saving = ((co2_merkle - co2_verkle) / co2_merkle) * 100
            print(f"  🍀 Green Impact: Saved {saving:.1f}% carbon footprint per validation cycle")
        else:
            print("  ⚠️ Scale is small: Standard Merkle is still efficient at this level.")
        print("-" * 50)

if __name__ == "__main__":
    simulate_energy_impact()
