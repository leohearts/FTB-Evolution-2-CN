---
navigation:
  title: 深海压力锻炉
  icon: nautec:pressure_forge
  position: 3
  parent: deep_engineering/deep_engineering-index.md
item_ids:
  - nautec:pressure_forge
  - nautec:pressure_synthesizer
  - nautec:atlantean_pressure_synthesizer
---

# <Color id="light_purple">深海压力锻炉</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="pressure_forge" scale="2"/>
  在深水之下使用激光束和蚀刻酸压制材料.
</Column>

深海压力锻炉可制造无瑕海棱水晶, 海洋金锭和深海钢镀板. 它只能在深处地下且处于水柱之下运行, 因此请建在海床上, 或向深井中注水.

***

## <Color id="gold">要求</Color>

以下条件必须同时满足. 只要其中任何一项不再满足, 当前的锻压就会从零开始.

* 深度: 锻炉必须位于 Y 0 或更低(`pressureForgeDepth`). 每个配方还有各自的最大 Y, 列于下文.
* 水: 锻炉正上方的 8 格必须全为水源方块(`pressureForgeWaterColumn`). 仅有深度不够; 干燥的竖井不算. 压力合成器可替代这一点, 见下文.
* 能量: 至少 40 AP/t 的光束(`pressureForgePowerUsage`). 锻炉可从四个侧面和顶部接收光束.
* 纯度: 光束必须达到配方的纯度.
* 蚀刻酸: 储罐中至少 250 mb. 每次完成锻压消耗 250 mb(`pressureForgeAcidUsage`). 储罐可容纳 4,000 mb(`pressureForgeCapacity`).

所有这些数值都在 `config/nautec-common.toml` 中.

***

## <Color id="gold">配方</Color>

| 输入 | 产出 | 纯度 | 最大 Y | 时间 |
|---|---|---|---|---|
| 共鸣碎片 | 无瑕海棱水晶 | 2.0 | -20 | 10 秒 |
| 金块 | 2 个海洋金锭 | 2.0 | -20 | 15 秒 |
| 海蓝钢锭 | 深海钢镀板 | 2.5 | -40 | 15 秒 |

这些配方也会在 JEI 中显示. 产出物的用途见[深海材料](materials.md).

***

## <Color id="gold">使用</Color>

空手右键点击可打开锻炉. 其界面包含输入槽, 输出槽, 酸储罐和合成器槽, 输入与输出之间有一个进度箭头. 下方有一个检查清单, 以绿色或红色显示每项要求及其当前值: 深度, 上方水量, 光束功率, 光束纯度与配方的对比, 以及蚀刻酸. 将鼠标悬停在某一行可查看其需求. 点击箭头可在 JEI 中查看锻炉的配方.

你仍然可以手持可锻造的物品右键点击将其放入, 并手持<ItemLink id="etching_acid_bucket"/>右键点击以填充储罐.

漏斗和管道可放入物品和蚀刻酸, 并取出成品, 默认可通过任意面. [侧面配置](nautec:getting_started/utilities.md)可分别设置每个面的物品和流体. 由于顶部必须保持在水下, 请从侧面输入. 锻炉一次锻压一个物品, 且仅在输出槽有空间时才会完成一次锻压.

透过<ItemLink id="prism_monocle"/>看向它可进行检查. 设置正确时, 它会显示"压力充足"以及酸液量和光束纯度; 不正确时则显示仍需要的深度和水.

## <Color id="gold">压力合成器</Color>

安装在锻炉上的合成器可替代深水, 因此你可以按自己喜欢的外观选择锻炉的建造位置. 手持合成器右键点击锻炉, 或将其放入界面的合成器槽, 即可安装. 从该槽中取出, 或空手潜行右键点击, 即可卸下. 安装不同的合成器会替换它们并返还旧的, 破坏锻炉会掉落已安装的合成器. <ItemLink id="prism_monocle"/>会显示已安装的是哪一个.

<Row>
  <ItemImage id="pressure_synthesizer"/>
  <ItemImage id="atlantean_pressure_synthesizer"/>
</Row>

* <ItemLink id="pressure_synthesizer"/>: 替代锻炉上方的水柱. 锻炉仍必须位于 Y 0 或更低, 每个配方的最大 Y 仍然生效. 在[搅拌机](nautec:laser_chemistry/mixer.md)中由 1 个无瑕海棱水晶和 8,000 mB 盐水制成.
* <ItemLink id="atlantean_pressure_synthesizer"/>: 锻炉可在任意地点, 任意高度运行, 上方无需有水, 且配方会忽略其最大 Y. 在搅拌机中由 1 个压力合成器, 1 个海洋之心, 1 个下界之星和 4 个末影珍珠加 8,000 mB 盐水制成.

你首先需要一台在真实水下运转的锻炉, 因为无瑕海棱水晶由它产出.

<Color id="gold">提示</Color>: 激光束可穿过水. 处于满纯度(2.5)的<ItemLink id="bacterial_fuel_cell"/>可满足全部三个配方, <ItemLink id="prismarine_crystal"/>(3.0)也可以, 并通过中继器或[激光转接器](nautec:laser_chemistry/laser_manipulation.md)路由以拐弯.

***

### <Color id="aqua">深海压力锻炉配方</Color>

<Recipe id="nautec:pressure_forge"/>

***

## <Color id="gold">更强的光束</Color>

压力锻炉需要 40 AP. 更强的光束锻压更快: 其速度为 (光束 ÷ 40) 的平方根.

| 光束 | 速度 |
|---|---|
| 40 AP | ×1(正常) |
| 160 AP | ×2 |
| 360 AP | ×3 |
| 640 AP | ×4 |

配方表中的时间基于 40 AP 光束. 每个配方消耗的蚀刻酸不变.

关于该规则及其适用的每台机器, 见[更强的光束](nautec:getting_started/stronger_beams.md).
