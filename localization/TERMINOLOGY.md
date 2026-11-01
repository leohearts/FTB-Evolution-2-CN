# 术语裁决记录

## 用法

本文件记录跨任务书、手册和普通文本的术语决定及证据, 不是自动替换词典. 规范见根目录 `AGENTS.md`. 已记录 1.4.0 任务书新增内容所需的术语裁决, 历史词表其余条目未因此视为已复核.

1. 核对当前模组版本、有效英文源及资源 ID/语言键, 查询官方中文、CFPA 和已有项目裁决. CFPA 候选包括已合并仓库、未合并 PR 以及不同 Minecraft/模组版本的汉化; 不仅查询与目标版本相同的目录.
2. 比较版本适配、语义准确性、模组内一致性与辨识度. 官方中文和 CFPA 没有固定的胜出顺序.
3. 将决定、理由和来源记入下表, 在 `glossary/glossary.json` 登记规范条目, 再更新对应词表、正文与游戏名称覆盖. 未决项标为待核实, 不作为规范译名传播.
4. 更改既有决定时保留旧译名和变更原因, 查找并同步所有引用, 记录构建及校验结果. 具体细节较长时链接批次报告.

## 现有词表的职责

| 路径 | 用途 |
| --- | --- |
| `terms.json` | 任务书的完整字符串匹配及明确保留的专名, 不是任意词片替换 |
| `manuals/terms.json` | 已翻译手册的术语参考 |
| `manuals/nodeworks-terms.json` | Nodeworks 专用术语参考 |
| `cfpa_review/terms.json` | 1.4.0 CFPA 审校复用的命名空间及上下文术语, 不用于全局替换 |
| 本文件 | 跨范围裁决、来源、适用上下文及同步状态 |
| `glossary/glossary.json` | 已裁决术语的结构化规范库: 按命名空间/任务章节限定, 绑定语言键与禁用变体, 由 `glossary.py check` 校验; 用法见 `glossary/README.md` |

现有词表是待逐步复核的历史资产, 不因存在于词表就优于官方中文或 CFPA. 英文文本相同的章节标题与设备分类可能含义不同, 不将其自动判为冲突. 新增领域词表时在此登记用途.

## 记录字段

一行对应一个确定的概念及适用范围. 来源需包含可追溯的 JAR/模组版本及语言键, 或 CFPA 提交/文件路径; PR 来源附编号、作者和 head SHA. 跨版本来源另记录来源 Minecraft/模组版本、目标版本及原文/含义匹配依据; 语言键更名时记录新旧映射. 不适用的候选填 `无`, 不凭记忆补造译名.

| 模组/命名空间与版本 | 资源 ID/语言键及语义 | 英文 | 官方中文候选 | CFPA/PR 候选及来源 | 项目规范译名 | 裁决理由/证据 | 旧译名及同步范围 | 状态/校验记录 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| replication / 1.2.7 / MC 26.1.2 | `block.replication.chip_storage`, 芯片容器 | Chip Storage | 芯片仓 | 芯片存储器, CFPA 1.21 | 芯片仓 | 当前版本命名简洁且含义正确, 与实际界面一致 | 无既有本项目译名; 新章节与任务词表 | 已审定, 见下方证据 |
| replication / 1.2.7 / MC 26.1.2 | `item.replication.memory_chip`, 样板载体 | Memory Chip | 内存芯片 | 存储芯片, CFPA 1.21 | 内存芯片 | 两者均可理解, 保持当前版本物品名便于查找 | 新章节与任务词表 | 已审定 |
| replication / 1.2.7 / MC 26.1.2 | `replication.matteropedia`, 物质值查询界面 | MatterOpedia | 万物源典 | 物质百科, CFPA 1.21 | 物质百科 | 直接表达物质值查询功能, 较诗化名称清晰; 当前英文含义与跨版本来源一致 | 新章节, 词表及 Replication 界面覆盖 | 已审定, `quest_extra_labels.json` 验证覆盖 |
| replication / 1.2.7 / MC 26.1.2 | `replication.matter_type.living`, `.precious` | Living / Precious | 生命 / 珍宝 | 活体 / 珍稀, CFPA 1.21 | 生命 / 珍宝 | 均为类别专名, 当前官方译名能对应含义并与界面匹配 | 新章节 | 已审定 |
| witchery / 0.5.22 / MC 26.1.2 | `entity.witchery.coven_witch`, `item.witchery.coven_contract`, `item.witchery.seer_stone` | Coven Witch / Coven Contract / Seer Stone | 当前 JAR 无中文文件 | 旧 CFPA 转换包: 聚会女巫 / 聚会合约 / 先知之石 | 聚会女巫 / 聚会合约 / 先知之石 | 复核新 JAR 英文及旧任务书, 沿用既有资源名称; 组织概念沿用项目命令文本的“巫师会” | Witchery 新任务与任务词表 | 已审定; 实体, 物品与组织分别按上下文命名 |
| witchery / 0.5.22 / MC 26.1.2 | `block.witchery.golden_ritual_chalk` | Golden Ritual Chalk | 当前 JAR 无中文文件 | 项目有效覆盖为金黄仪式粉笔 | 金黄仪式粉笔 | 补全既有任务书中的简称, 与当前覆盖物品名一致 | 4 个旧任务说明及新任务, 任务词表 | 已同步 |
| FTB / 1.4.0 / MC 26.1.2 | `bacteria.ftb.replicophiles`, `witchery:ritual/summon_coven_witch` 及对应标题键 | Replicophiles / Summon Coven Witch | 新增源键无现成中文 | 本批未采用 PR 候选 | 嗜复制物质菌 / 召唤聚会女巫 | 前者按细菌名称和物质产出用途表意; 后者沿用实体名称, 与召唤普通女巫区分 | 新任务, 词表及 FTB 名称覆盖 | 已同步, 只补任务直接依赖的名称 |
| occultism / 本包当前版本 | 任务书 `chapters/occultism.json5` 已有 3 阶精灵名称 | Afrit | 本批未变更 | 本项目既有火灵 | 火灵 | 新任务引用已有任务书概念, 沿用既定名称 | Replication 获取来源说明, 任务词表 | 已同步 |

本批来源详见 `reports/quests-1.4.0-terms.json`: 固定 CFPA 提交 `719672954d9df4ea51877e3d5ce2912148273682`, 对比 `CFPA/projects/assets/replication/1.21/replication/lang/zh_cn.json` 与当前 Replication JAR. 新旧英文源及翻译增量见 `reports/quests-1.4.0-source-delta.json`. PR 检索未获得可核验候选, 未采用 PR 内容, 不声称已穷尽全部 PR. 后续发现更好译名时按本文件流程复核, 不静默覆盖.

## 1.4.0 CFPA 审校复用裁决

逐条来源, 目标语言键, 修改理由及键映射保存在 `cfpa_review/decisions/`, 命名空间术语保存于 `cfpa_review/terms.json`. 本阶段未改写历史任务词表的完整句子匹配规则.

