---
navigation:
  title: 聚变电站
  icon: nautec:fusion_controller
  position: 8
  parent: deep_engineering/deep_engineering-index.md
item_ids:
  - nautec:fusion_controller
  - nautec:fusion_casing
  - nautec:aquamarine_structural_glass
  - nautec:laser_injector
  - nautec:fusion_collector
  - nautec:containment_coil
  - nautec:fusion_port
---

# <Color id="light_purple">聚变电站</Color>

<Column alignItems="center" fullWidth={true}>
  <Row>
    <ItemImage id="fusion_controller" scale="2"/>
    <ItemImage id="laser_injector" scale="2"/>
    <ItemImage id="containment_coil" scale="2"/>
  </Row>
  围绕培育海棱水晶建造的激光聚变反应堆. 它燃烧盐水, 为其他模组的机器产生 Forge 能量(FE).
</Column>

激光注入器向水晶核心发射光束. 水晶将其作为等离子束继续射入两个聚变收集器, 等离子体则将盐水聚变为 FE. 小型腔室约产生 20,000 FE/t; 装有全套约束线圈的大型腔室可产生 300,000 FE/t, 角落中的辅助水晶可将其提升到 700,000 FE/t.

***

## <Color id="gold">需求</Color>

* 一颗培育海棱水晶, 按[水晶培育](crystal_cultivation.md)所述培育. 核心必须是培育水晶.
* 纯度 2.0 或更高的激光束. 纯度 3.0 可获得全额输出, 因此最强的电站会通过另一颗水晶供能. [细菌燃料电池](nautec:aquatic_biology/bacterial_fuel_cell.md)在其最佳状态(2.5)下可提供全额输出的六分之五.
* 来自[深海排水口](nautec:laser_chemistry/drain.md)的稳定盐水供应.
* 下列部件. JEI 会显示它们的配方: 它们需要深海钢镀板, 海洋金, 末影珍珠, 无瑕海棱水晶, 以及控制器所需的下界之星.

***

## <Color id="gold">建造腔室</Color>

水晶矗立在一个中空的方形箱体中央. 箱体内部的高度恰好等于水晶高度(6 格), 宽和深为 3, 5, 7 或 9 格. 围绕该空间的墙壁, 地板和顶部各厚一格.

