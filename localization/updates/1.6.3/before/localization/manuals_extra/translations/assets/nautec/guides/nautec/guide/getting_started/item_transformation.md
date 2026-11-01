---
navigation:
  title: 物品转化
  icon: nautec:aquarine_steel_ingot
  position: 2
  parent: getting_started/getting_started-index.md
---

# <Color id="light_purple">物品转化</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="aquarine_steel_ingot" scale="2"/>
  通电的激光束会把丢入其中的物品变成别的东西.
</Column>

将物品丢下, 使其位于通电光束之内, 在发射方块和接收方之间的任意位置均可. 若某个转化配方与该物品匹配, 且光束纯度足够高, 物品会在配方时间结束后发生变化. 无需任何点击, 整堆丢下的物品会同时转化, 每个输入物品都会给出配方的完整产出: 3 个海晶水晶产出 6 个海棱水晶碎片.

物品必须在光束中停留完整的时间. 若被推出, 或光束哪怕瞬间失去功率, 都要从头开始.

***

## <Color id="gold">配方</Color>

| 输入 | 产出 | 所需纯度 | 时间 |
|---|---|---|---|
| 海蓝钢混合物 | 海蓝钢锭 | 任意 | 5 秒 |
| 海蓝钢混合物 | 2 个海蓝钢锭 | 2.0 | 4 秒 |
| <ItemLink id="burnt_coil"/> | 激光引导线圈 | 1.5 | 10 秒 |
| 海晶水晶 | 2 个<ItemLink id="prismarine_crystal_shard"/> | 2.0 | 8 秒 |
| <ItemLink id="cast_iron_block"/> | 4 个<ItemLink id="gear"/> | 2.5 | 8 秒 |

当有多个配方匹配时, 光束会使用它所满足的纯度最高的那一个, 因此 2.0 或更高的光束会把每个混合物变成 2 个锭.

JEI 会在物品转化分类下列出所有转化, 包括其他模组或数据包添加的转化.

要自动化这些转化, [激光合成矩阵](laser_crafting_matrix.md)可在一台机器内完成本页的所有转化, 由管道输入.

***

## <Color id="gold">海蓝钢</Color>

海蓝钢是首先要制作的东西. 其混合物不需要纯度, 因此任何正在运行的<ItemLink id="aquatic_catalyst"/>光束都可以: 将催化器对准一个接收方, 例如<ItemLink id="prismarine_laser_relay"/>, 然后把混合物丢在光束下方的地面上.

<Recipe id="nautec:aquarine_steel_compound"/>

之后[搅拌机](nautec:laser_chemistry/mixer.md)可以批量制作该混合物.

***

## <Color id="gold">更高纯度</Color>

激光引导线圈和海棱水晶碎片需要的纯度高于催化器的 1.2. 可使用以下之一:

* <ItemLink id="prismarine_crystal"/>, 纯度 3.0. 见下方的布置.
* <ItemLink id="bacterial_fuel_cell"/>, 最高 2.5, 取决于其菌落.
* 光束路径上的<ItemLink id="focusing_lens"/>, 可为径直穿过它的光束增加 0.5, 最高 2.0(`lensPurityBonus`).
* 与催化器接触的<ItemLink id="budding_prismarine"/>, 每个方块增加 0.1, 最高 2.0. 参见[激光能量](laser_power.md).

物品以其所在光束的纯度来判定. 对于离开透镜的光束, 即透镜提升后的纯度. 以海棱水晶碎片为燃料的催化器穿过一个透镜后, 在透镜射出的光束中为 1.7, 足以处理线圈.

***

## <Color id="gold">在海棱水晶下方</Color>

每座水晶晶洞(参见[结构](structures.md))都有一株海棱水晶立在一个开放的间隙之上(石头晶洞为一格, 深板岩晶洞为两格), 这正是所需的布置.

* 将海蓝催化器与水晶的任意方块同高放置, 从侧面朝向它. 保持在 16 格以内, 中间不能有实心方块.
* 给催化器装入任意燃料. 水晶的底部方块现在会向下射出一道纯度 3.0 的光束, 直射入地面.
* 将物品丢入水晶下方的间隙, 使它们落在地面上并处于该光束内.

请保持催化器有燃料. 燃料耗尽时, 水晶的光束会停止, 其中的所有物品都要从头开始.

<Color id="gold">提示</Color>: 光束会灼烧其中的任何东西. 请从侧面丢入物品, 而不要站到水晶下方.
