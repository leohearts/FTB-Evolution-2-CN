---
navigation:
  title: 深海储液库
  icon: nautec:deep_sea_reservoir
  position: 15
  parent: deep_engineering/deep_engineering-index.md
item_ids:
  - nautec:deep_sea_reservoir
  - nautec:reservoir_upgrade_2
  - nautec:reservoir_upgrade_3
  - nautec:reservoir_upgrade_4
---

# <Color id="light_purple">深海储液库</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="deep_sea_reservoir" scale="2"/>
  一座 3x3x3 的储罐, 单种流体容量远超其他储罐.
</Column>

## <Color id="gold">放置</Color>

储液库是单个物品, 放置后占据 3x3x3 的空间. 对着方块放置时, 它会以该方块为中心, 在上方建成 3x3x3 的结构, 液位表朝向你. 该空间必须先空出(空气, 水或可以覆盖的植物), 因此也能建在海床上.

如果水流到原本建在干燥位置的储液库, 就会按水流规则穿过框架: 从侧面横向流入, 或从上方流下, 不会从下方往上流.

破坏任意部分都会使整个储液库掉落为一个物品. 物品会保留等级和全部流体, 因此可以搬走装满的储液库.

***

## <Color id="gold">注入与抽出</Color>

* 3x3x3 结构每个方块的所有外侧面都连接同一个储罐, 管道接触任意位置都能使用.
* 手持桶或其他流体容器右击可注入或抽出流体.
* 空手右击打开界面. 鼠标拿着流体容器点击界面中的液位表, 也能注入或抽出.
* 正面的玻璃条会按当前液位显示内部流体.
* 红石比较器可读取装满程度.

每次只能存储一种流体. 完全清空后, 就能重新接受任意流体.

***

## <Color id="gold">等级</Color>

| 等级 | 容量 | 升级 |
|---|---|---|
| I | 500,000,000 桶 | 基础储液库 |
| II | 2,000,000,000 桶 | <ItemLink id="reservoir_upgrade_2"/> |
| III | 10,000,000,000 桶 | <ItemLink id="reservoir_upgrade_3"/> |
| IV | 50,000,000,000 桶 | <ItemLink id="reservoir_upgrade_4"/> |

每级外观都会变化: II 级带钢制框架和铆接箍带, III 级增加铜箍, 管道与阀轮, IV 级则增加发光海晶水晶饰边.

升级必须按顺序安装. 手持下一级升级右击储液库, 或将其放入界面的升级槽, 即可立即生效.

界面的 **移除升级** 会取出并返还最高一级升级, 使储液库下降一级. 如果现有流体超过降级后的容量, 按钮会要求再次点击确认, 并显示将损失的量. 超过较低等级容量的部分会被销毁.

***

## <Color id="gold">合成</Color>

<Recipe id="nautec:deep_sea_reservoir"/>

<Recipe id="nautec:reservoir_upgrade_2"/>

<Recipe id="nautec:reservoir_upgrade_3"/>

<Recipe id="nautec:reservoir_upgrade_4"/>

各级容量位于`config/nautec-common.toml`.