| 范围 | 规范用词 | 裁决与同步 |
| --- | --- | --- |
| AE2 Network Analyser | ME刻耗时分析仪, 性能分析 | μs/tick 衡量耗时, 不译作模型分析; 物品名, 界面与手册同页已同步 |
| Collapsible Groups | 折叠, 可折叠, 分组 | 描述查看器显示状态, 不沿用合并/群组; 不新增 Macaw 等排除模组的分组中文 |
| GeoOre | 矿晶, 矿晶簇, 矿晶母岩, 矿晶芽, 矿晶碎片 | 区分生长阶段与材料类型, 沿用已有任务术语 |
| Cable Tiers | 精英, 终极, 极巨, 创造 | Elite/Ultra/Mega/Creative 在接口等子类保持同一等级用语 |
| Integrated 系列 | 动态联合, 集成管道, 存储终端, 移动式存储终端 | 修复继承管道/集成动力错名, 保持同系列对象一致 |
| 动态联合逻辑 | 配方, 原料, 显示面板, 运算符, 求值 | 按值类型及程序上下文裁决, 不把普通求值改为检测是否 |
| 神秘时代兼容项 | 要素, 灵气场基值, 灵气场咒波 | Aspect 与 Aura Base/Flux 按领域含义区分 |
| XyCraft | 磊岩, Xy晶, 生物树脂 | 保留专名及既有任务名称, 不按单词机械替换其他模组材料 |
| Neo Vitae / BMAddon | 生命源质, 气血生成机, 气血装配室 | 流体沿用当前官方生命源质名称; 器件名保留气血前缀, 不混同原始血液与祭坛流体 |
| Modular Routers | 路由器刻, 运行间隔 | 以服务器刻表示的周期不作每秒频率理解; 同步升级说明补明取模运算 |

本地半角标点要求优先于上游审查中的全角标点建议, CFPA/PR 原文保持原样. 旧翻译及审校初稿中的不同说法仍保留在来源字段用于追溯, 不代表当前输出混用.

## 1.4.0 整合包特色内容批次

- `Base Armor Toughness`: 基础盔甲韧性. Apotheosis 的 12 个整合包装备进度条件明确新增 Base 限制, 在既有“盔甲韧性”前补全“基础”, 数值与稀有度不变.
- `item.ftb.meat_ingot`: 肉锭. 同义候选取 CFPA 固定提交 `719672954d9df4ea51877e3d5ce2912148273682`, productive-metalworks/1.21/productivemetalworks/lang/zh_cn.json 的 `item.productivemetalworks.meat_ingot`; 跨模组仅作同义命名参考, 不移植机制或整文件. 目标本包 1.4.0 当前 KubeJS 源文.
- `random_hat` 商品说明: 解锁一顶随机帽子. 当前商店执行 `givehat @s random`, 表达外观解锁, 不译为获得物理帽子物品. 两处说明同步, 交易命令与价格保持.
- 聚会女巫与巫师会延用既有 Witchery 裁决. 两条新增手册正文延后, 本阶段不计完成.

逐条源文、译文和版本证据见 `custom/batches/batch-001/manifest.json` 至 `batch-004/manifest.json`, 以对应 verification.json 及全项目检查验证.

## 1.4.0 Anima 普通语言批次

来源为 `Anima-1.0.3+Neoforge-26.1.2.jar` 的 `assets/anima/lang/en_us.json`, 由第 020 批处理 299 键. 该 JAR 与固定 CFPA 提交均无中文, 因此以已完成的 `translations/chapters/anima.json5` 作为规范译名来源, 不为新译另立体系. 后续手册沿用下列名称.

- `Soulbone` 魂骨, `Crystallized Soulbone` 结晶魂骨, `Soulbone Splinter` 魂骨碎片, `Soulbone Conduit` 魂骨导体. 任务书已用该组名称, 不译作灵魂之骨.
- `Saronite` 萨隆铁, `Raw Saronite` 粗萨隆铁, `Saronite Ingot` 萨隆铁锭. 保留音译与铁的后缀, 与任务书的萨隆铁剑, 萨隆铁箭一致.
- `Blue Crystal` / `Blue Gem` 分别为蓝色水晶与蓝色宝石; `Yellow Crystal` / `Yellow Gem` 同理. 水晶指材料, 宝石指压印产物, 两者不互换.
- `Soul Well` 灵魂之井, `Soul Stone` 魂石, `Soul Relay` 灵魂中继器, `Soul Forge` 灵魂锻炉, `Soul Gem` 灵魂宝石.
- `Golem` 魔像, `Workshop Golem` 工坊魔像, `Golem Fabricator` 魔像制造器, `Golem Part Assembler` 魔像部件装配台, `Soul Leash` 灵魂缰绳. 不译作傀儡, 以免与任务书既有称呼冲突.
- `Foci` 法器, `Spell Book` 法术书, `Infusion Table` 灌注台, `Research Table` 研究台.
- 神系: `Deity` 神祇, `Pantheon` 万神殿, `Deity Shrine` 神祇神龛, `Deity Hammer` 神祇之锤, `Deity Fabricator` 神祇制造器, `Offering Plate` 供奉盘, `Plinth` 基座, `Priest Rod` 祭司杖, `devout` 虔诚信徒, `worship` 崇拜.
- 九类灵魂: 温和, 掠食, 厄运, 狂乱, 水生, 末影, 炼狱, 睿智, 神魂.
- 玻璃工艺: `Blow Mold` 为放置在世界中的吹制模台, 各 `*_mold` 物品为模具, 两者不合并为同一名称. 本批新定 `Decanter` 醒酒瓶, `Splitter` 分流器, `Gourd` 葫芦瓶, `Spiral` 螺旋管.
- 本批新定且无既有来源的名称: 合成共振器, 凝聚石板, 灵魂传送门, 灵魂触须, 灵魂幽光, 宇宙之神.

`block.anima.soul_altar` 的英文值为 Research Table, 与 `block.anima.dark_altar` 的 Altar of Souls 不同; 按键面英文分别译为研究台与灵魂祭坛, 未按键名或推测语义改写, 也不作为源文勘误. 证据见 `ordinary/batch-020/README.md` 与 `verification.json`.

## 1.4.0 Energized Power 官方中文缺口批次

来源为 `energizedpower-3.0.1+26.1.x-neoforge.jar` 自带 `zh_cn.json`. 该文件键数齐全但 395 键仍为英文, 由第 021 批补齐. 已有 1394 条中文不改写, 下列名称取自其既有体系, 新名称按同一构词补齐.

- 机器等级: 基础, 硬化, 高级, 精英, 对应 Basic / Hardened / Advanced / Elite. 任务书原称自动合成机, 与 JAR 内官方 `自动合成器` 冲突, 按游戏内名称同步任务书 5 处.
- `Press Mold` 压模, 依据官方压模制造机; 按产物分齿轮压模, 棒材压模, 线材压模, 不译作模具.
- 电压: 低压, 中压, 高压, 超高压, 特高压, 对应 LV / MV / HV / EHV / UHV; 括号内方向沿用官方 `(1 转 n)` 写法.
- 传送带: 基础, 高速, 极速, 涡轮, 对应无前缀 / Fast / Express / Turbo; 组件统一为装载机, 合并器, 分拣机, 分离器, 切换器.
- 经验: `XP Drain` 经验汲取, `XP Storage` 经验存储, `XP Extraction` 经验提取, `Liquid XP` 液态经验, `XP Yield` 经验产出. 经验存储容量单位用 级, 不译作等级点数.
- 升级模块类别: 物品弹出, 物品吸取, 充能速度, 能量产出, 能量容量, 能量效率, 提取深度, 提取范围, 熔炉模式, 月光, 范围, 速度, 持续时间.

该批自行编写译文使用英文标点, 上游既有中文保留全角标点, 不因本篇统一而回改 JAR. 证据见 `ordinary/batch-021/README.md` 与 `verification.json`.

## 1.4.0 Logistics Networks 缺口批次

来源为 `logisticsnetworks-26.1.2-1.13.0.jar` 自带 `zh_cn.json`, 由第 022 批补齐 277 个缺失键.

- Network 网络, Node 节点, Channel 频道, Label 标签, Filter 过滤器, Wrench 扳手, 均沿用官方既有译名.
- `channel_mode.import` / `export` 官方为输入 / 输出, 因此网络图的 Import / Export 同作输入 / 输出, 不使用导入 / 导出.
- 频道类型: 物品, 流体, 能量, 化学品, 魔源. `Source` 取官方魔源, 不用源或魔源能量.
- `distribution_mode.priority_robin` 为优先级轮询, 与既有优先级, 最近优先, 最远优先, 轮询分配并列.
- 存储集成中的 `Refined Storage` 用精致存储, `AE2`, `RS`, `NBT` 保留缩写, 单位 `mB/s`, `RF`, `SRC` 等不译.

