# 1. 前端（全平台覆盖）
|平台|方案|优势|
| ------------ | ------------ | ------------ |
|web端|Vue3 + Vite + Element Plus|响应式设计，适配PC/移动浏览器|
|App|Uniapp（编译为Android/iOS）|一套代码生成原生App，复用小程序逻辑|
|微信/抖音小程序|Uniapp（跨平台编译）|直接编译为各平台小程序，省去重复开发|

关键工具：
Uniapp：用Vue语法写小程序/App，插件市场有现成组件。
Vite：秒级热更新，提升Web开发效率。

# 2. 后端（数据中台）
|需求|技术选型|理由|
| ------------ | ------------ | ------------ |
|API服务|FastAPI（Python）|异步支持、自动文档、代码简洁|
|数据库操作|SQLAlchemy + PostgreSQL|支持复杂查询，JSONB字段灵活存储爬虫数据|
|爬虫/自动化|Playwright（Python）|比Selenium更快的无头浏览器操作|
|文件处理|python-docx / openpyxl|直接操作Word/Excel|
|任务队列|Celery + Redis（可选）|异步处理耗时操作（如大批量文件生成）|

# 3. 模块职责说明 
|模块|职责|依赖关系|
| ------------ | ------------ | ------------ |
|API入口层|接收HTTP请求，路由到具体模块|依赖所有业务模块|
|用户服务模块|用户认证、权限管理|依赖数据库核心层|
|数据操作模块|数据库CRUD、复杂查询|依赖数据库核心层|
|文件处理模块|Word/Excel/PDF生成与解析|无依赖（可独立单元测试）|
|爬虫/自动化模块|网页爬取、无头浏览器操作|依赖数据库存储爬取结果|
|数据库核心层|封装数据库连接、ORM操作|无依赖（最底层）|

# 4. 中台基本结构
backend/
├── app/                      # FastAPI 应用层
│   ├── __init__.py           # 应用初始化
│   ├── main.py               # FastAPI 主入口，路由聚合
│   ├── dependencies.py       # 全局依赖（如数据库会话、认证）
│   ├── schemas/              # API 数据模型（Pydantic）
│   │   └── task.py           # 任务请求/响应模型
│   │
│   └── api/                  # 可选的子路由分组（大型项目适用）
│       ├── v1/               # 版本1路由
│       │   ├── __init__.py
│       │   └── health.py     # 健康检查路由（示例）
│       │   └── auth.py       # 用户鉴权
│       └── v2/               # 版本2路由（未来扩展）
│
├── utils/                    # 基础工具库（无业务逻辑）
│   ├── db/                   # 数据库核心
│   │   ├── __init__.py
│   │   ├── connector.py      # 数据库连接管理（SQLAlchemy）
│   │   ├── models.py         # ORM 模型定义
│   │   └── crud.py           # 基础增删改查操作（可选）
│   │
│   ├── file_ops/             # 文件操作
│   │   ├── __init__.py
│   │   ├── excel.py          # Excel 处理（openpyxl）
│   │   ├── word.py           # Word 处理（openpyxl）
│   │   ├── pdf.py            # PDF 处理（PyPDF2/reportlab）
│   │   └── storage.py        # 文件存储（本地/OSS 封装）
│   │
│   ├── crawler/              # 爬虫核心
│   │   ├── __init__.py
│   │   ├── browser.py        # Playwright 封装
│   │   ├── parser.py         # 数据解析器（BeautifulSoup）
│   │   └── validator.py      # 数据清洗验证
│   │
│   ├── scheduler/            # 定时任务工具
│   │   ├── __init__.py
│   │   ├── celery_app.py     # Celery 实例化配置
│   │   └── decorators.py     # 任务装饰器（如重试逻辑）
│   │
│   └── helpers.py            # 通用辅助函数（加密、日期等）
│
├── modules/                  # 业务服务模块（暴露API）
│   ├── auth/                 # 用户认证模块
│   │   ├── __init__.py
│   │   ├── service.py        # 登录/注册/权限逻辑
│   │   ├── router.py         # 路由定义（FastAPI APIRouter）
│   │   └── models.py         # 业务专属模型（可选）
│   │
│   ├── report/               # 报表服务模块
│   │   ├── __init__.py
│   │   ├── service.py        # 报表生成逻辑
│   │   ├── router.py         # 路由定义
│   │   └── templates/        # 报表模板（Jinja2 HTML/Excel）
│   │
│   └── task/                 # 任务管理模块
│       ├── __init__.py
│       ├── tasks.py          # 定时任务具体实现
│       ├── router.py         # 任务API路由
│       └── models.py          # 任务状态模型
│
├── config/                   # 配置管理
│   ├── __init__.py
│   ├── settings.py           # 主配置（加载环境变量）
│   ├── celery.py             # Celery 专属配置
│   └── security.py           # 安全相关配置（JWT密钥等）
│
├── scripts/                  # 数据库脚本
│
├── source/                   # 静态文件
│
├── requirements.txt          # 依赖列表
├── README.md                 # 项目说明
└── .env.example              # 环境变量模板


# 5. 依赖安装
pip install -r .\requirements.txt
需要单独安装：playwright install chromium


