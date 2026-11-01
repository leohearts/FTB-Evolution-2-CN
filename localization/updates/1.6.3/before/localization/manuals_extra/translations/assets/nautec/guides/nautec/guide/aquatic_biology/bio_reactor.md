---
navigation:
  title: 生物反应机
  icon: nautec:bio_reactor
  position: 8
  parent: aquatic_biology/aquatic_biology-index.md
item_ids:
  - nautec:bio_reactor
  - nautec:bacterial_containment_shield
---

# <Color id="light_purple">生物反应机</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="bio_reactor" scale="2"/>
  生物反应机最多让三个菌落工作来制造物品.
</Column>

只要反应机有能量, 每个菌落就会逐个制造其菌株产出的物品. 生产物品不会消耗菌落, 而由反应机营养物槽持续喂养的菌落也不会衰老. [工业生物反应机](industrial_bio_reactor.md)是能容纳九个菌落的更大版本.

***

## <Color id="gold">建造</Color>

一座 3 x 3 x 2 的结构:

* 底层: 角落是暗海晶石柱, 边缘是细菌防护罩, 中间是磨制海晶石.
* 顶层: 角落是暗海晶石柱, 边缘是细菌防护罩, 中间是生物反应机.

<GameScene zoom="4" background="#333333" interactive={true}>
  <Block id="nautec:dark_prismarine_pillar" x="0" y="1" z="0"/>
  <Block id="nautec:bacterial_containment_shield" x="1" y="1" z="0"/>
  <Block id="nautec:dark_prismarine_pillar" x="2" y="1" z="0"/>
  <Block id="nautec:bacterial_containment_shield" x="0" y="1" z="1"/>
  <Block id="nautec:bio_reactor" x="1" y="1" z="1"/>
  <Block id="nautec:bacterial_containment_shield" x="2" y="1" z="1"/>
  <Block id="nautec:dark_prismarine_pillar" x="0" y="1" z="2"/>
  <Block id="nautec:bacterial_containment_shield" x="1" y="1" z="2"/>
  <Block id="nautec:dark_prismarine_pillar" x="2" y="1" z="2"/>
  <Block id="nautec:dark_prismarine_pillar" x="0" y="0" z="0"/>
  <Block id="nautec:bacterial_containment_shield" x="1" y="0" z="0"/>
  <Block id="nautec:dark_prismarine_pillar" x="2" y="0" z="0"/>
  <Block id="nautec:bacterial_containment_shield" x="0" y="0" z="1"/>
  <Block id="nautec:polished_prismarine" x="1" y="0" z="1"/>
  <Block id="nautec:bacterial_containment_shield" x="2" y="0" z="1"/>
  <Block id="nautec:dark_prismarine_pillar" x="0" y="0" z="2"/>
  <Block id="nautec:bacterial_containment_shield" x="1" y="0" z="2"/>
  <Block id="nautec:dark_prismarine_pillar" x="2" y="0" z="2"/>
  <IsometricCamera yaw="225" pitch="30"/>
</GameScene>

手持<ItemLink id="aquarine_steel_wrench"/>, 在旋转模式下不潜行地右键点击生物反应机即可成型. 如果某个方块不对, 聊天栏会指出它的位置, 当前方块和应有的方块. 破坏成型反应机的任意方块都会把它拆开.

成型后, 右键点击生物反应机即可打开它.

***

## <Color id="gold">界面</Color>

* 三个菌落槽从培养皿接收菌落, 如[细菌介绍](bacteria_introduction.md)所述.
* 每个菌落旁边的细条是它的营养物缓冲. 悬停可查看还剩多少秒的喂养时间.
* 每个菌落在其右侧有独立的输出槽.
* 最左边的两个槽是营养物槽. [菌落喂养](colony_feeding.md)说明了里面该放什么.
* 最右边的两个槽用于放置[反应机升级](reactor_upgrades.md), 每槽一个.
* 将鼠标悬停在进度箭头上, 可以查看到达的能量与所需能量.
* 菌落上出现黄色或红色的 "!" 表示它需要处理: 它的营养物不在营养物槽里, 它正在衰老, 或者它已进入衰老. 悬停菌落可查看是哪一种, 以及它吃什么.

***

## <Color id="gold">能量与舱口</Color>

反应机通过舱口接收能量. 用扳手右键点击顶层四个细菌防护罩之一, 把它变成舱口(再次点击可恢复), 然后从上方向舱口内射入光束. 这在物品面模式下不可用, 该模式设置的是反应机的各个面. 你可以打开多个舱口, 它们的能量会相加.

| 菌落数 | 所需 AP |
|---|---|
| 1 | 20 |
| 2 | 35 |
| 3 | 50 |

即反应机自身 5 AP, 加上每个已占用菌落槽 15 AP, 两者均可配置. 升级会乘以总量, 参见[反应机升级](reactor_upgrades.md). 能量是阈值, 不是消耗. 低于它什么都不会运行, 所有进度都会重置, 而更强的光束会加快反应机(见下文更强的光束).

