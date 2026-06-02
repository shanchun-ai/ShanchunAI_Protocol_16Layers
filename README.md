[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](LICENSE)
[![SCAI Commercial License](https://img.shields.io/badge/Commercial-SCAI%20License-blue.svg)](legal/SCAI-COMMERCIAL-LICENSE-v1.0.md)

# 善春 AI 16 层安全协议 | ShanchunAI 16 Layers Protocol

**中文**：让 AI 从"简单对话"升级为可落地、可审计、合规安全、支持商业化的标准化运行框架。

**English**: Empower AI to evolve from simple dialogue into a standardized framework that is practical, auditable, compliant, secure and commercial-ready.

---

## 🔒 项目定位 | Project Positioning

**中文**：本项目并非普通提示词，而是一套自研 AI 底层交互协议。系统性解决行业三大痛点：AI 指令易被绕过、输出结果不可信、安全防御无法自主迭代。整套架构支持私有化部署、端到端校验与版本溯源。

**English**: This is not a regular prompt, but a self-developed underlying interaction protocol for AI. It systematically solves three major industry pain points: prompt injection vulnerabilities, unreliable outputs, and non-adaptive defense mechanisms. The whole architecture supports private deployment, end-to-end verification and version traceability.

---

## ⚠️ 许可协议 | License

本仓库采用**双协议**模式：

| 协议 | 适用场景 |
|------|----------|
| **CC BY-NC-SA 4.0** | 个人学习、研究、非商业使用 |
| **SCAI 商业许可协议 v1.0** | 任何商业用途（详见定义） |

> 🔒 **DNA溯源编码不可移除** · 🏷️ **SCAI商标未经授权不得使用** · 🛡️ **安全层保护不可绕过**

### 商业授权分层

| 用户类型 | 年营收 | 授权方式 |
|----------|--------|----------|
| 个人/非商业 | — | 完全免费 |
| 小微企业 | <100万元 | 协议免费，增值服务收费 |
| 中小企业 | 100万-5000万元 | 商业授权 99-499元/年 |
| 大型企业 | >5000万元 | 按需报价，含企业级支持 |

**强制约束**：DNA 溯源编码、SCAI 品牌标识禁止擅自移除、篡改；安全防御架构禁止关闭、绕过、删减。

商业合作：GitHub Issues 或邮件联系

---

## 🧠 核心架构：16 层串行闭环体系 | Core Architecture

**中文**：
- **防御模块（第 1-7 层）**：身份校验、合规风控、成本极限分析、跨领域迁移
- **溯源模块（第 8-12 层）**：多智能体辩论、上下文管理、DNA 溯源编码、版本管理
- **进化模块（第 13-16 层）**：对抗防御、样本变异、跨模型适配、实验知识沉淀

**English**:
- **Defense Module (Layer 1-7)**: Identity verification, compliance risk control, cost neutralization & cross-domain transfer
- **Traceability Module (Layer 8-12)**: Multi-agent debate, context management, DNA traceability code & version control
- **Evolution Module (Layer 13-16)**: Adversarial defense, sample mutation, cross-model adaptation & knowledge accumulation

完整架构定义文档：[spec/16-layers-spec-v2.0.md](spec/16-layers-spec-v2.0.md)

---

## 🚀 旗舰产品：蓝图指挥部·AI 开发梦之队 | Blueprint HQ

| 版本 | 文件 | 说明 |
|------|------|------|
| **V2.2（最新）** | [skills/blueprint-hq-v2.2.md](skills/blueprint-hq-v2.2.md) | 5角色（PM/Dev/QA/User/法务Agent）+ 不可逆操作清单 + 人类确认锁定 + 安全闭环 |
| V2.1（历史版本） | [skills/blueprint-hq-v2.1.md](skills/blueprint-hq-v2.1.md) | 4角色（PM/Dev/QA/User）+ 强制回归测试 + 数据治理 |

**中文**：内置虚拟角色形成完整软件开发团队。标准流程：需求定义 → 双向挑战辩论 → 代码开发 → 多维度测试 → 回归验证 → 量化验收 → 最终交付。核心优势：低算力消耗、高交付效率，个人/小团队一人即可达到传统5人开发小组的输出水平。

**English**: Equipped with virtual roles to form a complete software development team. Standard Workflow: Requirement Definition → Two-way Debate & Challenge → Coding Development → Multi-dimensional Testing → Regression Verification → Quantitative Acceptance → Final Delivery. Core Advantages: Low compute overhead & high delivery efficiency. One person can match the output of a traditional 5-person team.

**实测验证**：裁判AI综合评分 4.8/5.0 | 详见 [benchmark/judge-report-20260526.md](benchmark/judge-report-20260526.md)

---

## 🔥 适用人群与价值 | Target Users & Value

**中文**：
- **中小企业**：解决 AI 使用合规、数据安全、结果可追溯难题
- **个人/小型开发团队**：大幅压缩开发周期与算力成本，提升产品质量
- **行业从业者/AI 学习者**：搭建标准化 AI 使用规范，规避使用风险
- **创业者**：快速落地产品想法，低成本完成项目验证

**English**:
- **SMEs**: Solve problems of AI compliance, data security and traceability
- **Individual & Small Development Teams**: Shorten development cycles, reduce computing costs and improve product quality
- **Practitioners & AI Learners**: Build standardized AI usage rules and avoid risks
- **Entrepreneurs**: Turn ideas into products rapidly and verify projects at low cost

---

## 📂 仓库结构 | Repository Structure
ShanchunAI-Protocol-16Layers/
├── README.md # 本文件
├── LICENSE # CC BY-NC-SA 4.0
├── .github/skills/ # Copilot技能包
│ ├── scai-security-governance/SKILL.md # 安全治理
│ ├── scai-blueprint-hq/SKILL.md # 蓝图指挥部
│ └── scai-prompt-guard/SKILL.md # 提示词安全卫士
├── spec/
│ └── 16-layers-spec-v2.0.md # 17层架构V2.3
├── code/
│ ├── dna_encoder.py # DNA溯源编码生成器
│ └── security_scorer.py # 五维安全评分计算器
├── skills/
│ ├── README.md # 技能商店橱窗
│ ├── blueprint-hq-v2.1.md # 蓝图指挥部V2.1
│ └── blueprint-hq-v2.2.md # 蓝图指挥部V2.2
├── benchmark/
│ ├── judge-report-20260526.md # 裁判AI评分报告
│ └── security-benchmark-v1.0.json # 安全基准测试集
├── legal/
│ └── SCAI-COMMERCIAL-LICENSE-v1.0.md # 商业许可协议
└── docs/
├── iteration-roadmap.md # 迭代路线图
├── methodology-comparison.md # 行业方法论对比
└── industry-comparison.md # 行业对比分析

---

## 🛒 商业服务与合作 | Commercial Services & Cooperation

**安远县趣玩网络科技工作室** 提供全链路商业化服务：

- 企业级 AI 协议部署与私有化落地
- 定制化 AI 技能包开发
- 16 层协议技术培训与认证
- 专属商业授权与长期技术支持

**定价模式**：根据企业规模与需求按需报价，支持对公合作与发票开具。

**联系方式 | Contact**：
- 微信：EZT8888888
- 邮箱：352522833@qq.com
- 公众号：善春智诊
- 技术社区：CSDN / 掘金 搜索「善春智诊」

---

## 🧱 关于善春 AI | About ShanchunAI

善春 AI 由独立开发者善春创立，历时 18 个月系统性打磨，构建出 156 个功能模块、完整协议体系与多智能体开发系统。项目坚持"协议优先，技术为本"的研发理念，致力于打造人人可用、安全可靠的 AI 底层标准。

核心产品已上架 **小米应用商店** 与 **腾讯元器**，服务覆盖 7 个行业场景。

**研发理念**：我不写提示词，我设计认知架构。协议优先，对话次之。

---

## ⭐ 支持与关注 | Support & Follow

**中文**：如果本项目对你有帮助，欢迎 Star、Fork、Watch。欢迎全球开发者交流技术、洽谈合作。

**English**: If this project helps you, please Star, Fork and Watch. Developers worldwide are welcome to collaborate and discuss business cooperation.

---

## 关于作者 | About the Author

**善春（Shan Chun）| AI Security Protocol Researcher & Founder**

跨领域技术背景，深耕 AI 安全协议与多智能体架构设计。基于个人电脑与移动设备完成全栈开发，独立构建 156 个 AI 功能模块，覆盖 7 个行业领域。产品已上架小米应用商店与腾讯元器。

**技术信仰**：协议优先，对话次之。

**English**: Cross-disciplinary technical background, specializing in AI security protocols and multi-agent architecture design. Completed full-stack development using personal computing resources, independently built 156 AI functional modules across 7 industries. Products listed on Xiaomi App Store and Tencent Yuanqi.

**Technical Belief**: Protocol first, dialogue second.

---

**开源协议：SCAI-16Layers**
**GitHub：https://github.com/shanchun-ai/ShanchunAI_Protocol_16Layers**
