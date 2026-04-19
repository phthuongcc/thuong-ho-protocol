# Mô phỏng tiết kiệm năng lượng (Energy Simulation)
# So sánh lượng dữ liệu và điện năng tiêu thụ giữa Blockchain truyền thống (Merkle) và Thương Hồ (Verkle)
# Tích hợp Google Gemini API để xuất báo cáo đánh giá tác động môi trường tự động.

import math
import os
import google.generativeai as genai

def get_gemini_environmental_insight(co2_saved, trees):
    """Gọi Gemini API để phân tích số liệu và đưa ra nhận định môi trường"""
    print("\n" + "="*65)
    print("🤖 GEMINI API: DYNAMIC ENVIRONMENTAL INSIGHT")
    print("="*65)
    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("⚠️ GEMINI_API_KEY not found in environment variables.")
        print("💡 Please run: export GEMINI_API_KEY='your_api_key' to see AI insights.")
        return

    try:
        genai.configure(api_key=api_key)
        # Sử dụng model Gemini 1.5 Flash (nhanh và tối ưu chi phí)
        model = genai.GenerativeModel('gemini-1.5-flash') 
        
        # Thiết kế Prompt đóng vai một nhà khoa học môi trường
        prompt = f"""
        Act as an expert environmental scientist analyzing Web3 sustainability. 
        A new decentralized protocol (Thuong Ho Protocol) just saved {co2_saved:.2f} kg of CO2 per validation cycle, 
        which is equivalent to planting {trees} trees annually compared to legacy architectures. 
        Write a short, punchy 2-sentence insight on why eliminating 'digital state bloat' is crucial for Earth Day and the future of green tech.
        """
        
        response = model.generate_content(prompt)
        print(f"🌍 Gemini Insight:\n{response.text.strip()}")
        print("="*65)
    except Exception as e:
        print(f"❌ API Error: {e}")

def simulate_energy_impact():
    print("="*65)
    print("THUONG HO PROTOCOL: GREEN TECH & EARTH IMPACT REPORT")
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
            
            # GỌI GEMINI API Ở QUY MÔ LỚN NHẤT ĐỂ TỔNG KẾT
            if tx == 10**9:
                get_gemini_environmental_insight(co2_saved, int(trees_equivalent))
                
        else:
            print("  ℹ️ Note: At small scale, proof sizes are comparable.")
        print("-" * 65)

if __name__ == "__main__":
    simulate_energy_impact()
