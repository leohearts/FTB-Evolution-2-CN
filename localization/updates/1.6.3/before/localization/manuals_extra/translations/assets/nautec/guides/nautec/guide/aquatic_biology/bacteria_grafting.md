---
navigation:
  title: 细菌移植
  icon: nautec:grafting_tool
  position: 3
  parent: aquatic_biology/aquatic_biology-index.md
item_ids:
  - nautec:grafting_tool
  - nautec:grafting_station
  - nautec:grafting_anchor
  - nautec:advanced_grafting_anchor
---

# <Color id="light_purple">细菌移植</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="grafting_tool" scale="2"/>
  移植工具从方块上刮取第一个菌落, 放入培养皿.
</Column>

将移植工具拿在主手, 空<ItemLink id="petri_dish"/>拿在副手, 然后右键点击所需生物群系中可移植的方块. 每次尝试消耗一点耐久, 并有机会在培养皿中放入一个新菌落. 持续点击, 直到成功为止.

<Color id="gold">提示</Color>: 向空培养皿中移植. 如果副手的培养皿已经装有菌落, 工具会提示该培养皿中已装有菌落, 并且不执行任何操作, 也不消耗耐久.

***

## <Color id="gold">移植工具</Color>

<RecipeFor id="grafting_tool"/>

该工具有 80 点耐久.

***

## <Color id="gold">在哪里移植</Color>

| 方块 | 生物群系 | 菌株 | 几率 |
|---|---|---|---|
| 石头 | 任意海洋 | 蓝细菌 | 40% |
| 沙子 | 任意沙滩 | 盐细菌 | 40% |
| 灰化土 | 任意森林 | 甲烷菌 | 40% |
| 下界岩 | 下界 | 嗜热菌 | 40% |
| 荧光珊瑚虫 | 荧光海林 | 蓝细菌 | 50% |
| 深海海带 | 荧光海林 | 盐细菌 | 30% |
| 荧光藻 | 荧光海林 | 成藻菌 | 30% |
| 海晶叶丛 | 海晶礁 | 光养菌 | 35% |
| <ItemLink id="budding_prismarine"/> | 海晶礁, 荧光海林, 深渊海沟, 暖水海洋, 深温水海洋 | 嗜岩石菌 | 30% |
| 深渊珊瑚 | 深渊海沟 | 嗜钙菌 | 30% |
| 热泉管虫 | 海底热泉 | 嗜硫菌 | 25% |

整合包可以更改此列表. JEI 的细菌移植类别始终显示当前列表, 并在 "Only In" 下显示生物群系.

***

## <Color id="gold">移植站</Color>

<Row>
  <ItemImage id="grafting_station" scale="2"/>
</Row>

移植站无需工具, 也无需生物群系即可移植. 给它一个空<ItemLink id="petri_dish"/>, 上表中的一个可移植方块以及盐水, 每个循环都会在培养皿中放入一个新菌落. 此过程没有几率判定, 因此永远不会浪费尝试.

* 能量: 至少 100 AP, 纯度 2.8 或更高的光束, 从除正面以外的任意一面输入. 直接输入<ItemLink id="prismarine_crystal"/>光束(3.0), 或通过中继器和转接器输入, 均可.
* 盐水: 每个菌落 4,000 mB. 储罐容量为 16,000 mB. 用管道输入, 或手持桶右键点击.
* 时间: 每个菌落一分钟. 较弱的光束会暂停它, 但不会丢失进度.
* 每个菌落消耗一个培养皿和一个方块, 除非安装了移植锚或高级移植锚.

右键点击可打开它. 将鼠标悬停在箭头上可查看它在等待什么, 或通过<ItemLink id="prism_monocle"/>观察它. 漏斗和管道可以插入培养皿和方块, 并抽出已接种的培养皿, 默认可通过任意一面([侧面配置](nautec:getting_started/utilities.md)). 工作时正面窗口会亮起.

所有这些数值都在 `config/nautec-common.toml` 中.

<RecipeFor id="grafting_station"/>

<Row>
  <ItemImage id="grafting_anchor"/>
  ### <Color id="aqua">移植锚</Color>
</Row>

用于移植站的升级. 将其放入移植站界面左下角的槽中, 每次移植后样本方块都会留在原处, 因此只要持续供应培养皿和盐水, 一个方块就能不断移植出菌落. 从物品栏中按住 Shift 点击移植锚, 可将其直接放入对应槽中. 管道无法访问该槽, 因此自动化永远不会误将其抽出.

<RecipeFor id="grafting_anchor"/>

<Row>
  <ItemImage id="advanced_grafting_anchor"/>
  ### <Color id="aqua">高级移植锚</Color>
</Row>

用四个来自[生物反应机](bio_reactor.md)的反应机速度升级强化而成的移植锚. 它放入同一个槽, 并以相同方式保留样本方块, 同时移植速度提高 200%, 因此一个菌落只需 20 秒而不是一分钟. 代价是能量: 此时移植站需要 500 AP 的光束, 是通常 100 AP 的五倍, 纯度仍需 2.8 或更高. 将鼠标悬停在移植站界面的箭头上, 可查看装上你所安装的移植锚后它需要什么.

<RecipeFor id="advanced_grafting_anchor"/>

***

## <Color id="gold">更强的光束</Color>

移植站在强于其需求的光束下移植得更快: 速度为 (光束 ÷ 其需求量) 的平方根. 它需要 100 AP, 或装有高级移植锚时 500 AP, 纯度始终需为 2.8 或更高.

| 光束, 相对于其需求量的倍数 | 速度 |
|---|---|
| 1× | ×1 (正常) |
| 4× | ×2 |
| 9× | ×3 |
| 16× | ×4 |

两者可以叠加. 高级移植锚在 500 AP 下已经快三倍, 而 2,000 AP 的光束又会将其翻倍, 因此一个菌落只需 10 秒而不是 60 秒.

参见[更强的光束](nautec:getting_started/stronger_beams.md), 了解该规则及其适用的每台机器.

***

## <Color id="gold">从哪个菌落开始</Color>

蓝细菌, 盐细菌, 甲烷菌和嗜热菌不产出任何东西, 也无法培养. 它们是起点: 直接将它们带到[诱变机](mutator.md), 将其突变为能产出东西的菌株.

深海菌株一获得就可以投入工作. 盐细菌产出海带, 成藻菌产出海草, 光养菌产出甘蔗, 嗜岩石菌产出石头, 嗜钙菌产出骨粉, 嗜硫菌产出火药. 嗜岩石菌是许多其他菌株的母株, 从海晶母岩移植它可跳过从嗜热菌到嗜岩石菌那一步 15% 的突变, 因此去一趟[深海](nautec:getting_started/deep_oceans.md)可以节省大量突变.

新菌落是未分析的. 将其放入[细菌分析机](bacterial_analyzer.md), 看看你得到了什么.