计量单位与坐标格式保留原样, 属于合理英文与技术标识, 已登记在 `batch-022/manifest.json` 的 `unchanged_values`. 证据见 `ordinary/batch-022/README.md` 与 `verification.json`.

## 1.4.0 CakestickLib 与 Collapsible Groups 批次

**CakestickLib** 无上游中文, 第 023 批按材料体系确定名称:

- Wrought Iron 熟铁 (不译锻铁), Steel 钢, Advanced Alloy 高级合金, Mixed Ingot 混合锭.
- 流体一律 熔融 X: 熔融铜, 熔融金, 熔融铁, 熔融钢, 熔融下界合金, 熔融远古残骸, 熔融荧石, 熔融红石.
- 加工件: 粉, 板, 箔, 齿轮, 粒, 锭, 线圈, 螺栓; 模具统一为 X模具, 不写作铸模.
- 矿石按矿物学名: 辉银矿, 金银矿, 铝土矿, 锡石矿, 黄铜矿, 方铅矿, 赤铁矿, 高岭土, 褐煤, 孔雀石, 锇铱矿, 镍黄铁矿, 辉橄岩, 石英岩, 沥青铀矿, 圆柱锡矿.
- `Xenothite` 为虚构矿物, 定名泽诺石; `Molten Blazing` 语义不可核验, 按字面作熔融烈焰. 两项待后续手册或配方出现新证据时复核.

**Collapsible Groups** 第 024 批按键面英文补简体中文, JAR 内 `zh_tw.json` 只作语义参考:

- Group 分组, 不采用繁体的群組; Category 分类, Manager 管理器, Rule 规则, Condition 条件, Subgroup 子分组.
- Tag 标签, Namespace 命名空间, Path 路径, Exact Stack 精确堆叠, Component 组件.
- `ID`, `KubeJS`, `patch`, `iconIds[0]`, `iconIds[1]` 作为技术标识保留; `patch` 是 JSON 补丁节点, 不译作补丁.

证据见 `ordinary/batch-023/README.md` 与 `batch-024/README.md` 及对应 `verification.json`.

## 1.4.0 Occultism 与 Better Fish Tanks 批次

**Occultism** 第 025 批只补 JAR 自带中文的 185 个缺口, 术语全取官方既有译名:

- Familiar 使魔, Spirit 魔灵, Infused 灌注, Otherworld 异界, Iesnium 艾瑟金属, Spirit Attuned 魔灵同调.
- Flame of Automation 自动化之火, Pentacle 五芒星阵, Third Eye 第三只眼, True Sight Staff 真视法杖, Spirit Fire 灵火.
- 使魔名 Drikwing 德里克翼, Wingnis 翼尼斯, 无官方中文, 按音译.
- `Pentacle Alt/Eye/Gear` 无官方说明, 按既有五芒星阵合成/杂项/附身/召唤构词译为五芒星阵祭坛/五芒星阵眼/五芒星阵装备, 属推断项, 待手册出现明确类别名时复核.

**Better Fish Tanks** 第 026 批无上游中文, 术语为:

- Aquarist 水族师 (工作台, 村民, 指南同用), Fish Tank 鱼缸, Fish Bag 鱼袋.
- 鱼食: 薄片饲料, 颗粒饲料, 混合颗粒, 小虾, 干海带; 容器统一为 X容器.
- 装饰方块: 微型/小型/中型树枝, 微型/小型石块, 洞穴结构, 沉船残骸, 塔楼; Stripped 统一去皮.

证据见 `ordinary/batch-025/README.md` 与 `batch-026/README.md` 及对应 `verification.json`.

## 1.4.0 科技三批: 材料与编辑器术语

按“科技与能源”顺序处理的第 027-029 批, 材料名一律取上游官方中文, 新名称按同一构词补齐.

- Just Dire Things 体系 (第 027 批): 核源铁, 烈焰金, 蚀空合金, 苍穹晶; 凝胶系列为原初浆/烈焰蕾/虚空辉/暗影脉; 时间手杖, 标签枪. Ticker 统一刻速器, Tick rate 刻速. 光源/拾取/交换手杖为新增变体, 按同类手杖构词.
- Super Factory Manager 体系 (第 028 批): 工厂管理器, 标签, 标签枪. 本模组 Label 用标签, 物品/方块 Tag 用物品标签, 二者区分. SFML 保持缩写; Node 节点, Pin 引脚, Wire 连线, Blueprint 蓝图, Round robin 轮询.
- FTB Industrial Contraptions (第 029 批): 铝, 青铜, 钢, 铅, 镍, 银, 锡, 铀, 铱, 钚, 康铜, 琥珀金, 殷钢. Wire 为导线, Cable 为线缆, 不混用. 粉碎/洗净/精炼精矿保留原料名占位.
- `Forge Energy` 在 RFM 中译作 Forge 能量, 不写 FE 能量: 原文未用 FE 缩写, 且与单位保护表冲突.

证据见 `ordinary/batch-027/README.md` 至 `batch-029/README.md` 及对应 `verification.json`.

## 1.4.0 Auroral 与 MORE Red 批次

- Auroral (第 030 批): Aurora 极光, Aura 灵气, Liquid Aura 液态灵气, Glacial Basin 冰川之盆, Frostbite 霜噬. Shimmersteel 微光钢, Shimmerweave 微光编织; Glow-Leek 发光韭葱, Hearthwood 炉木, Shimmer Soil 微光土壤, Shimmering Ice 微光冰. 模组名 Auroral 与双关物品 S'nore 保留英文.
- MORE Red (第 031 批): 沿用官方 更多红石电路, 红石合金, 石底座, 红石线柱/线轴. Axle 传动轴, Clutch 离合器, Gear 齿轮, Gearshifter 换挡器, Windcatcher 捕风器. Cable 线缆, Tube 管道, 集束线缆, 线缆接点/中继器.
- 11 种木材与 16 种颜色的系列名称由模式生成, 木材用原版译名, 颜色用 16 色标准译名.

证据见 `ordinary/batch-030/README.md` 与 `batch-031/README.md`.

### 任务书与手册同步 (2026-10-18)

- 任务书 Auroral 章节已按游戏内名称同步: Frostbite 霜噬, Cold Brewing Stand 低温酿造台, Glacial Basin 冰川之盆, Shimmerweave 微光编织 (Shimmerweave Fabric 物品为 微光布, 装备名按各件官方名). 不再使用 冻伤/寒冷酿造台/冰川盆/微光织物.
- 手册沿用同一组名称; `remaining-1.4.0` 手册批次中的 Auroral 30 页与任务书一致.

## 1.4.0 剩余手册批次 (305 页)

