---
navigation:
  title: 工业生物反应机
  icon: nautec:industrial_bio_reactor
  position: 12
  parent: aquatic_biology/aquatic_biology-index.md
item_ids:
  - nautec:industrial_bio_reactor
---

# <Color id="light_purple">工业生物反应机</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="industrial_bio_reactor" scale="2"/>
  一座 5 x 5 x 4 的反应机, 可运行九个菌落, 并有四个升级槽.
</Column>

它的工作方式与[生物反应机](bio_reactor.md)相同: 相同的[生产公式](production_rates.md)和基础速度, 相同的[喂养](colony_feeding.md), 衰老与衰败, 以及相同的[升级](reactor_upgrades.md). 它增加的是空间: 9 个菌落槽和 9 个输出槽, 3 个营养物槽和 4 个升级槽.

***

## <Color id="gold">建造</Color>

四层, 每层 5 x 5:

* 第 1 层(底层): 四个角落是暗海晶石柱, 其余位置是磨制海晶石.
* 第 2 层和第 3 层: 角落是暗海晶石柱, 边缘是细菌防护罩, 中间的 3 x 3 区域留空. 第 2 层中, 工业生物反应机占据一面墙正中间的防护罩位置.
* 第 4 层(顶部): 角落是暗海晶石柱, 其余位置是海蓝钢块.

