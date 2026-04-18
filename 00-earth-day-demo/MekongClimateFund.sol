// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

/**
 * @title MekongClimateFund
 * @dev Hợp đồng quản lý giải ngân ODA/ESG trong hệ sinh thái Thuong Ho Protocol.
 * Tích hợp ReentrancyGuard và các ràng buộc phi trạng thái (Statelessness).
 */
contract MekongClimateFund is Ownable, ReentrancyGuard {
    struct Project {
        string name;
        uint256 fundingGoal;
        uint256 currentFunding;
        bool isVerified;
    }

    // Quản lý danh sách các dự án thích ứng biến đổi khí hậu
    mapping(uint256 => Project) public projects;

    // Sự kiện sử dụng 'indexed' để dễ dàng lọc và truy vấn dữ liệu từ phía Frontend
    event Funded(uint256 indexed projectId, uint256 amount, string verkleProof);
    event Withdrawn(uint256 indexed projectId, uint256 amount);

    // Khởi tạo hợp đồng với người sở hữu (Owner) là Public Anchor
    constructor() Ownable(msg.sender) {}

    /**
     * @dev Đăng ký dự án mới sau khi đã xác minh thực địa. 
     */
    function registerProject(uint256 _id, string memory _name, uint256 _goal) public onlyOwner {
        projects[_id] = Project(_name, _goal, 0, true);
    }

    /**
     * @dev Gửi tiền ủng hộ dự án kèm bằng chứng Verkle Proof. 
     */
    function fundProject(uint256 _id, string memory _verkleProof) public payable {
        require(projects[_id].isVerified, "Project not verified by THP nodes");
        
        // Ràng buộc về kích thước bằng chứng (Trọng tâm của tính Phi trạng thái và Green Tech)
        require(bytes(_verkleProof).length > 0, "THP Proof required");
        require(bytes(_verkleProof).length <= 2048, "Exceeds THP stateless limit (2KB)");

        projects[_id].currentFunding += msg.value;
        
        emit Funded(_id, msg.value, _verkleProof);
    }

    /**
     * @dev Giải ngân quỹ khi dự án đạt mục tiêu.
     * Sử dụng 'nonReentrant' để ngăn chặn mọi nỗ lực tấn công gọi lại (Reentrancy attack).
     */
    function withdrawFunding(uint256 _id) public onlyOwner nonReentrant {
        Project storage project = projects[_id];
        require(project.currentFunding > 0, "No funds available");
        require(project.currentFunding >= project.fundingGoal, "Funding goal not yet reached");

        uint256 amount = project.currentFunding;
        
        // Mẫu Check-Effects-Interactions: Đưa số dư về 0 trước khi thực hiện chuyển tiền
        project.currentFunding = 0; 

        // Chuyển tiền tới địa chỉ ví điều phối dự án (Owner) bằng phương thức .call an toàn
        (bool success, ) = owner().call{value: amount}("");
        require(success, "Transfer failed");

        emit Withdrawn(_id, amount);
    }

    /**
     * @dev Hàm xem trạng thái hiện tại của một dự án.
     */
    function getProjectDetails(uint256 _id) public view returns (
        string memory name, 
        uint256 goal, 
        uint256 current, 
        bool verified
    ) {
        Project memory p = projects[_id];
        return (p.name, p.fundingGoal, p.currentFunding, p.isVerified);
    }
}
