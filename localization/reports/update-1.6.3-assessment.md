# FTB Evolution 2 1.6.3 汉化更新检查

> 本文保留更新前的检查结论. 随后适配已实施, 最新结果见 [1.6.3 发布与校验记录](release-pack-1.6.3.md).

检查日期: 2026-11-02. 1.5.1 汉化不能直接标为已适配 1.6.3. 机器可读报告见 [update-1.6.3-assessment.json](update-1.6.3-assessment.json), 由 `python localization/assess_pack_update.py` 生成; 当前语言快照见 [update-1.6.3-language-snapshot.json.gz](update-1.6.3-language-snapshot.json.gz).

## 版本与输入

- 实例: FTB Evolution 2 **1.6.3**, Minecraft 26.1.2, NeoForge 26.1.2.121. 实例来自 HMCL, `instance.json` 按 CurseForge `manifest.json` 生成.
- 扫描 427 个顶层 JAR、131 个递归嵌套 JAR. 与 1.5.1 的模组清单相比, 368 个同名 JAR 内容不变, 其余为版本替换、新增 (Just Enough Crafting Tables、AE2-复制桥接器、Refined Wireless Upgrades 等) 与移除 (Crafting Station).

## 发现

| 范围 | 发现 |
| --- | --- |
| 任务书 | 4183 键不变, 10 键修改, 1 键新增, 无删除. 另有 13 个任务结构文件变化. |
| 整合包文案 | `ftb` 语言 1 键修改 (Jewler → Jeweler). 44 条自定义输入中, `broker_early.json` 新增一条交易, 其余与保存的英文源一致. |
| 手册 | 1394 条来源记录中 11 条源变化 (FTBIC 采石场 1 页, 补充手册 10 页), 另有 5 个新页面候选 (海蓝科技 1 页, AE2-复制桥接器 4 页). |
| 普通语言 | 72 个批次的 JAR 绑定失效 (文件名或哈希变化). 维护快照中 72 个已选键英文变化 (含 CFPA 审校的 Witchery 塔罗牌条目), 84 个旧键不再出现. |
| 新观察语言 | 597 个新观察键, 其中 54 个已有 JAR 自带中文. |
| 语法问题 | Animal Pen 自带 `zh_cn.json` 仍有 JSON 语法错误, 与 1.5.1 相同, 由既有 CFPA 修复覆盖处理. |

适配顺序与结果见 [1.6.3 增量适配](../updates/1.6.3/README.md).