<GameScene zoom="3" background="#333333" interactive={true}>
  <Block id="nautec:dark_prismarine_pillar" x="0" y="0" z="0"/>
  <Block id="nautec:polished_prismarine" x="1" y="0" z="0"/>
  <Block id="nautec:polished_prismarine" x="2" y="0" z="0"/>
  <Block id="nautec:polished_prismarine" x="3" y="0" z="0"/>
  <Block id="nautec:dark_prismarine_pillar" x="4" y="0" z="0"/>
  <Block id="nautec:polished_prismarine" x="0" y="0" z="1"/>
  <Block id="nautec:polished_prismarine" x="1" y="0" z="1"/>
  <Block id="nautec:polished_prismarine" x="2" y="0" z="1"/>
  <Block id="nautec:polished_prismarine" x="3" y="0" z="1"/>
  <Block id="nautec:polished_prismarine" x="4" y="0" z="1"/>
  <Block id="nautec:polished_prismarine" x="0" y="0" z="2"/>
  <Block id="nautec:polished_prismarine" x="1" y="0" z="2"/>
  <Block id="nautec:polished_prismarine" x="2" y="0" z="2"/>
  <Block id="nautec:polished_prismarine" x="3" y="0" z="2"/>
  <Block id="nautec:polished_prismarine" x="4" y="0" z="2"/>
  <Block id="nautec:polished_prismarine" x="0" y="0" z="3"/>
  <Block id="nautec:polished_prismarine" x="1" y="0" z="3"/>
  <Block id="nautec:polished_prismarine" x="2" y="0" z="3"/>
  <Block id="nautec:polished_prismarine" x="3" y="0" z="3"/>
  <Block id="nautec:polished_prismarine" x="4" y="0" z="3"/>
  <Block id="nautec:dark_prismarine_pillar" x="0" y="0" z="4"/>
  <Block id="nautec:polished_prismarine" x="1" y="0" z="4"/>
  <Block id="nautec:polished_prismarine" x="2" y="0" z="4"/>
  <Block id="nautec:polished_prismarine" x="3" y="0" z="4"/>
  <Block id="nautec:dark_prismarine_pillar" x="4" y="0" z="4"/>
  <Block id="nautec:dark_prismarine_pillar" x="0" y="1" z="0"/>
  <Block id="nautec:bacterial_containment_shield" x="1" y="1" z="0"/>
  <Block id="nautec:industrial_bio_reactor" x="2" y="1" z="0"/>
  <Block id="nautec:bacterial_containment_shield" x="3" y="1" z="0"/>
  <Block id="nautec:dark_prismarine_pillar" x="4" y="1" z="0"/>
  <Block id="nautec:bacterial_containment_shield" x="0" y="1" z="1"/>
  <Block id="nautec:bacterial_containment_shield" x="4" y="1" z="1"/>
  <Block id="nautec:bacterial_containment_shield" x="0" y="1" z="2"/>
  <Block id="nautec:bacterial_containment_shield" x="4" y="1" z="2"/>
  <Block id="nautec:bacterial_containment_shield" x="0" y="1" z="3"/>
  <Block id="nautec:bacterial_containment_shield" x="4" y="1" z="3"/>
  <Block id="nautec:dark_prismarine_pillar" x="0" y="1" z="4"/>
  <Block id="nautec:bacterial_containment_shield" x="1" y="1" z="4"/>
  <Block id="nautec:bacterial_containment_shield" x="2" y="1" z="4"/>
  <Block id="nautec:bacterial_containment_shield" x="3" y="1" z="4"/>
  <Block id="nautec:dark_prismarine_pillar" x="4" y="1" z="4"/>
  <Block id="nautec:dark_prismarine_pillar" x="0" y="2" z="0"/>
  <Block id="nautec:bacterial_containment_shield" x="1" y="2" z="0"/>
  <Block id="nautec:bacterial_containment_shield" x="2" y="2" z="0"/>
  <Block id="nautec:bacterial_containment_shield" x="3" y="2" z="0"/>
  <Block id="nautec:dark_prismarine_pillar" x="4" y="2" z="0"/>
  <Block id="nautec:bacterial_containment_shield" x="0" y="2" z="1"/>
  <Block id="nautec:bacterial_containment_shield" x="4" y="2" z="1"/>
  <Block id="nautec:bacterial_containment_shield" x="0" y="2" z="2"/>
  <Block id="nautec:bacterial_containment_shield" x="4" y="2" z="2"/>
  <Block id="nautec:bacterial_containment_shield" x="0" y="2" z="3"/>
  <Block id="nautec:bacterial_containment_shield" x="4" y="2" z="3"/>
  <Block id="nautec:dark_prismarine_pillar" x="0" y="2" z="4"/>
  <Block id="nautec:bacterial_containment_shield" x="1" y="2" z="4"/>
  <Block id="nautec:bacterial_containment_shield" x="2" y="2" z="4"/>
  <Block id="nautec:bacterial_containment_shield" x="3" y="2" z="4"/>
  <Block id="nautec:dark_prismarine_pillar" x="4" y="2" z="4"/>
  <Block id="nautec:dark_prismarine_pillar" x="0" y="3" z="0"/>
  <Block id="nautec:aquarine_steel_block" x="1" y="3" z="0"/>
  <Block id="nautec:aquarine_steel_block" x="2" y="3" z="0"/>
  <Block id="nautec:aquarine_steel_block" x="3" y="3" z="0"/>
  <Block id="nautec:dark_prismarine_pillar" x="4" y="3" z="0"/>
  <Block id="nautec:aquarine_steel_block" x="0" y="3" z="1"/>
  <Block id="nautec:aquarine_steel_block" x="1" y="3" z="1"/>
  <Block id="nautec:aquarine_steel_block" x="2" y="3" z="1"/>
  <Block id="nautec:aquarine_steel_block" x="3" y="3" z="1"/>
  <Block id="nautec:aquarine_steel_block" x="4" y="3" z="1"/>
  <Block id="nautec:aquarine_steel_block" x="0" y="3" z="2"/>
  <Block id="nautec:aquarine_steel_block" x="1" y="3" z="2"/>
  <Block id="nautec:aquarine_steel_block" x="2" y="3" z="2"/>
  <Block id="nautec:aquarine_steel_block" x="3" y="3" z="2"/>
  <Block id="nautec:aquarine_steel_block" x="4" y="3" z="2"/>
  <Block id="nautec:aquarine_steel_block" x="0" y="3" z="3"/>
  <Block id="nautec:aquarine_steel_block" x="1" y="3" z="3"/>
  <Block id="nautec:aquarine_steel_block" x="2" y="3" z="3"/>
  <Block id="nautec:aquarine_steel_block" x="3" y="3" z="3"/>
  <Block id="nautec:aquarine_steel_block" x="4" y="3" z="3"/>
  <Block id="nautec:dark_prismarine_pillar" x="0" y="3" z="4"/>
  <Block id="nautec:aquarine_steel_block" x="1" y="3" z="4"/>
  <Block id="nautec:aquarine_steel_block" x="2" y="3" z="4"/>
  <Block id="nautec:aquarine_steel_block" x="3" y="3" z="4"/>
  <Block id="nautec:dark_prismarine_pillar" x="4" y="3" z="4"/>
  <IsometricCamera yaw="225" pitch="30"/>