- Colossal Reactors: 巨型反应堆, 裂变反应堆, 蒸汽涡轮机, 反应堆外壳/玻璃/控制器/燃料棒, 能量端口/资源端口/红石端口, 涡轮机外壳/玻璃/控制器/转轴/叶片, 散热介质, 加热线圈, 熔化器. 不使用 散热片/散热器.
- Nautec: 保留 NauTec 英文名; Laser Power/AP 激光能量, 纯度, 光束, 海棱水晶, 海晶碎片, 海晶水晶, 海蓝催化器, 海蓝钢, 深海钢镀板, 海洋侦察艇, 水流喷射器, 聚变电站, 共鸣 (Resonance; 不用 共振), 传送门, 棱镜卫星.
- Nautec 细菌系统以当前 kubejs `zh_cn` UI 为准: Colony 菌落, Mutation 突变, Mutation Resistance 突变抗性, Size 规模, Nutrients 营养物, Colony Feeding 菌落喂养, Refine 提纯, Strain Yield 菌株产量, Lifespan 寿命, Vitality 活力, Growth Rate 生长速率, Production Rate 生产速率.
- 菌株名以当前语言文件为准: Lithophiles 嗜岩石菌, Ferrophiles 嗜铁菌, Metallophiles 嗜金属菌, Carbophages 噬碳菌, Acidophiles 嗜酸菌, Azuritophiles 嗜青金菌, Sulfurophiles 嗜硫菌, Aurrophiles 嗜金菌, Adamantophiles 嗜金刚菌, Smaragdophiles 嗜绿宝石菌, Calciophiles 嗜钙菌, Silicophiles 嗜硅菌, Halobacteria 盐细菌, Cyanobacteria 蓝细菌, Methanogens 甲烷菌, Thermophiles 嗜热菌, Algaeformers 成藻菌, Phototrophs 光养菌, Rhizobacteria 根际细菌, Betulophiles 嗜白桦菌, Boreophiles 嗜寒林菌, Acaciophyles 金合欢嗜植菌, Junglophiles 嗜丛林菌, Prunus Lignocytes 樱李木细胞, Rhizophora Lignocytes 红树木细胞. 不使用 石头菌/铁菌/盐菌/蓝菌/海草弧菌/钻石菌 等简称.
- Kindred Spirits: 灵魂, 羁绊, 伙伴, 羁绊护符, 羁绊界面, 威望, 等级; 模组名保留英文.
- Horse Powered: 工作鞍, 手摇磨石, 马匹磨石, 切菜墩, 马匹压碎机, 马匹压榨机, 马力发电机, 创造电池, 晾晒架, 花岗岩铁砧, 动物陷阱, 火镰与火绒.
- Mystian Apiary: 蜂房蜜蜂箱/蜂房花箱/蜂房存储/蜂房控制器, 蜜脾块, 劳力, 产量, 基因采样器. Productive Bees 统一作 资源蜜蜂.
- Stellaris 保留英文模组名; 月球, 感染, 寄生村民, 星界爬行者, 星界爬行者母体, 着陆舱, 火箭发射台, 空间站; 单位 FE/mB 与数值不改.
- Oracle Index 书籍使用 `translated/zh_cn/<原相对路径>`; Drones、Oritech 等书籍同一规则. Oracle Index 模组名保留英文.

## 1.4.0 科技类收尾 (批次 032-059)

- Malisis Switches: 绿石/绿石催化剂, 能量连接器, 无线开关与传感器; 动作传感器不译作运动传感器.
- Oritech: 沿用官方 方块破坏器; 新增 共振器, 资源节点, 晶洞. 保留 Oritech, NBT, 单位与 K/M/B/T 缩写.
- Drones: 模块化无人机, 组装框架, 旋翼, 离子推进器; 能力名用动词短语.
- Cable Tiers: 沿用 精英/终极/极巨/创造; 接口与自动合成器为 分级接口.
- NeoSync: 躯壳 (shell) 统一, 不用外壳, 以区别于方块外壳.
- Ender IO: 导管按 充能/活力 + 能量/流体/物品 组合; 保留 µI 与 mb 原写法.
- XyCraft: 多方块组件, 代理方块, 过滤网; Aurey 音译奥瑞.
- MFFS 力场系统, 福特龙 (Fortron); 激光桥系列为 激光源/激光栅栏源.
- 纯格式串模组 (Hostile Neural Networks, Little Big Redstone, MTR, Iron Furnaces, Powah, Oritech Things, Tesseract) 只登记保留值, 不产出中文.

证据见 `ordinary/batch-032` 至 `batch-059` 与 `reports/tech-completion-027-059.md`.

## 1.4.0 存储与物流 (第 061-097 批)

- Compressium: 沿用上游既有中文的 压缩 + 材质 构词, 铁/金/钻石/绿宝石/下界合金 补 块 (压缩铁块, 压缩钻石块), 等级后缀保留 (1x)-(9x). 上游中文键名 block.* 与英文源 item.* 不一致属上游错位, 不改其资源.
- Refined Types: Essentia 作 源质 (神秘时代既有译名); Storage Part 存储组件, Storage Disk 存储磁盘, Storage Block 存储方块, 与同文件既有中文一致, 不采用 RS 官方的 存储元件.
- AE2 生态: 样板供应器, 样板编码终端, 智能线缆, 致密智能线缆, 包层线缆, 替代品, 均取 AE2 官方中文. ME 前缀保留.
- Step Crafter: 分步合成器, 分步请求器, 分步合成监视器; 自动合成器 指 Auto Crafter, 二者不混用.
- Integrated 系列: 存储终端, 合成任务, 频道, 变量卡箱, 延迟器, 取或默认, 逻辑编程器, 实体化器, 网络诊断, 挤压机, 烘干池 沿用任务书章节; 手册正文的 无状态, 反馈回路, 锁存器 为新增.
- 其余: 维度箱子, 维度储罐, 量子方块, 无限驱动器, 分步 (Step), 上限 (out of), 透明度 (Alpha), 能量单元 (Cell).
- 纯格式串模组 (AE2 部分键, Advanced AE, Extended AE, Sophisticated Core/Storage, Pipez, Modular Routers, Applied Flux, Nodeworks, appflux) 只登记保留值.

证据见 `ordinary/batch-061` 至 `batch-097` 与 `reports/storage-completion-061-097.md`.

## 1.4.0 整合包与 FTB (第 098-106 批)

- FTB Quests: 章节, 任务, 奖励, 外观, 尺寸, 形状, 视觉预设, 变更历史, 奖励表, 固定追踪器 与任务书保持一致. 键位名用 界面/界面编辑器模式/任务查看面板.
- FTB Echoes: Echo 回响, 回响投影器, 阶段, 购物篮, 钱包, 限购, 下单. 阶段与 FTB Teams 的队伍阶段同词.
- FTB Teams: party 与 team 均作 队伍, lives 作 生命, 游戏阶段/队伍阶段 分开表述.
- FTB Pack Companion: 整合包伴侣, 随机传送门, 玩家触发器, 动作面板, 结构放置器, 锚定/微调/重置位置.
- FTB Materials 沿用同文件金属名: 铱, 钨, 银.
- 保留值: FTB Quests 的 FE / RF, %d FE, E, %d E, mJ, %d MJ, EU, %d EU, ID; FTB Backups 3 的 [%d%% | %d / %d].

证据见 `ordinary/batch-098` 至 `batch-106` 与 `reports/ftb-completion-098-106.md`.

## 1.4.0 界面与信息显示 (第 107-134 批)

