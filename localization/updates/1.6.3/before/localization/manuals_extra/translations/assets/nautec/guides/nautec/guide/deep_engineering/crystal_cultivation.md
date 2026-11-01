---
navigation:
  title: 水晶培育
  icon: nautec:prismarine_crystal_seed
  position: 7
  parent: deep_engineering/deep_engineering-index.md
item_ids:
  - nautec:dormant_crystal_seed
  - nautec:prismarine_crystal_seed
  - nautec:crystal_cradle
---

# <Color id="light_purple">水晶培育</Color>

<Column alignItems="center" fullWidth={true}>
  <Row>
    <ItemImage id="prismarine_crystal_seed" scale="2"/>
    <ItemImage id="crystal_cradle" scale="2"/>
  </Row>
  培育一颗属于你自己的海棱水晶, 一颗可以拿起并搬走的水晶.
</Column>

<ItemLink id="prismarine_crystal"/>可将任何光束转变为纯度 3.0 的光束, 但水晶晶洞中的天然水晶扎根于其生长处. **培育海棱水晶**的功能完全相同, 并且可以用扳手抬起, 放到任何地方. 培育一颗需要晶种, 培育座和一千万 AP 的高纯度激光能量.

***

## <Color id="gold">1. 找到天然水晶</Color>

唤醒晶种需要纯度 3.0 的光束, 而只有海棱水晶能产生这种光束. 在海床下的水晶晶洞中找到一颗(见[结构](nautec:getting_started/structures.md)), 并按[激光能量](nautec:getting_started/laser_power.md)所述向它发射光束. 你只需要它一次: 你的第一颗培育水晶可以唤醒之后的所有晶种.

***

## <Color id="gold">2. 制作休眠晶种</Color>

用共鸣碎片和海棱水晶碎片环绕无瑕海棱水晶, 即可制成<ItemLink id="dormant_crystal_seed"/>. 它目前还没有作用.

<RecipeFor id="dormant_crystal_seed"/>

***

## <Color id="gold">3. 唤醒它</Color>

<Row>
  <ItemImage id="dormant_crystal_seed" scale="2"/>
  <ItemImage id="prismarine_crystal_seed" scale="2"/>
</Row>

将休眠晶种放入由纯度 3.0 光束供能的[共鸣室](resonance_chamber.md). 当共鸣室进入临界状态时, 它会将晶种制成发光的<ItemLink id="prismarine_crystal_seed"/>: 一份休眠晶种进, 一份苏醒晶种出. JEI 会在共鸣室分类下显示此配方.

***

## <Color id="gold">4. 放入培育座</Color>

将<ItemLink id="crystal_cradle"/>放置在你希望水晶矗立的位置, 并让**其上方有六个空闲方块**. 空气和水都算, 因此培育座可在水下工作. 手持苏醒的晶种右键点击培育座即可放入; 顶部会出现一颗微小的水晶.

<RecipeFor id="crystal_cradle"/>

在它开始生长之前, 你可以用空手取回晶种. 漏斗和管道也可以放入晶种.

***

## <Color id="gold">5. 为其提供一千万 AP</Color>

将激光束射入培育座的任意四个侧面. 每 tick 培育座都会将其光束的全部功率加入晶种的生长, 但**只有在光束纯度达到 2.0 或更高时**才会如此. 纯度 2.0 的光束来自:

* <ItemLink id="bacterial_fuel_cell"/>(最高 2.5)
* 加在现有光束上的[聚焦透镜](beam_optics.md)(最高提升到 2.0)
* 另一颗海棱水晶(3.0)

当多束光束供给培育座时, 它们的功率相加, 纯度则接近最纯的一束, 并损失其与平均值之间差距的四分之一. 弱光束仍会略微拉低纯度, 因此 2.1 光束与 0 光束汇合后会降到 2.0 以下.

晶种在积累 **10,000,000 AP** 后长成完整水晶(`config/nautec-common.toml` 中的 `crystalGrowthPower`; 纯度下限为 `crystalGrowthPurity`). 功率越高, 生长越快:

| 光束功率 | 生长时间 |
|---|---|
| 100 AP/t | 约 83 分钟 |
| 250 AP/t | 约 33 分钟 |
| 500 AP/t | 约 17 分钟 |
| 1,000 AP/t | 约 8 分钟 |

培育座上方的水晶会随着进度逐渐长高. 生长进度永不流失: 若光束停止, 晶种会等待它恢复, 因此你可以分多次积累这一千万.

用 Jade 查看培育座, 可看到其进度, 到达的功率和纯度, 以当前功率计算的剩余时间, 以及停止时的原因(无晶种, 上方没有空间, 无能量或纯度过低).

<Color id="gold">移动正在生长的晶种</Color>: 用任意工具破坏培育座. 它会连同晶种及其全部生长进度掉落, 工具提示会显示其生长程度. 再次放置后生长继续进行.

***

## <Color id="gold">6. 培育水晶</Color>

达到一千万 AP 时, 晶种会变成立在培育座上的完整培育海棱水晶. 它的功能与天然水晶完全相同: 向其侧面发射光束, 顶部和底部会发出纯度 3.0 的光束, 并共享输入的功率(见[激光能量](nautec:getting_started/laser_power.md)). 培育座重新变空, 可以放入下一个晶种.

**要移动它**, 请潜行并用扳手右键点击它的任意部分. 任何模组的扳手都可以, 只要它位于 `c:tools/wrench` 标签中, 包括<ItemLink id="aquarine_steel_wrench"/>. 你会以物品形式取回水晶, 再次放置仍需要六格空闲高度.

天然水晶保持扎根状态, 海蓝钢镐的碎裂能力只对天然水晶生效, 因此培育水晶绝不会意外破碎. Jade 会将每颗水晶标记为培育或天然.

培育水晶也是 海蓝科技 最大的发电机[聚变电站](fusion_plant.md)的核心.