</GameScene>

工业生物反应机可以放在四面墙中任意一面的正中间, 因此你可以先搭好框架, 再把反应机方块放在朝向你的那一面. 示意图展示的是它在北墙的情况. 内部的 3 x 3 x 2 腔室必须是空气, 不能有水, 也不能有方块. 没有顶部时它看起来是这样:

<GameScene zoom="3" background="#333333" interactive={true}>
  <Block id="nautec:dark_prismarine_pillar" x="0" y="0" z="0"/>
  <Block id="nautec:polished_prismarine" x="1" y="0" z="0"/>
  <Block id="nautec:polished_prismarine" x="2" y="0" z="0"/>
  <Block id="nautec:polished_prismarine" x="3" y="0" z="0"/>
  <Block id="nautec:dark_prismarine_pillar" x="4" y="0" z="0"/>
  <Block id="nautec:polished_prismarine" x="0" y="0" z="1"/>
  <Block id="nautec:polished_prismarine" x="1" y="0" z="1"/>
  <Block id="nautec:polished_prismarine" x="2" y="0" z="1"/>
  <Block id="nautec:polished_prismarine" x="3" y="0" z="1"/>
  <Block id="nautec:polished_prismarine" x="4" y="0" z="1"/>
  <Block id="nautec:polished_prismarine" x="0" y="0" z="2"/>
  <Block id="nautec:polished_prismarine" x="1" y="0" z="2"/>
  <Block id="nautec:polished_prismarine" x="2" y="0" z="2"/>
  <Block id="nautec:polished_prismarine" x="3" y="0" z="2"/>
  <Block id="nautec:polished_prismarine" x="4" y="0" z="2"/>
  <Block id="nautec:polished_prismarine" x="0" y="0" z="3"/>
  <Block id="nautec:polished_prismarine" x="1" y="0" z="3"/>
  <Block id="nautec:polished_prismarine" x="2" y="0" z="3"/>
  <Block id="nautec:polished_prismarine" x="3" y="0" z="3"/>
  <Block id="nautec:polished_prismarine" x="4" y="0" z="3"/>
  <Block id="nautec:dark_prismarine_pillar" x="0" y="0" z="4"/>
  <Block id="nautec:polished_prismarine" x="1" y="0" z="4"/>
  <Block id="nautec:polished_prismarine" x="2" y="0" z="4"/>
  <Block id="nautec:polished_prismarine" x="3" y="0" z="4"/>
  <Block id="nautec:dark_prismarine_pillar" x="4" y="0" z="4"/>
  <Block id="nautec:dark_prismarine_pillar" x="0" y="1" z="0"/>
  <Block id="nautec:bacterial_containment_shield" x="1" y="1" z="0"/>
  <Block id="nautec:industrial_bio_reactor" x="2" y="1" z="0"/>
  <Block id="nautec:bacterial_containment_shield" x="3" y="1" z="0"/>
  <Block id="nautec:dark_prismarine_pillar" x="4" y="1" z="0"/>
  <Block id="nautec:bacterial_containment_shield" x="0" y="1" z="1"/>
  <Block id="nautec:bacterial_containment_shield" x="4" y="1" z="1"/>
  <Block id="nautec:bacterial_containment_shield" x="0" y="1" z="2"/>
  <Block id="nautec:bacterial_containment_shield" x="4" y="1" z="2"/>
  <Block id="nautec:bacterial_containment_shield" x="0" y="1" z="3"/>
  <Block id="nautec:bacterial_containment_shield" x="4" y="1" z="3"/>
  <Block id="nautec:dark_prismarine_pillar" x="0" y="1" z="4"/>
  <Block id="nautec:bacterial_containment_shield" x="1" y="1" z="4"/>
  <Block id="nautec:bacterial_containment_shield" x="2" y="1" z="4"/>
  <Block id="nautec:bacterial_containment_shield" x="3" y="1" z="4"/>
  <Block id="nautec:dark_prismarine_pillar" x="4" y="1" z="4"/>
  <Block id="nautec:dark_prismarine_pillar" x="0" y="2" z="0"/>
  <Block id="nautec:bacterial_containment_shield" x="1" y="2" z="0"/>
  <Block id="nautec:bacterial_containment_shield" x="2" y="2" z="0"/>
  <Block id="nautec:bacterial_containment_shield" x="3" y="2" z="0"/>
  <Block id="nautec:dark_prismarine_pillar" x="4" y="2" z="0"/>
  <Block id="nautec:bacterial_containment_shield" x="0" y="2" z="1"/>
  <Block id="nautec:bacterial_containment_shield" x="4" y="2" z="1"/>
  <Block id="nautec:bacterial_containment_shield" x="0" y="2" z="2"/>
  <Block id="nautec:bacterial_containment_shield" x="4" y="2" z="2"/>
  <Block id="nautec:bacterial_containment_shield" x="0" y="2" z="3"/>
  <Block id="nautec:bacterial_containment_shield" x="4" y="2" z="3"/>
  <Block id="nautec:dark_prismarine_pillar" x="0" y="2" z="4"/>
  <Block id="nautec:bacterial_containment_shield" x="1" y="2" z="4"/>
  <Block id="nautec:bacterial_containment_shield" x="2" y="2" z="4"/>
  <Block id="nautec:bacterial_containment_shield" x="3" y="2" z="4"/>
  <Block id="nautec:dark_prismarine_pillar" x="4" y="2" z="4"/>
  <IsometricCamera yaw="225" pitch="30"/>