一个<ItemLink id="aquatic_catalyst"/>燃烧海晶碎片提供 12 AP, 因此两个舱口上的两个催化器可以运行一个菌落, 三个可以运行两个. 对于三个菌落, 可以用<ItemLink id="budding_prismarine"/>接触催化器来增强它们, 增加第四个舱口, 或者在光束到达舱口前用<ItemLink id="laser_junction"/>合并光束. [细菌燃料电池](bacterial_fuel_cell.md)用单束光就能提供最高 48 AP.

***

## <Color id="gold">生产速度</Color>

速度等于生产速率乘以规模系数(从微小菌落的 0.5 到规模上限的 1), 再乘以菌株的菌株产量. 对于菌株产量为 1 的菌株, 例如嗜岩石菌:

| 菌落 | 每件物品耗时 |
|---|---|
| 生产速率 0.3, 规模 400 | 约 2 秒 |
| 生产速率 1, 规模 20,000 | 约 0.4 秒 |
| 生产速率 2, 规模 40,000 | 约 0.15 秒 |

珍贵的菌株更慢: 钻石菌落所需时间要长八倍多一点. [生产速率](production_rates.md)给出了完整公式和每种菌株的菌株产量.

每个菌落都有独立的输出槽. 当槽满时, 该菌落会暂停直到有空位: 它不生产, 不进食, 不衰老, 也不缩小.

***

## <Color id="gold">自动化</Color>

* 成型反应机的每个外侧面都可以输入和输出物品: 底座下方的漏斗可以抽出产物, 生物反应机方块顶部的漏斗可以输入营养物, 管道则可用于任意一面.
* [侧面配置](nautec:getting_started/utilities.md)决定结构每一侧的功能. 使用反应机界面右侧的标签页, 或在物品面模式下用扳手点击反应机的任意方块. 一项设置覆盖整个侧面, 因此把底面设为抽取后, 管道就只能从整个底座抽取. 反应机把北面视为正面.
* 通过培养皿端口装入和取出菌落. 培养皿放入左下槽, 装有菌落的培养皿从旁边的槽位输出; 空皿从升级槽下方输出. 装有菌落的培养皿会将其装入第一个能容纳整个菌落的槽位. 所有菌落槽都装满后, 新菌落培养皿只会替换衰老菌落: 新菌落替换最老的衰老菌落, 旧菌落则装入同一个培养皿输出, 不会留下空皿. 没有衰老菌落时, 培养皿会在端口中等待; 菌落输出槽已满时, 替换也会等待. 空皿会取出最老的衰老菌落, 没有衰老菌落时则留在端口中等待. 端口拒绝装有衰老菌落的培养皿, 因此同一个箱子可以同时从端口收集并向其供料. 若要取出尚未衰老的菌落, 请手持空皿点击它的菌落槽. 自动化可从能访问其他槽位的位置访问此端口.

自动化只会把物品放入营养物槽, 升级槽和培养皿端口, 并且只从输出槽和培养皿端口取出物品. 只要有营养物输入, 产物输出, 反应机就能无限运行.

***

## <Color id="gold">衰老与衰败</Color>

工作中的菌落消耗营养物缓冲, 而不是衰老. 当缓冲耗尽时, 反应机会从营养物槽中取出下一种匹配的营养物喂养它. 只有在没有匹配的营养物时, 菌落才会衰老, 工作时每 tick 衰老一 tick, 它的进度条会显示 "缺少营养物: 菌落正在衰老".

一旦菌落的年龄超过其寿命, 它就进入衰老. 处于饥饿状态的衰老菌落每工作一秒会损失 2% 的规模(至少 1), 因此大约 35 秒后就会失去一半. 该速率可配置.

喂养会立即停止损失, 但不会让菌落重新变年轻: 它仍处于衰老状态, 一旦营养物耗尽就会再次开始缩小. 完成一次[培养机](incubator.md)循环可以重置它的年龄.

***

## <Color id="gold">配方</Color>

<Recipe id="nautec:bio_reactor"/>

<RecipesFor id="bacterial_containment_shield"/>

***

## <Color id="gold">更强的光束</Color>

生物反应机会先根据其菌落和升级算出所需的 AP. 比这更强的光束会在速度升级之外进一步加快生产: 速度等于 (光束 ÷ 所需值) 的平方根.

| 光束(相对于所需值的倍数) | 速度 |
|---|---|
| 1× | ×1(正常) |
| 4× | ×2 |
| 9× | ×3 |
| 16× | ×4 |

两者相乘. 速度升级让反应机以 ×1.5 运行, 同时又获得所需能量四倍的光束时, 它以 ×3 运行. 营养物按工作 tick 消耗, 因此更强的光束能用同样的营养物造出更多物品. 将鼠标悬停在进度箭头上, 可以查看光束速度和含升级的总速度; Jade 也会显示光束速度.

规则及其适用的每台机器参见[更强的光束](nautec:getting_started/stronger_beams.md).

<RecipeFor id="polished_prismarine"/>

<RecipeFor id="dark_prismarine_pillar"/>
