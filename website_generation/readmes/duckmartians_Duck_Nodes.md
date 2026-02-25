### Duck Nodes for ComfyUI: Hướng Dẫn Toàn Tập (Cài Đặt, Tính Năng & Quản Lý)

**Duck Nodes** được xây dựng dựa trên ba trụ cột chính: **Tải và tự động hóa dữ liệu**, **Tiện ích xử lý văn bản & hình ảnh**, và **Bảo mật cấp doanh nghiệp**.

### 📦 Cài đặt

**1. Tải và đặt extension**

Clone repository này vào thư mục `custom_nodes` của ComfyUI:

```bash
cd ComfyUI/custom_nodes
```

```bash
git clone https://github.com/duckmartians/Duck_Nodes.git
```

**2. Cài đặt dependencies**

Bộ node này tự động kiểm tra và cài đặt thư viện cần thiết khi khởi động ComfyUI.
Tuy nhiên, bạn có thể cài thủ công bằng lệnh sau trong môi trường của ComfyUI:

```bash
pip install -r requirements.txt
```

**`requirements.txt` bao gồm:**

```txt
pandas
requests
openpyxl
python-docx
aiohttp_session
bcrypt
Jinja2
```

### ✨ Các Nhóm Node Chức Năng

#### 1\. 📂 Nhóm Node Tải Dữ Liệu: Kho Prompt Vô Tận

Đây là nhóm node cốt lõi giúp tự động hóa quy trình sáng tạo của bạn. Thay vì phải sao chép-dán từng prompt, bạn có thể quản lý chúng trong các file quen thuộc.

  * **Các Node:**
      * `Duck - Load Google Sheet Row`: Đọc dữ liệu theo từng dòng từ Google Sheet công khai.
      * `Duck - Load Google Doc Line`: Đọc từng dòng văn bản từ Google Docs công khai.
      * `Duck - Load Excel Row`: Đọc dữ liệu từ file Excel (`.xlsx`) trên máy tính của bạn.
      * `Duck - Load Word Line`: Đọc từng đoạn văn từ file Word (`.docx`) trên máy.
      * `Duck - Load Prompt From File`: Đọc từng dòng từ file văn bản thuần túy (`.txt`).
  * **Điểm Mạnh:** Biến các file văn bản và bảng tính quen thuộc thành một kho prompt sống, dễ dàng quản lý và cập nhật. Khi kết hợp với tham số `seed` và chế độ lặp của ComfyUI, bạn có thể tự động chạy hàng trăm, hàng nghìn prompt khác nhau mà không cần can thiệp thủ công.
<img width="1028" height="830" alt="image" src="https://github.com/user-attachments/assets/5ca19a64-ce8a-459c-8785-8d940edd6f48" />


#### 2\. 🛠️ Nhóm Node Tiện Ích & Xử Lý Ảnh: Tinh Chỉnh Workflow

Nhóm này cung cấp các công cụ linh hoạt để xử lý văn bản và hình ảnh ngay trong ComfyUI.

  * **`Duck - Text Replacer`**
      * **Chức năng:** Tìm kiếm và thay thế một chuỗi ký tự trong văn bản đầu vào.
      * **Điểm Mạnh:** Cực kỳ hữu ích để tạo ra các biến thể prompt một cách nhanh chóng. Ví dụ, bạn có thể dùng một prompt mẫu và chỉ thay đổi tên nhân vật, màu sắc hoặc bối cảnh một cách tự động.
  * **`Duck - Add Text Overlay`**
      * **Chức năng:** Thêm một dải văn bản (text bar) lên trên hoặc dưới hình ảnh.
      * **Điểm Mạnh:** Đây là một công cụ đóng dấu (branding) và thêm chú thích chuyên nghiệp. Sức mạnh của nó nằm ở khả năng **tùy chỉnh toàn diện**: bạn có thể kiểm soát mọi thứ từ vị trí, căn lề, màu sắc, cỡ chữ, cho đến độ trong suốt của nền.

#### 3\. 🖼️ Nhóm Node Tạo Latent: Khởi Đầu Nhanh Chóng

