---
navigation:
  title: 充能器
  icon: nautec:charger
  position: 6
  parent: laser_chemistry/laser_chemistry-index.md
item_ids:
  - nautec:charger
---

# <Color id="light_purple">充能器</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="charger" scale="2"/>
  用激光束为依靠 AP 运行的物品充能.
</Column>

## <Color id="gold">使用</Color>

手持物品右键点击充能器可将其放到托座上, 用空手右键点击可取回. 它一次只能放置一件物品.

将光束对准任意一面. 充能器是低矮方块, 因此沿地面运行的光束既能从上方也能从侧面命中它. 充能时会冒出火花, 物品充满后停止.

每 tick 物品会接收光束输送的能量, 直至物品自身的输入上限. 更强的光束充电更快, 直至达到该上限.

它可以为任何储存 AP 的物品充能, 包括[海蓝钢工具](tools.md)和[盔甲](nautec:laser_augmentation/aquarine_steel_armor.md), [海晶电池](prismatic_battery.md), <ItemLink id="wave_jet"/>以及<ItemLink id="atlantean_rifle"/>.

| 物品 | 容量 | 每 tick 最多接收 |
|---|---|---|
| 海蓝钢镐, 斧, 锹或剑 | 1,200 AP | 128 AP |
| 海蓝钢锄 | 700 AP | 128 AP |
| 海晶电池 | 10,000 AP | 128 AP |

***

### <Color id="aqua">充能器配方</Color>

<RecipeFor id="charger"/>
