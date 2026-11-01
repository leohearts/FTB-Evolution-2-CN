---
navigation:
  title: 激光提纯熔炉
  icon: nautec:laser_purification_smelter
  position: 13
  parent: deep_engineering/deep_engineering-index.md
item_ids:
  - nautec:laser_purification_smelter
---

# <Color id="light_purple">激光提纯熔炉</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="laser_purification_smelter" scale="2"/>
  不用燃料, 而是在激光束上并排熔炼最多九组物品.
</Column>

激光提纯熔炉可烧炼原版熔炉能烧炼的任何东西, 其输入槽只接受熔炉能烧炼的物品. 它有九个输入槽, 每个都配有独立的输出槽, 另有一个导管升级槽. 升级决定开放的槽位数量以及整台熔炉的工作速度. 更纯的光束可降低运行成本.

***

## <Color id="gold">能量</Color>

熔炉可从顶部以及除正面外的三个侧面接收光束. 它不需要燃料.

每个工作的 tick 需要以下数量的 AP:

**工作槽位数 × 升级的每槽 AP ÷ 光束纯度**, 向上取整.

工作槽位是指已开放, 装有可烧炼物品且输出槽有空间的槽位. 空槽位, 锁定槽位以及输出已满的槽位不产生消耗, 空闲的熔炉完全不需要光束.

* 弱于消耗的光束会使其停止. 它会保留当前进度, 并在光束重新足够强时继续.
* 强于消耗的光束不会使其更快. 只有升级决定速度.
* 高于 1.0 的纯度会除以消耗. 纯度 2.0 的光束使其减半. 从不要求纯度, 低于 1.0 的光束按 1.0 处理, 因此既不提供折扣, 也不增加消耗.

***

## <Color id="gold">升级与速度</Color>

在升级槽中放入一个<ItemLink id="eddy_upgrade"/>, <ItemLink id="surge_upgrade"/>, <ItemLink id="riptide_upgrade"/>或<ItemLink id="maelstrom_upgrade"/>. 这些与[水流导管](current_conduits.md)接口使用的是相同的升级.

| 升级 | 开放槽位 | 熔炼速度 | 每个工作槽位的 AP |
|---|---|---|---|
| 无 | 1 | 每 20 tick 8 个物品 | 1 |
| 涡流 | 3 | 每 10 tick 16 个物品 | 2 |
| 涌流 | 5 | 每 5 tick 32 个物品 | 4 |
| 激流 | 7 | 每 2 tick 64 个物品 | 8 |
| 大漩涡 | 9 | 每 tick 64 个物品 | 16 |

该速度是整台熔炉的速度, 而不是每个槽位的速度. 每个间隔结束时, 它会依次从每个工作槽位熔炼一个物品, 然后再次循环, 直到熔炼完该数量的物品或没有可做的工作. 因此, 九个槽位全部工作的大漩涡熔炉每 tick 从每个槽位熔炼约 7 个物品, 纯度 1.0 时消耗 144 AP, 纯度 2.0 时消耗 72 AP.

每个物品会进入与其输入槽配对的输出槽. 输出槽只接受更多相同物品, 且仅当整个结果都能放下时才会接受, 因此输出已满只会停止其对应的槽位.

***

## <Color id="gold">锁定槽位</Color>

超过升级开放数量的槽位会被锁定, 并画有挂锁. 将鼠标悬停其上可查看哪个升级能解锁它. 锁定的输入槽不会从你或自动化中接收任何东西.

如果在锁定槽位中存有物品时取出升级, 物品会留在原处. 在槽位再次开放之前它们不会被熔炼, 但你仍然可以将它们取出.

***

## <Color id="gold">自动分配</Color>

两个网格之间的自动按钮可开启或关闭自动分配. 开启时, 熔炉每半秒会将输入物品均匀分配到已开放的输入槽位, 使每个槽位同时熔炼.

* 单一物品种类会尽可能均匀地分配. 10 个圆石分配到 3 个开放槽位会变成 4, 3 和 3.
* 多种物品会按各自数量比例共享开放槽位. 每种物品至少保留一个槽位, 然后每种物品在其自己的槽位中均匀分配.
* 不会丢失或增加任何东西, 也不会有槽位超过其堆叠上限. 锁定槽位中的物品不受影响.

新熔炉默认关闭此功能. <ItemLink id="configuration_card"/>会将设置连同已安装的升级复制到另一台熔炉.

***

## <Color id="gold">使用</Color>

空手右键点击可打开它. 左侧是输入网格, 右侧是输出网格, 两者之间有一个进度箭头, 显示当前间隔的进度. 下方的面板显示:

* 当前获得的光束与当前所需的光束
* 光束的纯度及其提供的折扣
* 使用已安装升级时每个间隔熔炼的物品数量
* 已开放的槽位数量

其状态显示在"物品栏"标签旁: 熔炼中, 等待光束, 输出已满或空闲. 将鼠标悬停在面板中的某一行可查看更多细节. 点击箭头可在 JEI 中查看所有熔炼配方.

漏斗和管道可将物品放入输入槽, 并从输出槽取出, 默认可通过任意面. [侧面配置](nautec:getting_started/utilities.md)可分别设置每个面. 自动化永远无法访问升级槽. 破坏熔炉会掉落其中的所有东西, 包括升级.

熔炉不提供经验.

***

## <Color id="gold">面向整合包作者</Color>

在 `config/nautec-common.toml` 中, `smelterSlots` 列出了无升级, 涡流, 涌流, 激流和大漩涡对应的开放槽位(默认 1, 3, 5, 7, 9), `smelterApMultipliers` 按相同顺序列出了每个工作槽位的 AP(默认 1, 2, 4, 8, 16). 速度遵循导管接口的物品设置(`conduitItemIntervalBase` 到 `conduitItemIntervalMaelstrom`, 以及 `conduitItemsPerOpBase` 到 `conduitItemsPerOpMaelstrom`), 因此修改这些会同时改变两者.

***

### <Color id="aqua">激光提纯熔炉配方</Color>

<Recipe id="nautec:laser_purification_smelter"/>