Các node này giúp đơn giản hóa bước đầu tiên của mọi workflow: tạo ra một "khung tranh" (latent) trống với kích thước chuẩn.

  * **`Duck - Qwen Aspect Ratios`**
      * **Chức năng:** Cung cấp một danh sách các tỷ lệ khung hình và kích thước được tối ưu hóa riêng cho các mô hình AI của Qwen.
      * **Điểm Mạnh:** Giúp người dùng **đạt được chất lượng hình ảnh tốt nhất** mà không cần phải tra cứu hay ghi nhớ các thông số kỹ thuật phức tạp của model.
  * **`Duck - Empty Latent Image`**
      * **Chức năng:** Tạo latent trống từ một danh sách dài các kích thước và tỷ lệ khung hình phổ biến (1:1, 16:9, 4:3, v.v.).
      * **Điểm Mạnh:** Tiết kiệm thời gian và công sức so với việc nhập chiều rộng và chiều cao thủ công, khuyến khích người dùng thử nghiệm với các bố cục khung hình khác nhau một cách dễ dàng.

### 🛡️ Hệ Thống Đăng Nhập và Bảo Mật

Đây là tính năng độc đáo và đáng giá nhất của Duck Nodes, biến ComfyUI thành một dịch vụ web an toàn.

  * **Chức năng:** Tích hợp một trang đăng nhập chuyên nghiệp, yêu cầu xác thực trước khi truy cập vào giao diện ComfyUI. Hỗ trợ đa ngôn ngữ (Anh/Việt), cho phép thay đổi mật khẩu và có thể tắt đi nếu không cần thiết.
  * **Điểm Mạnh:**
      * Biến ComfyUI thành Dịch vụ An toàn: Cho phép bạn chạy ComfyUI trên một máy chủ từ xa và truy cập qua mạng mà không lo bị người khác can thiệp. Đây là một tính năng **cấp doanh nghiệp** mà hiếm có extension nào cung cấp.
<img width="1215" height="613" alt="image" src="https://github.com/user-attachments/assets/16a91665-2cb9-4bb7-9992-d050ca15b24a" />
<img width="1055" height="551" alt="image" src="https://github.com/user-attachments/assets/2eddced7-5e52-447c-bc07-661cb6021b84" />

### 🔑 Quản Lý Mật Khẩu

#### Hướng dẫn xóa mật khẩu (Reset)

Để xóa hoàn toàn mật khẩu đã đặt và quay lại màn hình thiết lập ban đầu, bạn cần xóa tệp tin lưu trữ thông tin đăng nhập.

**Các bước thực hiện:**

1.  **Tắt ComfyUI:** Đảm bảo rằng ComfyUI không đang chạy để tránh lỗi.
2.  **Đi tới thư mục `user`:** Mở thư mục cài đặt ComfyUI của bạn và tìm đến thư mục con có tên là `user`. Đường dẫn sẽ tương tự như sau:
      * `ComfyUI/user/`
3.  **Xóa tệp tin cấu hình:** Bên trong thư mục `user`, tìm và xóa tệp có tên là `PASSWORD`.
      * (Tùy chọn) Để reset hoàn toàn, bạn cũng có thể xóa tệp `login_config.json`.
<img width="761" height="366" alt="image" src="https://github.com/user-attachments/assets/f526ab22-afc5-4c1f-a586-4c3009941ed4" />

4.  **Khởi động lại ComfyUI:** Chạy lại ComfyUI.

Sau khi khởi động, bạn sẽ thấy lại màn hình thiết lập ban đầu. Tại đây, bạn có thể tạo một tài khoản và mật khẩu mới, hoặc nhấn **"Skip (Disable Login)"** để tắt hoàn toàn tính năng đăng nhập.
***

### Duck Nodes for ComfyUI: The Complete Guide (Installation, Features & Management)

**Duck Nodes** is a comprehensive toolkit that upgrades ComfyUI in every aspect. It is built on three main pillars: **Data Loading and Automation**, **Utility & Image Processing Nodes**, and **Enterprise-grade Security**.

### 📦 Installation

**1. Download and place the extension**

Clone this repository into the `custom_nodes` directory of your ComfyUI:

```bash
cd ComfyUI/custom_nodes
```

```bash
git clone https://github.com/duckmartians/Duck_Nodes.git
```

**2. Install dependencies**

This node pack automatically checks and installs the necessary libraries when ComfyUI starts.
However, you can install them manually with the following command in your ComfyUI environment:

```bash
pip install -r requirements.txt
```

**`requirements.txt` includes:**

```txt
pandas
requests
openpyxl
python-docx
aiohttp_session
bcrypt
Jinja2
```

### ✨ Functional Node Groups