<GameScene zoom="2.5" background="#333333" interactive={true}>
  <Block id="nautec:fusion_casing" x="0" y="0" z="0"/>
  <Block id="nautec:fusion_casing" x="1" y="0" z="0"/>
  <Block id="nautec:fusion_casing" x="2" y="0" z="0"/>
  <Block id="nautec:fusion_casing" x="3" y="0" z="0"/>
  <Block id="nautec:fusion_casing" x="4" y="0" z="0"/>
  <Block id="nautec:fusion_casing" x="0" y="0" z="1"/>
  <Block id="nautec:aquamarine_structural_glass" x="1" y="0" z="1"/>
  <Block id="nautec:aquamarine_structural_glass" x="2" y="0" z="1"/>
  <Block id="nautec:aquamarine_structural_glass" x="3" y="0" z="1"/>
  <Block id="nautec:fusion_casing" x="4" y="0" z="1"/>
  <Block id="nautec:fusion_casing" x="0" y="0" z="2"/>
  <Block id="nautec:aquamarine_structural_glass" x="1" y="0" z="2"/>
  <Block id="nautec:fusion_collector" x="2" y="0" z="2"/>
  <Block id="nautec:aquamarine_structural_glass" x="3" y="0" z="2"/>
  <Block id="nautec:fusion_casing" x="4" y="0" z="2"/>
  <Block id="nautec:fusion_casing" x="0" y="0" z="3"/>
  <Block id="nautec:aquamarine_structural_glass" x="1" y="0" z="3"/>
  <Block id="nautec:aquamarine_structural_glass" x="2" y="0" z="3"/>
  <Block id="nautec:aquamarine_structural_glass" x="3" y="0" z="3"/>
  <Block id="nautec:fusion_casing" x="4" y="0" z="3"/>
  <Block id="nautec:fusion_casing" x="0" y="0" z="4"/>
  <Block id="nautec:fusion_casing" x="1" y="0" z="4"/>
  <Block id="nautec:fusion_casing" x="2" y="0" z="4"/>
  <Block id="nautec:fusion_casing" x="3" y="0" z="4"/>
  <Block id="nautec:fusion_casing" x="4" y="0" z="4"/>
  <Block id="nautec:fusion_casing" x="0" y="1" z="0"/>
  <Block id="nautec:aquamarine_structural_glass" x="1" y="1" z="0"/>
  <Block id="nautec:aquamarine_structural_glass" x="2" y="1" z="0"/>
  <Block id="nautec:aquamarine_structural_glass" x="3" y="1" z="0"/>
  <Block id="nautec:fusion_casing" x="4" y="1" z="0"/>
  <Block id="nautec:aquamarine_structural_glass" x="0" y="1" z="1"/>
  <Block id="nautec:aquamarine_structural_glass" x="0" y="1" z="2"/>
  <Block id="nautec:aquamarine_structural_glass" x="0" y="1" z="3"/>
  <Block id="nautec:fusion_casing" x="0" y="1" z="4"/>
  <Block id="nautec:fusion_casing" x="4" y="1" z="4"/>
  <Block id="nautec:fusion_casing" x="0" y="2" z="0"/>
  <Block id="nautec:containment_coil" x="1" y="2" z="0"/>
  <Block id="nautec:aquamarine_structural_glass" x="2" y="2" z="0"/>
  <Block id="nautec:containment_coil" x="3" y="2" z="0"/>
  <Block id="nautec:fusion_casing" x="4" y="2" z="0"/>
  <Block id="nautec:fusion_port" x="0" y="2" z="1"/>
  <Block id="nautec:aquamarine_structural_glass" x="0" y="2" z="2"/>
  <Block id="nautec:aquamarine_structural_glass" x="0" y="2" z="3"/>
  <Block id="nautec:fusion_casing" x="0" y="2" z="4"/>
  <Block id="nautec:fusion_casing" x="4" y="2" z="4"/>
  <Block id="nautec:fusion_casing" x="0" y="3" z="0"/>
  <Block id="nautec:aquamarine_structural_glass" x="1" y="3" z="0"/>
  <Block id="nautec:aquamarine_structural_glass" x="2" y="3" z="0"/>
  <Block id="nautec:aquamarine_structural_glass" x="3" y="3" z="0"/>
  <Block id="nautec:fusion_casing" x="4" y="3" z="0"/>
  <Block id="nautec:aquamarine_structural_glass" x="0" y="3" z="1"/>
  <Block id="nautec:aquamarine_structural_glass" x="0" y="3" z="2"/>
  <Block id="nautec:aquamarine_structural_glass" x="0" y="3" z="3"/>
  <Block id="nautec:fusion_casing" x="0" y="3" z="4"/>
  <Block id="nautec:fusion_casing" x="4" y="3" z="4"/>
  <Block id="nautec:fusion_casing" x="0" y="4" z="0"/>
  <Block id="nautec:aquamarine_structural_glass" x="1" y="4" z="0"/>
  <Block id="nautec:aquamarine_structural_glass" x="2" y="4" z="0"/>
  <Block id="nautec:aquamarine_structural_glass" x="3" y="4" z="0"/>
  <Block id="nautec:fusion_casing" x="4" y="4" z="0"/>
  <Block id="nautec:aquamarine_structural_glass" x="0" y="4" z="1"/>
  <Block id="nautec:laser_injector" x="0" y="4" z="2" p:facing="east"/>
  <Block id="nautec:laser_injector" x="4" y="4" z="2" p:facing="west"/>
  <Block id="nautec:aquamarine_structural_glass" x="0" y="4" z="3"/>
  <Block id="nautec:fusion_casing" x="0" y="4" z="4"/>
  <Block id="nautec:fusion_casing" x="4" y="4" z="4"/>
  <Block id="nautec:fusion_casing" x="0" y="5" z="0"/>
  <Block id="nautec:aquamarine_structural_glass" x="1" y="5" z="0"/>
  <Block id="nautec:fusion_controller" x="2" y="5" z="0" p:facing="north"/>
  <Block id="nautec:aquamarine_structural_glass" x="3" y="5" z="0"/>
  <Block id="nautec:fusion_casing" x="4" y="5" z="0"/>
  <Block id="nautec:aquamarine_structural_glass" x="0" y="5" z="1"/>
  <Block id="nautec:aquamarine_structural_glass" x="0" y="5" z="2"/>
  <Block id="nautec:aquamarine_structural_glass" x="0" y="5" z="3"/>
  <Block id="nautec:fusion_casing" x="0" y="5" z="4"/>
  <Block id="nautec:fusion_casing" x="4" y="5" z="4"/>
  <Block id="nautec:fusion_casing" x="0" y="6" z="0"/>
  <Block id="nautec:aquamarine_structural_glass" x="1" y="6" z="0"/>
  <Block id="nautec:aquamarine_structural_glass" x="2" y="6" z="0"/>
  <Block id="nautec:aquamarine_structural_glass" x="3" y="6" z="0"/>
  <Block id="nautec:fusion_casing" x="4" y="6" z="0"/>
  <Block id="nautec:aquamarine_structural_glass" x="0" y="6" z="1"/>
  <Block id="nautec:aquamarine_structural_glass" x="0" y="6" z="2"/>
  <Block id="nautec:aquamarine_structural_glass" x="0" y="6" z="3"/>
  <Block id="nautec:fusion_casing" x="0" y="6" z="4"/>
  <Block id="nautec:fusion_casing" x="4" y="6" z="4"/>
  <Block id="nautec:fusion_casing" x="0" y="7" z="0"/>
  <Block id="nautec:fusion_casing" x="1" y="7" z="0"/>
  <Block id="nautec:fusion_casing" x="2" y="7" z="0"/>
  <Block id="nautec:fusion_casing" x="3" y="7" z="0"/>
  <Block id="nautec:fusion_casing" x="4" y="7" z="0"/>
  <Block id="nautec:fusion_casing" x="0" y="7" z="1"/>
  <Block id="nautec:fusion_casing" x="4" y="7" z="1"/>
  <Block id="nautec:fusion_casing" x="0" y="7" z="2"/>
  <Block id="nautec:fusion_collector" x="2" y="7" z="2"/>
  <Block id="nautec:fusion_casing" x="4" y="7" z="2"/>
  <Block id="nautec:fusion_casing" x="0" y="7" z="3"/>
  <Block id="nautec:fusion_casing" x="4" y="7" z="3"/>
  <Block id="nautec:fusion_casing" x="0" y="7" z="4"/>
  <Block id="nautec:fusion_casing" x="1" y="7" z="4"/>
  <Block id="nautec:fusion_casing" x="2" y="7" z="4"/>
  <Block id="nautec:fusion_casing" x="3" y="7" z="4"/>
  <Block id="nautec:fusion_casing" x="4" y="7" z="4"/>
  <BoxAnnotation min="2 1 2" max="3 7 3" color="#52e8ff" thickness="0.6">
    培育海棱水晶矗立于此, 从地板一直延伸到顶部, 填满腔室.
  </BoxAnnotation>
  <BlockAnnotation x="2" y="5" z="0" color="#ffd86b">
    聚变控制器, 位于侧墙中, 朝外.
  </BlockAnnotation>
  <BlockAnnotation x="0" y="4" z="2" color="#52e8ff">
    激光注入器, 位于侧墙中央, 与水晶核心同高, 朝向水晶.
  </BlockAnnotation>
  <BlockAnnotation x="2" y="0" z="2" color="#b8a6ff">
    聚变收集器, 位于地板中央. 另一个放在顶部中央.
  </BlockAnnotation>
  <BlockAnnotation x="1" y="2" z="0" color="#ffd86b">
    约束线圈, 可位于墙壁, 地板或顶部的任意位置.
  </BlockAnnotation>
  <BlockAnnotation x="0" y="2" z="1" color="#8cc4f2">
    聚变端口, 可位于墙壁, 地板或顶部的任意位置.
  </BlockAnnotation>
  <IsometricCamera yaw="135" pitch="25"/>
