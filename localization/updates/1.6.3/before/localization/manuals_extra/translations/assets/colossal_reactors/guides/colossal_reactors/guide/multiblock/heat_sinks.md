---
navigation:
  parent: multiblock/multiblock-index.md
  title: 散热介质
  icon: colossal_reactors:graphite_block
  position: 15
item_ids:
  - colossal_reactors:graphite_block
---

# 散热介质

**散热介质**是放置在反应堆外壳内部, 燃料棒旁的**被动**方块与静止流体(见[外壳, 各面与燃料棒](shell_and_rods.md)). 内部填充物会从三个方面改变反应堆的运行:

- **燃料效率**: 燃料能持续多久. 反应堆的燃料燃烧速度会*除以*该数值, 因此数值越高燃烧越慢.
- **能量**: 反应堆产出多少 **RF**.
- **过热**: 该方块把反应堆推向不稳定的程度. 只有在启用**反应堆不稳定性**时才有意义(见[反应堆不稳定性](reactor_instability.md)). 本整合包中不稳定性为**关闭**, 因此这一列目前没有效果.

每个数值都是一个**倍率**. `1.0` 为中性, 相当于该属性上的空位(空气). **燃料效率**越高燃料持续越久; **能量**越高 RF 越多; **负值**能量表示该材料会主动*抑制*产出. **过热**越高, 反应堆运行温度越高, 也越快失稳.

## 材料

放置对应的**储存方块**(或用**流体**填充内部格子)即可应用其数值. 固体方块与静止液体都算作内部填充.

| 材料 | 燃料效率 | 能量 | 过热 |
|---|:---:|:---:|:---:|
| 空位(空气) | 1.0 | 1.0 | 0.75 |
| <ItemImage id="minecraft:water_bucket"/> 水 | 1.0 | 1.0 | 1.0 |
| <ItemImage id="minecraft:gold_block"/> 金块 | 1.25 | 1.25 | 1.7 |
| <ItemImage id="ftbmaterials:ruby_block"/> 红宝石块 | 1.3 | 1.3 | 1.75 |
| <ItemImage id="ftbmaterials:sapphire_block"/> 蓝宝石块 | 1.3 | 1.3 | 1.75 |
| <ItemImage id="minecraft:diamond_block"/> 钻石块 | 1.5 | 1.3 | 1.8 |
| <ItemImage id="minecraft:emerald_block"/> 绿宝石块 | 1.4 | 1.4 | 1.8 |
| <ItemImage id="minecraft:netherite_block"/> 下界合金块 | 1.5 | 1.75 | 1.7 |
| <ItemImage id="colossal_reactors:graphite_block"/> 石墨块 / 冰 | 2.0 | −5.0 | 2.5 |
| <ItemImage id="colossal_reactors:ender_goo_bucket"/> 末影黏液 | 1.5 | 2.0 | 3.0 |
| <ItemImage id="ftb:industrial_coolant_bucket"/> 工业冷却剂 | 1.75 | 2.15 | 3.2 |
| <ItemImage id="colossal_reactors:gelid_breezium_bucket"/> 冰寒旋风冷媒 | 1.5 | 3.0 | 5.0 |

## 解读表格

- **空位(空气)**是基准. 表中每种散热介质都能让燃料持续**更久**, 并且(石墨/冰除外)产出**更多** RF, 因此散热介质真正的代价是材料本身.

- **廉价档位**: 金, 红宝石和蓝宝石提供适度的 RF 增幅, 并让燃料延长 25-30%.

- **高产出**: 下界合金与特殊流体对 RF 的提升最大: **末影黏液** ×2.0, **工业冷却剂** ×2.15, **冰寒旋风冷媒** ×3.0 能量. 工业冷却剂在流体中燃料效率也最高(×1.75).

- **工业冷却剂**的制作方法是将**干冰**投入静止的水源方块. 用它的源方块填充内部格子.

- **石墨块 / 冰**是个例外: 它拥有最高的燃料效率(×2.0, 大约使燃料燃烧减半), 但能量倍率为 **−5.0**, 会抵消 RF. 只在延长燃料比产出更重要时使用. `#minecraft:ice` 标签也算在内(冰, 浮冰, 蓝冰).

- **流体**以静止液体的形式放置在外壳内部. **水**即使不是源方块也会生效; 熔融流体按源方块填充处理.

- 配方数据还列出了**橄榄石块**散热介质(燃料效率 1.4 / 能量 1.4 / 过热 1.76), 但本整合包中没有方块绑定到 `#c:storage_blocks/peridot` 标签, 因此在有模组提供之前它没有效果.

数据包配方可以重新调整这些数值, 因此你的整合包实际使用的数字可能不同; 如有疑问请查看反应堆配方数据或 **JEI**.