#### 1\. 📂 Data Loading Nodes: An Endless Prompt Repository

This is the core group of nodes that helps automate your creative process. Instead of copy-pasting every prompt, you can manage them in familiar files.

  * **The Nodes:**
      * `Duck - Load Google Sheet Row`: Reads data row by row from a public Google Sheet.
      * `Duck - Load Google Doc Line`: Reads each line of text from a public Google Docs.
      * `Duck - Load Excel Row`: Reads data from an Excel file (`.xlsx`) on your computer.
      * `Duck - Load Word Line`: Reads each paragraph from a Word file (`.docx`) on your machine.
      * `Duck - Load Prompt From File`: Reads each line from a plain text file (`.txt`).
  * **Key Strengths:** This feature turns familiar text files and spreadsheets into a living, easy-to-manage prompt repository. When combined with the `seed` parameter and ComfyUI's batch mode, you can automatically run hundreds or thousands of different prompts without manual intervention.
<img width="1028" height="830" alt="image" src="https://github.com/user-attachments/assets/5ca19a64-ce8a-459c-8785-8d940edd6f48" />

#### 2\. 🛠️ Utility & Image Processing Nodes: Fine-tuning the Workflow

This group provides flexible tools for processing text and images directly within ComfyUI.

  * **`Duck - Text Replacer`**
      * **Functionality:** Finds and replaces a string of characters in the input text.
      * **Key Strengths:** Extremely useful for quickly creating prompt variations. For example, you can use a template prompt and automatically change only the character name, color, or setting.
  * **`Duck - Add Text Overlay`**
      * **Functionality:** Adds a text bar on top of or below an image.
      * **Key Strengths:** This is a professional tool for branding and captioning. Its power lies in its **comprehensive customization**: you can control everything from the position, alignment, color, and font size to the background's opacity.

#### 3\. 🖼️ Latent Generation Nodes: A Quick Start

These nodes simplify the first step of any workflow: creating an empty "canvas" (latent) with standard dimensions.

  * **`Duck - Qwen Aspect Ratios`**
      * **Functionality:** Provides a list of aspect ratios and dimensions specifically optimized for Qwen's AI models.
      * **Key Strengths:** Helps users **achieve the best image quality** without needing to look up or remember the model's complex technical specifications.
  * **`Duck - Empty Latent Image`**
      * **Functionality:** Creates an empty latent from a long list of common sizes and aspect ratios (1:1, 16:9, 4:3, etc.).
      * **Key Strengths:** Saves time and effort compared to manually entering width and height, and encourages users to easily experiment with different frame compositions.

### 🛡️ Login and Security System

This is the most unique and valuable feature of Duck Nodes, transforming ComfyUI into a secure web service.

  * **Functionality:** Integrates a professional login page that requires authentication before accessing the ComfyUI interface. It supports multiple languages (English/Vietnamese), allows for password changes, and can be disabled if not needed.
  * **Key Strengths:**
      * Transforms ComfyUI into a Secure Service: It allows you to run ComfyUI on a remote server and access it over the network without worrying about unauthorized access. This is an **enterprise-grade feature** rarely found in community extensions.
<img width="1215" height="613" alt="image" src="https://github.com/user-attachments/assets/16a91665-2cb9-4bb7-9992-d050ca15b24a" />
<img width="1055" height="551" alt="image" src="https://github.com/user-attachments/assets/2eddced7-5e52-447c-bc07-661cb6021b84" />

### 🔑 Password Management

#### How to Delete the Password (Reset)

To completely delete the set password and return to the initial setup screen, you need to delete the file that stores the login information.

**Steps:**

1.  **Shut down ComfyUI:** Ensure that ComfyUI is not running to avoid any errors.
2.  **Navigate to the `user` directory:** Open your ComfyUI installation folder and find the subdirectory named `user`. The path will look like this:
      * `ComfyUI/user/`
3.  **Delete the configuration files:** Inside the `user` directory, find and delete the file named `PASSWORD`.
      * (Optional) For a full reset, you can also delete the `login_config.json` file.
<img width="761" height="366" alt="image" src="https://github.com/user-attachments/assets/f526ab22-afc5-4c1f-a586-4c3009941ed4" />

4.  **Restart ComfyUI:** Run ComfyUI again.

After restarting, you will see the initial setup screen again. From here, you can create a new account and password, or press **"Skip (Disable Login)"** to turn off the login feature completely.
