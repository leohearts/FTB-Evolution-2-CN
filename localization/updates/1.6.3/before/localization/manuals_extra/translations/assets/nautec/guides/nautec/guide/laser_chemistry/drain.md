---
navigation:
  title: 深海排水口
  icon: nautec:deep_sea_drain
  position: 5
  parent: laser_chemistry/laser_chemistry-index.md
item_ids:
  - nautec:deep_sea_drain
  - nautec:deep_sea_drain_wall
---

# <Color id="light_purple">深海排水口</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="deep_sea_drain" scale="2"/>
  一个从海洋中泵出盐水的 3x3 多方块结构.
</Column>

## <Color id="gold">建造</Color>

铺一个平整的 3x3: 深海排水口在中间, 周围八块深海排水口壁. 用<ItemLink id="aquarine_steel_wrench"/>右键点击深海排水口即可成型.

<GameScene zoom="4" background="#333333" interactive={true}>
  <Block id="nautec:deep_sea_drain_wall" x="0" y="0" z="0"/>
  <Block id="nautec:deep_sea_drain_wall" x="1" y="0" z="0"/>
  <Block id="nautec:deep_sea_drain_wall" x="2" y="0" z="0"/>
  <Block id="nautec:deep_sea_drain_wall" x="0" y="0" z="1"/>
  <Block id="nautec:deep_sea_drain" x="1" y="0" z="1"/>
  <Block id="nautec:deep_sea_drain_wall" x="2" y="0" z="1"/>
  <Block id="nautec:deep_sea_drain_wall" x="0" y="0" z="2"/>
  <Block id="nautec:deep_sea_drain_wall" x="1" y="0" z="2"/>
  <Block id="nautec:deep_sea_drain_wall" x="2" y="0" z="2"/>
  <IsometricCamera yaw="225" pitch="30"/>
</GameScene>

它会在类似海洋的生物群系中泵水, 且其正上方九格全部是水. 建在海床上即可同时满足两者. 任何带有海洋或海标签的生物群系都算, 包括模组添加的; 排水口本身或其上方水面顶部任一处于此类群系即可, 因此即使世界生成模组把海床设为洞穴或海沟群系也仍然有效.

***

## <Color id="gold">供能</Color>

排水口需要每 tick 超过 20 AP(可配置). 一个<ItemLink id="aquatic_catalyst"/>可提供:

| 燃料 | 每 tick 的 AP |
|---|---|
| 海晶水晶 | 6 |
| 海晶碎片 | 12 |
| 海棱水晶碎片 | 12 |

两个燃烧碎片的催化器在[激光转接器](laser_manipulation.md)中合并后提供 24, 可驱动排水口. 若使用海晶水晶则需要四个. 转接器会在其输出之间平均分配功率, 因此只保留一个朝向排水口的输出.

光束通过激光端口输入. 手持扳手右键点击四块中间壁板之一(不是角部). 任意一面都可以: 端口始终朝外, 背离排水口, 并会有消息确认. 将光束对准该壁板的外侧. 排水口一次只有一个端口, 因此用扳手点击另一块中间壁板会移动端口, 再次点击同一块壁板则会重新设置.

***

## <Color id="gold">运行</Color>

双手为空时潜行右键点击排水口可将其打开. 只要能量足够它就会打开. 阀门转动, 然后盖子在几秒内摆开. 再次潜行右键点击可关闭.

如果它没有打开, 消息会说明它当前接收的功率与所需功率. 如果它打开了但某些条件会阻止泵水, 例如上方缺水或生物群系不对, 消息也会说明.

在打开且供能时, 它会将盐水泵入一个 128,000 mB 的储罐. 略高于 20 AP 的光束每秒泵入 500 mB, 更强的光束会按正比泵入更多, 且没有上限: 每 AP 每秒泵入 25 mB, 因此光束增强到四倍, 泵水量也增加到四倍.

| 光束 | 每秒盐水 |
|---|---|
| 略高于 20 AP | 约 500 mB |
| 80 AP | 2,000 mB |
| 320 AP | 8,000 mB |
| 2,000 AP | 50,000 mB |
| 20,000 AP | 500,000 mB |

Jade 会显示排水口当前的速率. 基础速率, 所需功率, 速率随光束增长的快慢(`drainPowerScaling`)以及储罐容量均可配置. 它是[搅拌机](mixer.md)稳定的盐水来源, 因为除非整合包在 `config/nautec-common.toml` 中开启 `collectSaltWater`, 否则用桶装取海水仍会得到普通水.

* 用连接在中心方块底部的管道抽出盐水.
* 或者用桶或其他流体容器右键点击排水口的任意部分. 储罐中至少有 1,000 mB 时桶才能装满.

用<ItemLink id="prism_monocle"/>注视壁板可查看储存的流体量. 安装 Jade 后, 注视排水口的任意部分会显示其状态(已关闭, 正在打开, 正在泵送盐水, 能量不足, 上方没有水, 不在海洋中或储罐已满)以及它接收的功率.

<Color id="gold">注意</Color>: 打开且供能的排水口会以气泡柱将上方的一切向下拉. 进入排水口的任何东西都会受到溺水伤害, 包括掉落的物品. 游过它上方之前请先关闭.

***

### <Color id="aqua">配方</Color>

***

## <Color id="gold">更强的光束</Color>

深海排水口在更强的光束下会泵出更多盐水, 按正比增长, 而不是机器遵循的平方根规则: 光束增强到四倍, 泵水量也增加到四倍. 上表列出了各速率. 整合包可通过 `config/nautec-common.toml` 中的 `drainPowerScaling` 改变这一点; 设为 0.5 时会采用平方根规则.

关于该规则及其适用的每台机器, 参见[更强的光束](nautec:getting_started/stronger_beams.md).

<RecipeFor id="deep_sea_drain"/>

<RecipeFor id="deep_sea_drain_wall"/>
