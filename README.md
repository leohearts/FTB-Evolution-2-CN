# FTB Evolution 2 简体中文汉化

为 **FTB Evolution 2 1.6.3** 提供简体中文翻译, 覆盖任务书、整合包自定义文案、模组界面与游戏内手册. 本项目结合人工翻译与经审校的上游中文, 保留来源、术语裁决和版本适配记录.

当前目标为 Minecraft **26.1.2**. 汉化包已通过静态检查和发布包校验, **尚未安装到本机游戏实例或完成游戏内验收**, 仍需检查排版、手册链接、配方显示和交互效果.

## 汉化范围

| 内容 | 当前进展 |
| --- | --- |
| 任务书 | 已适配 1.6.3, 覆盖 42 个可见章节、4,194 个语言键 |
| 整合包特色内容 | 已分批处理商店、支持对话及相关语言和运行时提示; FancyMenu 图片内嵌文字仍待处理 |
| 模组文本 | 已完成第 001-367 批范围内的物品、方块、界面、提示等文本 |
| 游戏内手册 | 已处理指南、GuideME / Markdown / MDX、Patchouli 与 Stellaris Wiki 等内容; 补充手册共 322 篇, 另有 571 个 Patchouli 可见字段 |
| CFPA 复用 | 按当前英文源逐条审校, 采用适用的跨版本及固定 PR 译文, 以独立覆盖维护 |

以建筑、装饰为主要用途的模组不新增专门翻译, 已有中文继续保留. 整合包任务书中的相关章节仍完整翻译. 具体排除项见 [翻译范围清单](localization/language_scope.json).

部分专名和代码内硬编码界面保留英文, 包括 Nodeworks 的硬编码 UI. 当前盘点范围内文本已通过静态检查, 不代表所有实际游戏界面都已验收. 详细范围、产物组成与边界见 [汉化进度](localization/reports/verified-progress-summary.md)、[1.6.3 汇总包说明](localization/reports/release-pack-1.6.3.md) 和 [近期反馈修复](localization/feedback_20261019/README.md).

## 获取与安装

仓库保存翻译源码与文本资源, `dist/` 下的发布压缩包不随 Git 提交. GitHub 的 **Download ZIP 是源码包**, 不能直接作为资源包加载. 当前可按下方说明从源码构建安装包.

构建后会得到两种 ZIP:

| 文件 | 用途 |
| --- | --- |
| `FTB-Evolution-2-1.6.3-zh_CN.zip` | 资源包, 提供语言与手册覆盖 |
| `FTB-Evolution-2-1.6.3-zh_CN-install.zip` | 完整安装包, 另含任务书语言、整合包数据、数据包和运行时脚本 |

完整汉化需要安装包中的实例文件, 仅启用资源包无法覆盖任务书和部分交互文案.

1. 确认使用 FTB Evolution 2 **1.6.3**, 关闭游戏并备份将被覆盖的文件.
2. 解压完整安装包, 按包内 `INSTALL.md` 将文件合并到游戏实例的对应目录. 内层资源包 ZIP 保持压缩状态, 放入 `resourcepacks/`.
3. 启动游戏, 将语言设为简体中文, 在资源包界面启用本项目资源包并移到最高优先级.
4. 重载资源或重启客户端, 检查任务书、物品名称和手册显示.

更新整合包后应重新确认版本兼容性. 请勿将仓库中的整个 `.minecraft/` 目录覆盖到游戏实例. 产物组成、安装脚本与还原方式见 [构建与安装说明](localization/reports/release-pack-1.6.3.md).

## 一键打包

下载本仓库的 [源码 ZIP](https://github.com/AstronW/FTB-Evolution-2-CN/archive/refs/heads/main.zip) 并解压. 电脑需安装 [Python 3.8 或更新版本](https://www.python.org/downloads/), 不需要了解 Python 或安装额外的库; Windows 安装时勾选 **Add python.exe to PATH**.

- **Windows**: 双击解压目录中的 `build.cmd`.
- **Linux / macOS**: 在解压目录打开终端, 运行一条命令:

  ```bash
  ./build.sh
  ```

脚本会自动打包并校验, 完成后在 `dist/` 文件夹中找到 `FTB-Evolution-2-1.6.3-zh_CN-install.zip`, 按上方安装步骤使用即可. 同时生成单独的资源包 ZIP 和 SHA-256 清单.

打包只使用仓库内已有资源, 不需要安装游戏、下载模组或 CFPA, 也不需要修改配置和填写游戏路径. 维护译文与运行完整源文检查的说明见 [AGENTS.md](AGENTS.md).

## 仓库结构

| 路径 | 内容 |
| --- | --- |
| `localization/` | 可维护译文、术语表、构建工具、源文清单和审校报告 |
| `.minecraft/` | 翻译工作副本中的源文及输出文本, 与实际游戏实例分开 |
| `review/` | 英中对照审查网页源码, 使用方式见 [审查网页说明](review/README.md) |
| `docs/research/` | 上游译文复用等研究记录 |
| `project.json` | 目标版本、实例路径与各组件基线 |

模组 JAR、完整 CFPA 克隆、下载压缩包、缓存和 Node 依赖不随仓库分发.

## 反馈与贡献

欢迎通过 [Issues](https://github.com/AstronW/FTB-Evolution-2-CN/issues) 反馈漏译、误译、术语冲突和显示问题. 请尽量提供整合包版本、相关模组或手册页面、当前文本、预期译法及截图; 如有其他资源包, 请说明加载顺序.

提交译文前请阅读 [翻译风格](localization/STYLE.md) 与 [术语约定](localization/TERMINOLOGY.md). 中文译文统一使用英文半角标点, 保留资源 ID、占位符、命令和点击动作. 优先修改可维护译文并更新对应来源记录, 再生成产物. Agent 的工作流程、本地依赖准备和校验要求集中在 [AGENTS.md](AGENTS.md).

## 致谢与许可

感谢 Feed The Beast、各模组作者及 [CFPA 社区](https://github.com/CFPAOrg/Minecraft-Mod-Language-Package) 的原始内容与中文贡献.

CFPA 复用部分遵循 **CC BY-NC-SA 4.0**, 其他第三方内容保留各自许可. 来源、修改说明及许可全文入口见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). 本仓库中的混合来源内容不统一声明为单一许可.