</GameScene>

场景省略了两面墙和顶部, 以便看到内部.

* 箱体的每条棱边都使用<ItemLink id="fusion_casing"/>.
* 墙壁, 地板和顶部的其余部分可使用<ItemLink id="aquamarine_structural_glass"/>, 聚变外壳, 约束线圈或聚变端口. 玻璃可让你观察等离子体.
* 顶部中央和地板中央各放一个<ItemLink id="fusion_collector"/>, 与水晶对齐.
* 任意侧墙的中央放一个<ItemLink id="laser_injector"/>, 与水晶核心(自其底部向上的第四格)同高. 放置时朝腔室内部看, 使其朝向水晶. 最多可装四个, 每面墙一个.
* <ItemLink id="fusion_controller"/>可放在侧墙中远离棱边的任意位置, 朝外. 它会寻找其后方 2 到 5 格处的水晶.
* 除水晶及其角落中的辅助水晶外(见下文"辅助水晶"), 内部保持空旷. 空气和水都可以, 因此电站可建在水下.

右键点击控制器或任意聚变端口可打开其界面. 当腔室不完整时, 底部一行会指出第一处问题.

***

## <Color id="gold">运行</Color>

1. **燃料.** 将盐水输入控制器或<ItemLink id="fusion_port"/>. 它们不接受其他东西.
2. **点火.** 从外部向注入器的背面射入光束. 冷却的电站会先将最初的 5,000,000 AP 作为热量吸收, 然后才开始产出; 在 6,000 AP/t 下约需 40 秒, 输入较小时则需要数分钟. 界面左侧的条显示热量.
3. **能量.** 热量条充满后, 每注入的 AP 最多产生 50 FE. 较低的纯度会按比例降低该值: 纯度 2.4 时每 AP 产生 40 FE.
4. **燃烧.** 每 mB 盐水产生 2,000 FE, 因此 300,000 FE/t 的电站每 tick 燃烧 150 mB. 这正是六台深海排水口的抽取量.
5. **输出.** 控制器和每个聚变端口都会向接触它们的线缆或机器输出 FE.