</GameScene>

手持<ItemLink id="aquarine_steel_wrench"/>, 在旋转模式下不潜行地右键点击工业生物反应机即可成型. 如果某个方块不对, 聊天栏会指出它的位置, 当前方块和应有的方块. 破坏成型反应机的任意方块都会把它拆开.

成型后, 手持非扳手物品右键点击它的任意方块即可打开它.

***

## <Color id="gold">能量</Color>

它需要 100 AP, 加上每个已占用菌落槽 50 AP: 一个菌落 150 AP, 九个菌落 550 AP, 尚未计入升级的倍率. 与生物反应机一样, 这是最低要求. 低于它什么都不会运行, 所有进度都会重置, 而高于它的更强光束会加快反应机(见下文更强的光束).

能量通过顶部的舱口输入. 用扳手右键点击成型顶部的一个海蓝钢块, 把它变成舱口, 再次点击可恢复. 这在物品面模式下不可用, 该模式设置的是反应机的各个面. 舱口接受从上方射入的光束, 位于顶部边缘的舱口也接受射入其外侧面的光束. 你可以打开任意数量的舱口, 它们的能量会相加. 射入工业生物反应机方块正面的光束同样有效.

这远远超过一个催化器所能提供的. 一台没有升级的[能量转换器](nautec:laser_chemistry/energy_converter.md)每 tick 最多发送 150 AP, 因此四台接在四个舱口上, 无需升级就能覆盖九个菌落. 光束也可以在到达舱口前用<ItemLink id="laser_junction"/>合并.