- 配置界面通用词: 待应用的更改, 应用, 放弃, 撤销, 重置, 默认值, 配置项, 分类, 小节, 侧栏层级. 两套配置模组共用, 不各写一套.
- Traveler's Titles 维度名: Dormis 多弥斯, Glacium 格拉西姆, Omnidrome 奥姆尼穹, Panacea 万灵乡, Pax 静和境, Sanctum 圣所, Brine 卤海, Faewild 妖精荒野, Underdark 幽暗地域, Varskpace 瓦尔斯克空域, Lightwoods 微光林地, Afterdark 暗夜之后, Voidscape 虚空景观; The Ceilands 天穹之地, Eternal Starlight 永恒星光.
- Traveler's Titles 生物群系: 按语义翻译, 如 灰烬荒原, 炼狱沙丘, 倒悬森林, 石英平原, 剧毒废堆, 火山三角洲, 泣泪山谷, 凋朽森林, 水晶峰, 暗影之地, 虚空荒原, 北极丘, 北境边疆, 荒芜要塞, 破碎荒原, 冰川巨体, 入侵森林, 档案厅, 铸造厂, 下层都市, 逆流地带, 竹谷, 受诅针叶林, 苦力怕领地, 绯红有机体, 蜜蜂群系, 木贼热带, 饥渴丛林, 多孔菌平原, 流沙泉, 贪食绿林, 酷热沼泽, 野花泥沼, 秋日田园, 纪念碑, 云冠, 大滨海草原, 花瓣林, 空中花园, 黑煤烟沙丘, 无人之地, 碎石城, 毒盐滩, 虚空船港, 黑水深渊, 花簇礁, 死寂礁, 侵入真菌, 靛蓝中域, 守望者街区, 海藻湾, 崇圣水域, 海绵牧场, 糖沙滩, 隐秘堡场, 暗雷灌丛, 梦落幽谷, 丰饶田野, 隐秘村庄, 马尔姆齐草甸, 中间层, 游光林地, 水晶洞窟, 闪长岩海, 侵蚀盆地, 石化森林, 红宝石菌林, 硫磺火山口, 泰坦滴水石洞窟, 玄武岩坡, 骸骨峡谷, 北境山谷, 骸骨洞窟, 结晶洞室, 冰川刻蚀, 滨海空穴, 地下丛林, 结晶峰, 冰窖, 苔藓盆地, 异客平原, 沉没深渊, 附魔之地, 翠绿尖塔, 下方虚空, 下方逆虚空, 逆虚空, 苦痛, 花开, 变迁, 荒芜, 绝望, 恐惧, 希望, 孤绝, 霜寒小林, 生长林地, 静谧森林, 泥炭沼泽, 牧野草甸, 阴森林, 方解石原野, 诡谲雪原, 深层暗夜, 滴水石三角洲, 枯死旱地, 繁茂花园, 海晶石峰, 海晶石池塘.
- 考古结构 (JEI Archaeology): 稀有度标记 [C] 常见, [UC] 少见, [R] 稀有; 模组标记 [ATM] 与 [BA] 保留原样. 结构名如 史前繁茂巢穴, 史前水胆玛瑙, 废弃吉米塔, 日轮/月轮石阵遗迹, 倾倒石柱遗迹.
- 其它: 世界内生命条, 粒子, 友方/敌方, 战利品表, 色彩空间, 伪装, 生物帽, 玩偶, 全色盲/全色弱/红色盲/红色弱/绿色盲/绿色弱/蓝色盲/蓝色弱.

证据见 `ordinary/batch-107` 至 `batch-134` 与 `reports/ui-completion-107-134.md`.

## 1.4.0 农业与食物 (第 135-156 批)

- 种植设施: 种植盆 (种植盆按木材与陶瓦区分), 堆肥桶, 筒仓, 施肥器, 覆盖物 (Mulch), 灌注耕地, 钟形罩 (Cloche), 生物质燃烧器, 电容.
- 蜂类: 蜂房, 蜜蜂箱, 花箱, 存储箱, 离心机, 蜂巢 (comb), 基因采样器; 特殊蜜蜂 诡秘/灵气/神秘金属/虚空金属/嘎吱/废料/天空史莱姆/壮硕.
- 神秘时代术语 (Productive Bees): 咒波 (flux), 腐化 (taint), 腐化之地, 空灵之花, 咒波黏浆, 咒波气体, 灵气节点, 要素 (aspect), 创造节点放置器.
- 神秘农业: 精华等级 下级/初级/中级/高级/终极; Sickle 镰刀 与 Scythe 巨镰 必须分开; 注魔水晶 / 矿石灌注器.
- 营养: 乳制品/水果/谷物/蛋白质/蔬菜; 等级 营养不良/维持/营养充足/美食家; 营养素吸收, 衰减速率.
- 其它: 出货箱, 运输气球, 洒水壶, 兔子陷阱, 花匠骨粉, 压缩骨粉, 极压缩骨粉, 雀鳝, 海獭, 公牛鲨, 鸟舍.

证据见 `ordinary/batch-135` 至 `batch-156` 与 `reports/agriculture-completion-135-156.md`.

## 1.4.0 战斗与冒险 (第 158-175 批)

- Resonance 沿用任务书章节: 共鸣, 共鸣剑/长矛/箭/灯笼/图腾/中继器, 水晶森林, 水晶怨灵, 水晶哨兵, 水晶潜猎者, 破碎回响, 破碎回响, 紫颂共鸣器, 谐振者, 谐振护盾, 谐振碎片, 低语碎片, 紫水晶锭. 投掷用的 Crystal Shard 作 水晶裂片, 与召唤用的 水晶碎片 (Crystal Fragment) 区分, 二者不同物品不混用.
- Graveless: 灵魂庇护 (Spirit Ward), 坟墓, 幽灵, 灵魂指南针, 归档备份; 方位值写成 北侧/东北侧 等, 以便 12 格北侧 的拼接.
- Apotheosis 新词缀按既有 名称+后缀 双词体系: 破符/破符者, 虚无/虚无化, 从容/静旅, 稳步/丈步, 坚毅/刚硬. Steadfast 用 坚毅 以避让已有的 stalwart 坚定. 塑石 (Stoneforming).
- Iron's Gems & Jewelry: 图样 (pattern), 部件 (part), 主部件, 品质 (quality), 珠宝商; 珠宝 与 环带材料 沿用任务书.
- FrostBear: 霜熊, 霜牙, 冰封之心, 冰川核心, 凛冬之心, 暖身炖菜, 冰刺; Frostbite 统一作 霜噬, 与 Auroral 一致.
- Iron's Artifice: 魂火硬币, 子弹盒, 跳弹, 魂伤.
- Gateways: 铁自动机之门, 自动机制造者无尽之门, 铁哨兵, 铁巨兽.
- 其它: 训练假人, 排行榜假人, 最高伤害排行榜, 翻滚次数/翻滚距离, 多重射击/快速拉弦 (原版附魔), 变异怪物.
- 保留原文: Weezer 专辑与歌曲名 (Surfer Rosa, Weezer, In The Garage, Surf Wax America, Undone), 乐曲名与画作作者, DPS, HUD, 键位提示 [shift]/[ctrl]/[alt].

证据见 `ordinary/batch-158` 至 `batch-175` 与 `reports/combat-completion-158-175.md`.

## 1.4.0 工具与生活品质 (第 176-211 批)

- 界面动词统一: 转移/补货/倾倒/整理 (Inventory Essentials), 补充配方材料 (Sophisticated Item Actions), 松开以交换 与 轮盘菜单 (Toolbelt), 将鼠标限制在圆内.
- Little Joys: 挖掘点, 钓鱼点, 掉落狂欢, 黄金狂欢, 流星, 四类星之祝福 丰饶/命运/繁荣/宁静; 渐隐/闪耀/辉耀/璀璨 为祝福剩余次数档位.
- 传送: 归家水晶 与 归家点 (Simple Teleporters), 末影核心 与 强化末影核心; 传送石碑 沿用 Waystones 官方中文, 传送设置 对应 warpSettings.
- 容器: 衰败 与 刷新 是 Lootr 的两种容器状态, 两个词不互换; 队伍战利品 与 按玩家实例化 区分.
- 其它: 扫描模块, 刷怪笼, 收购箱, 防雨罩, 蹲下催熟, 爬行动画, 吊床, 多棱锥 与 螺旋 (Build Guide 形状).
- 专名保留: Little Joys, Lootr, Simple Teleporters, Just Zoom, KeyBind Bundles, Measurements, Microsoft, Snad, Drit, TIAB, AABB, HUD, DPS, [EF] 前缀.
- 符号与键位串保留: ⇧ Shift, SHIFT/CTRL 组合提示, A->Z 与 Z->A, %s (%s), %d, %d, %d, §7- §f%s§r.

证据见 `ordinary/batch-176` 至 `batch-211` 与 `reports/qol-completion-176-211.md`.

## 1.4.0 世界生成与结构 (第 212-230 批)

