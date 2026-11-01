# 1.6.3 增量适配

目标: FTB Evolution 2 1.6.3 / Minecraft 26.1.2 / NeoForge 26.1.2.121. 本次仅写可维护译文、来源快照、工作副本及发布包, 未安装到游戏, 未游戏内验收. 更新前检查见 `../../reports/update-1.6.3-assessment.md`, 可复现步骤见 `migrate.py` 文件头.

## 分批成果

| 阶段 | 结果与证据 |
| --- | --- |
| 任务书 | 51 文件 / 4194 键全部解决. 英文修改 10 键, 新增 1 键 (`occultism` 的 `task.50A7FB14A0508D90.title`, 存储促动器基座). 14 个新片段逐条审校, 见 `quest-translations.json` / `quest-deltas.json`. 13 个任务结构文件随源更新, 不改任务逻辑. Companion 任务名绑定改到 `ftb-evolution-companion-26.1.2.26.jar`, 38 个英文名称逐条核对不变. |
| 特色文案 | 商店名 `ftb.shopkeeper.jewler` 英文由 The Jewler 改为 The Jeweler, 中文仍为珠宝商; 第 001 批复用记录与 `custom/pack.tsv` 同步. `broker_early.json` 仅新增复制物质锭交易, 无可见文本变化. 5 个运行时脚本与 2 个数据包覆盖的英文源与 1.6.3 逐字节一致, 既有中文继续使用. 新绑定 `../../custom/source-bindings-1.6.3.json`. |
| 关键手册 | FTBIC 采石场页 (`ftbic/machines/quarry.md`) 的整合包英文覆盖更新耗能和效率说明, 2 行改译, 见 `core-manual-translations.json`. 核心范围仍为 165 页. |
| 其他手册 | 10 页源变化 (巨型反应堆建造器/涡轮机 6 页, Horse Powered 动物陷阱, 海蓝科技 3 页) 共 64 个变化行改译. 新增 5 页 (137 行): 海蓝科技晶体培育器, 以及新模组 AE2-复制桥接器指南 4 页. 补充手册共 322 页. 逐行英文与译文见 `extra-manual-translations.json`. |
| 普通语言 | 342 个已完成批次逐源重绑, 72 个批次的 JAR 文件名或哈希变化. 29 个已选键英文变化, 逐键裁决见 `language-translations.json` (巨型反应堆建造器在第 0 位插入网站设计选项, 原有选项译文随英文顺移). 3 个键在新版语言文件中消失, 作为兼容输出保留. `ordinary-rebind.json` 保留差异和原件指针. |
| 新观察语言 | 597 个新观察键: 395 个由第 348-367 批新译, 54 个复用当前 JAR 自带中文, 24 个属于排除范围, 121 个是 Collective 附带的未安装 Serilum 模组文本, 3 个已有项目或 CFPA 译文. 逐键来源见 `new-language-review.json`. |
| CFPA 审校 | Witchery 41 条已采用译文的英文变化 (塔罗牌 40 条, 死灵之石提示 1 条): 牌名去掉下划线 (中文不变), 百分号改为 `%%` (中文同步为 `%%`), 破折号改句号或删去补充语 (中文同步断句或删除). Crafting Station 已被 Just Enough Crafting Tables 取代, 其 5 条译文改为 rejected 并保留来源. 见 `cfpa-review-adaptation.json`. |

## 环境与检查工具调整

- HMCL 等启动器的实例没有 FTB App 的 `instance.json`. 本次在只读源实例副本中按 `manifest.json` 生成同字段 `instance.json`, 并从实例副本中移除此前安装的汉化文件, 保证读取的是英文原件.
- GuideME 原生解析所需的 Gson/SLF4J/Guava 改由 `source_archive.guideme_classpath()` 统一查找: 优先读取 `project.json` 的可选键 `minecraft_libraries`, 否则沿用 FTB App 的 `bin/libraries` 布局. GuideME JAR 不再写死版本号. `audit_guideme_recipes.py` 只读取与实例 NeoForge 版本相同的 patched client.
- `cfpa_review/manuals/validate_native.py` 不再打开记录中的绝对 JAR 路径, 改为按资源路径从当前实例读取, 同名页面优先记录中的 JAR 文件.
- JEI 29.47 内嵌 mezz_config 0.6.6, 与独立的 0.6.9 同时提供 `mezz_config` 语言文件. 第 327 批明确绑定 0.6.9 的内层 JAR (JarJar 按最高版本加载, 未在游戏内确认).
- Crafting Station 模组已移除, `client_fixes/mod-names.json` 中对应映射退役, 名称脚本重新生成.
- `patchouli_translation.py` 的 Animal Pen 来源更新为 2.5.2.
- 术语库与物品名审计会读取本机 `.minecraft/resourcepacks/Minecraft-Mod-Language-Modpack-Converted-26.1.2.zip`. 本次用 `vendor/cfpa/sources.json` 固定的 CFPA 1.21 发布包 (`Snapshot-20260929014058`) 放在该路径, 与维护者本机的转换包不是同一文件.
- CFPA 审校构建中, 未逐条采用的 Patchouli 可见字段会沿用实例已选资源包里的现有中文. 为与 1.5.1 产物一致, 检查用实例的 `options.txt` 依次选中上述 CFPA 包和 1.5.1 汉化资源包. 这样构建出的 CFPA 审校包只有 Witchery 与 Crafting Station 两处预期变化. 两个 ZIP 均不随仓库提交.

## 校验与发布

`python project.py check` 共 386 项全部通过, 见 `../../reports/project-verification-1.6.3.json`. `python build.py` 生成 1.6.3 资源包与完整安装包, 共 32043 个语言键、996 个手册/书籍资源文件、51 个任务书中文文件. 未进行客户端资源重载、悬停、手册导航、配方显示或交互验收.
