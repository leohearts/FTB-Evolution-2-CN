---
navigation:
  title: 亚特兰蒂斯步枪
  icon: nautec:atlantean_rifle
  position: 5
  parent: deep_engineering/deep_engineering-index.md
item_ids:
  - nautec:atlantean_rifle
---

# <Color id="light_purple">亚特兰蒂斯步枪</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="atlantean_rifle" scale="2"/>
  一种需要供能的武器, 按住使用键时会持续发射粒子束.
</Column>

按住使用键会使步枪蓄能半秒, 随后向你所瞄准的目标发射光束. 只要按住, 光束每 2 tick 命中一次, 且持续射击越久越强. 它消耗储存的 AP, 耗尽时不会运作.

***

## <Color id="gold">伤害与能量</Color>

在持续射击的最初 10 秒内, 伤害和能量消耗都会从起始值攀升到最大值. 松开后两者都会重置.

| | 初始 | 10 秒后 |
|---|---|---|
| 每次命中伤害 | 4 | 20 |
| 每秒伤害 | 40 | 200 |
| 每次命中 AP | 125 | 625 |
| 每秒 AP | 1,250 | 6,250 |

* 每次命中都无视目标的受伤冷却, 因此每次命中都会生效.
* 光束最远 128 格. 它能穿过水, 会在第一个固体方块处停止, 并命中其路径上的第一个生物.
* 满能量的步枪可持续射击约 164 秒(2 分 45 秒). 短促点射会停留在攀升区间的低耗能端, 总体持续更久.
* 如果步枪没有足够的 AP 进行第一次命中, 它会显示"亚特兰蒂斯步枪未充能"并且不发射. 能量耗尽时它会停止射击.

本表中的每个数值, 蓄能时间和射程都在 `config/nautec-common.toml` 中(`rifleBaseDamage`, `rifleMaxDamage`, `rifleBaseDrain`, `rifleMaxDrain`, `rifleRampTicks`, `rifleChargeTicks`, `rifleRange`).

***

## <Color id="gold">充能</Color>

步枪可储存 1,000,000 AP(`riflePowerCapacity`), 从工作台制作出来时是空的. 其下方的进度条显示充能程度, 工具提示显示精确数值.

* <ItemLink id="charger"/>会以光束每 tick 输送的功率为其充能, 每 tick 最多 20,000 AP(`rifleMaxInput`). 输入充能器的光束越强, 充能越快.
* 佩戴在 Curios 槽位中并开启能力的<ItemLink id="prismatic_battery"/>会从电池自身的储量为其供能, 每 tick 最多 100 AP.

***

## <Color id="gold">附魔</Color>

步枪只能接受无限和诅咒, 不能接受其他附魔. 无限使能量消耗减半, 因此满能量的步枪可持续射击约 324 秒(5 分半). 它的附魔能力很低, 因此请在铁砧上使用附魔书, 而不要使用附魔台.

安装神化后, 步枪在词缀和宝石方面视为弓, 弓的属性会作用于光束:

* 拉弓速度缩短光束发射前的蓄能时间. +50% 拉弓速度使蓄能时间变为三分之二.
* 箭矢速度和箭矢伤害会乘算光束伤害. +50% 箭矢速度即为 1.5 倍伤害.
* 保护穿透和保护削减会无视目标的一部分保护, 护甲穿透和护甲削减会无视其一部分护甲, 数值随宝石缩放.
* 暴击几率和暴击伤害会像作用于任何攻击一样作用于光束.

***

## <Color id="gold">获取</Color>

该配方使用来自[深海压力锻炉](pressure_forge.md)的材料, 因此请先让一台锻炉运转起来. 见[深海材料](materials.md).

<Recipe id="nautec:atlantean_rifle"/>