如果燃料或光束停止, 等离子体会冷却, 电站会在 20 秒内重新变冷. 短暂中断只会损失已经散失的热量, 光束会很快将其补回.

***

## <Color id="gold">输出上限</Color>

腔室能容纳的等离子体有上限. 超过上限的光束会被浪费, 界面会显示**已达上限**.

| 内部尺寸 | 上限 |
|---|---|
| 3 x 3 | 20,000 FE/t |
| 5 x 5 | 50,000 FE/t |
| 7 x 7 | 100,000 FE/t |
| 9 x 9 | 200,000 FE/t |

外壳中的每个<ItemLink id="containment_coil"/>增加 4,000 FE/t, 总计最高 300,000 FE/t. 9 x 9 的腔室用 25 个线圈即可达到该值, 由 6,000 AP/t 的纯度 3.0 光束供能.

***

## <Color id="gold">辅助水晶</Color>

7 x 7 或 9 x 9 的腔室有空间容纳更多水晶. 在四个内侧角落各放置一颗培育海棱水晶, 立于地板并像核心一样延伸到顶部. 每颗辅助水晶:

* 使上限增加 100,000 FE/t, 并将 300,000 FE/t 的总上限提高相同数值
* 使每注入 AP 的产出增加 10 FE, 因此 50 在一颗辅助水晶时变为 60, 四颗全有时变为 90

