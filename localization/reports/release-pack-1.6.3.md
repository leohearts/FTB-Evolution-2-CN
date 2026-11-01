# FTB Evolution 2 1.6.3 简体中文汇总包

本次基于实际 1.6.3 实例更新任务书、自定义提示、语言及手册, 并修复 JAR 版本变化与启动器目录差异引起的额外静态检查失败. [适配与来源记录](../updates/1.6.3/README.md) 包含逐批差异、术语、复用与检查范围.

## 发布内容

- `dist/FTB-Evolution-2-1.6.3-zh_CN.zip`: 语言和资源型手册覆盖.
- `dist/FTB-Evolution-2-1.6.3-zh_CN-install.zip`: 完整安装包, 含内层资源包 ZIP、任务书中文、整合包中文数据、Stellaris 手册数据包及运行时提示脚本.
- `dist/FTB-Evolution-2-1.6.3-zh_CN-manifest.json`: 成员清单与 SHA-256. 两个 ZIP 另有 `.sha256` 文件.

汇总包共 32043 个语言键、95 个独立分组名称、996 个手册/书籍资源文件、51 个任务书中文文件、64 个整合包数据文件、7 个运行时脚本. 任务书单独包含 4194 个语言键; 语言、页面、字段和分组数不相加. 与 1.5.1 相比, 新增 Just Enough Crafting Tables、AE2-复制桥接器、Refined Wireless Upgrades 的语言文件和 5 个手册页面, 移除已退出整合包的 Crafting Station 语言文件.

## 构建与校验

```bash
python project.py check
python build.py
```

全量源文静态检查 386 项全部通过, 完整输出见 [project-verification-1.6.3.json](project-verification-1.6.3.json). 发布产物成员与内容哈希、ZIP CRC 校验通过. 只含 Git 文件的独立副本 (无 project.json、游戏实例、模组 JAR、CFPA 检出或 dist 记录) 中 `python build.py` 通过, 详见 [source-only-build-1.6.3.json](source-only-build-1.6.3.json). 未执行 Windows 原生环境测试.

当前 165 页核心手册通过 GuideME 原生解析与 AST 结构对照; 322 页补充手册通过来源、格式、链接与内容检查, 其中 261 页通过 GuideME 原生解析. 静态候选与结构通过不等于实际客户端配方或布局已验收.

## 安装状态

**本次尚未安装到游戏, 尚未游戏内验收.** 使用前关闭游戏并备份; 按安装包内 INSTALL.md 合并明确文件, 资源包 ZIP 保持压缩并启用为最高优先级. 1.6.3 的 5 个运行时脚本和 2 个数据包覆盖文件, 其英文源与 1.5.1 逐字节一致, 安装包中的中文版本不会带入旧逻辑.

维护者可在确认 project.json 指向当前 1.6.3 实例后运行 `python localization/release_pack.py install --enable`, 工具会按清单备份并安装; `revert` 按本地安装记录还原.

FancyMenu 图片文字、既定排除模组与硬编码英文的处理范围保持不变, 不因本次适配宣称全部游戏内界面已完成.