- XyCraft 建筑体系按四段构词: 颜色 (蓝色/暗色/绿色/浅色/红色) + 质地 (平滑/镶边/明亮/扁平/发光/不朽) + 材料 (铝/大理石/基维/奥瑞) + 构件 (方块/台阶/楼梯/板/饰条/瓷砖/砖/柱). 铝沿用 FTB IC, 奥瑞沿用第 032 批, 基维为 Kivi 音译.
- Tectonic: 垂直缩放, 海拔提升, 大陆/侵蚀/山脊缩放, 深度截断, 奶酪/面条/意面洞穴 (沿用社区对 cheese/noodle/spaghetti cave 的通行叫法), 雕刻器.
- Structurify: 边距 (padding), 平坦度检查, 起始高度类型 (固定/均匀/偏向底部/强偏向底部/梯形), 垂直锚点 (绝对/底部以上/顶部以下), 平台宽度, 模板池权重, 放置尝试次数.
- 结构类模组: 采矿维度, 末地/下界采矿传送门, 远古城市, 废弃矿井, 虚空维度, 液体区域, 芽生 GeOre 方块.
- 专名保留: XyCraft, Tectonic, Structurify, Moog 系列与 Moog's Structure Lib, YUNG's Better 系列, MES/MNS/MVS, Cloth, Jupiter, (Neo)Forge, GitHub Releases/Ko-fi/CurseForge/Modrinth.

证据见 `ordinary/batch-212` 至 `batch-230` 与 `reports/worldgen-completion-212-230.md`.

## 1.4.0 剩余普通文本收尾 (第 231-287 批)

- Reliquary: 炼金全书, 迈达斯试金石, 生物护符, 偏执提灯, 幸运硬币; 配置项按 对象+属性 (火药价值/末影珍珠上限/每刻最大方块编辑数).
- FTB Worlds 客户端: FTB 世界, 套餐, 区域, 计费周期, 结账, 邀请码 (一次性/共享), 世界槽位, 续订.
- NeoVitae / Animus: 血色外壳, 血色合成器, 仪式锚, 生命宝珠, 灵质, 炼金炉, 狱火锻炉, 命血台桌, 主仪式石, 神圣迅捷; EV 与 FE 保留.
- Apothic Enchanting: 位阶, 量子化, 阿卡那, 世界层级; 117 条罗马数字等级标签保留.
- 神秘农业附加: 熔融活化水晶, 熔融觉醒终极精华, 熔融究极精华, 沿用 究极精华/终极精华 官方等级.
- 建筑与渲染: CTM 纹理, 保护塔, 尾迹, 溅水平面, 泛洪填充, 天空包, 天空盒, 装饰盔甲.
- 标识符整批保留: ACI 的表达式函数名与关键字 (abs/ceil/clamp/mod/otherwise/True/False), ForgeEnderTech 的配置键名, EvilCraft 的罗马数字, EvilCraft 兼容里的模组专名, `hide` 关键字, `true`/`false`/`r` 值标识符.
- 只有模组名或格式串的批次: Lollipop, BM Addon, Plonk, PolyLib, Euphoria Patches, Placebo, Cable Facades, Cyclops Core, GuideME, Volumetrics.

证据见 `ordinary/batch-231` 至 `batch-287` 与 `reports/ordinary-remaining-231-287.md`.

## 1.4.0 手册语言键与分组名 (第 288-296 批)

- anima 死灵之书: 书名为 死灵之书; 章节 入门/部件/魔像/灌注与萨隆铁/收集灵魂/施法/神祇与信仰/进阶; 工坊机器 吹制模台/电路压印机/骨笼/漏斗/醒酒瓶/分流器/葫芦瓶/螺旋管/魔像部件装配台/魔像制造器/灵魂之井/灵魂祭坛/研究台/神祇制造器/神祇之锤/神祇神龛/万神殿.
- 九类灵魂 温和/掠食/厄运/狂乱/水生/末影/炼狱/睿智/神魂 与任务书一致; 祭拜相关 祭拜次数/虔信者/祭司权杖/圣物/识别物/神力/祝福/诅咒 全篇统一.
- 30 个法术名: 活化魔像/活化蜘蛛/闪现/引爆/厄运之矢/汲取生命/掘进/盛宴/御火结界/火球/飞行/冰霜新星/鳃/生长/猎手步伐/无形/洞察/铁皮/窑炉/点燃/修补/强能/净化/熄灭/收割/归返/修复盔甲/排斥/寻的/护盾/弹射/缓降/惩击/灵魂视界/魂群/触须/吸血拥抱/帷幕/攀壁.
- 书内结构标记一律保留: 段末 \\ 换行, 空行数, $(br2)/$(br) 宏, entry:// 链接, %% 转义.
- Ars Magica 能力: 亲和 奥术/水/末影/大地/风/火/冰/生命/自然/雷电; 能力数值范围与 %% 原样保留.
- Collapsible Groups 分组名: 应用能源2, 神化, 末影接口, 通用, 资源蜜蜂, 精致存储, 原版; 资源蜜蜂子分组 属性基因/类型基因/蜜蜂刷怪蛋/蜜蜂实体/蜂箱/蜂巢/帆布蜂箱/蜂巢块/蜜脾/石化蜂蜜/扩容盒/帆布扩容盒.

证据见 `ordinary/batch-288` 至 `batch-296`, `manuals/group_lang-zh.json` 与 `reports/manual-language-288-296.md`.

## 1.4.0 手册语言键与分组名 (第 288-296 批)

- anima 死灵之书: 书名为 死灵之书; 章节 入门/部件/魔像/灌注与萨隆铁/收集灵魂/施法/神祇与信仰/进阶; 工坊机器 吹制模台/电路压印机/骨笼/漏斗/醒酒瓶/分流器/葫芦瓶/螺旋管/魔像部件装配台/魔像制造器/灵魂之井/灵魂祭坛/研究台/神祇制造器/神祇之锤/神祇神龛/万神殿.
- 九类灵魂 温和/掠食/厄运/狂乱/水生/末影/炼狱/睿智/神魂 与任务书一致; 祭拜相关 祭拜次数/虔信者/祭司权杖/圣物/识别物/神力/祝福/诅咒 全篇统一.
- 30 个法术名: 活化魔像/活化蜘蛛/闪现/引爆/厄运之矢/汲取生命/掘进/盛宴/御火结界/火球/飞行/冰霜新星/鳃/生长/猎手步伐/无形/洞察/铁皮/窑炉/点燃/修补/强能/净化/熄灭/收割/归返/修复盔甲/排斥/寻的/护盾/弹射/缓降/惩击/灵魂视界/魂群/触须/吸血拥抱/帷幕/攀壁.
- 书内结构标记一律保留: 段末 \\ 换行, 空行数, $(br2)/$(br) 宏, entry:// 链接, %% 转义.
- Ars Magica 能力: 亲和 奥术/水/末影/大地/风/火/冰/生命/自然/雷电; 能力数值范围与 %% 原样保留.
- Collapsible Groups 分组名: 应用能源2, 神化, 末影接口, 通用, 资源蜜蜂, 精致存储, 原版; 资源蜜蜂子分组 属性基因/类型基因/蜜蜂刷怪蛋/蜜蜂实体/蜂箱/蜂巢/帆布蜂箱/蜂巢块/蜜脾/石化蜂蜜/扩容盒/帆布扩容盒.

证据见 `ordinary/batch-288` 至 `batch-296`, `manuals/group_lang-zh.json` 与 `reports/manual-language-288-296.md`.

## 1.4.0 手册语言键收尾 (第 297-314 批)