<GameScene zoom="2.5" background="#333333" interactive={true}>
  <ImportStructure src="fusion_plant_satellites.nbt" />
  <IsometricCamera yaw="225" pitch="30" />
  <BoxAnnotation min="3.97 0.97 3.97" max="5.03 7.03 5.03" color="#52e8ff" thickness="0.06" alwaysOnTop={true}>
    **核心.** 电站所围绕的培育海棱水晶矗立于此, 从地板到顶部.
  </BoxAnnotation>
  <BoxAnnotation min="0.97 0.97 0.97" max="2.03 7.03 2.03" color="#ff6ec7" thickness="0.06" alwaysOnTop={true}>
    **辅助水晶.** 一颗培育海棱水晶矗立于此, 从地板到顶部.
  </BoxAnnotation>
  <BoxAnnotation min="6.97 0.97 0.97" max="8.03 7.03 2.03" color="#ff6ec7" thickness="0.06" alwaysOnTop={true}>
    **辅助水晶.** 一颗培育海棱水晶矗立于此, 从地板到顶部.
  </BoxAnnotation>
  <BoxAnnotation min="0.97 0.97 6.97" max="2.03 7.03 8.03" color="#ff6ec7" thickness="0.06" alwaysOnTop={true}>
    **辅助水晶.** 一颗培育海棱水晶矗立于此, 从地板到顶部.
  </BoxAnnotation>
  <BoxAnnotation min="6.97 0.97 6.97" max="8.03 7.03 8.03" color="#ff6ec7" thickness="0.06" alwaysOnTop={true}>
    **辅助水晶.** 一颗培育海棱水晶矗立于此, 从地板到顶部.
  </BoxAnnotation>
  <BoxAnnotation min="3.97 4.97 -0.03" max="5.03 6.03 1.03" color="#ffd86b" thickness="0.06" alwaysOnTop={true}>
    **聚变控制器.** 位于侧墙中远离棱边处, 朝外.
  </BoxAnnotation>
  <BoxAnnotation min="3.97 3.97 -0.03" max="5.03 5.03 1.03" color="#52e8ff" thickness="0.06" alwaysOnTop={true}>
    **激光注入器.** 位于侧墙中央, 与水晶核心同高, 朝向水晶. 此电站每面墙各有一个.
  </BoxAnnotation>
  <BoxAnnotation min="3.97 -0.03 3.97" max="5.03 1.03 5.03" color="#b8a6ff" thickness="0.06" alwaysOnTop={true}>
    **聚变收集器.** 位于地板中央, 另一个位于顶部中央.
  </BoxAnnotation>
  <BoxAnnotation min="7.97 1.97 0.97" max="9.03 3.03 2.03" color="#ffb74d" thickness="0.06" alwaysOnTop={true}>
    **约束线圈.** 东墙有两排. 每个使上限增加 4,000 FE/t.
  </BoxAnnotation>
  <BoxAnnotation min="-0.03 1.97 3.97" max="1.03 3.03 5.03" color="#8cc4f2" thickness="0.06" alwaysOnTop={true}>
    **聚变端口.** 与控制器一样, 接收盐水并输出 FE.
  </BoxAnnotation>
</GameScene>

一座带全部四颗辅助水晶的 7 x 7 电站: 棱边上有 88 个聚变外壳, 244 个海蓝宝石结构玻璃, 14 个约束线圈, 4 个激光注入器, 2 个聚变收集器, 一个聚变端口和控制器, 共 354 个方块, 外加五颗水晶. 水晶由各自的渲染器绘制, 因此场景只标出它们的位置而不显示它们. 拖动场景可旋转视角.

| 辅助水晶 | 最高输出 | 每 AP 的 FE | 达到该输出所需的纯度 3.0 AP/t |
|---|---|---|---|
| 0 | 300,000 FE/t | 50 | 6,000 |
| 1 | 400,000 FE/t | 60 | 6,667 |
| 2 | 500,000 FE/t | 70 | 7,143 |
| 3 | 600,000 FE/t | 80 | 7,500 |
| 4 | 700,000 FE/t | 90 | 7,778 |

每颗辅助水晶都必须是培育水晶, 见[水晶培育](crystal_cultivation.md), 因此每颗都需要再花费 10,000,000 AP 培育. 盐水仍然每 mB 产生 2,000 FE, 因此 700,000 FE/t 的电站每 tick 燃烧 350 mB, 相当于 14 台深海排水口的抽取量. 界面的辅助水晶一行会显示腔室中的数量, 而内部其他任何位置出现水晶仍会阻止其成型.

这些数值是 `config/nautec-common.toml` 中的 `fusionSatelliteContainment` 和 `fusionSatelliteFePerAp`.

<Color id="gold">提示</Color>: [能量转换器](nautec:laser_chemistry/energy_converter.md)可将电站自身的一部分 FE 作为 AP 回馈给电站. 转换器的光束纯度为 0, 因此请先让它们经过另一颗海棱水晶, 将其提升到 3.0.
