# Tastify 网站分析

## 已分析页面

### 1. 登录页面 (Sign In)
- **URL**: https://app.tastify.com/sign-in
- **主要元素**:
  - Tastify Logo
  - 语言选择器 (English)
  - 邮箱输入框
  - 密码输入框
  - 登录按钮
  - 忘记密码链接
  - 注册链接
- **设计特点**:
  - 紫色和橙色为主色调
  - 现代插画风格
  - 简洁的表单设计
  - 响应式布局

### 2. 注册页面 (Sign Up)
- **URL**: https://app.tastify.com/sign-up
- **主要元素**:
  - Tastify Logo
  - 语言选择器 (English)
  - 邮箱输入框
  - 用户角色选择 (多选项):
    - Quality Control
    - Barista
    - Trader
    - Homebrewer
    - Coffee Buyer
    - Owner
    - Educator
    - Judges
    - Logistic
    - Other
  - 组织类型选择:
    - Farmers/Cooperative/Exporter/Miller
    - Importer
    - Wholesale roaster
    - Retail roaster
    - NGO
    - Education
  - Q Grader 资质确认 (Yes/No)
- **设计特点**:
  - 与登录页面保持一致的设计风格
  - 分步表单设计
  - 清晰的分类和选项布局

### 3. 主页/仪表盘 (Dashboard)
- **主要元素**:
  - 欢迎信息 ("Welcome, [用户名]!")
  - 快速访问卡片 (Cuppers, Start cupping, Samples)
  - 活动摘要区域 (My latest activity)
  - 品鉴生产力信息 (Samples Cupped, Cupping Sessions)
  - 即将到来的品鉴会话日历
- **设计特点**:
  - 卡片式布局
  - 图标和插图丰富
  - 数据可视化展示
  - 清晰的信息层次结构

### 4. 样品管理页面 (Samples)
- **主要元素**:
  - 样品列表/表格 (当前显示"No results found")
  - 排序和筛选选项
  - 操作下拉菜单，包含:
    - New Sample
    - Add multiple samples
    - Edit Sample
    - New Shipment
    - New Cupping Session
    - Compare
    - Share
    - Download To CSV
    - Download All To CSV
    - Generate Combined Report
    - Generate Label
    - Advance search
  - 列表/网格视图切换
- **设计特点**:
  - 数据表格布局
  - 丰富的操作选项
  - 空状态设计 (显示友好的无数据提示)

### 5. 样品信息页面 (Sample Information)
- **主要元素**:
  - 返回按钮
  - 样品信息表单，包含多个字段:
    - 样品名称、国家、类型、等级
    - 购买等级、供应商/制造商、生产商名称
    - 购买合同参考、销售合同参考
    - 策略、客户、客户代码
    - 各种日期字段 (接收日期、发货日期、到达日期、结果日期)
    - 收获、外部识别、参考编号
    - 咖啡处理、认证、首选品鉴协议
    - 品种、重量、年份、袋数
    - 袋重、水分、水活性、密度
    - 温度、质量、体积
    - 位置、装运月份、货物/船舶
    - 集装箱编号、批号/ICO标记、快递
    - 跟踪编号、备注和描述
  - 自定义字段按钮
  - 保存和放弃按钮
- **设计特点**:
  - 结构化表单布局
  - 分类字段组织
  - 日期选择器和下拉菜单
  - 输入验证

### 6. 品鉴会话页面 (Cupping Sessions)
- **主要元素**:
  - 会话列表 (当前显示"No results found")
  - "New cupping session"按钮
  - 导出选项
  - 筛选器
  - 列表/网格视图切换
- **设计特点**:
  - 与样品页面类似的布局
  - 鼓励创建新会话的设计

### 7. 创建品鉴会话页面 (Start your cupping session)
- **主要元素**:
  - 返回按钮
  - 会话名称和编辑按钮
  - "Start cupping now"按钮
  - 日期和时间选择器 (开始日期/时间，结束日期/时间)
  - 位置输入
  - 描述文本区域
  - 样品ID结构选择 (Numbers/Digit/Letter)
  - 品鉴协议下拉菜单
  - 样品数量设置
  - 盲品选项
  - 组合品鉴选项
  - 自定义杯数选项
  - 邀请品鉴师部分
  - 保存和放弃按钮
- **设计特点**:
  - 结构化表单
  - 分步设置流程
  - 协作功能

### 8. 品鉴师管理页面 (Cuppers)
- **主要元素**:
  - "Invite member"按钮
  - "Upgrade plans"按钮
  - 统计卡片 (Members, Admins, Pending invites, Seats available)
  - 搜索框
  - 品鉴师列表表格，包含:
    - 名称
    - 是否可创建品鉴会话
    - 管理员权限
    - 活动状态
    - 最后活动时间
  - 分页控件
- **设计特点**:
  - 团队管理界面
  - 权限控制
  - 用户状态可视化

## 网站整体功能和特点

基于分析的所有页面，Tastify是一个专业的咖啡品鉴管理平台，提供以下核心功能:

1. **用户和权限管理**
   - 用户注册和登录
   - 团队成员管理
   - 角色和权限控制

2. **样品管理**
   - 详细的样品信息记录
   - 样品分类和标记
   - 样品批次和物流跟踪

3. **品鉴会话管理**
   - 创建和安排品鉴会话
   - 邀请品鉴师参与
   - 设置品鉴协议和参数

4. **数据分析和报告**
   - 生成综合报告
   - 数据导出 (CSV)
   - 活动跟踪和统计

5. **协作功能**
   - 团队协作品鉴
   - 结果共享
   - 比较分析

## 设计特点

1. **UI设计**
   - 紫色和橙色为主色调
   - 现代简约风格
   - 卡片式布局
   - 响应式设计

2. **导航结构**
   - 左侧固定侧边栏
   - 主要功能分类清晰
   - 面包屑导航
   - 上下文相关操作菜单

3. **交互设计**
   - 丰富的表单控件
   - 下拉菜单和模态框
   - 列表/网格视图切换
   - 空状态友好提示

## 技术栈规划

计划使用以下技术栈实现类似网站:

1. **前端框架**: Vue 3 (Composition API)
2. **UI组件库**: Element Plus (更适合实现类似界面)
3. **状态管理**: Pinia
4. **路由**: Vue Router
5. **HTTP客户端**: Axios
6. **CSS预处理器**: SCSS
7. **构建工具**: Vite
8. **图标**: Font Awesome 或 Material Icons
9. **图表**: Chart.js 或 ECharts (用于数据可视化)
