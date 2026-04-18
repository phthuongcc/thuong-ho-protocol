
# Mô phỏng tiết kiệm năng lượng (Energy Simulation)
# So sánh lượng dữ liệu và điện năng tiêu thụ giữa Blockchain truyền thống (Merkle) và Thương Hồ (Verkle) qua 1 triệu giao dịch.

import math

def simulate_energy_impact():
    print("="*65)
    print("   THUONG HO PROTOCOL: GREEN TECH & EARTH IMPACT REPORT")
    print("Goal: Visualizing CO2 reduction in decentralized verification")
    print("="*65)
    
    # Giả định kỹ thuật: 
    # 1 GB dữ liệu truyền tải tiêu thụ khoảng 0.06 kWh (số liệu ước tính trung bình)
    # 1 kWh phát thải khoảng 0.4 kg CO2
    # Giả lập 1 triệu node xác thực toàn cầu
    KWH_PER_GB = 0.06
    CO2_PER_KWH = 0.4
    NETWORK_NODES = 1_000_000 
    
    transactions = [10**3, 10**4, 10**6, 10**9] # Từ 1 nghìn đến 1 tỷ giao dịch
    
    for tx in transactions:
        # Merkle: Mỗi proof cần log2(N) hashes, mỗi hash 32 bytes (0.03125 KB)
        # Merkle: O(log2 N) hashes * 32 bytes
        merkle_proof_kb = math.log2(tx) * 0.03125
        # Verkle: Cố định ~2KB cho mọi quy mô
        verkle_proof_kb = 2.0
        
        # Tính toán dữ liệu và CO2
        total_data_gb_merkle = (merkle_proof_kb * NETWORK_NODES) / (1024 * 1024)
        total_data_gb_verkle = (verkle_proof_kb * NETWORK_NODES) / (1024 * 1024)
        
        co2_merkle = total_data_gb_merkle * KWH_PER_GB * CO2_PER_KWH
        co2_verkle = total_data_gb_verkle * KWH_PER_GB * CO2_PER_KWH
        
        print(f"Scale: {tx:,} Transactions")
        print(f"  [Merkle] Proof: {merkle_proof_kb:.2f} KB | Network CO2: {co2_merkle:.4f} kg")
        print(f"  [Verkle] Proof: {verkle_proof_kb:.2f} KB | Network CO2: {co2_verkle:.4f} kg")
        
        if co2_merkle > co2_verkle:
            saving = ((co2_merkle - co2_verkle) / co2_merkle) * 100
            co2_saved = co2_merkle - co2_verkle
            # 1 cây xanh hấp thụ ~20kg CO2/năm. Giả định chạy 365 ngày/năm
            trees_equivalent = (co2_saved * 365) / 20 
            
            print(f"  🍀 Green Impact: Saved {saving:.1f}% carbon footprint")
            print(f"  🌍 Annual Impact: Equivalent to planting {int(trees_equivalent):,} trees/year")
        else:
            print("  ℹ️ Note: At small scale, proof sizes are comparable.")
        print("-" * 65)

if __name__ == "__main__":
    simulate_energy_impact()