- Ars Magica: 亲和元素名取官方 (空气/奥术/大地/末影/火焰/冰霜/生命/闪电/自然/水); 能力批次 296 的 风/火/冰/雷电 已同步改写. 合成祭坛, 源质, 亲和偏移, 形态组, 法术修饰, 银质法术部件 为本批定名; 守护者与掉落物沿用官方中文.
- Occultism 魔灵词典: Patchouli 软换行与 [#](十六进制) 着色逐行保留; 使魔名与升级分档 (默认/升级/艾瑟金属) 沿用官方; 精灵 (Foliot), 火灵 (Afrit), 巨灵 (Marid) 沿用神秘学术语.
- NeoVitae: 仪式锚, 迅捷仪式, 血色合成器, 感知长矛, 灵魂陷阱; 语序必须与原文数字顺序一致.
- EvilCraft 联动: 血晶球, 血能注入器, 血能箱, 暗黑矿石, 暗黑宝石, 亡灵树, 压榨机, 磨粉机, 笔与血 (第 271 批已回改对齐).
- Animus: 血色发电机, 血弹, 灵粉; 宝珠等级 见习/学徒/巫师/法师/领主/圣师/超凡.

证据见 `ordinary/batch-297` 至 `batch-314` 与 `reports/manual-language-297-314.md`.

## 1.4.0 Patchouli 书籍 (557 字段)

- 新增构建链 localization/patchouli_translation.py, 已入 project.py check; 产物在 Manuals 资源包 assets/<ns>/patchouli_books/<book>/zh_cn/.
- MFFS: 福特龙 (Fortron), 强制推导机, 福特龙电容, 拦截矩阵, 力场投射器, 生物识别仪, 身份卡, 频率卡, 遥控器; 模块名 规模/速度/容量/平移/旋转/电击/加固/伪装/解构/收集/稳定/穹顶/融合/反转/静音/海绵/发光.
- Animal Pen: 动物围栏/水族箱/鸟舍/动物笼/水生动物容器/捕鸟笼; 比较器二进制位 [0000] 原样保留.
- 任务书物品名按当前生效物品名同步 714 个片段 (含 Animal Pen 物品 水族罐/捕禽网, Nautec 共鸣/海棱水晶/生物反应机及菌种 嗜铁菌/嗜岩石菌/嗜金刚菌 等, 精致存储 输入总线/自动合成仓 等); 映射与保留项见 `reports/quest-item-name-sync-1.5.1.md`. Shimmerweave 概念仍作 微光编织.
- 神化: 世界层级沿用官方 居所/边境/高峰/顶点; 刷怪笼符文系列按层级 拓荒者/旅行者/登山者/雷霆; 词缀 耐久词缀.
- 上游自带中文的书 (apotheosis/justdirethings) 以 JAR zh_cn 为底并半角化; productivebees/modularrouters 以已装 CFPA 为底; 拉丁学名保留.

证据见 `reports/patchouli-manuals.md` 与 `patchouli/progress.json`.
## 2026-10-18 名称保留

用户指定 `Feed The Beast` 保留原文, 替代作为专名使用的“喂养巨兽”. 已同步任务书目录/正文, 任务组件名称与提示, Companion 排行榜/进度以及整合包进度说明. `Feed The Beast Progress` 采用 `Feed The Beast 进度`. 原文动词 `fed the Beast` 仍按语义翻译为“喂养巨兽”, `Heart of the Beast` 等独立名称保持既有译名. 详见 `reports/text-syntax-audit-2026-10-18.md`.

## 2026-10-18 玩家反馈修正

用户明确指定下列译名, 作为本轮跨任务书、手册、普通语言与客户端模组名显示的裁决. 原始英文、CFPA 原件与历史源快照不改写.

| 概念/当前命名空间 | 规范译名 | 说明 |
| --- | --- | --- |
| Nutritional / Nutritional Balance / nutritional | 营养均衡 | 模组名; Nutrients 译为营养, 不再使用营养素 |
| Iron Jetpacks / ironjetpacks | 铁制喷气背包 | 任务书 Simply Jetpacks 为源文误指, 当前 JAR 为 IronJetpacks 9.0.3 |
| Horse Powered / horsepowered | 马力 | 用户所称 Horse Power 对应当前模组 Horse Powered |
| Hephaestus Forge / hephaestus | 匠神 | Hephaestus Tools 扩展为匠神工具 |
| Stellaris / stellaris | 群星 | 同步任务书、手册与名称显示 |
| NauTec 2 / nautec | 海蓝科技 | 当前元数据名为 NauTec 2 |
| Auroral / auroral | 极光 | 同步任务书、手册与名称显示 |
| Dimensional Resources / dimresources | 维度资源 | 沿用 GuideME 已定名称并同步其他正文 |
| Celestine Shard / item.nodeworks.celestine_shard | 天青石碎片 | 复用 Nodeworks 既有术语, 修复汇总包漏带语言键 |

当前 JAR 名、哈希、元数据英文与中文映射见 `client_fixes/mod-names.json`. 运行时 API 和硬编码提示绑定见 `client_fixes/manifest.json`. 任务书合金炉新增颜色只允许 `quest_format_corrections.json` 中精确的一条源文/译文对, 其他格式保护继续生效. 修复范围、来源勘误、检查与游戏内未验收项见 `reports/user-fixes-2026-10-18.md`.

## 2026-10-18 已有中文模组名显示补接

神秘农业 (`mysticalagriculture`, 原生 `itemGroup.mysticalagriculture`) 与应用能源2 (`ae2`, 原生 `gui.ae2.CreativeTab`) 复用当前 JAR 自带中文, 英文名称与当前元数据名称匹配. 这些译名已在项目正文或分组使用, 本轮补入客户端名称显示映射. 同类新增 112 项的当前 JAR、源键、原始中文及采用理由见 `client_fixes/mod-names.json` 的 source_evidence 和 `client_fixes/mod-name-audit.json`. 现有玩家正文/语言资源不重译.

多候选时按语义区分: 变异怪物沿用本项目已定名称; 战术翻滚取原生显式 mod_name; 傻瓜烹饪取模组物品栏/配置名, 不把手册物品名当模组名; 黑盒存储取模组物品栏名称; 更多红石电路沿用本项目裁决; 垃圾槽取当前有效按键分类名. 这些选择只补模组显示名, 不把同模组中的不同对象名称按字符串全局替换. 7 项疑义单列暂缓, 包括 Refined Storage 的精炼存储/精致存储旧冲突, 未默默改写旧裁决.

## 2026-10-18 用户裁决关闭模组名疑义

Refined Storage 统一为精致存储, 类型扩展为精致存储: 类型扩展, Refined Cooking 为精致厨房. 用户最新明确 Quartz Arsenal 为无线合成, 完整显示名为精致存储 - 无线合成. 此决定取代此前保留英文的要求; 原生译名符合模组内容, 不再称其为误名. NeoSync 确定为新克隆, Auth Me 保留英文, Animal Pen 模组名为动物围栏. 旧待复核记录仅保留审计历史, 当前 7 项全部已裁决, 详情见 client_fixes/user-name-decisions.json. 同步第 022 批一条精炼存储旧称及第 315 批 Quartz Arsenal 的 6 条名称/配置标题覆盖.

## 2026-10-19 任务书模组名同步

复用当前 `client_fixes/mod-names.json` 中已有 JAR/语言键证据的裁决, 同步 32 个模组的任务书译文 85 处与任务词表 2 处. Energized Power 统一为充能能源, 其余映射逐项见 `feedback_20261019/quest-name-changes.json`. 仅修改可见译文, 不按英文全局替换资源 ID, 命令或点击动作. LaserIO 与 Just Dire Things 继续保留既有专名. Nodeworks 硬编码 UI 依据用户最新要求保留英文.

## 2026-10-19 Sodium 0.9.2

第 316 批采用当前原文逐项适配. Fast / Fancy 与原版选项一致, 使用流畅 / 高品质; 树叶透明对应高品质, 不透明对应流畅. 亮度指最低亮度, 不沿用旧版伽玛值解释. Texel Interpolation 译为纹素插值, Nearest / Linear 为最近邻 / 线性; Block Transparency Limits 为透明方块细分限制, 不解释为改变方块透明度. Chunk Updates 的 Deferred / Soon / Immediate 为延后 / 尽快 / 立即. CFPA 各版本及 PR #4962 / #3675 的键级对照和 head SHA 见 `ordinary/batch-316/source-review.json`.

## 1.4.1 Nodeworks 冷却任务

- `ftb:adamantite_coolant`, `ftb:aeternium_coolant`, `ftb:aurichalcum_coolant`: 精金冷却块, 永恒金属冷却块, 奥利哈刚冷却块. 沿用 Nodeworks 的 Crafting Coolant = 合成冷却块及本包现有材料名称, 不引入新材料译名. 本包 KubeJS 新增英文没有自带中文; CFPA 固定来源没有这些整合包专用键. 名称与新增任务同步, 见 `custom/batches/batch-005/manifest.json`.
- 新任务英文的 Crafting Storage 实际指 `nodeworks:crafting_storage`, 当前 JAR 名称为 Crafting Buffer, 中文沿用游戏的合成缓存. Co-Processor 沿用合成协处理器. Nodeworks 0.10.6 语言资源与原名称一致, 不按泛称另造物品名.
- 血弹说明继续沿用命血祭坛, 附魔子弹改装件和气血子弹; 本次只更正换弹机制, 不改既定物品术语.

## 1.5.1 增量裁决 (2026-10-23)

- Nodeworks `block.nodeworks.multi_processing_handler` / 对应手册: Multi-Processing Handler = 多配方加工处理器, 与既有加工处理器区分; Transfer Card = 传输卡. 当前官方中文与固定 CFPA 各版本/PR 缓存未检出候选, 沿用既有存储卡/加工配方集体系.
- 世界层级 Ascent / Summit / Pinnacle 继续使用攀升 / 高峰 / 巅峰, 新护甲示例标签与任务正文一致.
- `item.ftb.charged_buoyancy_tank` 继续使用既有充能浮力罐; 区分普通浮力罐与充能版本, 不改变物品 ID 或配方.
- Hephaestus Tools 的 Spirit Attuned 名称去掉 Gem 后用灵魂调谐; 修复提示保留 `%s` 动态耐久值, 不固定为 25%. Forge Table 沿用现有锻造台.
- Nautec Netheritophiles = 嗜下界合金菌, 按实际产物和既有细菌名称体系命名. 新键不是以旧拼法全局替换.
- 新增键审阅与来源见 `updates/1.5.1/new-language-review.json`, 旧/新译文裁决见 `language-translations.json` 和 `quest-translations.json`.

## 1.6.3 增量裁决 (2026-11-02)

- 巨型反应堆: 新增建造器选项 Website = 网站设计 (第三方 ModDecoded 计算器), Hyperflow = 超流. 涡轮机 closure deck 沿用界面已有的封闭平台; turbine rod / rod controller 继续作转轴 / 转轴控制器, heat sink 继续作散热介质.
- 海蓝科技 Crystal Cultivator = 晶体培育器, 与晶体培育座 (Crystal Cradle) 同属培育体系; Mob Sampler / Mob Sample = 生物采样器 / 生物样本.
- AE2-Replication Bridge = AE2-复制桥接器, Matter Assembler = 物质装配机, Matter Storage Cell = 物质存储元件. 物质类型名直接复用 Replication 自带中文 (Precious = 珍宝等); AE2 机器名用游戏内的 ME 前缀名称.
- Refined Wireless Upgrades: Insert / Export / Block Picker Upgrade = 插入 / 导出 / 方块选取升级, Wireless Grid 沿用 Refined Storage 的无线终端.
- Just Enough Crafting Tables 的 Crafting Station 沿用被其取代的 Crafting Station 模组译名合成站, Crafting Station Slab 同样沿用台阶型合成站.
- Witchery 神物 (Fetish) 章节英文为作者占位文本, 按原意译为占位说明; Poltergeist 沿用游戏内吵闹鬼.
- 新增键审阅与来源见 `updates/1.6.3/new-language-review.json`, 已有译文的源变化裁决见同目录 `language-translations.json`、`quest-translations.json` 与 `cfpa-review-adaptation.json`.

## 2026-10-23 规范术语库

新增 `glossary/glossary.json` 与 `glossary.py`, 从本文件已有裁决整理 74 条规范条目, 带语言键绑定与禁用变体, 已纳入 `project.py check`. 首次校验发现 4 项不一致, 经用户裁决全部修复:

- Apotheosis Pinnacle = 顶点, 与游戏内 (JAR `text.apotheosis.world_tier.pinnacle`) 及 Patchouli 手册一致, 取代上方 1.5.1 增量裁决中的巅峰. 任务书 Gearing Up 5 处已改 (`translations/chapters/gearing_up.json`, `updates/1.5.1/quest-translations.json` 与 `quest-deltas.json` 同步). 其他章节中作普通词义的巅峰/顶点不受影响.
- `advancements.apotheosis.progression.pinnacle.criteria.previous_tier` 英文为 Unlock the Summit World Tier, 由解锁巅峰世界等级更正为解锁高峰世界等级.
- Witchery `advancements.witchery.golden_chalk.title/description` 由金色仪式粉笔改为金黄仪式粉笔, 与方块名一致. 此项与上一项由 `custom/batches/batch-007` 承载, 并同步 `custom/advancements.tsv`.
- MFFS Fortron = 福特朗, 取代 1.4.0 Patchouli 批次的福特龙, 与流体名及 CFPA 审校采用的 PR #5193 一致. 同步 Patchouli 手册 8 个页面 22 处, 普通第 046 批 `info.mffs.fortron_usage` (修订记录见 `ordinary/overlay-revisions.json`). 用户随后裁决所有中文中的 Fortron 一律作福特朗, Fortron Capacitor 为福特朗能量储存器 (简称储存器). 同步任务书 MFFS, Power, Progression Tiers, Pyramid Challenge 共 16 行, 手册 5 页中的福特龙电容/电容; JAR 自带中文仍写 Fortron 的 5 键 (含 Fortron 衍生器 → 福特朗衍生器) 由普通第 347 批覆盖. 衍生器与手册"强制推导机"的名称差异未在本次裁决.

工具调整: `ordinary_translation.py` 认可 custom 批次 `language_entries` 中带 `previous` 的接管记录; `verify_ordinary_rebind.py` 允许源文未变的键通过 `overlay-revisions.json` 登记术语修订. 详见 `glossary/README.md`.

## 2026-10-23 物品名优先与说明文本对齐

用户裁决: 本项目自行翻译的任务书与手册可信度低于游戏内物品译名, 除非该内容经过大量翻译与校对. 说明文本提到物品、方块、实体、流体或效果时, 以游戏当前显示名称为准; 例外须写明依据并登记于 `glossary/name-audit-exceptions.json`. 该规则由 `audit_item_names.py` 检查, 已纳入 `project.py check`.

本轮据此取代的旧裁决: 1.4.0 Patchouli 批次的 MFFS 机器与模块名 (力场投射器, 拦截矩阵, 规模模块, 生物识别仪, 身份卡, 遥控器等, 现按游戏名), 强制推导机 (现为福特朗衍生器), 手册语言键批次的祭司权杖 (现为祭司杖), 神秘学魔灵"精灵 (Foliot), 巨灵 (Marid)" (官方为魔精, 巨灵为 Djinni, Marid 为魔王), 农业批次的花匠骨粉与极压缩骨粉 (现为花农的骨粉, 超级压缩骨粉), MORE Red 的红石合金与石底座 (现为红色合金锭/丝, 石板), NeoSync 说明中的躯壳存储器/构造器 (现为壳体存放仓/培育仓; 躯壳本身仍作躯壳). 逐条范围与统计见 `reports/item-name-alignment-2026-10-23.md`.