***

## <Color id="gold">界面</Color>

* 左侧的 3 x 3 网格用于放置菌落. 每个菌落右侧的细条是它的营养物缓冲, 下方的条是它的进度.
* 右侧的 3 x 3 网格是输出, 按相同顺序每个菌落一个槽.
* 底部一行左侧是三个营养物槽, 右侧是四个升级槽.
* 中间的箭头显示平均进度. 悬停它可以查看到达的能量与所需能量, 以及升级正在起什么作用.

九个菌落只能靠三个营养物槽喂养, 因此一次最多运行三种不同的营养物. 详情见[菌落喂养](colony_feeding.md).

***

## <Color id="gold">自动化</Color>

* 每个方块的每个外侧面都可以输入和输出物品: 顶部或朝向墙面的漏斗输入营养物和升级, 地板下的漏斗抽出产物, 管道可用于外侧任意位置.
* [侧面配置](nautec:getting_started/utilities.md)决定结构每一侧的功能. 使用反应机界面右侧的标签页, 或在物品面模式下用扳手点击反应机的任意方块. 一项设置覆盖整个侧面: 正面是装有工业生物反应机方块的那面墙, 左面和右面则是你从外面面对该方块时的左侧和右侧墙面. 例如, 把顶部设为输入, 地板设为抽取, 这样顶部的管道永远不会抽出产物, 地板下的管道也不会向里输入.

菌落通过培养皿端口装入和取出. 培养皿放入菌落网格与输出槽之间的上方槽位, 装有菌落的培养皿从下方槽位输出; 空皿从底行营养物槽与升级槽之间的槽位输出. 装有菌落的培养皿会将其装入第一个能容纳整个菌落的槽位. 所有菌落槽都装满后, 新菌落培养皿只会替换衰老菌落: 新菌落替换最老的衰老菌落, 旧菌落则装入同一个培养皿输出, 不会留下空皿. 没有衰老菌落时, 培养皿会在端口中等待; 菌落输出槽已满时, 替换也会等待. 空皿会取出最老的衰老菌落, 没有衰老菌落时则留在端口中等待. 端口拒绝装有衰老菌落的培养皿, 因此同一个箱子可以同时从端口收集并向其供料. 若要取出尚未衰老的菌落, 请手持空皿点击它的菌落槽. 自动化可从能访问其他槽位的位置访问此端口.

自动化只会把物品放入营养物槽, 升级槽和培养皿端口, 并且只从输出槽和培养皿端口取出物品. 不要在顶部舱口上放漏斗: 舱口上方的方块会挡住向下射入的光束.

一个简单的布局: 在顶部一个角落放箱子和漏斗来供应营养物, 顶部其余位置放带光束的舱口, 地板下放漏斗通向存储. 达到规模上限的菌落大约十秒就能填满输出槽, 因此菌落变强后要给输出配不止一个漏斗.

***

## <Color id="gold">配方</Color>

<RecipeFor id="industrial_bio_reactor"/>

***

## <Color id="gold">更强的光束</Color>

工业生物反应机会先根据其菌落和升级算出所需的 AP. 比这更强的光束会在速度升级之外进一步加快生产: 速度等于 (光束 ÷ 所需值) 的平方根.

| 光束(相对于所需值的倍数) | 速度 |
|---|---|
| 1× | ×1(正常) |
| 4× | ×2 |
| 9× | ×3 |
| 16× | ×4 |

两者相乘. 速度升级让反应机以 ×1.5 运行, 同时又获得所需能量四倍的光束时, 它以 ×3 运行. 营养物按工作 tick 消耗, 因此更强的光束能用同样的营养物造出更多物品. 将鼠标悬停在进度箭头上, 可以查看光束速度和含升级的总速度; Jade 也会显示光束速度.

规则及其适用的每台机器参见[更强的光束](nautec:getting_started/stronger_beams.md).
