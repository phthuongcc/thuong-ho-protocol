// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";

contract MekongClimateFund is Ownable {
    struct Project {
        string name;
        uint256 fundingGoal;
        uint256 currentFunding;
        bool isVerified;
    }

    mapping(uint256 => Project) public projects;

    // Event mang tính minh bạch cao, ghi nhận cả bằng chứng xác thực
    event Funded(uint256 indexed projectId, uint256 amount, string verkleProof);

    // Constructor để khởi tạo Ownable
    constructor() Ownable(msg.sender) {}

    // Chỉ cho phép "Public Anchors" (Owner) đăng ký dự án đã qua kiểm định thực địa
    function registerProject(uint256 _id, string memory _name, uint256 _goal) public onlyOwner {
        projects[_id] = Project(_name, _goal, 0, true);
    }

    function fundProject(uint256 _id, string memory _verkleProof) public payable {
        // 1. Kiểm tra tính chính danh của dự án
        require(projects[_id].isVerified, "Project not verified by THP");
        
        // 2. Ràng buộc kỹ thuật về tính "Phi trạng thái" (Statelessness)
        // Đây là minh chứng cho việc tiết kiệm năng lượng/băng thông (Earth Day focus)
        require(bytes(_verkleProof).length > 0, "THP Proof required");
        require(bytes(_verkleProof).length <= 2048, "Exceeds THP stateless limit (2KB)");

        projects[_id].currentFunding += msg.value;
        
        emit Funded(_id, msg.value, _verkleProof);
    }
}
